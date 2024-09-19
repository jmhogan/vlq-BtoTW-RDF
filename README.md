# vlq-BtoTW-RDF

## RDataFrame code for B->tW search on NanoAOD

This repository contains the R-Dataframe event selection code being used in the B->tW search, B2G-24-013.

----------------------------------------------------------------

## Structure of this repository

The key analysis files are located in the root directory of the repository, namely the .cc files. Each of these files plays a particular role in running the analysis.  Details about these files can be found in the descriptions below.

The python files in this repository are important for analyzing and training neural networks on the data produced by the RDF scripts. These are also located in the root directory.

The files required for preparing and submitting a condor job to run the analysis are located in the directory labeled *condor*.

Additonal files used for plotting both the output of the analysis files and the neutral network files are found in the directory labeled *plotting*.

----------------------------------------------------------------

## Getting started

In order to run the code, the user must have access to cmslpc-sl7.fnal.gov and the appropriate setup that comes with that (as described in [this tutorial](https://fnallpc.github.io/cms-das-pre-exercises/01-CMSDataAnalysisSchoolPreExerciseFirstSet/index.html)).

Use CMSSW_12_4_8 as the version of a CMSSW release area.  This will ensure there are no version issues.  

Within the `src/` directory of CMSSW_12_4_8, install [correctionLib](https://cms-nanoaod.github.io/correctionlib/install.html). Julie did this by cloning the correctionLib github repository and compiling with cmake.

Clone this repository into the `src/` folder, and copy or softlink the `correctionLib` files from cvmfs:
```
$ git clone https://github.com/jmhogan/vlq-BtoTW-RDF/
$ cd vlq-BtoTW-RDF
$ mkdir jsonpog-integration
$ cp /cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/...stuff... # or make symlinks
```

Once access is set up and the user has the github repository configured along with a working GRID certificate, the program should be runnable.

To actually run the analysis, use the following command:
```
$ root -l -b -q runRDF.C\(\"testNum1\",\"testNum2\",\"inputfile"\,\"year"\)`
```

- `testNum1` = An integer that states the number of the first file that will be included in the job
- `testNum2` = An integer that states the number of the last file that will be included in the job
- `inputfile` = path to input file containing prepared root files
- `year` = year of the sample

It's important to note that every parenthesis and quotation must be escaped for proper syntax. Refer to runCondorJob.py in the *condor* directory to see how to prepare the list of root files.

To run the analysis as a condor job, use the following command to first make a list of the root files.  

```
$ python2 runCondorJobs.py True False`
```

Once this command has completed, switch the True and False as shown below to submit a condor job for the sample specified within runCondorJobs.py.  The list of all samples and lists of combinations of samples can be found in samples.py.  Remember to change to the output directories to include your username and path.

```
$ python2 runCondorJobs.py False True`
```

After you have submitted the condor job, you can use the following command to to check their status, runtime, and location.

`$ condor_q`

When the jobs have stopped running either by completing or returning an error, refer to the folder labeled with the sample name in the directory you specificied in the variable *condorDir* in runCondorJobs.py.

----------------------------------------------------------------

## Analyzer Files

A few key files in this repository are listed below along with a brief description of how they play into the analysis.

- `runRDF.C` - This file is the primary interface between the user/condor and the code in this repository. The file takes input in the form [*testNum1*] [*testNum2*] [*inputfile*] [*year*] where input file is a file path.  `runRDF.C` primarily calls another file to do its work. In more detail, the file creates an rdf object t with the user defined arguments in addition to some preset arguments (including analysis year) and calls the analyzer_RDF function from `analyzer_RDF.cc` on this object. The goal of this file is to manage the RDF instance and include any extra functions also included in this repository.

- `analyzer_RDF.h` - This file contains the class and the constructor. The constructor is where the list of rootfiles in prepared from the file path and input range for the RDataFrame constructor in the .cc file.  There are variables that are set her such as several booleans, the sample name, and the year.

- `analyzer_RDF.cc` - This file is where the data begins being altered. The key function in this file is analyzer_RDF. This function takes in the user input and creates a dataframe. Initially, the function performs some preprocessing, setting up necessary variables for analysis. Then, the function implements the LWTNN library. Next, the function applies some flags and filtering to narrow the dataset down to only include necessary and "good" events. Finally, the function performs an analysis on the now cut data and creates a final snapshot file as an output. Note this cc file has a corresponding header file.

So, in summary, the flow is `runRDF.C` -> `analyzer_RDF.h`-> `analyzer_RDF.cc` with `runRDF.C` being the only file the user needs to interact with at runtime.

----------------------------------------------------------------

## Condor Files

- `runCondorJobs.py` - This is the main file for submitting condor jobs.  Instructions on how to run it are given above in the Getting Started Section.  The first argument is used to determine whether the program will make a list of all the root files.  This is a long process, and it is recommended to do this step seperately and then proceed to submitting condor jobs.  The second argument is used to determine whether the program will submit condor jobs based on the variables at the top of the file.  These variables are described in the bullet points below. Either filesPerJob or jobsPerSample will be used for each sample. filesPerJob is the default, and you can change a specific sample from filesPerJob to jobsPerSample with the if statement on line 83.
  - *sample_dic:* The name of a dictionary from samples.py containing the samples you want to loop over to submit
  - *filesPerJob:* The number of files submitted with each job
  - *jobsPerSample:* Number of jobs that will be submitted per sample

- `samples.py` - This file contains all the information about the different samples used in the analysis.  At the top is a class definiton stating the types of information we store about each sample.  Following that, all the samples are initialized into classes and saved to names that are the same as the prefix attribute.  The final part of the file contains several different dictionaries that group these classes together into a form that allows us to iterate over them.

- `condorRDF.sh` - This bash script is called within each condor job.  The user will not directly interact with this script.  It takes in several parameters, sets up the environment, calls runRDF.C, and moves files around accordingly.

HowThingsWork.md contains additional information.

----------------------------------------------------------------

## Machine Learning Files

In addition to these files, there are three primary python files.

- `root2NPZ.py` - This file takes the output of the RDF scripts and performs some further selections and cuts to make the data useful for training machine learning models. The output of this file is a numpy array (stored as a .npz) which stores an archive of the data. The archive contains a set of subarrays, one for each background type and signal mass. The second dimension is events and the third is features.

- `trainMLP.py` - This file takes the output of `root2NPZ` and trains a model on it. This model is a multilayer perceptron. This file trains this models, testsit on the testing data, and creates some plots analyzing the performance of the classifier. At the end, this models are saved to an h5 file along with a data scaler so they can be passed back into the RDF scripts to generate better plots. The input directory for this script should be pointed to the output directory of `root2NPZ.py`.

----------------------------------------------------------------

## Questions and Issues

- If your ROOT is not found by the program you are trying to run, submit the following command and run the code again.
`$ cmsenv`

 <br />

- If you are getting an error related to the macro or something that looks like what you have below, make sure the double quotes are straight up and down.  If they get autocorrected to their curly form, then it will output an error that looks like the one below.

```bash
Error in <TUnixSystem::SplitAclicMode>: Cannot parse argument in ”2016APVUL")
Warning in <TApplication::GetOptions>: macro ”2016APVUL") not found
Processing runRDF.C("-bash","condor/ZZ2016APVUL.txt",...
Error in <TApplication::ExecuteFile>: macro runRDF.C("-bash","condor/ZZ2016APVUL.txt", not found in path .:/cvmfs/cms.cern.ch/slc7_amd64_gcc820/lcg/root/6.18.04-nmpfii/macros
```
