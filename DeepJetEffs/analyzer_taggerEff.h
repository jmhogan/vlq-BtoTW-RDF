//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Mon Nov 16 20:39:17 2015 by ROOT version 6.02/05
// from TTree ljmet/ljmet
// found on file: /eos/uscms/store/user/lpcljm/LJMet_1lep_110915/X53X53_M-800_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_25ns/X53X53_M-800_RH_TuneCUETP8M1_13TeV-madgraph-pythia8_25ns_1.root
//////////////////////////////////////////////////////////

#ifndef rdf_h
#define rdf_h
#pragma once

#include <iostream>
#include <fstream>
#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include "TH1.h"
#include "TF1.h"

// Header file for the classes stored in the TTree if any.
#include "vector"
#include <string>
#include "TLorentzVector.h"
#include "ROOT/RDataFrame.hxx"
#include "ROOT/RVec.hxx"

using namespace std;

class rdf
{
private:
  TTree *inputTree; //! pointer to the analyzed TTree or TChain
  TFile *inputFile;
  TString psOutName, fsOutName;
  Int_t fCurrent; //! current Tree number in a TChain
  vector<string> files;

  string sample;
  string year;
  string era;
  string jecera;
  bool   isMC;

  // Fixed size dimensions of array or collections stored in the TTree if any.
public:
  // Main Methods
  rdf(string inputFileName, string testNum1, string testNum2, string yearIn);
  virtual ~rdf();
  virtual void analyzer_taggerEff(TString testNum, TString jesvar);
};

#endif

#ifdef rdf_cxx

rdf::rdf(string inputFileName, string testNum1, string testNum2, string yearIn) : inputTree(0), inputFile(0)
{
  // Make the vector with the text file listed in the input
  cout << "Input File Path: " << inputFileName << endl;
  ifstream listFiles;
  listFiles.open(inputFileName);

  string file = "";
  int i = 0;
  int start = atoi(testNum1.c_str());
  int end = atoi(testNum2.c_str());
  cout << "TestNum 1: " << start << " and TestNum 2: " << end << endl;

  if (listFiles.is_open())
  {
    while (listFiles >> file)
    {
      if (i >= start && i <= end) {
        files.push_back(file);
        cout << "files: " << file << endl;

      }
      i++;
    }
  }
  cout << "Number of Entries: " << files.size() << endl;

  TString sampleName = file;
  cout << "Sample Name: " << sampleName << endl;

  isMC = !(sampleName.Contains("Single") || sampleName.Contains("Data18") || sampleName.Contains("EGamma"));
  year = yearIn;
  
  TObjArray *tokens = sampleName.Tokenize("/");
  sample = ((TObjString *)(tokens->At(5)))->String();
  string ver;
  if(!isMC){ 
    string runera = (((TObjString *)(tokens->At(4)))->String()).Data();
    string process = (((TObjString *)(tokens->At(7)))->String()).Data();
    era = runera.back();
    ver = process.substr(process.find("_")+1,2);
  } 
  delete tokens;

  jecera = era;
  if(!isMC){
    if(year == "2022") jecera = "CD";
    else if(year == "2023"){
      if(ver != "v4") jecera = "Cv123";
      else jecera = "Cv4";
    }
  }

  if(isMC){
    if(sampleName.Contains("_ext1")) era = "ext1";
    if(sampleName.Contains("_ext2")) era = "ext2";
    if(sampleName.Contains("_ext3")) era = "ext3";
  }

}

rdf::~rdf()
{
  if (!inputTree)
    return;
  delete inputTree->GetCurrentFile();
}


#endif // #ifdef rdf_cxx
