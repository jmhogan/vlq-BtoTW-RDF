#!/bin/bash

## ADJUST ALL THE YEARS TO 2022, 2022EE, 2023, 2023BPix
## ADJUST ALL THE NANOAOD FILE LIST NAMES
## 0, 999 can be left alone (it will process all the files in the lists, there are definitely not > 999 of them)
## RUN MASS 400, 1000, 1600 for each of the 4 years
## PLOT MASS 400, 1000, 1600

## Can test that one of them runs, and then uncomment the entire group.
echo "2018 800..."
root -l -b -q runEff.C\(\"0\",\"999\",\"../condor/NanoList/Bprime_M800_2018ULNanoList.txt\",\"2018\"\)

# echo "2017 800..."
# root -l -b -q runEff.C\(\"0\",\"999\",\"../condor/NanoList/Bprime_M800_2017ULNanoList.txt\",\"2017\"\)

# echo "2016 800..."
# root -l -b -q runEff.C\(\"0\",\"999\",\"../condor/NanoList/Bprime_M800_2016ULNanoList.txt\",\"2016\"\)

# echo "2016APV 800..."
# root -l -b -q runEff.C\(\"0\",\"999\",\"../condor/NanoList/Bprime_M800_2016APVULNanoList.txt\",\"2016APV\"\)

# echo "2018 1400..."
# root -l -b -q runEff.C\(\"0\",\"999\",\"../condor/NanoList/Bprime_M1400_2018ULNanoList.txt\",\"2018\"\)

# echo "2017 1400..."
# root -l -b -q runEff.C\(\"0\",\"999\",\"../condor/NanoList/Bprime_M1400_2017ULNanoList.txt\",\"2017\"\)

# echo "2016 1400..."
# root -l -b -q runEff.C\(\"0\",\"999\",\"../condor/NanoList/Bprime_M1400_2016ULNanoList.txt\",\"2016\"\)

# echo "2016APV 1400..."
# root -l -b -q runEff.C\(\"0\",\"999\",\"../condor/NanoList/Bprime_M1400_2016APVULNanoList.txt\",\"2016APV\"\)

# echo "2018 2000..."
# root -l -b -q runEff.C\(\"0\",\"999\",\"../condor/NanoList/Bprime_M2000_2018ULNanoList.txt\",\"2018\"\)

# echo "2017 2000..."
# root -l -b -q runEff.C\(\"0\",\"999\",\"../condor/NanoList/Bprime_M2000_2017ULNanoList.txt\",\"2017\"\)

# echo "2016 2000..."
# root -l -b -q runEff.C\(\"0\",\"999\",\"../condor/NanoList/Bprime_M2000_2016ULNanoList.txt\",\"2016\"\)

# echo "2016APV 2000..."
# root -l -b -q runEff.C\(\"0\",\"999\",\"../condor/NanoList/Bprime_M2000_2016APVULNanoList.txt\",\"2016APV\"\)

#echo "Plotting 800..."
#root -l -b -q plotDeepFlav.C\(\"800\"\)

#echo "Plotting 1400..."
#root -l -b -q plotDeepFlav.C\(\"1400\"\)

#echo "Plotting 2000..."
#root -l -b -q plotDeepFlav.C\(\"2000\"\)

