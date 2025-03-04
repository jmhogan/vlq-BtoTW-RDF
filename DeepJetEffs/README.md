### DeepJet b-tagging efficiency calculation

The files `analyzer_taggerEff.cc` and `.h` are C++ scripts that define a class called `rdf` (acronym for RDataFrame). The main action of this class is to open a list of NanoAOD ROOT files, build an `RDataFrame` object from them, and perform database operations to create the histograms we will need for efficiency calculations.

## installation

Clone this repository in the same area used for TIMBER:

```
cd nobackup/BBto2B4Tau/ # check spelling!
git clone -b run3 https://github.com/jmhogan/vlq-BtoTW-RDF.git
cd vlq-BtoTW-RDF/DeepJetEffs/
```

## Editing for Run 3:

 - `analyzer_taggerEff.cc`:
    - Swap years wherever they appear: 2016APV, 2016, 2017, 2018 --> 2022, 2022EE, 2023, 2023BPix
    - Grab the correct "deepJet loose" and "deepJet medium" numerical values
    - In the jet block of definitions, 3 extra "numerator" definitions should be added that slice using the deepJet medium values
    - In the histogram block of definitions, 3 extra "numerator" histograms should be added using the new numerator definitions
 - `runallbtageffs.sh` is a "shell script", which is basically a collection of command-line instructions grouped into a script for convenience
    - Swap years! Search-replace would likely be helpful, there will be a lot of them
    - See the comment at the top for suggestions
 - `plotDeepFlav.C`
    - Swap years!
    - See the comment at the top for suggestions
    - This script has 8 repetitive segments that do the same thing for each year and loose/medium. Check out the first segment to see what's doing with the histograms to create a ratio, and then make a nice plot.

## Running the analysis

ROOT has a built-in C++ interpreter called CINT. We therefore don't need to compile this C++ code using a Makefile or explicit g++ command. Instead, we have a "ROOT macro" called `runEff.C` that will create an instance of the `rdf` class and call the `analyzer_taggerEff` member function. Test your edits by running the analyzer once:

```
cd ../CMSSW_13_2_10/
cmsenv
cd ../vlq-BtoTW-RDF/DeepJetEffs/
root -l -b -q runEff.C\(\"0\",\"999\",\"../condor/NanoList/BBTo2B4Tau_M400_2022NanoList.txt\",\"2022\"\)
```

If this fails it should do so fairly dramatically! If it succeeds it should print a report with cut statistics similar to the output of the TIMBER script.
After any debugging, prepare `runallbtageffs.sh` to run all of the analyses in sequence. Pipe the output to a log file and run it in the "background" so that you can disconnect from the cluster:

```
sh runallbtageffs.sh > output.log 2>&1 &  # 2>&1 pipes all output, including errors, to the file. The final & runs the job in the background
```

If the plotting worked, great! If it had errors, fit and rerun just the plotting commands at the end of the shell script.


