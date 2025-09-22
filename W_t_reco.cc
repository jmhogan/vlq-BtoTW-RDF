// Methods in this file:
// W_reco(C), dR_Wt_Calc(C), isLeptonic_X(C), t_reco(C), minM_lep_jet_calc(C)

// -------------------------------------------------
//         W-BOSON TLORENTZVECTOR CALCULATOR
// -------------------------------------------------

using namespace std;
using namespace ROOT::VecOps;

//This is needed for single search
// Commented Method Only
TLorentzVector W_reco(float corr_met, float corr_met_phi, TLorentzVector lepton_lv)
{
	const double MW = 80.4;
	double metpx = corr_met * cos(corr_met_phi);
	double metpy = corr_met * sin(corr_met_phi);
	double metpt = corr_met;
	TLorentzVector Wlv_1, Wlv_2, Wlv, Nulv_1, Nulv_2;
	double nuPz_1;
	double nuPz_2;
	
	double Dtmp = MW*MW - lepton_lv.M()*lepton_lv.M() + 2*(lepton_lv.Px()*metpx + lepton_lv.Py()*metpy);
	double Atmp = 4.0*(lepton_lv.Energy()*lepton_lv.Energy() - lepton_lv.Pz()*lepton_lv.Pz());
	double Btmp = -4.0*Dtmp*lepton_lv.Pz();
	double Ctmp = 4.0*lepton_lv.Energy()*lepton_lv.Energy()*metpt*metpt - Dtmp*Dtmp;
	
	double DETtmp = Btmp*Btmp - 4.0*Atmp*Ctmp;
	
	if(DETtmp >= 0)
	{
		nuPz_1 = (-Btmp + TMath::Sqrt(DETtmp))/(2.0*Atmp);
		nuPz_2 = (-Btmp - TMath::Sqrt(DETtmp))/(2.0*Atmp);
		Nulv_1.SetPxPyPzE(metpx,metpy,nuPz_1,TMath::Sqrt((metpt)*(metpt)+(nuPz_1)*(nuPz_1)));
		Nulv_2.SetPxPyPzE(metpx,metpy,nuPz_2,TMath::Sqrt((metpt)*(metpt)+(nuPz_2)*(nuPz_2)));
	}
	else
	{
		nuPz_1 = -Btmp/(2.0*Atmp);
		nuPz_2 = -Btmp/(2.0*Atmp);
		// does another quad solution for pT and scales pT in result. Reduces M, pT, DR.
		double alpha = lepton_lv.Px()*metpx/metpt + lepton_lv.Py()*metpy/metpt;
		double Delta = MW*MW - lepton_lv.M()*lepton_lv.M();
		Atmp = 4.0*(lepton_lv.Pz()*lepton_lv.Pz() - lepton_lv.Energy()*lepton_lv.Energy() + alpha*alpha);
		Btmp = 4.0*alpha*Delta;
		Ctmp = Delta*Delta;
		float DETtmp2 = Btmp*Btmp - 4.0*Atmp*Ctmp;
		double pTnu_1 = (-Btmp + TMath::Sqrt(DETtmp2))/(2.0*Atmp);
		double pTnu_2 = (-Btmp - TMath::Sqrt(DETtmp2))/(2.0*Atmp);
		Nulv_1.SetPxPyPzE(metpx*pTnu_1/metpt,metpy*pTnu_1/metpt,nuPz_1,TMath::Sqrt(pTnu_1*pTnu_1 + nuPz_1*nuPz_1));
		Nulv_2.SetPxPyPzE(metpx*pTnu_2/metpt,metpy*pTnu_2/metpt,nuPz_2,TMath::Sqrt(pTnu_2*pTnu_2 + nuPz_2*nuPz_2));
	}
	Wlv_1 = Nulv_1 + lepton_lv;
	Wlv_2 = Nulv_2 + lepton_lv;
	
	if(fabs(Wlv_1.M() - MW) < fabs(Wlv_2.M() - MW)) {Wlv = Wlv_1;}
	else {Wlv = Wlv_2;}
	return Wlv;
};

// ----------------------------------------------------
// 		  BABY dR_Wt CALCULATOR
// ----------------------------------------------------

// Commented Method Only
double dR_Wt_Calc(TLorentzVector Wlv, TLorentzVector lepton_lv){return Wlv.DeltaR(lepton_lv);};

// -----------------------------------------------------
// 		    isLEPTONIC W or t
// -----------------------------------------------------
// Commented Method Only
bool isLeptonic_X(float minMleppJet)
{
	int isLep_X = -1; // 0 for W --- 1 for t
	bool isLeptonic_W = false;
	bool isLeptonic_t = false;
	// best combo of W vs t truth match with this
	if(minMleppJet > 173){isLeptonic_W = true; isLep_X = 0;}
	else{isLeptonic_t = true; isLep_X = 1;}
	return isLep_X;
};

// -----------------------------------------------------
// 	  HOMEMADE TLORENTZVECTOR CONSTRUCTOR
// -----------------------------------------------------
// Commented Method Only
RVec<float> t_reco(int isLeptonic, RVec<int>& isB, RVec<float>& jet_pt, RVec<float>& jet_eta, RVec<float>& jet_phi, RVec<float>& jet_mass, TLorentzVector Wlv, int ind_MinMlj, int NSSB, RVec<int>& isSSb, RVec<float>& SSpt, RVec<float>& SSeta, RVec<float>& SSphi, RVec<float>& SSmass, TLorentzVector lepton_lv)
{
  float t_mass = -999;
  float t_pt = -999;
  float t_eta = -999;
  float t_phi = -999;
  float t_dRWb = -999;
  float tSS_mass = -999;
  float tSS_pt = -999;
  float tSS_eta = -999;
  float tSS_phi = -999;
  float tSS_dRWb = -999;
  float tSS_mlb = -999;
  float tSSmlb_mass = -999;
  float tSSmlb_pt = -999;
  float tSSmlb_eta = -999;
  float tSSmlb_phi = -999;
  float tSSmlb_dRWb = -999;
  float tSSmlb_mlb = -999;
  float tSSmlb_idx = -999;
  float minDR_Wb = 999;
  int bIndex = 999;
  TLorentzVector bottom_lv, top_lv;

  // Form a leptonic top candidate if the b is close enough
  if(isLeptonic == 1){
    RVec<float> Bpts = jet_pt[isB == 1];
    RVec<float> Betas = jet_eta[isB == 1];
    RVec<float> Bphis = jet_phi[isB == 1];
    RVec<float> Bmass = jet_mass[isB == 1];
    if(Sum(isB) > 0){
      minDR_Wb = Min(DeltaR_VecAndFloat(Betas, Bphis, Wlv.Eta(), Wlv.Phi()));  
      bIndex = ArgMin(DeltaR_VecAndFloat(Betas, Bphis, Wlv.Eta(), Wlv.Phi()));
    }
    if(minDR_Wb <= 0.8) bottom_lv.SetPtEtaPhiM(Bpts.at(bIndex),Betas.at(bIndex),Bphis.at(bIndex),Bmass.at(bIndex));
    else bottom_lv.SetPtEtaPhiM(jet_pt.at(ind_MinMlj),jet_eta.at(ind_MinMlj),jet_phi.at(ind_MinMlj),jet_mass.at(ind_MinMlj));      
    top_lv = bottom_lv + Wlv;
    t_mass = top_lv.M();
    t_pt = top_lv.Pt();
    t_eta = top_lv.Eta();
    t_phi = top_lv.Phi();
    t_dRWb = bottom_lv.DeltaR(Wlv);
  }

  // BTagging Method: Now we check whether there are any same side b-tagged jets
  if (NSSB > 0) {
    float SSBpt = SSpt[isSSb == 1].at(0);
    float SSBeta = SSeta[isSSb == 1].at(0);
    float SSBphi = SSphi[isSSb == 1].at(0);
    float SSBmass = SSmass[isSSb == 1].at(0);
    bottom_lv.SetPtEtaPhiM(SSBpt, SSBeta, SSBphi, SSBmass);
    top_lv = bottom_lv + Wlv;
    tSS_mass = top_lv.M();
    tSS_pt = top_lv.Pt();
    tSS_eta = top_lv.Eta();
    tSS_phi = top_lv.Phi();
    tSS_dRWb = bottom_lv.DeltaR(Wlv);
    tSS_mlb = (bottom_lv + lepton_lv).M();

    float minMlb = 999999.9;
    int minMlbidx = -1;
    for(unsigned int ib = 0; ib < NSSB; ib++){
      bottom_lv.SetPtEtaPhiM(SSpt[isSSb == 1].at(ib), SSeta[isSSb == 1].at(ib), SSphi[isSSb == 1].at(ib), SSmass[isSSb == 1].at(ib));
      top_lv = bottom_lv + lepton_lv;
      if(top_lv.M() < minMlb){
	minMlb = top_lv.M();
	minMlbidx = ib;
      }
    }
    bottom_lv.SetPtEtaPhiM(SSpt[isSSb == 1].at(minMlbidx), SSeta[isSSb == 1].at(minMlbidx), SSphi[isSSb == 1].at(minMlbidx), SSmass[isSSb == 1].at(minMlbidx));
    top_lv = Wlv + bottom_lv;
    tSSmlb_mass = top_lv.M();
    tSSmlb_pt = top_lv.Pt();
    tSSmlb_eta = top_lv.Eta();
    tSSmlb_phi = top_lv.Phi();
    tSSmlb_dRWb = bottom_lv.DeltaR(Wlv);
    tSSmlb_mlb = minMlb;
    tSSmlb_idx = minMlbidx;
    
  }

  RVec<float> t_FiveVec = {t_pt,t_eta,t_phi,t_mass,t_dRWb,tSS_pt,tSS_eta,tSS_phi,tSS_mass,tSS_dRWb,tSSmlb_pt,tSSmlb_eta,tSSmlb_phi,tSSmlb_mass,tSSmlb_dRWb,tSSmlb_mlb,tSSmlb_idx,tSS_mlb};
  return t_FiveVec;
};

// ----------------------------------------------------
//     minM_lep_jet VECTOR RETURN + NJETSDEEPFLAV
// ----------------------------------------------------

// Commented Method Only
auto minM_lep_jet_calc(RVec<float> &jet_pt, RVec<float> &jet_eta, RVec<float> &jet_phi, RVec<float> &jet_mass, TLorentzVector lepton_lv)
{
    float ind_MinMlj = -1; // This gets changed into int in .Define()
    float minMleppJet = 1e8;
    TLorentzVector jet_lv;

    for (unsigned int ijet = 0; ijet < jet_pt.size(); ijet++)
    {
        jet_lv.SetPtEtaPhiM(jet_pt.at(ijet), jet_eta.at(ijet), jet_phi.at(ijet), jet_mass.at(ijet));
        if ((lepton_lv + jet_lv).M() < minMleppJet)
        {
            minMleppJet = fabs((lepton_lv + jet_lv).M());
            ind_MinMlj = ijet;
        }
    }
    RVec<float> minMlj = {minMleppJet, ind_MinMlj};
    return minMlj;
};

