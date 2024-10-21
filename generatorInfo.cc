// Methods in this file:
// Bprime_gen_info(), t_gen_info(), W_gen_info(), t_bkg_idx(), W_bkg_idx(), FatJet_matching_sig(C), FatJet_matching_bkg(C)

// ----------------------------------------------------
//           Bprime truth extraction:
// ----------------------------------------------------

using namespace std;
using namespace ROOT::VecOps;

auto Bprime_gen_info(string sample, unsigned int nGenPart, RVec<int> &GenPart_pdgId, RVec<float> &GenPart_mass, RVec<float> &GenPart_pt, RVec<float> &GenPart_phi, RVec<float> &GenPart_eta, RVec<short> &GenPart_genPartIdxMother, RVec<int> &GenPart_status, RVec<unsigned short> &GenPart_statusFlags)
{
  RVec<float> BPrimeInfo(6, -999);
  if (sample.find("Bprime") == std::string::npos)
  {
    return BPrimeInfo;
  }

  for (unsigned int i = 0; i < nGenPart; i++)
  {
    int id = GenPart_pdgId[i];
    if (abs(id) != 6000007)
    {
      continue;
    }

    bitset<15> statusFlags(GenPart_statusFlags[i]);
    if (statusFlags.to_string()[1] == '0')
    {
      continue;
    } // takes the last B'
    BPrimeInfo[0] = GenPart_pt[i];
    BPrimeInfo[1] = GenPart_eta[i];
    BPrimeInfo[2] = GenPart_phi[i];
    BPrimeInfo[3] = GenPart_mass[i];
    BPrimeInfo[4] = GenPart_pdgId[i];
    BPrimeInfo[5] = GenPart_status[i];
  }

  return BPrimeInfo; // if entries -999, then no Bprime was found
};

// ----------------------------------------------------
//           t truth extraction:
// ----------------------------------------------------
auto t_gen_info(string sample, unsigned int nGenPart, RVec<int> &GenPart_pdgId, RVec<float> &GenPart_mass, RVec<float> &GenPart_pt, RVec<float> &GenPart_phi, RVec<float> &GenPart_eta, RVec<short> &GenPart_genPartIdxMother, RVec<int> &GenPart_status)
{
  RVec<float> t_gen_info(30, -999);
  if (sample.find("Bprime") == std::string::npos)
  {
    return t_gen_info;
    std::cout << "skipping t gen info" << std::endl;
  }

  int trueLeptonicT = -1;
  for (unsigned int i = 0; i < nGenPart; i++)
  {
    int id = GenPart_pdgId[i];
    int motherIdx = GenPart_genPartIdxMother[i];

    if (abs(GenPart_pdgId[motherIdx]) != 6)
    {
      continue;
    } // find t daughters
    if (abs(id) != 24 && abs(id) != 5)
    {
      continue;
    }

    // store t info
    if(t_gen_info[0] == -999){
      t_gen_info[0] = GenPart_pt[motherIdx];
      t_gen_info[1] = GenPart_eta[motherIdx];
      t_gen_info[2] = GenPart_phi[motherIdx];
      t_gen_info[3] = GenPart_mass[motherIdx];
      t_gen_info[4] = GenPart_pdgId[motherIdx];
      t_gen_info[5] = GenPart_status[motherIdx];
    }

    int igen = i;
    for (unsigned int j = i; j < nGenPart; j++)
    {
      if (GenPart_pdgId[j] != id)
      {
        continue;
      }
      if (GenPart_genPartIdxMother[j] != igen)
      {
        continue;
      }
      igen = j; // take the last copy of t daughter
    }

    if (abs(id) == 5)
    { // store b info
      t_gen_info[6] = GenPart_pt[igen];
      t_gen_info[7] = GenPart_eta[igen];
      t_gen_info[8] = GenPart_phi[igen]; // did not record gen mass, because =0 for all b
      t_gen_info[9] = GenPart_pdgId[igen];
      t_gen_info[10] = GenPart_status[igen];
    }
    else
    { // store W info
      t_gen_info[11] = GenPart_pt[igen];
      t_gen_info[12] = GenPart_eta[igen];
      t_gen_info[13] = GenPart_phi[igen];
      t_gen_info[14] = GenPart_mass[igen];
      t_gen_info[15] = GenPart_pdgId[igen];
      t_gen_info[16] = GenPart_status[igen];
      for (unsigned int j = igen; j < nGenPart; j++)
      {
        if (GenPart_genPartIdxMother[j] != igen)
        {
          continue;
        } // look for W daughters
        int j_id = GenPart_pdgId[j]; // ex: 11 for el

        int jgen = j; // save index of the electron
        for (unsigned int k = j; k < nGenPart; k++)
        {
          if (GenPart_pdgId[k] != j_id) // look for other electrons later
          {
            continue;
          }
          if (GenPart_genPartIdxMother[k] != jgen) // whose mother
          {
            continue;
          }
          jgen = k; // take the last copy of W daughter
        }

        int n = 0;
        if (abs(j_id) == 11 || abs(j_id) == 13 || abs(j_id) == 15)
        {
          trueLeptonicT = 1;
        } // store e/mu/tau first
        else if (abs(j_id) == 12 || abs(j_id) == 14 || abs(j_id) == 16)
        {
          trueLeptonicT = 1;
          n = 6;
        } // then neutrinos
        else if (trueLeptonicT == -1)
        {
          trueLeptonicT = 0;
        } // quark 1
        else if (trueLeptonicT == 0)
        {
          n = 6;
        } // quark 2
        else
        {
          cout << "Error in t_gen_info: didn't match a W daughter case. j_id = " << j_id << endl;
        }

        t_gen_info[17 + n] = GenPart_pt[jgen];
        t_gen_info[18 + n] = GenPart_eta[jgen];
        t_gen_info[19 + n] = GenPart_phi[jgen];
        t_gen_info[20 + n] = GenPart_mass[jgen];
        t_gen_info[21 + n] = GenPart_pdgId[jgen];
        t_gen_info[22 + n] = GenPart_status[jgen];
      }
    }
  }
  t_gen_info[29] = trueLeptonicT;

  // std::cout << "**********************************************************************" << std::endl;
  // std::cout << "trueLeptonicT = " << trueLeptonicT << std::endl;

  return t_gen_info;
};

// ----------------------------------------------------
//           W truth extraction:
// ----------------------------------------------------
auto W_gen_info(string sample, unsigned int nGenPart, RVec<int> &GenPart_pdgId, RVec<float> &GenPart_mass, RVec<float> &GenPart_pt, RVec<float> &GenPart_phi, RVec<float> &GenPart_eta, RVec<short> &GenPart_genPartIdxMother, RVec<int> &GenPart_status, int daughterW_gen_pdgId)
{
  RVec<float> W_gen_info(19, -999);
  if (sample.find("Bprime") == std::string::npos)
  {
    return W_gen_info;
  }
  int trueLeptonicW = -1;

  std::vector<int> WdaughterIDs;
  std::vector<int> WdaughterIdx;

  for (unsigned int i = 0; i < nGenPart; i++)
  {
    int id = GenPart_pdgId[i];
    int motherIdx = GenPart_genPartIdxMother[i];

    if (abs(id) > 17 || GenPart_pdgId[motherIdx] != (-daughterW_gen_pdgId)) // id of this W has to be opposite id of top decay W...
    {
      continue;
    } // look for daughters of W

    if (W_gen_info[0] == -999)
    {
      W_gen_info[0] = GenPart_pt[motherIdx];
      W_gen_info[1] = GenPart_eta[motherIdx];
      W_gen_info[2] = GenPart_phi[motherIdx];
      W_gen_info[3] = GenPart_mass[motherIdx];
      W_gen_info[4] = GenPart_pdgId[motherIdx];
      W_gen_info[5] = GenPart_status[motherIdx];
    }

    int igen = i;
    for (unsigned int j = igen; j < nGenPart; j++)
    {
      if (GenPart_pdgId[j] != id)
      {
        continue;
      }
      if (GenPart_genPartIdxMother[j] != igen)
      {
        continue;
      }
      igen = j; // take the last copy of W daughter
    }

    WdaughterIDs.push_back(id);
    WdaughterIdx.push_back(igen);
  }

  if(WdaughterIDs.size() < 2){
    std::cout << "Didn't find 2 W daughters! " << WdaughterIDs.size() << std::endl;
    return W_gen_info;
  }

  if(abs(WdaughterIDs.at(0)) > 10 && abs(WdaughterIDs.at(0)) < 17){ // lepton
    if(abs(WdaughterIDs.at(0)) == abs (WdaughterIDs.at(1))){
      //std::cout << "Pair production! " << WdaughterIDs.at(0) << ", " << WdaughterIDs.at(1) << std::endl;
      WdaughterIDs.erase(WdaughterIDs.begin()+1);
      WdaughterIDs.erase(WdaughterIDs.begin());
      WdaughterIdx.erase(WdaughterIdx.begin()+1);
      WdaughterIdx.erase(WdaughterIdx.begin());
      if(WdaughterIDs.size() >= 4 && (abs(WdaughterIDs.at(0)) == abs (WdaughterIDs.at(1)))){
	std::cout << "Found a double pair production!" << std::endl;
	WdaughterIDs.erase(WdaughterIDs.begin()+1);
	WdaughterIDs.erase(WdaughterIDs.begin());
	WdaughterIdx.erase(WdaughterIdx.begin()+1);
	WdaughterIdx.erase(WdaughterIdx.begin());
      }
      //std::cout << "Removed pair production, resulting daughter size = " << WdaughterIDs.size() << std::endl;
    }

    if(abs(abs(WdaughterIDs.at(0)) - abs(WdaughterIDs.at(1))) != 1){ 
      std::cout << "Lepton daughters not 1 ID apart! Check me: " << WdaughterIDs.at(0) << ", " << WdaughterIDs.at(1) << std::endl;
    }
    else{

      trueLeptonicW = 1;
      int n = 0;
      W_gen_info[6 + n] = GenPart_pt[WdaughterIdx.at(0)];
      W_gen_info[7 + n] = GenPart_eta[WdaughterIdx.at(0)];
      W_gen_info[8 + n] = GenPart_phi[WdaughterIdx.at(0)];
      W_gen_info[9 + n] = GenPart_mass[WdaughterIdx.at(0)];
      W_gen_info[10 + n] = GenPart_pdgId[WdaughterIdx.at(0)];
      W_gen_info[11 + n] = GenPart_status[WdaughterIdx.at(0)];
      n = 6;
      W_gen_info[6 + n] = GenPart_pt[WdaughterIdx.at(1)];
      W_gen_info[7 + n] = GenPart_eta[WdaughterIdx.at(1)];
      W_gen_info[8 + n] = GenPart_phi[WdaughterIdx.at(1)];
      W_gen_info[9 + n] = GenPart_mass[WdaughterIdx.at(1)];
      W_gen_info[10 + n] = GenPart_pdgId[WdaughterIdx.at(1)];
      W_gen_info[11 + n] = GenPart_status[WdaughterIdx.at(1)];
    }
  }

  if(abs(WdaughterIDs.at(0)) < 6 && abs(WdaughterIDs.at(1)) < 6){ // quarks
    
    trueLeptonicW = 0;
    int n = 0;
    W_gen_info[6 + n] = GenPart_pt[WdaughterIdx.at(0)];
    W_gen_info[7 + n] = GenPart_eta[WdaughterIdx.at(0)];
    W_gen_info[8 + n] = GenPart_phi[WdaughterIdx.at(0)];
    W_gen_info[9 + n] = GenPart_mass[WdaughterIdx.at(0)];
    W_gen_info[10 + n] = GenPart_pdgId[WdaughterIdx.at(0)];
    W_gen_info[11 + n] = GenPart_status[WdaughterIdx.at(0)];
    n = 6;
    W_gen_info[6 + n] = GenPart_pt[WdaughterIdx.at(1)];
    W_gen_info[7 + n] = GenPart_eta[WdaughterIdx.at(1)];
    W_gen_info[8 + n] = GenPart_phi[WdaughterIdx.at(1)];
    W_gen_info[9 + n] = GenPart_mass[WdaughterIdx.at(1)];
    W_gen_info[10 + n] = GenPart_pdgId[WdaughterIdx.at(1)];
    W_gen_info[11 + n] = GenPart_status[WdaughterIdx.at(1)];
  }

  if(trueLeptonicW == -1){
    std::cout << "Didn't identify W decay. Daughters are: " << std::endl;
    for(unsigned int idau = 0; idau < WdaughterIDs.size(); idau++){
      cout << WdaughterIDs.at(idau) << ", " << endl;
    }
  }
    // int n = 0;
    // if (abs(id) == 11 || abs(id) == 13 || abs(id) == 15)
    // {
    //   trueLeptonicW = 1;
    // } // store e/mu/tau first
    // else if (abs(id) == 12 || abs(id) == 14 || abs(id) == 16)
    // {
    //   trueLeptonicW = 1;
    //   n = 6;
    // } // then neutrinos
    // else if (trueLeptonicW == -1)
    // {
    //   trueLeptonicW = 0;
    // } // quark 1
    // else if (trueLeptonicW == 0)
    // {
    //   n = 6;
    // } // quark 2
    // else
    // {
    //   cout << "Error in W_gen_info: didn't match a case. id = " << id << ", trueLeptonicW = " << trueLeptonicW << endl;
    //   cout << "W daughter ID list = " << endl;
    // }

    // W_gen_info[6 + n] = GenPart_pt[i];
    // W_gen_info[7 + n] = GenPart_eta[i];
    // W_gen_info[8 + n] = GenPart_phi[i];
    // W_gen_info[9 + n] = GenPart_mass[i];
    // W_gen_info[10 + n] = GenPart_pdgId[i];
    // W_gen_info[11 + n] = GenPart_status[i];
  // }
  W_gen_info[18] = trueLeptonicW;

  //  std::cout << "trueLeptonicW = " << trueLeptonicW << std::endl;

  return W_gen_info;
};

// ----------------------------------------------------
//           W,t truth extraction for bkg:
// ----------------------------------------------------

auto t_bkg_idx(string sample, unsigned int nGenPart, RVec<int> &GenPart_pdgId, RVec<short> &GenPart_genPartIdxMother, RVec<unsigned short> &GenPart_statusFlags)
{
  // if (sample.find("Bprime") != std::string::npos)
  // {
  //   RVec<int> t_daughter_idx;
  //   return t_daughter_idx;
  // }

  RVec<int> t_idx;
  for (unsigned int i = 0; i < nGenPart; i++)
  {
    if (abs(GenPart_pdgId[i]) != 6)
    {
      continue;
    }
    bitset<15> statusFlags(GenPart_statusFlags[i]);

    if (statusFlags.to_string()[1] == '0')
    {
      continue;
    } // take last copy of t
    t_idx.push_back(i);
  }

  int Nt = t_idx.size();
  RVec<int> t_daughter_idx(Nt * 3, -99);

  for (unsigned int i = 0; i < Nt; i++)
  {
    for (unsigned int j = t_idx[i]; j < nGenPart; j++)
    {
      if (GenPart_genPartIdxMother[j] != t_idx[i])
      {
        continue;
      } // pick out daughters of t

      int id = GenPart_pdgId[j];
      if (abs(id) != 5 && abs(id) != 24)
      {
	std::cout << "Weird top daughter: " << id << std::endl;
        continue;
      } // pick out daughter b, W

      if (abs(id) == 5)
      {
        t_daughter_idx[i * 3] = j;
      } // record the first copy of b
      else
      {
        int jgen = j;
        for (unsigned int k = j; k < nGenPart; k++) // look later than this daughter in the list
        {
          if (GenPart_pdgId[k] != id) // skip particles not identical to this W
          {
            continue;
          }
          if (GenPart_genPartIdxMother[k] != jgen) // skip new W's whose mother is not this W
          {
            continue;
          }
          jgen = k; // found W -> W, update to the new W
        }
	// now have the last W

        int n = 1;
        for (unsigned int k = j; k < nGenPart; k++) // look after final W in the list
        {
          if (GenPart_genPartIdxMother[k] != jgen)
          {
            continue;
          } // pick out daughters of W
          if (abs(GenPart_pdgId[k]) > 17)
          {
	    std::cout << "Weird W daughter: " << GenPart_pdgId[k] << std::endl;
            continue;
          }                              // to exclude 24->22,24
          t_daughter_idx[i * 3 + n] = k; // record the first copy of W daughter
          n += 1;
        }
      }
    }
  }
  return t_daughter_idx;
};

auto W_bkg_idx(string sample, unsigned int nGenPart, RVec<int> &GenPart_pdgId, RVec<short> &GenPart_genPartIdxMother, RVec<unsigned short> &GenPart_statusFlags, RVec<int> &t_bkg_idx)
{
  // if (sample.find("Bprime") != std::string::npos)
  // {
  //   RVec<int> W_daughter_idx;
  //   return W_daughter_idx;
  // }
  //cout << "Event" << endl;
  RVec<int> W_idx;
  for (unsigned int i = 0; i < nGenPart; i++)
  {
    if (abs(GenPart_pdgId[i]) != 24)
    {
      continue;
    }

    bitset<15> statusFlags(GenPart_statusFlags[i]);
    if (statusFlags.to_string()[1] == '0')
    {
      continue;
    } // take last copy of W

    bool exclude = false;
    for (unsigned int j = 0; j < t_bkg_idx.size(); j += 3)
    {
      if (i == GenPart_genPartIdxMother[t_bkg_idx[j + 1]]) // if W index matches the top-W-daughter's mother, the W was from a t. Boost of t considered later
      {
        exclude = true;
        break;
      } // exclude W's from t
    }

    if (exclude)
    {
      continue;
    }
    W_idx.push_back(i);
  }

  int nW = W_idx.size();
  RVec<int> W_daughter_idx(nW * 2, -99);

  for (unsigned int i = 0; i < nW; i++)
  {
    int n = 0;
    for (unsigned int j = 0; j < nGenPart; j++)
    {
      if (GenPart_genPartIdxMother[j] != W_idx[i])
      {
        continue;
      } // pick out daughters of W
      if (abs(GenPart_pdgId[j]) > 17)
      {
	std::cout << "Weird W daughter: " << GenPart_pdgId[j] << std::endl;
        continue;
      } // to exclude 24->22,24

      W_daughter_idx[i * 2 + n] = j; // record the first copy of W daughter
      n += 1;
    }
  }

  return W_daughter_idx;
};

// The following functions could probably all go to the plotting marco
// Commented Method Only
auto FatJet_matching_sig(string sample, RVec<float> &goodcleanFatJets, RVec<float> &gcFatJet_eta, RVec<float> &gcFatJet_phi, int NFatJets, RVec<unsigned char> &gcFatJet_hadronFlavour, RVec<int> &GenPart_pdgId, double daughterb_gen_eta, double daughterb_gen_phi, double tDaughter1_gen_eta, double tDaughter1_gen_phi, int tDaughter1_gen_pdgId, double tDaughter2_gen_eta, double tDaughter2_gen_phi, int tDaughter2_gen_pdgId, double WDaughter1_gen_eta, double WDaughter1_gen_phi, int WDaughter1_gen_pdgId, double WDaughter2_gen_eta, double WDaughter2_gen_phi, int WDaughter2_gen_pdgId)
{
  RVec<int> matched_GenPart(NFatJets, -9);
  if (sample.find("Bprime") == std::string::npos)
  {
    return matched_GenPart;
  }

  // cout << "Event: " << endl;
  for (unsigned int i = 0; i < NFatJets; i++)
  {
    // cout << "\n" << "Fatjet: " << endl;
    double fatjet_eta = gcFatJet_eta[i];
    double fatjet_phi = gcFatJet_phi[i];

    double dR_b = DeltaR(fatjet_eta, daughterb_gen_eta, fatjet_phi, daughterb_gen_phi);
    double dR_q1 = DeltaR(fatjet_eta, tDaughter1_gen_eta, fatjet_phi, tDaughter1_gen_phi);
    double dR_q2 = DeltaR(fatjet_eta, tDaughter2_gen_eta, fatjet_phi, tDaughter2_gen_phi);

    double dR_q3 = DeltaR(fatjet_eta, WDaughter1_gen_eta, fatjet_phi, WDaughter1_gen_phi);
    double dR_q4 = DeltaR(fatjet_eta, WDaughter2_gen_eta, fatjet_phi, WDaughter2_gen_phi);

    if (dR_b < 0.8 && dR_q1 < 0.8 && dR_q2 < 0.8)
    {
      if (abs(tDaughter1_gen_pdgId) < 6)
      {
        matched_GenPart[i] = 6;
      } // pos stands for hadronic t
      else
      {
        matched_GenPart[i] = -6;
      } // neg stands for leptonic t
    }
    else if (dR_q1 < 0.8 && dR_q2 < 0.8)
    {
      if (abs(tDaughter1_gen_pdgId) < 6)
      {
        matched_GenPart[i] = 24;
      }
      else
      {
        matched_GenPart[i] = -24;
      }
    }

    if (dR_q3 < 0.8 && dR_q4 < 0.8)
    {
      if (abs(WDaughter1_gen_pdgId) < 6)
      {
        matched_GenPart[i] = 24;
      }
      else
      {
        matched_GenPart[i] = -24;
      }
    }

    if (matched_GenPart[i] != -9)
    {
      continue;
    }

    matched_GenPart[i] = gcFatJet_hadronFlavour[i];

  }
  return matched_GenPart;
};

// Commented Method Only
auto FatJet_matching(string sample, RVec<float> &gcFatJet_eta, RVec<float> &gcFatJet_phi, int NFatJets, RVec<unsigned char> &gcFatJet_hadronFlavour, unsigned int nGenPart, RVec<int> &GenPart_pdgId, RVec<float> &GenPart_phi, RVec<float> &GenPart_eta, RVec<short> &GenPart_genPartIdxMother, RVec<int> &t_bkg_idx, RVec<int> &W_bkg_idx) //, int trueLeptonicT, int trueLeptonicW)
{
  RVec<int> matched_GenPart(NFatJets, -9);
  // if (sample.find("Bprime") != std::string::npos)
  // {
  //   return matched_GenPart;
  // }
  
  //  std::cout << "Event has leptonic T? " << trueLeptonicT << ". Or leptonic W? " << trueLeptonicW << std::endl;
  
  int ntD = t_bkg_idx.size(); // really the daughters of t and W
  int nWD = W_bkg_idx.size();
  
  RVec<double> t_eta(ntD, -9);
  RVec<double> t_phi(ntD, -9);
  RVec<double> W_eta(nWD, -9);
  RVec<double> W_phi(nWD, -9);
  
  if (ntD != 0)
    {
      for (unsigned int i = 0; i < ntD; i++)
	{
	  int igen = t_bkg_idx[i];
	  int id = GenPart_pdgId[igen];
	  for (unsigned int j = igen; j < nGenPart; j++) // look at genParts later in the list
	    {
	      if (GenPart_pdgId[j] != id) // skip any that don't match this daughter
		{
		  continue;
		}
	      if (GenPart_genPartIdxMother[j] != igen) // skip any matches that point to a different mother
		{
		  continue;
		}
	      igen = j; // update to the copy, ultimately to the last copy
	    }
	  t_eta[i] = GenPart_eta[igen];
	  t_phi[i] = GenPart_phi[igen];
	}
    }
  
  if (nWD != 0)
    {
      for (unsigned int i = 0; i < nWD; i++)
	{
	  int igen = W_bkg_idx[i];
	  int id = GenPart_pdgId[igen];
	  for (unsigned int j = igen; j < nGenPart; j++)
	    {
	      if (GenPart_pdgId[j] != id)
		{
		  continue;
		}
	      if (GenPart_genPartIdxMother[j] != igen)
		{
		  continue;
		}
	      igen = j; // take the last copy of W daughter
	    }
	  W_eta[i] = GenPart_eta[igen];
	  W_phi[i] = GenPart_phi[igen];
	}
    }

  //  std::cout << "------------------------------------------" << std::endl;  
  for (unsigned int i = 0; i < NFatJets; i++)
    {
      double fatjet_eta = gcFatJet_eta[i];
      double fatjet_phi = gcFatJet_phi[i];
      
      for (unsigned int j = 0; j < t_bkg_idx.size() / 3; j++)
	{
	  // first reject tops with daughters 2 and 3 that are in the leptonic range
	  if (abs(GenPart_pdgId[t_bkg_idx[j * 3 + 1]]) > 10 && abs(GenPart_pdgId[t_bkg_idx[j * 3 + 1]]) < 17) continue;
	  if (abs(GenPart_pdgId[t_bkg_idx[j * 3 + 2]]) > 10 && abs(GenPart_pdgId[t_bkg_idx[j * 3 + 2]]) < 17) continue;

	  double dR_b = DeltaR(fatjet_eta, t_eta[j * 3], fatjet_phi, t_phi[j * 3]);
	  double dR_q1 = DeltaR(fatjet_eta, t_eta[j * 3 + 1], fatjet_phi, t_phi[j * 3 + 1]);
	  double dR_q2 = DeltaR(fatjet_eta, t_eta[j * 3 + 2], fatjet_phi, t_phi[j * 3 + 2]);
	  
	  if (std::min({dR_b,dR_q1,dR_q2}) < 0.8 && std::max({dR_b,dR_q1,dR_q2}) < 1.2)
	    //	  if (dR_b < 0.8 && dR_q1 < 0.8 && dR_q2 < 0.8)
	    {
	      if (abs(GenPart_pdgId[t_bkg_idx[j * 3 + 1]]) < 6)
		{
		  //std::cout << "hadronic t matched: dRb = " << dR_b << ", dRq1 = " << dR_q1 << ", dRq2 = " << dR_q2 << std::endl;
		  matched_GenPart[i] = 6;
		  break;
		} // pos stands for hadronic t
	      else
		{
		  std::cout << "leptonic t matched: weird!" << std::endl; //dRb = " << dR_b << ", dRq1 = " << dR_q1 << ", dRq2 = " << dR_q2 << std::endl;
		  //		  std::cout << "Check 661, t daughter is a lepton: " << GenPart_pdgId[t_bkg_idx[j * 3 + 1]] << std::endl;
		  matched_GenPart[i] = -6;
		  break;
		} // neg stands for leptonic t
	    }
	  else if (std::min({dR_q1,dR_q2}) < 0.8 && std::max({dR_q1,dR_q2}) < 1.2)
	    //	  else if (dR_q1 < 0.8 && dR_q2 < 0.8)
	    {
	      if (abs(GenPart_pdgId[t_bkg_idx[j * 3 + 1]]) < 6)
		{
		  //if(dR_b < 1.5) std::cout << "hadronic t didn't match the b, but W's work: dRb = " << dR_b << ", dRq1 = " << dR_q1 << ", dRq2 = " << dR_q2 << std::endl;
		  //else std::cout << "hadronic t partially merged" << std::endl;
		  matched_GenPart[i] = 24;
		  break;
		}
	      else
		{
		  std::cout << "t didn't match the b, but leptonic W's work: weird!" << std::endl; //dRb = " << dR_b << ", dRq1 = " << dR_q1 << ", dRq2 = " << dR_q2 << std::endl;
		  //		  std::cout << "Check 661, W daughter is a lepton: " << GenPart_pdgId[t_bkg_idx[j * 3 + 1]] << std::endl;
		  matched_GenPart[i] = -24;
		  break;
		}
	    }
	  //	  else{if ((dR_b < 1.5 || dR_q1 < 1.5 || dR_q2 < 1.5) && abs(GenPart_pdgId[t_bkg_idx[j * 3 + 1]]) < 6) std::cout << "hadronic t didn't match: dRb = " << dR_b << ", dRq1 = " << dR_q1 << ", dRq2 = " << dR_q2 << std::endl; }
	}
      
      if (matched_GenPart[i] != -9)
	{
	  continue;
	}
      for (unsigned int j = 0; j < W_bkg_idx.size() / 2; j++) // check tops first, then W's on remaining -9s
	{
	  // first reject leptonic W's
	  if (abs(GenPart_pdgId[W_bkg_idx[j * 2]]) > 10 && abs(GenPart_pdgId[W_bkg_idx[j * 2]]) < 17) continue;
	  if (abs(GenPart_pdgId[W_bkg_idx[j * 2 + 1]]) > 10 && abs(GenPart_pdgId[W_bkg_idx[j * 2 + 1]]) < 17) continue;

	  double dR_q1 = DeltaR(fatjet_eta, W_eta[j * 2], fatjet_phi, W_phi[j * 2]);
	  double dR_q2 = DeltaR(fatjet_eta, W_eta[j * 2 + 1], fatjet_phi, W_phi[j * 2 + 1]);
	  
	  if (std::min(dR_q1,dR_q2) < 0.8 && std::max(dR_q1,dR_q2) < 1.2)
	    //	  if (dR_q1 < 0.8 && dR_q2 < 0.8)
	    {
	      if (abs(GenPart_pdgId[W_bkg_idx[j * 2]]) < 6)
		{
		  //std::cout << "hadronic W matched: dRq1 = " << dR_q1 << ", dRq2 = " << dR_q2 << std::endl;
		  matched_GenPart[i] = 24;
		  break;
		}
	      else
		{
		  std::cout << "leptonic W matched: weird!" << std::endl; //dRq1 = " << dR_q1 << ", dRq2 = " << dR_q2 << std::endl;
		  //		  std::cout << "Check 686, W daughter is a lepton: " << GenPart_pdgId[W_bkg_idx[j * 2]] << std::endl;
		  matched_GenPart[i] = -24;
		  break;
		}
	    }
	  //	  else{if(abs(GenPart_pdgId[W_bkg_idx[j * 2]]) < 6) std::cout << "hadronic W didn't match: dRq1 = " << dR_q1 << ", dRq2 = " << dR_q2 << std::endl;}
	}
      
      if (matched_GenPart[i] != -9)
	{
	  continue;
	}

      matched_GenPart[i] = gcFatJet_hadronFlavour[i]; // 0, 4, 5. Matches highest Subjet_hadronFlavour and has 0 where no subjets.
    }
  return matched_GenPart;
};

// ----------------------------------------------------
//   		ttbar background mass CALCULATOR:
// ----------------------------------------------------

// Commented Method Only
auto genttbarMassCalc(string sample, unsigned int nGenPart, RVec<int> &GenPart_pdgId, RVec<float> &GenPart_mass, RVec<float> &GenPart_pt, RVec<float> &GenPart_phi, RVec<float> &GenPart_eta, RVec<short> &GenPart_genPartIdxMother, RVec<int> &GenPart_status)
{
    int returnVar = 0;
    if (sample.find("TTTo") != std::string::npos || sample.find("Mtt") != std::string::npos)
      {
        int genTTbarMass = -999;
        double topPtWeight = 1.0;
        TLorentzVector top, antitop;
        bool gottop = false;
        bool gotantitop = false;
        bool gottoppt = false;
        bool gotantitoppt = false;
        float toppt, antitoppt;
        for (unsigned int p = 0; p < nGenPart; p++)
        {
            int id = GenPart_pdgId[p];
            if (abs(id) != 6)
            {
                continue;
            }
            if (GenPart_mass[p] < 10)
            {
                continue;
            }
            int motherid = GenPart_pdgId[GenPart_genPartIdxMother[p]];
            if (abs(motherid) != 6)
            {
                if (!gottop && id == 6)
                {
                    top.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], GenPart_mass[p]);
                    gottop = true;
                }
                if (!gotantitop && id == -6)
                {
                    antitop.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], GenPart_mass[p]);
                    gotantitop = true;
                }
            }
            if (GenPart_status[p] == 62)
            {
                if (!gottoppt && id == 6)
                {
                    toppt = GenPart_pt[p];
                    gottoppt = true;
                }
                if (!gotantitoppt && id == -6)
                {
                    antitoppt = GenPart_pt[p];
                    gotantitoppt = true;
                }
            }
        }
        if (gottop && gotantitop)
        {
            genTTbarMass = (top + antitop).M();
        }
        if (gottoppt && gotantitoppt)
        {
            float SFtop = TMath::Exp(0.0615 - 0.0005 * toppt);
            float SFantitop = TMath::Exp(0.0615 - 0.0005 * antitoppt);
            topPtWeight = TMath::Sqrt(SFtop * SFantitop);
        }
        returnVar = genTTbarMass;
    }
    return returnVar;
};
