// --------------------------------------------------------------------------------------- //
// Implimentation of RDataFrame in C++.					                   //
// Comments on creating a singly produced VLQ search			                   //
// To Run on Command Line:   root -l callRDF.C\(\"Muon(OR)Electron\",\"testNumber\"\,\"root://cmsxrootd.fnal.gov//store/...file.root\")      //
// --------------------------------------------------------------------------------------- //

#define rdf_cxx
#include "analyzer_taggerEff.h"
#include "ROOT/RDataFrame.hxx"
#include "ROOT/RVec.hxx"
#include "Math/Vector4D.h"
#include <TFile.h>
#include <TChain.h>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <cmath>
#include <TCanvas.h>
#include <TStyle.h>
#include <TH3.h>
#include <algorithm> // std::sort
#include <TFile.h>
#include <TH1.h>
#include <TF1.h>
#include <TVector2.h>
#include <TRandom3.h>
#include <sstream>
#include <chrono> // for high_resolution_clock

using namespace std;

void rdf::analyzer_taggerEff(TString testNum, TString jesvar)
{
  ROOT::EnableImplicitMT();
  TStopwatch time;
  time.Start();
  string sample = this->sample;
  string year = this->year;
  bool isMC = this->isMC;

  bool debug = false;
  
  cout << "Sample in cc: " << sample << endl;
  cout << "Year in cc: " << year << endl;
  cout << "isMC? " << isMC << ", jesvar = " << jesvar << endl;
  if(!isMC) cout << "Data era = " << era << ", for jec " << jecera << endl;

  // ADJUST THESE YEARS AND VALUES FOR 2022 and 2023
  float deepjetL;
  if(year == "2016APV") deepjetL = 0.0508;
  else if(year == "2016") deepjetL = 0.0480;
  else if(year == "2017") deepjetL = 0.0532;
  else if(year == "2018") deepjetL = 0.0490;

  // ADJUST THESE YEARS AND VALUES FOR 2022 and 2023
  float deepjetM;
  if(year == "2016APV") deepjetM = 0.0508;
  else if(year == "2016") deepjetM = 0.0480;
  else if(year == "2017") deepjetM = 0.0532;
  else if(year == "2018") deepjetM = 0.0490;

  // -------------------------------------------------------
  //               Open Dataframe + select jets
  // -------------------------------------------------------

  auto rdf_input = ROOT::RDataFrame("Events", files); // Initial data
      
  auto JetSelect = rdf_input.Filter("nJet > 0","Pass 1 jet with pt > 15") // there should be at least one jet!
    .Define("weight","genWeight/abs(genWeight)") // positive or negative "weight" from simulation
    .Define("goodcleanJets", "abs(Jet_eta) < 2.5 && Jet_jetId > 1") // jets live in the central region and pass the noise id
    .Filter("(int) Sum(goodcleanJets) > 0","Pass 1 central jet passing loose ID") // there's at least one GOOD jet
    .Define("gcJet_pt","Jet_pt[goodcleanJets == true]") // list of good jet momentum
    .Define("gcJet_hflav","Jet_hadronFlavour[goodcleanJets == true]") // list of good jet quark type from simulation
    .Define("gcJet_deepjet","Jet_btagDeepFlavB[goodcleanJets == true]") // list of good jet b-tagging deep network score
    .Define("bJet_pt","gcJet_pt[gcJet_hflav == 5]") // sublist of pt for only b-flavor jets
    .Define("cJet_pt","gcJet_pt[gcJet_hflav == 4]") // sublist of pt for only c-flavor jets
    .Define("lJet_pt","gcJet_pt[gcJet_hflav < 4]")  // sublist of pt for only lighter quark jets
    .Define("bJet_pt_loose",Form("gcJet_pt[gcJet_hflav == 5 && gcJet_deepjet > %f]",deepjetL)) // sublist for b-flavor + passing tag
    .Define("cJet_pt_loose",Form("gcJet_pt[gcJet_hflav == 4 && gcJet_deepjet > %f]",deepjetL)) // sublist for c-flavor + passing tag
    .Define("lJet_pt_loose",Form("gcJet_pt[gcJet_hflav < 4 && gcJet_deepjet > %f]",deepjetL));  // sublist for light + passing tag
  // MAKE 3 MORE .Define STATEMENTS HERE FOR THE MEDIUM TAGGING CRITERIA (and move the ; to the end)


  double ptbins[16] = {15,20,30,50,70,100,150,200,300,400,500,600,800,1000,1200,1500};

  // denominator histograms from the flavor-specific pt sublists
  auto h1 = JetSelect.Histo1D({"BEff_Dptbins_b",";Jet p_T (GeV);",15,ptbins},"bJet_pt","weight");
  auto h2 = JetSelect.Histo1D({"BEff_Dptbins_c",";Jet p_T (GeV);",15,ptbins},"cJet_pt","weight");
  auto h3 = JetSelect.Histo1D({"BEff_Dptbins_udsg",";Jet p_T (GeV);",15,ptbins},"lJet_pt","weight");

  // numerator histograms from the "flavor + passing tag" pt sublists
  auto h4 = JetSelect.Histo1D({"BEffLoose_Nptbins_b",";Jet p_T (GeV);DeepJetL: b efficiency",15,ptbins},"bJet_pt_loose","weight");
  auto h5 = JetSelect.Histo1D({"BEffLoose_Nptbins_c",";Jet p_T (GeV);DeepJetL: c efficiency",15,ptbins},"cJet_pt_loose","weight");
  auto h6 = JetSelect.Histo1D({"BEffLoose_Nptbins_udsg",";Jet p_T (GeV);DeepJetL: udsg efficiency",15,ptbins},"lJet_pt_loose","weight");
  // MAKE 3 NEW HISTOGRAMS HERE FOR MEDIUM TAGGING CRITERIA
  
  // -------------------------------------------------
  // 		Save histos to file
  // -------------------------------------------------
  
  cout << "-------------------------------------------------" << endl
       << ">>> Saving " << sample << " Snapshot..." << endl;
  TString finalFile = "RDF_" + sample + "_" + year + "_DeepJetEff.root";
  const char *stdfinalFile = finalFile;

  TFile::Open(finalFile,"recreate");
  h1->Write();
  h2->Write();
  h3->Write();
  h4->Write();
  h5->Write();
  h6->Write();

  time.Stop();
  time.Print();
  
  cout << "Cut statistics:" << endl;
  JetSelect.Report()->Print();

  cout << "Done!" << endl;
}
