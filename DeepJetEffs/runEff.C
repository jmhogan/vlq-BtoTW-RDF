#include "analyzer_taggerEff.cc"
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

  t.analyzer_taggerEff(testNum1,"Nominal");


};
