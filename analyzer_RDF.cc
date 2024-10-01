// --------------------------------------------------------------------------------------- //
// Implimentation of RDataFrame in C++.					                   //
// Comments on creating a singly produced VLQ search			                   //
// To Run on Command Line:   root -l callRDF.C\(\"Muon(OR)Electron\",\"testNumber\"\,\"root://cmsxrootd.fnal.gov//store/...file.root\")      //
// --------------------------------------------------------------------------------------- //

#define rdf_cxx
#include "analyzer_RDF.h"
#include "lumiMask.h"
#include "ROOT/RDataFrame.hxx"
#include "ROOT/RVec.hxx"
#include "Math/Vector4D.h"
#include <TFile.h>
#include <TChain.h>
#include <string>
#include <vector>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <TFile.h>
#include <TF1.h>
#include <TVector2.h>
#include <TRandom3.h>
#include <sstream>
#include "../correctionlib/include/correction.h"

using namespace std;
using namespace ROOT::VecOps;
using correction::CorrectionSet;

void rdf::analyzer_RDF(TString testNum, TString jesvar)
{
  //  ROOT::EnableImplicitMT();
  TStopwatch time;
  time.Start();
  string sample = this->sample;
  //  int samplebin = this->samplebin;
  string year = this->year;
  bool isMC = this->isMC;

  bool debug = false;
  
  cout << "Sample in cc: " << sample << ", bin # " << samplebin << endl;
  cout << "Year in cc: " << year << endl;
  cout << "isMC? " << isMC << ", jesvar = " << jesvar << endl;
  if(!isMC) cout << "Data era = " << era << ", for jec " << jecera << endl;
  else cout << "MC extension tag (blank or ext) = " << era << endl;

  // -------------------------------------------------------
  //               Golden JSON
  // -------------------------------------------------------
  std::string jsonfile;
  if(year == "2016" or year == "2016APV") jsonfile = "Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt";
  else if(year == "2017") jsonfile = "Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt";
  else if(year == "2018") jsonfile = "Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt";
  else std::cout << "ERROR: Can't parse the year to assign a golden json file. Expected 2016, 2016APV, 2017, or 2018. Got: " << year << std::endl;
  const auto myLumiMask = lumiMask::fromJSON(jsonfile);
  //  std::cout << "Testing the JSON! Known good run/lumi returns: " << myLumiMask.accept(315257, 10) << ", and known bad run returns: " << myLumiMask.accept(315257, 90) << std::endl;
  auto goldenjson = [myLumiMask](unsigned int &run, unsigned int &luminosityBlock){return myLumiMask.accept(run, luminosityBlock);};
  
  // -------------------------------------------------------
  //               Self-derived corrections
  // -------------------------------------------------------
  
  // polynomials defined in the .h
  TF1 *poly2 = this->poly2;
  TF1 *poly2U = this->poly2U;
  TF1 *poly2D = this->poly2D;
  TF1 *polyHT = this->polyHT;
  TF1 *polyHTU = this->polyHTU;
  TF1 *polyHTD = this->polyHTD;
  auto wjetHTpoly = [poly2,poly2U,poly2D](float &LHE_HT){RVec<double> sf = {poly2->Eval(LHE_HT),poly2U->Eval(LHE_HT),poly2D->Eval(LHE_HT)}; return sf;};
  auto topHTpoly = [polyHT,polyHTU,polyHTD](float &AK4HT){RVec<double> sf = {polyHT->Eval(AK4HT),polyHTU->Eval(AK4HT),polyHTD->Eval(AK4HT)}; return sf;};

  // Lepton scale factors not in correctionLib
  std::vector<std::vector<float>> elecidsfs = this->elIDSF;
  std::vector<std::vector<float>> elecidsfuncs = this->elIDSFUnc;  
  std::vector<std::vector<float>> elecisosfs = this->elISOSF;
  float elecisosfunc = this->elISOSFUnc;  
  std::vector<std::vector<float>> muonisosfs = this->muISOSF;
  std::vector<std::vector<float>> elechltsfs = this->elHLTSF;
  std::vector<std::vector<float>> elechltuncs = this->elHLTSFUnc;
  std::vector<std::vector<float>> muonhltsfs = this->muHLTSF;
  std::vector<std::vector<float>> muonhltuncs = this->muHLTSFUnc;

  std::vector<float> elid_pts = {50,100,200,99999}; // from susy double disco UMN paper, UL
  std::vector<float> elsf_etas = {-2.5, -2.0, -1.566, -1.442, -0.8, 0.0, 0.8, 1.442, 1.566, 2.0, 2.5};
  std::vector<float> muiso_pts = {50,60,99999};
  std::vector<float> musf_etas = {0,0.9,1.2,2.1,2.4};
  std::vector<float> elhlt_pts = {55,120,200,99999}; 
  std::vector<float> muhlt_pts = {55,60,120,200,300,99999};
  float muonisosfunc = 0.002;

  // DeepJet Loose efficiencies
  std::vector<float> btagpts = this->btagpts;
  std::vector<std::vector<float>> btageffs = this->btageffs;

  // ParticleNet Top and W efficiencies
  // std::vector<float> pnetpts = this->pnetpts;
  // std::vector<std::vector<float>> pnet_t_t = this->pnet_t_t;
  // std::vector<std::vector<float>> pnet_t_W = this->pnet_t_W;
  // std::vector<std::vector<float>> pnet_W_t = this->pnet_W_t;
  // std::vector<std::vector<float>> pnet_W_W = this->pnet_W_W;
  // std::vector<std::vector<float>> pnet_J_t = this->pnet_J_t;
  // std::vector<std::vector<float>> pnet_J_W = this->pnet_J_W;
  
  // -------------------------------------------------------
  //               correctionLib corrections
  // -------------------------------------------------------
  
  std::string yrstr, yr, jecyr, jeryr, jecver;
  float deepjetL;
  int pubit = 0;
  if(year == "2016APV") {deepjetL = 0.0508; yrstr = "2016preVFP"; yr = "16"; jecyr = "UL16APV"; jeryr = "Summer20UL16APV_JRV3"; jecver = "V7";}
  else if(year == "2016") {deepjetL = 0.0480; yrstr = "2016postVFP"; yr = "16"; jecyr = "UL16"; jeryr = "Summer20UL16_JRV3"; jecver = "V7";}
  else if(year == "2017") {pubit = 2; deepjetL = 0.0532; yrstr = "2017"; yr = "17"; jecyr = "UL17"; jeryr = "Summer19UL17_JRV2"; jecver = "V5";}
  else if(year == "2018") {pubit = 2; deepjetL = 0.0490; yrstr = "2018"; yr = "18"; jecyr = "UL18"; jeryr = "Summer19UL18_JRV2"; jecver = "V5";}
  else std::cout << "ERROR: Can't parse the year to assign correctionLib json files. Expected 2016, 2016APV, 2017, or 2018. Got: " << year << std::endl;

  auto pileupcorrset = CorrectionSet::from_file("/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/LUM/"+yrstr+"_UL/puWeights.json.gz");
  auto electroncorrset = CorrectionSet::from_file("/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/EGM/"+yrstr+"_UL/electron.json.gz");
  auto muoncorrset = CorrectionSet::from_file("/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/MUO/"+yrstr+"_UL/muon_Z.json.gz");
  auto btagcorrset = CorrectionSet::from_file("/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/BTV/"+yrstr+"_UL/btagging.json.gz");
  auto jetvetocorrset = CorrectionSet::from_file("/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/JME/"+yrstr+"_UL/jetvetomaps.json.gz");
  auto jmarcorrset = CorrectionSet::from_file("/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/JME/"+yrstr+"_UL/jmar.json.gz");
  auto metcorrset = CorrectionSet::from_file("/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/JME/"+yrstr+"_UL/met.json.gz");

  auto pileupcorr = pileupcorrset->at("Collisions"+yr+"_UltraLegacy_goldenJSON"); std::cout << "\t loaded pileup" << std::endl;
  auto electroncorr = electroncorrset->at("UL-Electron-ID-SF"); std::cout << "\t loaded elec id" << std::endl;
  auto muoncorr = muoncorrset->at("NUM_TrackerMuons_DEN_genTracks"); std::cout << "\t loaded muon reco" << std::endl;
  auto muonidcorr = muoncorrset->at("NUM_MediumID_DEN_TrackerMuons"); std::cout << "\t loaded muon id" << std::endl;
  auto btagcorr = btagcorrset->at("deepJet_shape"); std::cout << "\t loaded btags" << std::endl;
  auto btagwpbccorr = btagcorrset->at("deepJet_comb"); std::cout << "\t loaded btags" << std::endl;
  auto btagwplcorr = btagcorrset->at("deepJet_incl"); std::cout << "\t loaded btags" << std::endl;
  auto jetvetocorr = jetvetocorrset->at("Summer19UL"+yr+"_V1"); std::cout << "\t loaded jet veto (only applied for 2018 HEM1516)" << std::endl;
  auto topcorr = jmarcorrset->at("ParticleNet_Top_Nominal"); std::cout << "\t loaded ParticleNet top" << std::endl;
  auto Wcorr = jmarcorrset->at("ParticleNet_W_Nominal"); std::cout << "\t loaded ParticleNet W" << std::endl;
  auto pujetcorr = jmarcorrset->at("PUJetID_eff"); std::cout << "\t loaded PU Jet ID" << std::endl;
  auto metptcorr = metcorrset->at("pt_metphicorr_pfmet_mc"); std::cout << "\t loaded met pt xy" << std::endl;
  auto metphicorr = metcorrset->at("phi_metphicorr_pfmet_mc"); std::cout << "\t loaded met phi xy" << std::endl;
  if(!isMC){metptcorr = metcorrset->at("pt_metphicorr_pfmet_data"); metphicorr = metcorrset->at("phi_metphicorr_pfmet_data");}
  
  auto ak4corrset = CorrectionSet::from_file("jsonpog-integration/POG/JME/"+yrstr+"_UL/jet_jerc.json"); 
  auto ak8corrset = CorrectionSet::from_file("jsonpog-integration/POG/JME/"+yrstr+"_UL/fatJet_jerc.json"); 
  auto ak4corr = ak4corrset->compound().at("Summer19"+jecyr+"_"+jecver+"_MC_L1L2L3Res_AK4PFchs"); std::cout << "\t loaded jerc MC" << std::endl;
  auto ak4corrL1 = ak4corrset->at("Summer19"+jecyr+"_"+jecver+"_MC_L1FastJet_AK4PFchs"); std::cout << "\t loaded jerc L1" << std::endl;
  if(!isMC){ ak4corr = ak4corrset->compound().at("Summer19"+jecyr+"_Run"+jecera+"_"+jecver+"_DATA_L1L2L3Res_AK4PFchs"); std::cout << "\t loaded jerc data" << std::endl;}
  auto ak4corrUnc = ak4corrset->at("Summer19"+jecyr+"_"+jecver+"_MC_Total_AK4PFchs"); std::cout << "\t loaded jec unc" << std::endl;
  
  auto ak4ptres = ak4corrset->at(jeryr+"_MC_PtResolution_AK4PFchs"); std::cout << "\t loaded pt res" << std::endl;
  auto ak4jer = ak4corrset->at(jeryr+"_MC_ScaleFactor_AK4PFchs"); std::cout << "\t loaded jer" << std::endl;
  auto ak8corr = ak8corrset->compound().at("Summer19"+jecyr+"_"+jecver+"_MC_L1L2L3Res_AK8PFPuppi"); std::cout << "\t loaded fat jerc MC" << std::endl;
  if(!isMC){ ak8corr = ak8corrset->compound().at("Summer19"+jecyr+"_Run"+jecera+"_"+jecver+"_DATA_L1L2L3Res_AK8PFPuppi"); std::cout << "\t loaded fat jerc data" << std::endl;}
  auto ak8corrUnc = ak8corrset->at("Summer19"+jecyr+"_"+jecver+"_MC_Total_AK8PFPuppi"); std::cout << "\t loaded fat jec unc" << std::endl;
  
  auto pnetWPs = [year](const RVec<float> &dnnT, const RVec<float> &dnnW){
    float wpT, wpW;
    if(year == "2016APV"){wpT = 0.490; wpW = 0.677;}
    else if(year == "2016"){wpT = 0.495; wpW = 0.668;}
    else if(year == "2017"){wpT = 0.581; wpW = 0.709;}
    else{wpT = 0.580; wpW = 0.700;}
    RVec<int> tag;
    for(int i=0; i<dnnT.size(); i++){
      int tagval = 0; // will stay 0 if not t, W
      if(dnnT[i] > wpT) tagval += 1; // 1 if only top, 3 if top or W
      if(dnnW[i] > wpW) tagval += 2; // 2 if only W, 3 if top or W
      tag.push_back(tagval);
    }
    return tag;
  };

  auto pufunc = [pileupcorr](const float &numTrueInt){
    RVec<double> pu = {pileupcorr->evaluate({numTrueInt, "nominal"}), pileupcorr->evaluate({numTrueInt, "up"}), pileupcorr->evaluate({numTrueInt, "down"})};
    return pu;
  };
  auto metfunc = [metptcorr,metphicorr](const float &met, const float &phi, const int &npvs, const unsigned int &run){
    float floatrun = run;
    float floatnpvs = npvs;
    float tmpmet = met; if(tmpmet > 6500) tmpmet = 6499;
    RVec<float> corrmet = {static_cast<float>(metptcorr->evaluate({tmpmet, phi, floatnpvs, floatrun})),
			   static_cast<float>(metphicorr->evaluate({tmpmet, phi, floatnpvs, floatrun}))};
    return corrmet;
  };
  auto recofunc = [electroncorr,muoncorr,yrstr](const float &pt, const float &eta, const bool &isEl){
    RVec<double> reco;
    if(isEl == 0) { 
      reco = {muoncorr->evaluate({yrstr+"_UL",abs(eta),pt,"sf"}), 
	      muoncorr->evaluate({yrstr+"_UL",abs(eta),pt,"systup"}), 
	      muoncorr->evaluate({yrstr+"_UL",abs(eta),pt,"systdown"})};
    }else{
      reco = {electroncorr->evaluate({yrstr,"sf","RecoAbove20",eta,pt}), 
	      electroncorr->evaluate({yrstr,"sfup","RecoAbove20",eta,pt}), 
	      electroncorr->evaluate({yrstr,"sfdown","RecoAbove20",eta,pt})};
    }
    return reco;
  }; 
  auto idfunc = [muonidcorr,elid_pts,elsf_etas,elecidsfs,elecidsfuncs,yrstr](const float &pt, const float &eta, const bool &isEl){
    RVec<double> id;
    if(isEl > 0){
      int ptbin = (std::upper_bound(elid_pts.begin(), elid_pts.end(), pt) - elid_pts.begin())-1;
      int etabin = (std::upper_bound(elsf_etas.begin(), elsf_etas.end(), eta) - elsf_etas.begin())-1;
      id = {elecidsfs[ptbin][etabin], elecidsfuncs[ptbin][etabin]};      
    }else{
      id = {muonidcorr->evaluate({yrstr+"_UL",abs(eta),pt,"sf"}), 
	    muonidcorr->evaluate({yrstr+"_UL",abs(eta),pt,"systup"}), 
	    muonidcorr->evaluate({yrstr+"_UL",abs(eta),pt,"systdown"})};
    }
    return id;
  }; 
  auto isofunc = [muiso_pts,musf_etas,muonisosfs,muonisosfunc,elid_pts,elsf_etas,elecisosfs,elecisosfunc](const float &pt, const float &eta, const bool &isEl){
    RVec<double> iso;
    if(isEl > 0){
      int ptbin = (std::upper_bound(elid_pts.begin(), elid_pts.end(), pt) - elid_pts.begin())-1;
      int etabin = (std::upper_bound(elsf_etas.begin(), elsf_etas.end(), eta) - elsf_etas.begin())-1;
      iso = {elecisosfs[ptbin][etabin], elecisosfunc};      
    }else{
      int ptbin = (std::upper_bound(muiso_pts.begin(), muiso_pts.end(), pt) - muiso_pts.begin())-1;
      int etabin = (std::upper_bound(musf_etas.begin(), musf_etas.end(), abs(eta)) - musf_etas.begin())-1;
      iso = {muonisosfs[ptbin][etabin], muonisosfunc};      
    }
    return iso;
  }; 
  auto hltfunc = [muhlt_pts,musf_etas,muonhltsfs,muonhltuncs,elhlt_pts,elsf_etas,elechltsfs,elechltuncs](const float &pt, const float &eta, const bool &isEl){
    RVec<double> hlt;
    if(isEl > 0){
      int ptbin = (std::upper_bound(elhlt_pts.begin(), elhlt_pts.end(), pt) - elhlt_pts.begin())-1;
      int etabin = (std::upper_bound(elsf_etas.begin(), elsf_etas.end(), abs(eta)) - elsf_etas.begin())-1;
      hlt = {elechltsfs[etabin][ptbin], elechltuncs[etabin][ptbin]};      
    }else{
      int ptbin = (std::upper_bound(muhlt_pts.begin(), muhlt_pts.end(), pt) - muhlt_pts.begin())-1;
      int etabin = (std::upper_bound(musf_etas.begin(), musf_etas.end(), abs(eta)) - musf_etas.begin())-1;
      hlt = {muonhltsfs[etabin][ptbin], muonhltuncs[etabin][ptbin]};      
    }
    return hlt;
  }; 
  auto jetvetofunc = [jetvetocorr,year,isMC](const RVec<float> &eta, const RVec<float> &phi, const RVec<float> &pt, const RVec<int> &id, const RVec<int> &pupass, const RVec<float> &area, const unsigned int &run){
    bool isAK4 = false;
    if(ROOT::VecOps::Mean(area) < 1.0) isAK4 = true;
    RVec<double> map(eta.size(), 0.0);
    TRandom3 rand(0);
    if(year == "2018" && (run >= 319077 || (run == 1 && rand.Rndm() > 0.35))){
      for(unsigned int ijet = 0; ijet < eta.size(); ijet++){
	float phitemp = phi[ijet];
	if(phitemp < -3.14159) phitemp = -3.14159;
	else if(phitemp > 3.14159) phitemp = 3.14159;
	if(pt[ijet] > 30 && id.at(ijet) > 1 && eta[ijet] < -1.0 && eta[ijet] > -3.5 && phitemp < -0.7 && phitemp > -1.7){
	  bool passesPUID = true;
	  if(isAK4 && pt[ijet] < 50 && pupass[ijet] == 0) passesPUID = false; // only 2018, only AK4
	  if(passesPUID) map[ijet] = jetvetocorr->evaluate({"jetvetomap_hem1516",eta.at(ijet),phitemp});
	}
      }
    }
    return map;
  };
  
  std::string nominal = "central";
  if(jesvar == "JECup") nominal = "up_jes";
  else if (jesvar == "JECdn") nominal = "down_jes";
  auto btagshapefunc = [btagcorr,btagwpbccorr,btagwplcorr,btagpts,btageffs,nominal,deepjetL](const RVec<float> &pt, const RVec<float> &eta, const RVec<float> &disc, const RVec<int> &flav){
    RVec<float> weights(26, 1.0); // collect product of SFs over jets
    for(unsigned int ijet = 0; ijet < eta.size(); ijet++){
      int ptbin = (std::upper_bound(btagpts.begin(), btagpts.end(), pt.at(ijet)) - btagpts.begin())-1;
      correction::Correction::Ref wpcorr;
      float eff;
      std::vector<int> shift = {0,4};
      if(flav.at(ijet) < 4){wpcorr = btagwplcorr; eff = btageffs[ptbin][2]; shift = {4,0};}
      else if(flav.at(ijet) == 4){wpcorr = btagwpbccorr; eff = btageffs[ptbin][1];}
      else{wpcorr = btagwpbccorr; eff = btageffs[ptbin][0];}

      // if(flav.at(ijet) != 4){
      // 	weights[0] *= btagcorr->evaluate({nominal, flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // 	weights[1] *= btagcorr->evaluate({"up_hf", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // 	weights[2] *= btagcorr->evaluate({"down_hf", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // 	weights[3] *= btagcorr->evaluate({"up_lf", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // 	weights[4] *= btagcorr->evaluate({"down_lf", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // 	weights[5] *= btagcorr->evaluate({"up_hfstats1", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // 	weights[6] *= btagcorr->evaluate({"down_hfstats1", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // 	weights[7] *= btagcorr->evaluate({"up_hfstats2", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // 	weights[8] *= btagcorr->evaluate({"down_hfstats2", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // 	weights[9] *= btagcorr->evaluate({"up_lfstats1", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // 	weights[10] *= btagcorr->evaluate({"down_lfstats1", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // 	weights[11] *= btagcorr->evaluate({"up_lfstats2", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // 	weights[12] *= btagcorr->evaluate({"down_lfstats2", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // }else{
      // 	weights[0] *= btagcorr->evaluate({"central", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // 	weights[13] *= btagcorr->evaluate({"up_cferr1", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // 	weights[14] *= btagcorr->evaluate({"down_cferr1", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // 	weights[15] *= btagcorr->evaluate({"up_cferr2", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // 	weights[16] *= btagcorr->evaluate({"down_cferr2", flav.at(ijet), abs(eta.at(ijet)), pt.at(ijet), disc.at(ijet)});
      // }

      if(disc.at(ijet) > deepjetL){
	weights[17] *= wpcorr->evaluate({"central","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}); // seemed like P(Data)/P(MC) reduces to SF
	weights[18+shift[0]] *= wpcorr->evaluate({"up_correlated","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}); 
	weights[19+shift[0]] *= wpcorr->evaluate({"down_correlated","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)});
	weights[20+shift[0]] *= wpcorr->evaluate({"up_uncorrelated","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)});
	weights[21+shift[0]] *= wpcorr->evaluate({"down_uncorrelated","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)});
	weights[18+shift[1]] *= wpcorr->evaluate({"central","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)});
	weights[19+shift[1]] *= wpcorr->evaluate({"central","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)});
	weights[20+shift[1]] *= wpcorr->evaluate({"central","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)});
	weights[21+shift[1]] *= wpcorr->evaluate({"central","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)});
      }else{
	weights[17] *= (1.0-eff*wpcorr->evaluate({"central","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
	weights[18+shift[0]] *= (1.0-eff*wpcorr->evaluate({"up_correlated","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
	weights[19+shift[0]] *= (1.0-eff*wpcorr->evaluate({"down_correlated","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
	weights[20+shift[0]] *= (1.0-eff*wpcorr->evaluate({"up_uncorrelated","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
	weights[21+shift[0]] *= (1.0-eff*wpcorr->evaluate({"down_uncorrelated","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
	weights[18+shift[1]] *= (1.0-eff*wpcorr->evaluate({"central","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
	weights[19+shift[1]] *= (1.0-eff*wpcorr->evaluate({"central","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
	weights[20+shift[1]] *= (1.0-eff*wpcorr->evaluate({"central","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
	weights[21+shift[1]] *= (1.0-eff*wpcorr->evaluate({"central","L",flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
      }
    }
    return weights;      
  };

  auto pnetfunc = [topcorr,Wcorr](const RVec<float> &eta, const RVec<float> &pt, const RVec<int> &match, const RVec<int> &tag, const RVec<int> &OS){
  //auto pnetfunc = [samplebin,pnetpts,pnet_t_t,pnet_W_W,topcorr,Wcorr](const RVec<float> &eta, const RVec<float> &pt, const RVec<int> &match, const RVec<int> &tag, const RVec<int> &OS){
    // This is the classic SF weight. Btagging language is P(DATA)/P(MC) since we will require t or W tag for region 1,2 and reject for region 3,4
    // w = (prod-tagged SF*eff)*(prod-not-tagged 1-SF*eff) / (prod-tagged eff)*(prod-not-tagged 1-eff)
    // a tagged true-top/W jet contributes SF*eff/eff = SF
    // an untagged true-top/W jet contributes (1 - SF*eff)/(1-eff) --> instructed by Fabio that ParticleNet SFs do not need this. 
    // no SFs exist for any other flavor, so they contribute 1
    // save all good AK8 weights, and then just OSFJ1 weight
    RVec<float> pnetweights = {1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0};
    float topsf = 1.0; float topsfup = 1.0; float topsfdn = 1.0;
    float Wsf = 1.0; float Wsfup = 1.0; float Wsfdn = 1.0;
    int OSFJ1 = ROOT::VecOps::ArgMax(pt[OS]);
    for(unsigned int ijet = 0; ijet < pt.size(); ijet++){
      if(match[ijet] == 6 && pt[ijet] > 300 && pt[ijet] < 1200 && abs(eta[ijet]) < 2.4){
        topsf = static_cast<float>(topcorr->evaluate({eta[ijet], pt[ijet], "nom", "1p0"}));
        topsfup = static_cast<float>(topcorr->evaluate({eta[ijet], pt[ijet], "up", "1p0"}));
        topsfdn = static_cast<float>(topcorr->evaluate({eta[ijet], pt[ijet], "down", "1p0"}));
        if(tag[ijet] == 1 || tag[ijet] == 3){ // top tagged
          pnetweights[0] *= topsf;
          pnetweights[1] *= topsfup;
          pnetweights[2] *= topsfdn;
          if(ijet == OSFJ1){
            pnetweights[6] *= topsf;
            pnetweights[7] *= topsfup;
            pnetweights[8] *= topsfdn;
          }
        // }else{
        //   int ptbin = (std::upper_bound(pnetpts.begin(), pnetpts.end(), pt[ijet]) - pnetpts.begin())-1;
        //   float eff = pnet_t_t[samplebin][ptbin];
        //   pnetweights[0] *= (1.0 - topsf*eff)/(1.0 - eff);
        //   pnetweights[1] *= (1.0 - topsfup*eff)/(1.0 - eff);
        //   pnetweights[2] *= (1.0 - topsfdn*eff)/(1.0 - eff);
        //   if(ijet == OSFJ1){
        //     pnetweights[6] *= (1.0 - topsf*eff)/(1.0 - eff);
        //     pnetweights[7] *= (1.0 - topsfup*eff)/(1.0 - eff);
        //     pnetweights[8] *= (1.0 - topsfdn*eff)/(1.0 - eff);
        //   }
        }
      }else if(match[ijet] == 24 && pt[ijet] > 200 && pt[ijet] < 800 && abs(eta[ijet]) < 2.4){
        Wsf = static_cast<float>(Wcorr->evaluate({eta[ijet], pt[ijet], "nom", "1p0"}));
        Wsfup = static_cast<float>(Wcorr->evaluate({eta[ijet], pt[ijet], "up", "1p0"}));
        Wsfdn = static_cast<float>(Wcorr->evaluate({eta[ijet], pt[ijet], "down", "1p0"}));
        if(tag[ijet] == 2 || tag[ijet] == 3){ // W tagged
          pnetweights[3] *= Wsf;
          pnetweights[4] *= Wsfup;
          pnetweights[5] *= Wsfdn;
          if(ijet == OSFJ1){
            pnetweights[9] *= Wsf;
            pnetweights[10] *= Wsfup;
            pnetweights[11] *= Wsfdn;
          }
         // }else{
         //  int ptbin = (std::upper_bound(pnetpts.begin(), pnetpts.end(), pt[ijet]) - pnetpts.begin())-1;
         //  float eff = pnet_W_W[samplebin][ptbin];
         //  pnetweights[3] *= (1.0 - Wsf*eff)/(1.0 - eff);
         //  pnetweights[4] *= (1.0 - Wsfup*eff)/(1.0 - eff);
         //  pnetweights[5] *= (1.0 - Wsfdn*eff)/(1.0 - eff);
         //  if(ijet == OSFJ1){
         //    pnetweights[9] *= (1.0 - Wsf*eff)/(1.0 - eff);
         //    pnetweights[10] *= (1.0 - Wsfup*eff)/(1.0 - eff);
         //    pnetweights[11] *= (1.0 - Wsfdn*eff)/(1.0 - eff);
         //  }
        }
      }
    }
    return pnetweights;  
  };

  auto pujetpass = [pubit](const RVec<int> &puid){RVec<int> passes(puid.size()); for(int i = 0; i < puid.size(); i++){passes[i] = puid[i] & (1 << pubit);} return passes;};
  
  auto pujetfunc = [pujetcorr,year](const RVec<float> &jt_pt, const RVec<float> &jt_eta, const RVec<float> &jt_phi, const RVec<float> &jt_mass, const RVec<int> &jt_pupass, const RVec<TLorentzVector> &genjt_p4, const RVec<int> &jt_genidx){
    RVec<float> pujetidsf = {1.0, 1.0, 1.0};
    for(unsigned int ijet = 0; ijet < jt_pt.size(); ijet++){
      if(jt_pt[ijet] < 50.0 && jt_pupass[ijet] > 0 && jt_genidx[ijet] > -1){
	TLorentzVector jet;
	jet.SetPtEtaPhiM(jt_pt[ijet],jt_eta[ijet],jt_phi[ijet],jt_mass[ijet]);
	float dR = genjt_p4[jt_genidx[ijet]].DeltaR(jet);
	if(dR < 0.4){
	  pujetidsf[0] *= pujetcorr->evaluate({jt_eta[ijet],jt_pt[ijet],"nom","L"});
	  pujetidsf[1] *= pujetcorr->evaluate({jt_eta[ijet],jt_pt[ijet],"up","L"});
	  pujetidsf[2] *= pujetcorr->evaluate({jt_eta[ijet],jt_pt[ijet],"down","L"});
	}
      }
    }
    return pujetidsf;
  };
  
  auto cleanJets = [debug,jesvar,isMC,ak4corr,ak4corrL1,ak4corrUnc,ak4ptres,ak4jer,ak8corr,ak8corrUnc](const RVec<TLorentzVector> &jt_p4, const RVec<float> &jt_rf, const RVec<float> &jt_murf, const RVec<float> &jt_area, const RVec<float> &jt_em, const RVec<int> &jt_id, const RVec<TLorentzVector> &genjt_p4, const RVec<int> &jt_genidx, const RVec<TLorentzVector> &mu_p4, const RVec<int> mu_jetid, const RVec<TLorentzVector> &el_p4, const RVec<int> &el_jetid, const float &rho, const float &met, const float &phi){
    RVec<float> cleanJetPt(jt_p4.size()), cleanJetEta(jt_p4.size()), cleanJetPhi(jt_p4.size()), cleanJetMass(jt_p4.size()), rawfact(jt_p4.size());
    string jervar = "nom";
    float jesuncmult = 0;
    if(jesvar == "JERup") jervar = "up";
    else if(jesvar == "JERdn") jervar = "down";
    else if(jesvar == "JECup") jesuncmult = 1.0;
    else if(jesvar == "JECdn") jesuncmult = -1.0;
    correction::CompoundCorrection::Ref jescorr;
    correction::Correction::Ref jescorrUnc;
    float drmax = 0.2;
    if(ROOT::VecOps::Mean(jt_area) < 1.0){jescorr = ak4corr; jescorrUnc = ak4corrUnc;}
    else{drmax = 0.4; jescorr = ak8corr; jescorrUnc = ak8corrUnc;}    
    float metx = met*cos(phi);
    float mety = met*sin(phi);
    if(met > 0 && debug) std::cout<< "Incoming met = " << met << ", phi = " << phi << std::endl;

    for(unsigned int ijet = 0; ijet < jt_p4.size(); ijet++){
      TLorentzVector jet = jt_p4[ijet];
      int jetid = jt_id[ijet];   
      float rf = jt_rf[ijet];

      if(ROOT::VecOps::Mean(jt_area) < 1.0 && met == 0){ // only clean leptons out of AK4 jets (AK8 will require DR > 0.8 from lepton)
	for (unsigned int imu = 0; imu < mu_p4.size(); imu++){
	  if(mu_jetid[imu] != ijet) continue;                      // only consider muons matched to this jet
	  if (jetid < 2 || jet.DeltaR(mu_p4[imu]) > 0.4) continue; // bad jet, or too far from muon
	  jet *= (1 - rf);                                         // first undo the JEC
	  jet -= mu_p4[imu];                                       // subtract muon if it's sensible
	  rf = 0;                                                  // indicate that this is the raw jet
	}
	for (unsigned int iel = 0; iel < el_p4.size(); iel++){     // same for electrons
	  if (el_jetid[iel] != ijet) continue;
	  if (jetid < 2 || jet.DeltaR(el_p4[iel]) > 0.4) continue;	  
	  jet *= (1 - rf); 
	  jet -= el_p4[iel]; 
	  rf = 0; 
	}
      }
      float jes = 1.0; float jesL1 = 1.0; float jer = 1.0; float unc = 1.0;
      jet = jet * (1 - rf);                                                         // rf = 0 if JEC undone above
      if(met > 0 && jt_em[ijet] > 0.9) continue;                                    // not these jets for MET	
      if(met > 0) jet *= (1 - jt_murf[ijet]);                                       // further correct raw to muon-substracted raw for T1.
      float rawpt = jet.Pt();
      jes = jescorr->evaluate({jt_area[ijet],jet.Eta(),rawpt,rho});                 // Data & MC get jes
      if(met > 0) jesL1 = ak4corrL1->evaluate({jt_area[ijet],jet.Eta(),rawpt,rho}); // L1-only jes for MET T1
      if(isMC){
	float res = ak4ptres->evaluate({jet.Eta(),rawpt*jes,rho});
	float sf = ak4jer->evaluate({jet.Eta(),jervar});
	bool smeared = false;                                                       // MC only gets a JER smear, one of 2 methods below:
	if(jt_genidx[ijet] > -1 && genjt_p4[jt_genidx[ijet]].Pt() > 0){	  
	  double dPt = fabs(genjt_p4[jt_genidx[ijet]].Pt() - rawpt*jes);
	  double dR = genjt_p4[jt_genidx[ijet]].DeltaR(jet);
	  if(dR < drmax && dPt < 3*rawpt*jes*res){
	    jer = max(0.0, 1.0 + (sf - 1.0)*(rawpt*jes - genjt_p4[jt_genidx[ijet]].Pt())/(rawpt*jes));
	    smeared = true;
	  }
	}
	if(!smeared){
	  TRandom3 rand(abs(static_cast<int>(jet.Phi()*1e4)));
	  jer = max(0.0, 1.0 + rand.Gaus(0, res)*sqrt(max(0.0, sf*sf - 1.0)));
	}
	unc = 1.0 + jesuncmult*(jescorrUnc->evaluate({jet.Eta(),rawpt*jes*jer}));   // MC gets JEC unc
      }	
      TLorentzVector jetL1 = jet*jesL1*jer*unc;
      jet = jet*jes*jer*unc;                                                        // evals to jes*1 for data.
      rf = 1.0 - 1.0/(jes*jer*unc);	
      if(jet.Pt() > 15){
	metx += (jetL1 - jet).Px();
	mety += (jetL1 - jet).Py();
      }
      cleanJetPt[ijet] = jet.Pt();
      cleanJetEta[ijet] = jet.Eta();
      cleanJetPhi[ijet] = jet.Phi();
      cleanJetMass[ijet] = jet.M();
      rawfact[ijet] = rf;
    }
    TVector2 corrmet(metx,mety);
    RVec<float> corrmets = {float(corrmet.Mod()),float(TVector2::Phi_mpi_pi(corrmet.Phi()))};
    
    RVec<RVec<float>> output = {cleanJetPt, cleanJetEta, cleanJetPhi, cleanJetMass, rawfact, corrmets};
    return output;
  };

  // -------------------------------------------------------
  //               Open Dataframe + MET Filters
  // -------------------------------------------------------

  auto rdf_input = ROOT::RDataFrame("Events", files); // Initial data
  
  auto METgeneralFilters = rdf_input.Filter("Flag_EcalDeadCellTriggerPrimitiveFilter == 1 && Flag_goodVertices == 1 && Flag_HBHENoiseFilter == 1 && Flag_HBHENoiseIsoFilter == 1 && Flag_eeBadScFilter == 1 && Flag_globalSuperTightHalo2016Filter == 1 && Flag_BadPFMuonFilter == 1 && Flag_ecalBadCalibFilter == 1 && Flag_BadPFMuonDzFilter == 1", "MET Filters")
    .Filter("nJet > 0 && nFatJet > 0", "Event has > 1 AK4 and > 1 AK8");

  auto truth = METgeneralFilters;
  
  // --------------------------------------------------------
  // 	       Golden JSON (Data) || GEN Info (MC)
  // --------------------------------------------------------
  
  if(!isMC){ // apply golden json to data
    truth = METgeneralFilters.Define("passesJSON", goldenjson, {"run","luminosityBlock"})
      .Filter("passesJSON == 1", "Data passes Golden JSON");
  }
  
  else{ // calculate some gen-level stuff
    auto BprimeGen = METgeneralFilters.Define("Bprime_gen_info", Form("Bprime_gen_info(\"%s\", nGenPart, GenPart_pdgId, GenPart_mass, GenPart_pt, GenPart_phi, GenPart_eta, GenPart_genPartIdxMother, GenPart_status, GenPart_statusFlags)", sample.c_str()))
      .Define("Bprime_gen_pt", "Bprime_gen_info[0]")
      .Define("Bprime_gen_eta", "(double) Bprime_gen_info[1]")
      .Define("Bprime_gen_phi", "(double) Bprime_gen_info[2]")
      .Define("Bprime_gen_mass", "Bprime_gen_info[3]")
      .Define("Bprime_gen_pdgId", "(int) Bprime_gen_info[4]")
      .Define("Bprime_gen_status", "(int) Bprime_gen_info[5]");
    
    auto wjetHT = BprimeGen;
    if(!isVV) wjetHT = BprimeGen.Define("gcHTCorr_WjetLHE", wjetHTpoly, {"LHE_HT"}); // LHE_HT missing for Pythia-only samples
    
    truth = wjetHT.Define("t_gen_info", Form("t_gen_info(\"%s\", nGenPart, GenPart_pdgId, GenPart_mass, GenPart_pt, GenPart_phi, GenPart_eta, GenPart_genPartIdxMother, GenPart_status)", sample.c_str()))
      .Define("t_gen_pt", "t_gen_info[0]")
      .Define("t_gen_eta", "(double) t_gen_info[1]")
      .Define("t_gen_phi", "(double) t_gen_info[2]")
      .Define("t_gen_mass", "t_gen_info[3]")
      .Define("t_gen_pdgId", "(int) t_gen_info[4]")
      .Define("t_gen_status", "(int) t_gen_info[5]")
      .Define("daughterb_gen_pt", "t_gen_info[6]")
      .Define("daughterb_gen_eta", "(double) t_gen_info[7]")
      .Define("daughterb_gen_phi", "(double) t_gen_info[8]")
      .Define("daughterb_gen_pdgId", "(int) t_gen_info[9]")
      .Define("daughterb_gen_status", "(int) t_gen_info[10]")
      .Define("daughterW_gen_pt", "t_gen_info[11]")
      .Define("daughterW_gen_eta", "(double) t_gen_info[12]")
      .Define("daughterW_gen_phi", "(double) t_gen_info[13]")
      .Define("daughterW_gen_mass", "t_gen_info[14]")
      .Define("daughterW_gen_pdgId", "(int) t_gen_info[15]")
      .Define("daughterW_gen_status", "(int) t_gen_info[16]")
      .Define("daughterWb_gen_dr", "DeltaR(daughterW_gen_eta, daughterb_gen_eta, daughterW_gen_phi, daughterb_gen_phi)")
      .Define("tDaughter1_gen_pt", "t_gen_info[17]") // e/mu/tau or quark1
      .Define("tDaughter1_gen_eta", "(double) t_gen_info[18]")
      .Define("tDaughter1_gen_phi", "(double) t_gen_info[19]")
      .Define("tDaughter1_gen_mass", "t_gen_info[20]")
      .Define("tDaughter1_gen_pdgId", "(int) t_gen_info[21]")
      .Define("tDaughter1_gen_status", "(int) t_gen_info[22]")
      .Define("tDaughter2_gen_pt", "t_gen_info[23]") // neutrino or quark2
      .Define("tDaughter2_gen_eta", "(double) t_gen_info[24]")
      .Define("tDaughter2_gen_phi", "(double) t_gen_info[25]")
      .Define("tDaughter2_gen_mass", "t_gen_info[26]")
      .Define("tDaughter2_gen_pdgId", "(int) t_gen_info[27]")
      .Define("tDaughter2_gen_status", "(int) t_gen_info[28]")
      .Define("tdaughter12_gen_dr", "DeltaR(tDaughter1_gen_eta, tDaughter2_gen_eta, tDaughter1_gen_phi, tDaughter2_gen_phi)")
      .Define("trueLeptonicT", "(int) t_gen_info[29]")
      .Define("W_gen_info", Form("W_gen_info(\"%s\", nGenPart, GenPart_pdgId, GenPart_mass, GenPart_pt, GenPart_phi, GenPart_eta, GenPart_genPartIdxMother, GenPart_status, daughterW_gen_pdgId)", sample.c_str()))
      .Define("W_gen_pt", "W_gen_info[0]")
      .Define("W_gen_eta", "(double) W_gen_info[1]")
      .Define("W_gen_phi", "(double) W_gen_info[2]")
      .Define("W_gen_mass", "W_gen_info[3]")
      .Define("W_gen_pdgId", "(int) W_gen_info[4]")
      .Define("W_gen_status", "(int) W_gen_info[5]")
      .Define("WDaughter1_gen_pt", "W_gen_info[6]")
      .Define("WDaughter1_gen_eta", "(double) W_gen_info[7]")
      .Define("WDaughter1_gen_phi", "(double) W_gen_info[8]")
      .Define("WDaughter1_gen_mass", "W_gen_info[9]")
      .Define("WDaughter1_gen_pdgId", "(int) W_gen_info[10]")
      .Define("WDaughter1_gen_status", "(int) W_gen_info[11]")
      .Define("WDaughter2_gen_pt", "W_gen_info[12]")
      .Define("WDaughter2_gen_eta", "(double) W_gen_info[13]")
      .Define("WDaughter2_gen_phi", "(double) W_gen_info[14]")
      .Define("WDaughter2_gen_mass", "W_gen_info[15]")
      .Define("WDaughter2_gen_pdgId", "(int) W_gen_info[16]")
      .Define("WDaughter2_gen_status", "(int) W_gen_info[17]")
      .Define("Wdaughter12_gen_dr", "DeltaR(WDaughter1_gen_eta, WDaughter2_gen_eta, WDaughter1_gen_phi, WDaughter2_gen_phi)")
      .Define("trueLeptonicW", "(int) W_gen_info[18]")
      .Define("trueLeptonicMode", Form("leptonicCheck(\"%s\", trueLeptonicT, trueLeptonicW)", sample.c_str()))
      .Define("t_bkg_idx", Form("t_bkg_idx(\"%s\", nGenPart, GenPart_pdgId, GenPart_genPartIdxMother, GenPart_statusFlags)", sample.c_str()))
      .Define("W_bkg_idx", Form("W_bkg_idx(\"%s\", nGenPart, GenPart_pdgId, GenPart_genPartIdxMother, GenPart_statusFlags, t_bkg_idx)", sample.c_str()))
      .Define("PileupWeights", pufunc, {"Pileup_nTrueInt"});

  }
  
  // ---------------------------------------------------------
  //                    LEPTON Definitions
  // ---------------------------------------------------------
  
  string elHEMcut = "";
  if(year == "2018") elHEMcut = " && (Electron_eta > -1.479 || (Electron_phi < -1.57 || Electron_phi > -0.87))";
  auto LepDefs = truth.Define("Electron_cutBasedIdNoIso_tight", "Electron_cutBasedIdNoIso_tight(nElectron, Electron_vidNestedWPBitmap, Electron_cutBased, Electron_pfRelIso03_all,Electron_eta,Electron_pt,Electron_sieie,Electron_eInvMinusPInv)")
    .Define("TPassMu", "abs(Muon_eta)<2.4 && Muon_mediumId==1 && Muon_miniIsoId>=3 && abs(Muon_dz) < 0.5 && Muon_dxy < 0.2")
    .Define("TPassEl", Form("(abs(Electron_eta)<1.442 || (abs(Electron_eta)>1.566 && abs(Electron_eta)<2.5)) && Electron_cutBasedIdNoIso_tight==1 && Electron_miniPFRelIso_all<0.1%s",elHEMcut.c_str()))
    .Define("VetoMu", "TPassMu && (Muon_pt>25)")
    .Define("VetoEl", "TPassEl && (Electron_pt>25)")
    .Define("SignalIsoMu", "TPassMu && (Muon_pt>=55)")
    .Define("SignalIsoEl", "TPassEl && (Electron_pt>=55)")
    .Define("nVetoLep", "(int) (Sum(VetoMu)+Sum(VetoEl))")
    .Define("SMuon_pt", "Muon_pt[SignalIsoMu == true]")
    .Define("SMuon_eta", "Muon_eta[SignalIsoMu == true]")
    .Define("SMuon_phi", "Muon_phi[SignalIsoMu == true]")
    .Define("SMuon_mass", "Muon_mass[SignalIsoMu == true]")
    .Define("SElectron_pt", "Electron_pt[SignalIsoEl == true]")
    .Define("SElectron_eta", "Electron_eta[SignalIsoEl == true]")
    .Define("SElectron_phi", "Electron_phi[SignalIsoEl == true]")
    .Define("SElectron_mass", "Electron_mass[SignalIsoEl == true]")
    .Define("Muon_P4", "fVectorConstructor(Muon_pt,Muon_eta,Muon_phi,Muon_mass)")
    .Define("SMuon_P4", "fVectorConstructor(SMuon_pt,SMuon_eta,SMuon_phi,SMuon_mass)")
    .Define("SElectron_P4", "fVectorConstructor(SElectron_pt,SElectron_eta,SElectron_phi,SElectron_mass)")
    .Define("SMuon_jetIdx", "Muon_jetIdx[SignalIsoMu == true]")
    .Define("SElectron_jetIdx", "Electron_jetIdx[SignalIsoEl]")
    .Define("nSignalIsoMu", "(int) Sum(SignalIsoMu)")
    .Define("nSignalIsoEl", "(int) Sum(SignalIsoEl)")
    .Define("VetoIsoMu", "(VetoMu == true && Muon_pt < 55)")
    .Define("VetoIsoEl", "(VetoEl == true && Electron_pt < 55)")
    .Define("nVetoIsoLep", "(int) (Sum(VetoIsoMu)+Sum(VetoIsoEl))");

  // --------------------------------------------------------
  // 		      LEPTON SELECTION
  // --------------------------------------------------------
  
  string tkmutrig = " || HLT_OldMu100 || HLT_TkMu100";
  string eltrig = "HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165 || HLT_Photon200";
  if(year == "2017" && era == "B"){ tkmutrig = ""; eltrig = "HLT_Ele35_WPTight_Gsf || HLT_Photon200";}
  if(year == "2016" or year == "2016APV"){ tkmutrig = " || HLT_TkMu50"; eltrig = "HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165 || HLT_Photon175";}
  if(year == "2016APV" and (era == "A" || era == "B")){ tkmutrig = ""; eltrig = "HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165 || HLT_Photon175";}
  auto LepSelect = LepDefs.Define("isMu", Form("(nMuon>0) && (HLT_Mu50%s) && (nSignalIsoMu==1) && (nVetoIsoLep==0) && (nElectron == 0 || nSignalIsoEl == 0)",tkmutrig.c_str()))
    .Define("isEl", Form("(nElectron>0) && (%s) && (nSignalIsoEl==1) && (nVetoIsoLep==0) && (nMuon == 0 || nSignalIsoMu == 0)",eltrig.c_str()))
    .Filter("isMu || isEl", "Event is either muon or electron");
  
  auto LepAssign = LepSelect.Define("assignleps", "assign_leps(isMu,isEl,SignalIsoMu,SignalIsoEl,Muon_pt,Muon_eta,Muon_phi,Muon_mass,Muon_miniPFRelIso_all,Electron_pt,Electron_eta,Electron_phi,Electron_mass,Electron_miniPFRelIso_all)")
    .Define("lepton_pt", "assignleps[0]")
    .Define("lepton_eta", "assignleps[1]")
    .Define("lepton_phi", "assignleps[2]")
    .Define("lepton_mass", "assignleps[3]")
    .Define("lepton_miniIso", "assignleps[4]");
  
  // --------------------------------------------------------
  // 		      JET Cleaning and JERC
  // --------------------------------------------------------
  
  auto Jet4vecs = LepAssign.Define("Jet_P4", "fVectorConstructor(Jet_pt,Jet_eta,Jet_phi,Jet_mass)")
    .Define("FatJet_P4", "fVectorConstructor(FatJet_pt,FatJet_eta,FatJet_phi,FatJet_mass)")
    .Define("Jet_EmEF","Jet_neEmEF + Jet_chEmEF")
    .Define("DummyZero","float(0.0)");

  auto CleanJets = Jet4vecs;
  if(isMC){
    CleanJets = Jet4vecs.Define("GenJet_P4","fVectorConstructor(GenJet_pt,GenJet_eta,GenJet_phi,GenJet_mass)")
      .Define("cleanJets", cleanJets, {"Jet_P4","Jet_rawFactor","Jet_muonSubtrFactor","Jet_area","Jet_EmEF","Jet_jetId","GenJet_P4","Jet_genJetIdx","SMuon_P4","SMuon_jetIdx","SElectron_P4","SElectron_jetIdx","fixedGridRhoFastjetAll","DummyZero","DummyZero"}) // muon and EM factors unused in this call
      .Define("cleanMets", cleanJets, {"Jet_P4","Jet_rawFactor","Jet_muonSubtrFactor","Jet_area","Jet_EmEF","Jet_jetId","GenJet_P4","Jet_genJetIdx","SMuon_P4","SMuon_jetIdx","SElectron_P4","SElectron_jetIdx","fixedGridRhoFastjetAll","RawMET_pt","RawMET_phi"}) // lepton args are unused in this call
      .Define("GenJetAK8_P4", "fVectorConstructor(GenJetAK8_pt,GenJetAK8_eta,GenJetAK8_phi,GenJetAK8_mass)")
      .Define("cleanFatJets", cleanJets, {"FatJet_P4","FatJet_rawFactor","FatJet_rawFactor","FatJet_area","FatJet_area","FatJet_jetId","GenJetAK8_P4","FatJet_genJetAK8Idx","SMuon_P4","SMuon_jetIdx","SElectron_P4","SElectron_jetIdx","fixedGridRhoFastjetAll","DummyZero","DummyZero"}); // args 2 and 4 are dummies
  }else{
    // Replace all the GenJet arguments with fakes here for data. 
    CleanJets = Jet4vecs.Define("cleanJets", cleanJets, {"Jet_P4","Jet_rawFactor","Jet_muonSubtrFactor","Jet_area","Jet_EmEF","Jet_jetId","Jet_P4","Jet_jetId","SMuon_P4","SMuon_jetIdx","SElectron_P4","SElectron_jetIdx","fixedGridRhoFastjetAll","DummyZero","DummyZero"}) // muon and EM factors unused in this call, args 6-7 are dummies
      .Define("cleanMets", cleanJets, {"Jet_P4","Jet_rawFactor","Jet_muonSubtrFactor","Jet_area","Jet_EmEF","Jet_jetId","Jet_P4","Jet_jetId","Muon_P4","Muon_jetIdx","SElectron_P4","SElectron_jetIdx","fixedGridRhoFastjetAll","RawMET_pt","RawMET_phi"}) // lepton args unused in this call, args 6-7 are dummies
      .Define("cleanFatJets", cleanJets, {"FatJet_P4","FatJet_rawFactor","FatJet_rawFactor","FatJet_area","FatJet_area","FatJet_jetId","FatJet_P4","FatJet_jetId","SMuon_P4","SMuon_jetIdx","SElectron_P4","SElectron_jetIdx","fixedGridRhoFastjetAll","DummyZero","DummyZero"}); // args 2, 4, 6, 7 are dummies
  }
  
  auto JetAssign = CleanJets.Define("corrMETnoxy_pt","cleanMets[5][0]")
    .Define("corrMETnoxy_phi","cleanMets[5][1]")
    .Define("cleanJet_pt", "cleanJets[0]")
    .Define("cleanJet_eta", "cleanJets[1]")
    .Define("cleanJet_phi", "cleanJets[2]")
    .Define("cleanJet_mass", "cleanJets[3]")
    .Define("cleanJet_rawFactor", "cleanJets[4]")
    .Define("cleanJet_puPass", pujetpass, {"Jet_puId"})
    .Define("cleanJet_vetomap", jetvetofunc, {"cleanJet_eta","cleanJet_phi","cleanJet_pt","Jet_jetId","cleanJet_puPass","Jet_area","run"})
    .Define("cleanFatJet_pt", "cleanFatJets[0]")
    .Define("cleanFatJet_eta", "cleanFatJets[1]")
    .Define("cleanFatJet_phi", "cleanFatJets[2]")
    .Define("cleanFatJet_mass", "cleanFatJets[3]")
    .Define("cleanFatJet_rawFactor", "cleanFatJets[4]")
    .Define("cleanFatJet_vetomap", jetvetofunc, {"cleanFatJet_eta","cleanFatJet_phi","cleanFatJet_pt","FatJet_jetId","cleanJet_puPass","FatJet_area","run"}); //puId is a dummy

  // ---------------------------------------------------------
  //                    MET Selection
  // ---------------------------------------------------------
  
  
  auto METSelect = JetAssign.Define("metxyoutput",metfunc,{"corrMETnoxy_pt","corrMETnoxy_phi","PV_npvs","run"})
    .Define("corrMET_pt","metxyoutput[0]")
    .Define("corrMET_phi","metxyoutput[1]")
    .Define("corrMET_dPhiLep","DeltaPhi(lepton_phi, corrMET_phi)")
    .Filter("corrMET_pt > 60", "Pass corr MET > 60");
    //.Filter("isMu || corrMET_pt>((130/1.5)*DeltaPhi(lepton_phi, corrMET_phi)-130)", "Electron Triangle Cut");
  
  // ---------------------------------------------------------
  // 	  HT Calculation and N Jets cuts
  // ---------------------------------------------------------

  auto JetSelect = METSelect.Define("DR_lepJets","DeltaR_VecAndFloat(cleanJet_eta,cleanJet_phi,lepton_eta,lepton_phi)")
    .Define("ptrel_lepJets","ptRel(cleanJet_pt,cleanJet_eta,cleanJet_phi,cleanJet_mass,lepton_pt,lepton_eta,lepton_phi,lepton_mass)")
    .Define("goodcleanJets", "cleanJet_pt > 30 && (cleanJet_pt > 50 || cleanJet_puPass > 0) && abs(cleanJet_eta) < 2.5 && Jet_jetId > 1 && (DR_lepJets > 0.4 || ptrel_lepJets > 20) && cleanJet_vetomap == 0")
    .Define("gcJet_pt_unsort", "cleanJet_pt[goodcleanJets == true]")
    .Define("gcJet_ptargsort","ROOT::VecOps::Reverse(ROOT::VecOps::Argsort(gcJet_pt_unsort))")
    .Define("gcJet_pt","reorder(gcJet_pt_unsort,gcJet_ptargsort)")
    .Define("gcJet_HT","Sum(gcJet_pt)")
    .Define("gcJet_leadpt","gcJet_pt[0]")
    .Define("DR_lepFatJets","DeltaR_VecAndFloat(cleanFatJet_eta,cleanFatJet_phi,lepton_eta,lepton_phi)")
    .Define("goodcleanFatJets", "cleanFatJet_pt > 200 && abs(cleanFatJet_eta) < 2.5 && FatJet_jetId > 1 && (DR_lepFatJets > 0.8) && cleanFatJet_vetomap == 0") 
    .Define("NFatJets", "(int) Sum(goodcleanFatJets)")
    .Define("NOS_gcFatJets","(int) Sum(DR_lepFatJets[goodcleanFatJets == true] > TMath::Pi()/2)")
    .Filter("gcJet_HT > 250","Pass HT > 250")
    .Filter("isMu || lepton_pt > 120 || gcJet_leadpt > 185","Pass lead AK4 > 185 for El trig if El_pt < 120")
    .Filter("NFatJets > 0","Pass N good central AK8 > 0")
    .Filter("NOS_gcFatJets > 0","Pass N good central other side AK8 > 0");

  // ---------------------------------------------------------
  // 	  Jet pt ordering, counting, lepton association
  // ---------------------------------------------------------

  auto JetVars = JetSelect.Define("gcHTCorr_top", topHTpoly, {"gcJet_HT"})
    .Define("NJets_central", "(int) Sum(goodcleanJets)")
    .Define("gcJet_eta", "reorder(cleanJet_eta[goodcleanJets == true],gcJet_ptargsort)")
    .Define("gcJet_phi", "reorder(cleanJet_phi[goodcleanJets == true],gcJet_ptargsort)")
    .Define("gcJet_mass", "reorder(cleanJet_mass[goodcleanJets == true],gcJet_ptargsort)")
    .Define("gcJet_genJetIdx","reorder(Jet_genJetIdx[goodcleanJets == true],gcJet_ptargsort)")
    .Define("gcJet_puPass","reorder(cleanJet_puPass[goodcleanJets == true],gcJet_ptargsort)")
    .Define("gcJet_DeepFlav", "reorder(Jet_btagDeepFlavB[goodcleanJets == true],gcJet_ptargsort)")
    .Define("gcJet_DeepFlavL", Form("gcJet_DeepFlav > %f",deepjetL)) 
    .Define("NJets_DeepFlavL", "(int) Sum(gcJet_DeepFlavL)")
    .Define("DR_gcJets_central","reorder(DR_lepJets[goodcleanJets == true],gcJet_ptargsort)")
    .Define("minDR_lepJets","ROOT::VecOps::Min(DR_gcJets_central)")
    .Define("ptrel_atMinDR_lepJets","reorder(ptrel_lepJets[goodcleanJets == true],gcJet_ptargsort)[ROOT::VecOps::ArgMin(DR_gcJets_central)]")
    .Define("OS_gcJets","DR_gcJets_central > TMath::Pi()/2")
    .Define("SS_gcJets","DR_gcJets_central <= TMath::Pi()/2")
    .Define("NOS_gcJets_central","(int) Sum(OS_gcJets)")
    .Define("NSS_gcJets_central","(int) Sum(SS_gcJets)")
    .Define("gcOSJet_pt","gcJet_pt[OS_gcJets == true]")
    .Define("gcOSJet_eta","gcJet_eta[OS_gcJets == true]")
    .Define("gcOSJet_phi","gcJet_phi[OS_gcJets == true]")
    .Define("gcOSJet_mass","gcJet_mass[OS_gcJets == true]")
    .Define("gcOSJet_DeepFlavL","gcJet_DeepFlavL[OS_gcJets == true]")
    .Define("gcSSJet_pt","gcJet_pt[SS_gcJets == true]")
    .Define("gcSSJet_eta","gcJet_eta[SS_gcJets == true]")
    .Define("gcSSJet_phi","gcJet_phi[SS_gcJets == true]")
    .Define("gcSSJet_mass","gcJet_mass[SS_gcJets == true]")
    .Define("gcSSJet_DeepFlavL","gcJet_DeepFlavL[SS_gcJets == true]")
    .Define("NOS_gcJets_DeepFlavL","(int) Sum(gcOSJet_DeepFlavL)")
    .Define("NSS_gcJets_DeepFlavL","(int) Sum(gcSSJet_DeepFlavL)");

  auto ForwardJetVars = JetVars.Define("goodcleanForwardJets", "cleanJet_pt > 30 && (cleanJet_pt > 50 || cleanJet_puPass > 0) && abs(cleanJet_eta) >= 2.5 && Jet_jetId > 1 && cleanJet_vetomap == 0")
    .Define("NJets_forward", "(int) Sum(goodcleanForwardJets)")
    .Define("gcforwJet_pt_unsort", "cleanJet_pt[goodcleanForwardJets == true]")
    .Define("gcforwJet_ptargsort","ROOT::VecOps::Reverse(ROOT::VecOps::Argsort(gcforwJet_pt_unsort))")
    .Define("gcforwJet_pt", "reorder(gcforwJet_pt_unsort,gcforwJet_ptargsort)")
    .Define("gcforwJet_eta", "reorder(cleanJet_eta[goodcleanForwardJets == true],gcforwJet_ptargsort)")
    .Define("gcforwJet_phi", "reorder(cleanJet_phi[goodcleanForwardJets == true],gcforwJet_ptargsort)")
    .Define("gcforwJet_mass", "reorder(cleanJet_mass[goodcleanForwardJets == true],gcforwJet_ptargsort)")
    .Define("gcforwJet_genJetIdx","reorder(Jet_genJetIdx[goodcleanForwardJets == true],gcforwJet_ptargsort)")
    .Define("gcforwJet_puPass","reorder(cleanJet_puPass[goodcleanForwardJets == true],gcforwJet_ptargsort)")
    .Define("gcforwJet_DeepFlav", "reorder(Jet_btagDeepFlavB[goodcleanForwardJets == true],gcforwJet_ptargsort)");

  auto FatJetVars = ForwardJetVars.Define("gcFatJet_pt_unsort", "FatJet_pt[goodcleanFatJets == true]")
    .Define("gcFatJet_ptargsort","ROOT::VecOps::Reverse(ROOT::VecOps::Argsort(gcFatJet_pt_unsort))")
    .Define("gcFatJet_pt","reorder(gcFatJet_pt_unsort,gcFatJet_ptargsort)")
    .Define("gcFatJet_eta", "reorder(FatJet_eta[goodcleanFatJets == true],gcFatJet_ptargsort)")
    .Define("gcFatJet_phi", "reorder(FatJet_phi[goodcleanFatJets == true],gcFatJet_ptargsort)")
    .Define("gcFatJet_mass", "reorder(FatJet_mass[goodcleanFatJets == true],gcFatJet_ptargsort)")
    .Define("gcFatJet_sdmass", "reorder(FatJet_msoftdrop[goodcleanFatJets == true],gcFatJet_ptargsort)")
    .Define("DR_gcFatJets", "reorder(DR_lepFatJets[goodcleanFatJets == true],gcFatJet_ptargsort)")
    .Define("minDR_lepFatJets","ROOT::VecOps::Min(DR_gcFatJets)")
    .Define("ptrel_atMinDR_lepFatJets","ptRel(gcFatJet_pt,gcFatJet_eta,gcFatJet_phi,gcFatJet_mass,lepton_pt,lepton_eta,lepton_phi,lepton_mass)[ROOT::VecOps::ArgMin(DR_gcFatJets)]")
    .Define("SS_gcFatJets","DR_gcFatJets <= TMath::Pi()/2")
    .Define("NSS_gcFatJets","(int) Sum(SS_gcFatJets)")
    .Define("OS_gcFatJets","DR_gcFatJets > TMath::Pi()/2")
    .Define("gcOSFatJet_pt","gcFatJet_pt[OS_gcFatJets == true]")
    .Define("gcOSFatJet_eta","gcFatJet_eta[OS_gcFatJets == true]")
    .Define("gcOSFatJet_phi","gcFatJet_phi[OS_gcFatJets == true]")
    .Define("gcOSFatJet_mass","gcFatJet_mass[OS_gcFatJets == true]")
    .Define("gcOSFatJet_sdmass","gcFatJet_sdmass[OS_gcFatJets == true]");
  
  // ---------------------------------------------------------
  // 		Add scale factors and MC jet-based calcs
  // ---------------------------------------------------------
  auto scaleFactors = FatJetVars;
  
  if (isMC) {
    scaleFactors = FatJetVars.Define("genttbarMass", Form("genttbarMassCalc(\"%s\", nGenPart, GenPart_pdgId, GenPart_mass, GenPart_pt, GenPart_phi, GenPart_eta, GenPart_genPartIdxMother, GenPart_status)",sample.c_str()))
      .Define("gcFatJet_hadronFlavour","reorder(FatJet_hadronFlavour[goodcleanFatJets == true],gcFatJet_ptargsort)")
      .Define("gcFatJet_genmatch", Form("FatJet_matching(\"%s\", gcFatJet_eta, gcFatJet_phi, NFatJets, gcFatJet_hadronFlavour, nGenPart, GenPart_pdgId, GenPart_phi, GenPart_eta, GenPart_genPartIdxMother, t_bkg_idx, W_bkg_idx)",sample.c_str()))
      .Define("gcOSFatJet_genmatch", "gcFatJet_genmatch[OS_gcFatJets==true]")
      .Define("leptonRecoSF", recofunc, {"lepton_pt","lepton_eta","isEl"})
      .Define("leptonIDSF", idfunc, {"lepton_pt","lepton_eta","isEl"})
      .Define("leptonIsoSF", isofunc, {"lepton_pt","lepton_eta","isEl"})
      .Define("leptonHLTSF", hltfunc, {"lepton_pt","lepton_eta","isEl"})
      .Define("ak4Jet_pt","ROOT::VecOps::Concatenate(gcJet_pt,gcforwJet_pt)") // won't store these in the tree
      .Define("ak4Jet_eta","ROOT::VecOps::Concatenate(gcJet_eta,gcforwJet_eta)")
      .Define("ak4Jet_phi","ROOT::VecOps::Concatenate(gcJet_phi,gcforwJet_phi)")
      .Define("ak4Jet_mass","ROOT::VecOps::Concatenate(gcJet_mass,gcforwJet_mass)")
      .Define("ak4Jet_puPass","ROOT::VecOps::Concatenate(gcJet_puPass,gcforwJet_puPass)")
      .Define("ak4Jet_genJetIdx","ROOT::VecOps::Concatenate(gcJet_genJetIdx,gcforwJet_genJetIdx)")
      .Define("puJetSF", pujetfunc, {"ak4Jet_pt","ak4Jet_eta","ak4Jet_phi","ak4Jet_mass","ak4Jet_puPass","GenJet_P4","ak4Jet_genJetIdx"}) 
      .Define("gcJet_hflav","reorder(Jet_hadronFlavour[goodcleanJets == true],gcJet_ptargsort)")
      .Define("btagWeights",btagshapefunc, {"gcJet_pt", "gcJet_eta", "gcJet_DeepFlav", "gcJet_hflav"});
  }

  // ---------------------------------------------------------
  // 		JET Tagging variables
  // ---------------------------------------------------------

  auto Taggers = scaleFactors.Define("lepton_lv", "lvConstructor(lepton_pt,lepton_eta,lepton_phi,lepton_mass)")
    .Define("gcJet_ST", "gcJet_HT + lepton_pt + MET_pt")
    .Define("gcFatJet_pNetJ", "reorder(FatJet_particleNet_QCD[goodcleanFatJets == true],gcFatJet_ptargsort)")
    .Define("gcFatJet_pNetTvsQCD", "reorder(FatJet_particleNet_TvsQCD[goodcleanFatJets == true],gcFatJet_ptargsort)")
    .Define("gcFatJet_pNetWvsQCD", "reorder(FatJet_particleNet_WvsQCD[goodcleanFatJets == true],gcFatJet_ptargsort)")
    .Define("gcOSFatJet_pNetJ", "gcFatJet_pNetJ[OS_gcFatJets == true]") 
    .Define("gcOSFatJet_pNetTvsQCD", "gcFatJet_pNetTvsQCD[OS_gcFatJets == true]") 
    .Define("gcOSFatJet_pNetWvsQCD", "gcFatJet_pNetWvsQCD[OS_gcFatJets == true]")
    .Define("gcFatJet_pNetT", "(gcFatJet_pNetTvsQCD * gcFatJet_pNetJ) / (1 - gcFatJet_pNetTvsQCD)")
    .Define("gcFatJet_pNetW", "(gcFatJet_pNetWvsQCD * gcFatJet_pNetJ) / (1 - gcFatJet_pNetWvsQCD)")
    .Define("gcOSFatJet_pNetT", "gcFatJet_pNetT[OS_gcFatJets == true]")
    .Define("gcOSFatJet_pNetW", "gcFatJet_pNetW[OS_gcFatJets == true]")
    .Define("gcFatJet_pNetTag", pnetWPs, {"gcFatJet_pNetTvsQCD", "gcFatJet_pNetWvsQCD"})    
    .Define("gcOSFatJet_pNetTag", "gcFatJet_pNetTag[OS_gcFatJets==true]")
    .Define("gcFatJet_nJ", "Sum(gcFatJet_pNetTag == 0)")
    .Define("gcFatJet_nT", "Sum(gcFatJet_pNetTag == 1)")
    .Define("gcFatJet_nW", "Sum(gcFatJet_pNetTag == 2)")
    .Define("gcFatJet_tau21", "reorder((FatJet_tau2 / FatJet_tau1)[goodcleanFatJets == true],gcFatJet_ptargsort)")
    .Define("gcOSFatJet_tau21", "gcFatJet_tau21[OS_gcFatJets == true]")
    .Define("gcFatJet_tau32", "reorder((FatJet_tau3 / FatJet_tau2)[goodcleanFatJets == true],gcFatJet_ptargsort)")
    .Define("gcOSFatJet_tau32", "gcFatJet_tau32[OS_gcFatJets == true]")
    .Define("minDR_leadAK8otherAK8", "minDR_leadJetOtherJet_calc(gcFatJet_eta,gcFatJet_phi)")
    .Define("minDR_leadAK4otherAK4", "minDR_leadJetOtherJet_calc(gcJet_eta,gcJet_phi)")
    .Define("minDR_AK8s_discrete","std::floor(minDR_leadAK8otherAK8/0.5)")
    .Define("minDR_AK4s_discrete","std::floor(minDR_leadAK4otherAK4/0.5)");

  auto pnetWeights = Taggers;
  if(isMC){
    pnetWeights = Taggers.Define("gcFatJet_pnetweights", pnetfunc,{"gcFatJet_eta", "gcFatJet_pt", "gcFatJet_genmatch", "gcFatJet_pNetTag", "OS_gcFatJets"});
  }
  
  // ---------------------------------------------------------
  // 		W, top, and B reconstruction
  // ---------------------------------------------------------

  auto Reconstruction = pnetWeights.Define("W_lv", "W_reco(MET_pt,MET_phi,lepton_lv)")
    .Define("W_pt", "W_lv.Pt()")
    .Define("W_eta", "W_lv.Eta()")
    .Define("W_phi", "W_lv.Phi()")
    .Define("W_mass", "W_lv.M()")
    .Define("W_MT", "sqrt(2*lepton_pt*corrMET_pt*(1-cos(lepton_phi - corrMET_phi)))")
    .Define("minMlj_output", "minM_lep_jet_calc(gcJet_pt, gcJet_eta, gcJet_phi, gcJet_mass, lepton_lv)")
    .Define("DR_W_lep", "W_lv.DeltaR(lepton_lv)")
    .Define("minM_lep_Jet", "minMlj_output[0]")
    .Define("minM_lep_Jet_jetID", "(int) minMlj_output[1]")
    .Define("minM_lep_Jet_TorW", "isLeptonic_X(minM_lep_Jet)")
    .Define("t_output", "t_reco(minM_lep_Jet_TorW,gcJet_DeepFlavL,gcJet_pt,gcJet_eta,gcJet_phi,gcJet_mass,W_lv,minM_lep_Jet_jetID,NSS_gcJets_DeepFlavL,gcSSJet_DeepFlavL,gcSSJet_pt,gcSSJet_eta,gcSSJet_phi,gcSSJet_mass)")
    .Define("t_pt_SSb", "t_output[5]")
    .Define("t_eta_SSb", "t_output[6]")
    .Define("t_phi_SSb", "t_output[7]")
    .Define("t_mass_SSb", "t_output[8]")
    .Define("DR_W_b_SSb", "t_output[9]")
    .Define("Bprime_output", "BPrime_reco_new(W_lv,NOS_gcJets_DeepFlavL,NSS_gcJets_DeepFlavL,gcSSJet_DeepFlavL,gcOSJet_DeepFlavL,gcOSFatJet_pt,gcOSFatJet_eta,gcOSFatJet_phi,gcOSFatJet_mass,gcOSFatJet_pNetTag,gcOSJet_pt,gcOSJet_eta,gcOSJet_phi,gcOSJet_mass,gcSSJet_pt,gcSSJet_eta,gcSSJet_phi,gcSSJet_mass)")
    .Define("Bprime_mass", "Bprime_output[0]")
    .Define("Bprime_pt", "Bprime_output[1]")
    .Define("Bprime_eta", "Bprime_output[2]")
    .Define("Bprime_phi", "Bprime_output[3]")
    .Define("Bprime_DR", "Bprime_output[4]")
    .Define("Bprime_ptbal", "Bprime_output[5]")
    .Define("Bprime_chi2", "Bprime_output[6]")
    .Define("Bdecay_obs", "Bprime_output[7]")
    .Define("Bprime_chi2_discrete", "Bprime_output[8]");
  
  // -------------------------------------------------
  // 		Save Snapshot to file
  // -------------------------------------------------
  
  cout << "-------------------------------------------------" << endl
       << ">>> Saving " << sample << " Snapshot..." << endl;
  //TString finalFile = "RDF_" + sample + "_" + year + "_" + testNum.Data() + ".root";
  TString finalFile = "RDF_" + sample + era + "_" + year + "_" + testNum.Data() + ".root";
  const char *stdfinalFile = finalFile;
  
  auto ColNames = Reconstruction.GetColumnNames();
  vector<string> snapCol;
  int i = 0;
  for (auto &&ColName : ColNames)
    {
      TString colName = ColName;
      if(colName.Contains("P4") || colName.Contains("cleanJets") || colName.Contains("cleanFatJets") || colName.Contains("cleanMets") || colName.Contains("Dummy")) continue;
      if(colName.Contains("LHE") && !colName.Contains("Weight") && colName != "LHE_HT" && colName != "LHE_Vpt" && colName != "gcHTCorr_WjetLHE") continue;
      if(colName.BeginsWith("Muon") && !colName.Contains("_tightId") && !colName.Contains("_isPF") && !colName.Contains("tunep") && !colName.Contains("genPartFlav")) continue;
      if(colName.BeginsWith("Electron") && !colName.Contains("genPartFlav")) continue;
      if(colName.BeginsWith("Jet") && !colName.Contains("rawFactor")) continue;
      if(colName.BeginsWith("FatJet") && !colName.Contains("rawFactor")) continue;
      if(colName.BeginsWith("ak4Jet_")) continue;
      if(colName.BeginsWith("PPS") || colName.BeginsWith("Proton") || colName.BeginsWith("L1_")) continue;
      if(colName.BeginsWith("Gen") || colName.BeginsWith("Soft") || colName.BeginsWith("fixed")) continue;
      if(colName.BeginsWith("Sub") || colName.BeginsWith("RawPuppi") || colName.BeginsWith("Calo") || colName.BeginsWith("Chs")) continue;
      if(colName.BeginsWith("Corr") || colName.BeginsWith("Fsr") || colName.BeginsWith("Iso") || colName.BeginsWith("Tau")) continue;
      if(colName.BeginsWith("SV") || colName.BeginsWith("Puppi") || colName.BeginsWith("Photon") || colName.BeginsWith("Low")) continue;
      if(colName.BeginsWith("HLT") || colName.BeginsWith("HT") || colName.BeginsWith("boosted") || colName.BeginsWith("Deep")) continue;
      if(colName.BeginsWith("Flag") || colName == "Bprime_gen_info" || colName == "t_gen_info" || colName == "W_gen_info" || colName == "metxyoutput") continue;
      if(colName == "assignleps" || colName == "pnetoutput" || colName == "t_output" || colName == "Bprime_output" || colName.BeginsWith("Other")) continue;
      if(colName.BeginsWith("PS") || colName.BeginsWith("PV") || colName.BeginsWith("Tk") || colName.BeginsWith("Trig")) continue;
      if(colName.BeginsWith("nCorr") || colName.BeginsWith("nFsr")) continue;
      if(colName.BeginsWith("nGen") || colName.BeginsWith("nIso") || colName.BeginsWith("nLow")) continue;
      if(colName.BeginsWith("nOther") || colName.BeginsWith("nPS") || colName.BeginsWith("nPhoton")) continue;
      if(colName.BeginsWith("nSV") || colName.BeginsWith("nSub") || colName.BeginsWith("nTau") || colName.BeginsWith("nTrig")) continue;
      if(colName.BeginsWith("nboosted")) continue;

      string name = colName.Data();
      snapCol.push_back(name);
      i++;
    }
  cout << "Number of Columns in Snapshot: " << i << endl;
  
  ROOT::RDF::RSnapshotOptions opts;
  if(jesvar != "Nominal") opts.fMode = "UPDATE";
  Reconstruction.Snapshot("Events_"+jesvar, stdfinalFile, snapCol, opts);
  cout << "Output File: " << finalFile << endl
       << "-------------------------------------------------" << endl;
  
  time.Stop();
  time.Print();
  
  cout << "Cut statistics:" << endl;
  Reconstruction.Report()->Print();

  std::cout << "Got past the report" << std::endl;
  
  if(jesvar == "Nominal"){
    cout << "Adding Counter tree to the file:" << endl;
    auto rdf_runs = ROOT::RDataFrame("Runs", files);
    opts.fMode = "UPDATE";
    rdf_runs.Snapshot("Runs", stdfinalFile, rdf_runs.GetColumnNames(), opts);
  }

  cout << "Done!" << endl;
}
