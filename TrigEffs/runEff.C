#include "analyzer_trigEff.cc"
#include "utilities.cc"
#include "../lumiMask.cc"
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

void runEff(string testNum1, string testNum2, string inputFile, string year)
{
  rdf t(inputFile, testNum1, testNum2, year); // names get set to class members, should be known w/o passing

  //t.analyzer_RDF(testNum1);

  bool isData = false;
  if(inputFile.find("Single") != std::string::npos || inputFile.find("EGamma") != std::string::npos) isData = true;

  if(isData) t.analyzer_trigEff(testNum1,"Nominal");
  else{
    vector<TString> shifts = {"Nominal"}; //,"JECup","JECdn","JERup","JERdn"};
    for(size_t i = 0; i < shifts.size(); i++){
      cout << "\nRunning shift " << shifts[i] << endl;

      t.analyzer_trigEff(testNum1,shifts[i]);

      cout << "\nFinished shift " << shifts[i] << endl;
    }
  }
  cout << "\nFinished all analyzing" << endl;

};
