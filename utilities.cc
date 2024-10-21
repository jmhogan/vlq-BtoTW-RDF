// Methods in this file:
// leptonicCheck(), Electron_cutBasedIdNoIso_tight(), genttbarMassCalc(C), fVectorConstructor(), lvConstructor(C), DeltaR_VecAndFloat(), ptRel()
// I put some of the methods in here becasue I didn't know where else to put them.

using namespace std;
using namespace ROOT::VecOps;

// -------------------------------------------------------
//               Sorting
// -------------------------------------------------------
template<typename T>
RVec<T> reorder(const RVec<T> &v, const RVec<int> &idx){
  RVec<T> vnew(v.size());
  for(unsigned int i = 0; i < idx.size(); i++){
    vnew[i] = v[idx[i]];
  }
  return vnew;
};

// The following functions could probably all go to the plotting marco
auto leptonicCheck(string sample, int trueLeptonicT, int trueLeptonicW)
{
  if (sample.find("Bprime") == std::string::npos)
    {
      return -9;
    } // not sure if this line is needed. check.

  int trueLeptonicMode = -9;

  if ((trueLeptonicT != 1) && (trueLeptonicW == 1))
    {
      trueLeptonicMode = 0;
    } // leptonic W
  else if ((trueLeptonicT == 1) && (trueLeptonicW != 1))
    {
      trueLeptonicMode = 1;
    } // leptonic T
  else if ((trueLeptonicT == 1) && (trueLeptonicW == 1))
    {
      trueLeptonicMode = 2;
    } // dileptonic
  else if ((trueLeptonicT == 0) && (trueLeptonicW == 0))
    {
      trueLeptonicMode = -1;
    } // hadronic
  
  return trueLeptonicMode;
};

auto Electron_cutBasedIdNoIso_tight(unsigned int nElectron, RVec<int> &Electron_vidNestedWPBitmap, RVec<unsigned char> &Electron_cutBased, RVec<float> &Electron_pfRelIso03_all, RVec<float> &eta, RVec<float> &pt, RVec<float> &sieie, RVec<float> &ooemoop)
{
  // VID compressed bitmap (MinPtCut,GsfEleSCEtaMultiRangeCut,GsfEleDEtaInSeedCut,GsfEleDPhiInCut,GsfEleFull5x5SigmaIEtaIEtaCut,GsfEleHadronicOverEMEnergyScaledCut,GsfEleEInverseMinusPInverseCut,GsfEleRelPFIsoScaledCut,GsfEleConversionVetoCut,GsfEleMissingHitsCut), 3 bits per cut

  RVec<int> noIso_tight(nElectron, 0);
  for (unsigned int i = 0; i < nElectron; i++){
    //std::cout << "------------------------------" << std::endl;
    list<int> vars{0, 1, 2, 3, 4, 5, 6, 8, 9}; // checking this
    noIso_tight[i] = 1;
    for (int x : vars){
      if (((Electron_vidNestedWPBitmap[i] >> (x * 3)) & 0x7) < 4){
	noIso_tight[i] = 0;
      }
      // These printouts were helpful to convince me that we understand the ordering
      // if(x == 0){
      // 	std::cout << "pt = " << pt[i] << " and eta = " << eta[i] << ", compared to limit of 10? (barrel) 10? (endcap)" << std::endl;
      // 	std::cout << "value for this bit group: " << ((Electron_vidNestedWPBitmap[i] >> (x * 3)) & 0x7) << std::endl;
      // }
      // if(x == 4){
      // 	std::cout << "sieie = " << sieie[i] << " and eta = " << eta[i] << ", compared to limit of 0.0104 (barrel) 0.0353 (endcap)" << std::endl;
      // 	std::cout << "value for this bit group: " << ((Electron_vidNestedWPBitmap[i] >> (x * 3)) & 0x7) << std::endl;
      // }
      // if(x == 6){
      // 	std::cout << "ooemoop = " << abs(ooemoop[i]) << " and eta = " << eta[i] << ", compared to limit of 0.159 (barrel) 0.0197 (endcap)" << std::endl;
      // 	std::cout << "value for this bit group: " << ((Electron_vidNestedWPBitmap[i] >> (x * 3)) & 0x7) << std::endl;
      // }
    }
    // int passCBtight = 0;
    // if(Electron_cutBased[i] == 4) passCBtight = 1;    
    // if(passCBtight != noIso_tight[i]){
    //   float cut = 0.0287+0.506/pt[i];
    //   if(abs(eta[i]) > 1.479) cut = 0.0445+0.963/pt[i]; 
    //   std::cout << "CBtight = " << passCBtight << ", noIso = " << noIso_tight[i] << ", rel iso = " << Electron_pfRelIso03_all[i] << ", which fails iso < " << cut << std::endl;
    // }      
  }
  return noIso_tight;
};


// -------------------------------------------
// 	  TLORENTZVECTOR CONSTRUCTOR
// -------------------------------------------
RVec<TLorentzVector> fVectorConstructor(RVec<float> &pt, RVec<float> &eta, RVec<float> &phi, RVec<float> &mass)
{
    RVec<TLorentzVector> lv;
    TLorentzVector tlv;
    for (int i = 0; i < pt.size(); i++)
    {
        tlv.SetPtEtaPhiM(pt[i], eta[i], phi[i], mass[i]);
        lv.push_back(tlv);
    }
    return lv;
};

// -------------------------------------------------
//    TLORENTZVECTOR CONSTRUCTOR FOR FLOAT ONLYS
// -------------------------------------------------
// Commented Method Only
TLorentzVector lvConstructor(float pt, float eta, float phi, float mass)
{
	TLorentzVector lv;
	lv.SetPtEtaPhiM(pt,eta,phi,mass);
	return lv;
};

auto getHighestPt(RVec<float> &VLepton_pt, RVec<float> &VLepton_eta, RVec<float> &VLepton_phi){
  RVec<float> Lepton0_PtEtaPhi(3,-1);

  if(VLepton_pt.size()==0){return Lepton0_PtEtaPhi;}

  auto maxIdx = ArgMax(VLepton_pt);

  Lepton0_PtEtaPhi[0] = VLepton_pt[maxIdx];
  Lepton0_PtEtaPhi[1] = VLepton_eta[maxIdx];
  Lepton0_PtEtaPhi[2] = VLepton_phi[maxIdx];

  return Lepton0_PtEtaPhi;
};

// --------------------------------------------
//               DR CALCULATORS
// --------------------------------------------
ROOT::VecOps::RVec<float> DeltaR_VecAndFloat(ROOT::VecOps::RVec<float>& jet_eta, ROOT::VecOps::RVec<float>& jet_phi, const float& lep_eta, const float& lep_phi)
{
  ROOT::VecOps::RVec<float> DR (jet_eta.size(),999);
  for(int i = 0; i < jet_eta.size(); i++) { DR[i] = DeltaR(jet_eta[i],lep_eta,jet_phi[i],lep_phi); }
  return DR;
};

ROOT::VecOps::RVec<float> ptRel(ROOT::VecOps::RVec<float>& jet_pt, ROOT::VecOps::RVec<float>& jet_eta, ROOT::VecOps::RVec<float>& jet_phi, ROOT::VecOps::RVec<float>& jet_mass, const float& lepton_pt, const float& lepton_eta, const float& lepton_phi, const float& lepton_mass)
{
  ROOT::VecOps::RVec<float> ptrel (jet_pt.size(),-1);
  TLorentzVector jet;
  TLorentzVector lepton;
  lepton.SetPtEtaPhiM(lepton_pt, lepton_eta, lepton_phi, lepton_mass);
  for(int i = 0; i < jet_pt.size(); i++) {
      jet.SetPtEtaPhiM(jet_pt[i], jet_eta[i], jet_phi[i], jet_mass[i]);
      ptrel[i] = (jet.Vect().Cross(lepton.Vect())).Mag() / jet.P();
  }
  return ptrel;
}

float minDR_leadJetOtherJet_calc(ROOT::VecOps::RVec<float>& jet_eta, ROOT::VecOps::RVec<float>& jet_phi)
{
  if(jet_eta.size() < 2) return 6.5;
  else{
    ROOT::VecOps::RVec<float> nonlead_eta = jet_eta;
    nonlead_eta.erase(nonlead_eta.begin());
    ROOT::VecOps::RVec<float> nonlead_phi = jet_phi;
    nonlead_phi.erase(nonlead_phi.begin());
    ROOT::VecOps::RVec<float> drs = DeltaR_VecAndFloat(nonlead_eta, nonlead_phi, jet_eta.at(0), jet_phi.at(0));
    float mindr = ROOT::VecOps::Min(drs);
    return mindr;
  }
};

ROOT::VecOps::RVec<float> floorfunc(ROOT::VecOps::RVec<float> items)
{
  ROOT::VecOps::RVec<float> floored;
  for(unsigned int i = 0; i < items.size(); i++){
    floored.push_back(std::floor(items.at(i)/0.5));
  }
  return floored;
};
