#include "lumiMask.cc"
#include "analyzer_RDF.cc"
#include "BPrime.cc"   // reco functions
#include "cleanJet.cc" // assignleps
#include "generatorInfo.cc" // generator truth
#include "utilities.cc" // many things
#include "W_t_reco.cc" // leptonic reco
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

void runRDF(string testNum1, string testNum2, string inputFile, string year)
{
  rdf t(inputFile, testNum1, testNum2, year); // names get set to class members, should be known w/o passing

  //t.analyzer_RDF(testNum1);

  bool isData = false;
  if(inputFile.find("Single") != std::string::npos || inputFile.find("EGamma") != std::string::npos) isData = true;

  if(isData) t.analyzer_RDF(testNum1,"Nominal");
  else{
    vector<TString> shifts = {"Nominal","JECup","JECdn","JERup","JERdn"};
    for(size_t i = 0; i < shifts.size(); i++){
      cout << "\nRunning shift " << shifts[i] << endl;

      t.analyzer_RDF(testNum1,shifts[i]);

      cout << "\nFinished shift " << shifts[i] << endl;
    }
  }
  cout << "\nFinished all analyzing" << endl;

};
