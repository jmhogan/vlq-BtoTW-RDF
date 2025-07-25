# Instructions for Condor Jobs

## How to Run Stuff

**Make a list of the files:**

``` 
$ python2 runCondorJobs.py True False 
```

This corresponds to the first argument of runCondorJobs.py and the code inside the first if statment of that same script.

**Submit Condor Jobs:**

``` 
$ python2 runCondorJobs.py False True
```

There are three things to change depending on what condor jobs you want to submit:
- sample_dic (The name of a dictionary from samples.py containing the samples you want to loop over to submit)
- filesPerJob (The number of files submitted with each job)
- jobsPerSample (Number of divisions per sample)

Only one of filesPerJob and jobsPerSample will be used for each sample.  Currently, only TTToSemiLeptonic samples use jobsPerSample, and all the rest use filesPerJob.  This can be changed with an if statement on line 83.

Condor jobs will only submit files together that come from the same sample.  You don't need to worry about filesPerJob including files from different samples in the same condor job.

After you submit a condor job, you can check the status of your jobs with:

``` 
$ condor_q
```

If you want to remove a condor job, use the condor_q to get the id of the job and the name of the scheduler, and input them in the command below.

``` 
$ condor_rm 2321568.0 -name lpcschedd4.fnal.gov
```

The condor job will disappear when it is finished.  To see the output of the condor job, use the following command to access the eos area after replacing the part of the path after kjohnso with your path.  

```
eosls /store/user/...
```

You can change the output path with outDir in runCondorJobs.py at the top.

Also refer to the .err and .out files in Outputs/Prefix to see if everything completed correctly and to view errors.


**Run the Analyzer**

If you want to run the analyzer without submitting a condor job, you can use the command below.

```
$ root -l -b -q runRDF.C\(\"0\",\"1\",\"condor/Rootfiles/SingleMuonRun2018D2018UL.txt\",\"2018\"\)
```

The first argument is the list of files that will be read in in the contructor of the analyzer class.  For organizational purposes, they are stored in Rootfiles.  The second argument is the output location in the eos area.  The output can be viewed with the following command if you replace path starting with kjohnso to match the output you have.

```
eosls /store/user/...
```

The third and fourth arguments are the range over which the analyzer will run.  In this example it will run over one file, which is the second one in the file becasue it is zero based.  The final argument is the year of the sample, which is used in the analyzer.


Make sure the double quotes are straight up and down.  If they get autocorrected to their curly form, then it will output an error that looks like the one below.
```
Error in <TUnixSystem::SplitAclicMode>: Cannot parse argument in ”2016APVUL")
Warning in <TApplication::GetOptions>: macro ”2016APVUL") not found
Processing runRDF.C("-bash","condor/ZZ2016APVUL.txt",...
Error in <TApplication::ExecuteFile>: macro runRDF.C("-bash","condor/ZZ2016APVUL.txt", not found in path .:/cvmfs/cms.cern.ch/slc7_amd64_gcc820/lcg/root/6.18.04-nmpfii/macros
```

## Purpose of each of the Folders

**NanoList** 

This folder contains all the NanoList root files that are created in the first part of runCondorJobs.py. 

The different samples are seperated into different files named after the prefix of the sample.  The prefix is defined in samples.py

These files are read in in the second part of runCondorJobs.py, and they are used to make the files in Rootfiles.

**Output** 

This folder contains folder named after different samples that contain several files:

-  .err
-  .log
- .job
-  .out 

 for each condor job submitted from that sample.  They ar also labeled by numbers that correspond to the highest file that job could process.  If it is larger than the number of files in the sample, it will just process up to the last file.

**PrepSamples** 

This folder contains several files and folders that were used to automate the process of preparing the samples to go in samples.py.  

The background and signal(BPrime) samples are prepared in two different files.  The file used for the background prep was getNano.py.  This puts the output in nano.txt, which I sorted adn copied into samples.py. I got the background samples from four files in [the github repository of an old analysis](https://github.com/cms-ljmet/FWLJMET/tree/10_6_29_UL/LJMet/CRAB3).

- sample_list_singleLep2016APVUL.py
- sample_list_singleLep2016UL.py
- sample_list_singleLep2017UL.py
- sample_list_singleLep2018UL.py

There were several changes that had to be made on these names.  

The file used for the signal prep was sortBPrimes.py.  The output goes in BPrimeNanos.txt and BPrimeSamples.txt.

I am still waiting for some of the signal files on DAS, so I will include those when they are available.

**Rootfiles** 

This folder contains all the root files that are ready to be passed in the condor job.  These files are made in the second part of runCondorJobs.py, and they are read in in the contructor in analyzer_RDF.h

## Flow of Files

1. runCondorJobs.py  <- samples.py
2. condorRDF.sh
3. runRDF.C
4. analyzer_RDF.h
5. analyzer_RDF.cc <- BPrime.cc, cleanJet.cc, cut_ptrel.cc, generatorInfo.cc, utilities.cc, W_t_reco.cc
