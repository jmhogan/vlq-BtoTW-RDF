import os,sys,subprocess,fnmatch

resubmit = False
deletefakes = False
killdisconnect = False
splitjobs = False
nsplit = -1

logdir = '/afs/cern.ch/work/j/jmhogan/public/BtoTW_condor/rdfjobs_Oct2024_fullRun2/'

def findfiles(path, filtre):
    for root, dirs, files in os.walk(path):
        for f in fnmatch.filter(files, filtre):
            yield os.path.join(root, f)

reruns = []
killandrerun = {}
fakes = []

for file in findfiles('/afs/cern.ch/work/j/jmhogan/public/BtoTW_condor/rdfjobs_Oct2024_fullRun2/', '*.job'):
    hasout = True
    hasFinished = 0
    hasCopied = 0
    isrunning = True
    disconnected = False
    started = 0
    fakejob = 0
    outname = file.replace('.job','.out').replace('F_','F_RDF_').replace('UL_','UL_RDF_').replace('A_','A_RDF_').replace('B_','B_RDF_').replace('C_','C_RDF_').replace('D_','D_RDF_').replace('E_','E_RDF_').replace('G_','G_RDF_').replace('H_','H_RDF_')
    logname = outname.replace('.out','.log')
    if not os.path.exists(outname):
        hasout = False
    else:
        command = 'grep "Finished all analyzing" '+outname+' | wc'
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = out.strip()
        out = out.decode('utf-8')
        digits = out.find(' ')
        hasFinished = int("".join(out[0:digits]))

        command = 'grep "fully done through copying" '+outname+' | wc'
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = out.strip()
        out = out.decode('utf-8')
        digits = out.find(' ')
        hasCopied = int("".join(out[0:digits]))

        command = 'grep "Number of Entries: 0" '+outname+' | wc'
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = out.strip()
        out = out.decode('utf-8')
        digits = out.find(' ')
        fakeJob = int("".join(out[0:digits]))
        
    command = 'tail -2 '+logname
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    out = out.strip()
    out = out.decode('utf-8')
    
    if 'terminated' in out or 'condor_rm' in out or 'exceeding requested memory' in out or 'wall time exceeded' in out:
        isrunning = False
    if 'Can not reconnect' in out:
        disconnected = True
    if 'attempting to reconnect' in out or 'rying to reconnect' in out:
        disconnected = True

    command = 'grep "executing on host" '+logname+' | wc'
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    out = out.strip()
    out = out.decode('utf-8')
    digits = out.find(' ')
    started = int("".join(out[0:digits]))

    if isrunning and disconnected == True:  #started == 0 # seems like logs update late...
        command = 'tail -4 '+logname
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        out = out.strip()
        out = out.decode('utf-8')

        jobnum = ((out.split(" ")[1]).split(".")[0])[1:]
        killandrerun[outname] = jobnum

    if not isrunning and (not hasFinished or not hasCopied or not hasout):
        if fakeJob > 0:
            fakes.append(outname)
        else:
            reruns.append(outname)


print('Found several jobs that are disconnected:',len(killandrerun))
print(killandrerun)

print('Found several fake jobs:',len(fakes))
print(fakes)

if deletefakes:
    print('Deleting the fakes...')
    for fake in fakes:
        os.system('rm '+fake)
        os.system('rm '+fake.replace('out','err'))
        os.system('rm '+fake.replace('out','log'))
        os.system('rm '+fake.replace('_RDF','').replace('out','job'))

print('Found several jobs that failed:',len(reruns))
for ijob in reruns:
    print(ijob)


resubs = {}

if not resubmit: exit()

if killdisconnect:
    for outname in killandrerun.keys():
        os.system('condor_rm '+killandrerun[outname])
        reruns.append(outname)

for rerun in reruns:
    os.chdir(logdir)
    rerun = rerun.replace('_RDF','').replace('.out','.job')
    command = 'grep "Arguments" '+rerun
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    out = out.decode('utf-8')
    jobnums = [int(out.split(" ")[4]),int(out.split(" ")[5])]
    
    print('\''+rerun+'\':'+str(jobnums))
    resubs[rerun] = jobnums
    #os.system('ls -l '+rerun.replace('_','_RDF_').replace('.job','.out'))
    #os.system('tail -20 '+rerun.replace('_','_RDF_').replace('.job','.err'))

for rerun in resubs.keys():
    folder = rerun.split('/')[-2]
    jobfile = rerun.split('/')[-1]

    if splitjobs:
        if resubs[rerun][0] == resubs[rerun][1]:
            print('NOT SPLITTING THIS ONE, SINGLE FILE '+folder+'/'+jobfile)
            os.chdir(logdir+folder)
            os.system('condor_submit '+jobfile)
            continue

        if nsplit == 2: 
            half = int(resubs[rerun][0] + (resubs[rerun][1] - resubs[rerun][0])/2.0)
            print(folder+': new ranges '+str(resubs[rerun][0])+' - '+str(half)+' , '+str(half+1)+' - '+str(resubs[rerun][1]))

            newjobfile = jobfile.replace('_'+str(resubs[rerun][0]),'_'+str(half+1))
            os.chdir(logdir+folder)
            os.system('cp '+jobfile+' '+newjobfile)
            os.system('sed -i "s| '+str(resubs[rerun][1])+' | '+str(half)+' |" '+jobfile) # only change upper in original file
            os.system('sed -i "s| '+str(resubs[rerun][0])+' | '+str(half+1)+' |" '+newjobfile) # only change lower in new file
            os.system('sed -i "s|_'+str(resubs[rerun][0])+'\.|_'+str(half+1)+'\.|" '+newjobfile)
            
            os.system('condor_submit '+jobfile)
            os.system('sleep 0.5')
            os.system('condor_submit '+newjobfile)
            os.system('sleep 0.5')

        if nsplit == 3:
            third = int(resubs[rerun][0] + (resubs[rerun][1] - resubs[rerun][0])/3.0)
            third2 = int(resubs[rerun][0] + 2*(resubs[rerun][1] - resubs[rerun][0])/3.0)
            print(folder+': new ranges '+str(resubs[rerun][0])+' - '+str(third)+' , '+str(third+1)+' - '+str(third2)+', and '+str(third2+1)+' - '+str(resubs[rerun][1]))
    
            newjobfile = jobfile.replace('_'+str(resubs[rerun][0]),'_'+str(third+1))
            newjobfile2 = jobfile.replace('_'+str(resubs[rerun][0]),'_'+str(third2+1))
        
            os.chdir(logdir+folder)
            os.system('cp '+jobfile+' '+newjobfile)
            os.system('cp '+jobfile+' '+newjobfile2)
            os.system('sed -i "s| '+str(resubs[rerun][1])+' | '+str(third)+' |" '+jobfile) # only change upper in original file

            os.system('sed -i "s| '+str(resubs[rerun][1])+' | '+str(third2)+' |" '+newjobfile) # change upper in middle file
            os.system('sed -i "s| '+str(resubs[rerun][0])+' | '+str(third+1)+' |" '+newjobfile) # change lower in middle file
            os.system('sed -i "s|_'+str(resubs[rerun][0])+'\.|_'+str(third+1)+'\.|" '+newjobfile)

            os.system('sed -i "s| '+str(resubs[rerun][0])+' | '+str(third2+1)+' |" '+newjobfile2) # only change lower in last file
            os.system('sed -i "s|_'+str(resubs[rerun][0])+'\.|_'+str(third2+1)+'\.|" '+newjobfile2)
            
            os.system('condor_submit '+jobfile)
            os.system('sleep 0.5')
            os.system('condor_submit '+newjobfile)
            os.system('sleep 0.5')
            os.system('condor_submit '+newjobfile2)
            os.system('sleep 0.5')

        if nsplit == -1:
            print(folder+': new ranges:')
            os.chdir(logdir+folder)
            for ijob in range(resubs[rerun][0]+1,resubs[rerun][1]+1): # loop for everything past the first file
                newjobfile = jobfile.replace('_'+str(resubs[rerun][0]),'_'+str(ijob))
                print('\t ',ijob,' with file name ',newjobfile)
                os.system('cp '+jobfile+' '+newjobfile)
                os.system('sed -i "s| '+str(resubs[rerun][0])+' | '+str(ijob)+' |" '+newjobfile)
                os.system('sed -i "s| '+str(resubs[rerun][1])+' | '+str(ijob)+' |" '+newjobfile)
                os.system('sed -i "s|_'+str(resubs[rerun][0])+'\.|_'+str(ijob)+'\.|" '+newjobfile)
                os.system('condor_submit '+newjobfile)
                os.system('sleep 0.5')


            print('\t ',resubs[rerun][0],' with file name ',jobfile)
            os.system('sed -i "s| '+str(resubs[rerun][1])+' | '+str(resubs[rerun][0])+' |" '+jobfile) # edit first file .job
            os.system('condor_submit '+jobfile)
            os.system('sleep 0.5')
            
            
    else:
        os.chdir(logdir+folder)
        os.system('condor_submit '+jobfile)
            
