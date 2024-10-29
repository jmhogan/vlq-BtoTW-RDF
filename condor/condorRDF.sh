#!/bin/bash

hostname
export SCRAM_ARCH=el8_amd64_gcc11
echo $SCRAM_ARCH

# Take in Input Arguments
infilename=${1}  # Filename is a really long string
outputDir=${2}
testnum1=${3}
testnum2=${4}
year=${5}

# Print out Input Arguments
echo "filename: ${infilename}"
echo "output dir: ${outputDir}"
echo "testnum1: ${testnum1}"
echo "testnum2: ${testnum2}"
echo "year: ${year}"

# Setup Environment
scratch=${PWD}  
macroDir=${PWD}
source /cvmfs/cms.cern.ch/cmsset_default.sh
scramv1 project CMSSW CMSSW_13_0_18
cd CMSSW_13_0_18
cmsenv

# Unpack the tar file
echo "unpacking tar"
tar -xf ${scratch}/rdfjobs.tar
rm ${scratch}/rdfjobs.tar

eval `scramv1 runtime -sh`
cd src/vlq-BtoTW-RDF/

export PATH=$PATH:$macroDir

# Run analyzer_RDF files through two C files
echo "Running RDF:"
#root -l -b -q runRDF.C\(\"testnum1\",\"testnum2\",\"infilename\",\"year\"\) 
root -l -b -q runRDF.C\(\"${testnum1}\",\"${testnum2}\",\"${infilename}\",\"${year}\"\) 

# Viewing ROOT Files
echo "ROOT Files:"
ls -l *${testnum1}*.root

# Remove our copy of the files to clean up
# echo "Removing presel files:"
# rm *preselTree*.root

# Copy Output to EOS
echo "xrdcp output for condor"
for FILE in *${testnum1}*.root
do
  echo "xrdcp -f ${FILE} root://cmseos.fnal.gov/${outputDir}/${FILE}"
  xrdcp -f ${FILE} root://cmseos.fnal.gov/${outputDir}/${FILE} 2>&1
  XRDEXIT=$?
  if [[ $XRDEXIT -ne 0 ]]; then
    rm *.root
    echo "exit code $XRDEXIT, failure in xrdcp"
    exit $XRDEXIT
  fi
  rm ${FILE}
done

echo "fully done through copying"
