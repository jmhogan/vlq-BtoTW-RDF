# Arguments: 
# The first argument is True or False depending on whether you want to query the dasgoclient to make lists of root files in Nano List text files
# The second argument is True or False depending on whether you want to submit a condor job with the sample specified in the thrid argument
# The third argument is the prefix of the sample you want to use when you submit a condor job

import os,sys,shutil,datetime,time, subprocess
from samples import *

exec(open("/uscms_data/d3/jmanagan/EOSSafeUtils.py").read()) # this is a python2 command, so ignore the error and run with python2
start_time = time.time()

# --- Sample Dictionary ---
sample_dic = samples # This is the name of the list (using list of class objects to keep ordering)

# --- Size of Condor Job ---
filesPerJob = 999
jobsPerSample = 10 # This is only used for the TTToSemiLeptonic samples

# Take in Arguments from the command line
makelists = False
runanalyzer = False
if len(sys.argv) >= 2: makelists = bool(eval(sys.argv[1]))
if len(sys.argv) >= 3: runanalyzer = bool(eval(sys.argv[2]))
if len(sys.argv) >= 4: 
    prefix = sys.argv[3] # 'singleTb'
    textlist = prefix + "NanoList.txt"
    
relbase = '/uscms/home/jmanagan/nobackup/BtoTW/CMSSW_12_4_8/'
outDir='/store/user/jmanagan/BtoTW_Sep2023_fullRun2/'
condorDir='/uscms/home/jmanagan/nobackup/BtoTW/rdfjobs_Sep2023_fullRun2/' # recommend this be outside git area!
tarfile = '/uscms/home/jmanagan/nobackup/rdfjobs.tar' # outside the CMSSW

runDir=os.getcwd()
cTime=datetime.datetime.now()
date='%i_%i_%i_%i_%i_%i'%(cTime.year,cTime.month,cTime.day,cTime.hour,cTime.minute,cTime.second)

print ('--- Starting Submission ---')

# --- Make Lists ---
if makelists:
    queryStatement = '/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="file dataset = /'
        
    #if (os.path.isdir('NanoList')): os.system("rm -r NanoList")
    if not os.path.exists("NanoList/"):
        os.system("mkdir NanoList")
    
    # Loops through all the samples listed in samples.py
    print ('--- DAS queries ---')
    for k,v in sample_dic.items():
        if os.path.exists("NanoList/"+v.textlist): 
            print(v.textlist+' exists, skipping')
            continue
        query = queryStatement + v.samplename + "\" > " + "NanoList/" + v.textlist
        print ('\t'+v.textlist)
        os.system(query)

        # --- Making string of root files --- (Delimiter is  "\n")
        with open(os.path.abspath("NanoList/"+v.textlist),'r') as rootlist:
            rootfiles = [''.join(["root://cmsxrootd.fnal.gov/", line.strip(), "\n"]) for line in rootlist.readlines()]

        with open(os.path.abspath("NanoList/"+v.textlist),'w') as rootlist:
            rootlist.writelines(rootfiles)
        
# --- Submit Condor Jobs ---
if runanalyzer:    
    
    if (not os.path.isdir('Rootfiles')): os.system("mkdir Rootfiles")
    if (not os.path.isdir('Output')): os.system("mkdir Output")
    
    # ------ Making the Tar File ------
    
    print ('--- Making tar ---')    
    if os.path.exists(tarfile): 
        print ('*********** tar already exists! I ASSUME YOU WANT TO MAKE A NEW ONE! *************')
        os.system('rm '+tarfile)
    os.chdir(relbase)
    print ('tar --exclude="src/.git" --exclude="src/*/.git" --exclude="tmp/" --exclude="src/vlq-BtoTW-SLA" --exclude="src/VLQRDF" --exclude="src/vlq-singleProd-RDF" --exclude="src/vlq-BtoTW-RDF/*.root" --exclude="src/vlq-BtoTW-RDF/*.npz" --exclude=".SCRAM" -zcf '+tarfile+' ./*')
    os.system('tar --exclude="src/.git" --exclude="src/*/.git" --exclude="tmp/" --exclude="src/vlq-BtoTW-SLA" --exclude="src/VLQRDF" --exclude="src/vlq-singleProd-RDF" --exclude="src/vlq-BtoTW-RDF/*.root" --exclude="src/vlq-BtoTW-RDF/*.npz" --exclude=".SCRAM" -zcf '+tarfile+' ./*')
    os.chdir(runDir)

    count = 0

    for k,v in sample_dic.items(): # This is fine.  It is a dictionary that exists in samples.py that gets imported at runtime
        prefix = v.prefix;
        textlist = "NanoList/" + v.textlist;
        year = v.year;

        print('Submitting ' + prefix)

        # --- Check sample size and aim for <= 50GB per job
        command = '/cvmfs/cms.cern.ch/common/dasgoclient --query="dataset dataset='+v.samplename+' | grep dataset.size" '
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        try: 
            samplesize = int(out.split('\n')[0])
        except:    
            try: 
                samplesize = int(out.split('\n')[1])
            except:
                try: 
                    samplesize = int(out.split('\n')[2])
                except: 
                    try: 
                        samplesize = int(out.split('\n')[3])
                    except: 
                        print('need more than 3 levels to get sample size')
                        exit(1)

        jobsPerSample = max(1,round(samplesize/50000000000.))
        if "TTToSemiLeptonic" in v.samplename or "TTToHadronic" in v.samplename or "SingleMuon" in v.samplename or "TT_Mtt-1000" in v.samplename or "WJets" in v.samplename or 'ST_t-' in v.samplename:
            jobsPerSample *= 1.1 # add jobs to the ones that seem to go over or take too long
            
        
        num = newNum = 0
        
        with open(textlist,'r') as rootfiles:
            num = len(rootfiles.readlines())

        print ('\t Number of Rootfiles: ' + str(num))
    
        #if "TTToSemiLeptonic" in prefix: 
        filesPerJob = int(max(1,round(num/jobsPerSample)))
        
        os.system('eos root://cmseos.fnal.gov/ mkdir -p '+outDir+'/')
        os.system('mkdir -p '+condorDir+'/'+prefix)
        
        # Redefining fileName so it is accessed from the directory above for analyzer_RDF.h
        fileName = "condor/"+textlist
        
        for i in range(filesPerJob,num+filesPerJob,filesPerJob):
            oldNum = newNum
            newNum = i
            print("Num test: " + str(oldNum) + " -> " + str(newNum))
            
            dict={'RUNDIR':runDir, 'CONDORDIR':condorDir+'/'+prefix, 'CMSSWBASE':relbase, 'OUTPUTDIR':outDir, 'TARBALL':tarfile, 'TESTNUM1':oldNum, 'TESTNUM2':newNum-1, 'PREFIX':prefix, 'FILENAME':fileName, 'YEAR':year}
            jdfName=condorDir+prefix+'/%(PREFIX)s_%(TESTNUM1)s.job'%dict
            print ("jdfname: ",jdfName)
            jdf=open(jdfName,'w')
            jdf.write(
            """use_x509userproxy = true
universe = vanilla
Executable = %(RUNDIR)s/condorRDF.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Transfer_Input_Files = %(TARBALL)s
Output = %(PREFIX)s_RDF_%(TESTNUM1)s.out
Error = %(PREFIX)s_RDF_%(TESTNUM1)s.err
Log = %(PREFIX)s_RDF_%(TESTNUM1)s.log
Notification = Never
Arguments = %(FILENAME)s %(OUTPUTDIR)s %(TESTNUM1)s %(TESTNUM2)s %(YEAR)s 

Queue 1"""%dict)
            jdf.close()
            os.chdir('%s/'%(condorDir+'/'+prefix))
            os.system('condor_submit %(PREFIX)s_%(TESTNUM1)s.job'%dict)
            os.system('sleep 0.5')                                
            os.chdir('%s'%(runDir))
            print ( str(count) + " jobs submitted!!!")
            count += 1
        
        #Formatting line 101
                
    #for k,v in sample_dic.items():
    #    os.system('mv ' + prefix + ' Output/')

print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))




