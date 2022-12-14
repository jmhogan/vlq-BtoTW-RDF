#include "analyzer_RDF.cpp"
#include "cleanJet.cc"
#include "dnnPrep.cc"
#include "W_t_reco.cc"
#include "BPrime.cc"
// Going to need new root files

void runRDF(TString testNum, std::string inputFile)
{

	rdf t(inputFile,"preselTree_"+testNum,"finalselTree_"+testNum); // names get set to class members, should be known w/o passing
	int year = 2017;

	t.analyzer_RDF(inputFile, testNum ,year);
};
