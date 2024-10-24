import os, sys, math
from ROOT import TFile, TTree, TH1D, TH2D, TCanvas, gStyle, gPad

readFile = True
if readFile:
    inFile = TFile.Open("root://cmseos.fnal.gov//store/user/jmanagan/BtoTW_Jan2024_pNetAlt3/RDF_BprimeBtoTW_M-1400_NWALO_TuneCP5_13TeV-madgraph-pythia8_2018_0.root")

    decaymodes_den = TH2D("B_decays_den",";reconstructed decay mode;true decay mode",4,0,4,4,0,4)
    decaymodes_num = TH2D("B_decays",";reconstructed decay mode;true decay mode",4,0,4,4,0,4)
    decaymodes_den.Sumw2()
    decaymodes_num.Sumw2()

    leptonmodes_den = TH2D("lepton_source_den",";reconstructed lepton source;true lepton source",2,0,2,2,0,2)
    leptonmodes_num = TH2D("lepton_source",";reconstructed lepton source;true lepton source",2,0,2,2,0,2)
    leptonmodes_den.Sumw2()
    leptonmodes_num.Sumw2()

    t = inFile.Get("Events_Nominal")

    for ievent in range(t.GetEntries()):

        t.GetEntry(ievent)
        i = 0
        j = 0
        
        # Fill truth info into all x-axis values
        if t.trueLeptonicT == 1:
            if t.W_gen_pt <= 200:
                i = 3.5
                j = 1.5
            else:
                i = 2.5
                j = 1.5
        else:
            if t.t_gen_pt <= 400:
                i = 1.5
                j = 0.5
            else:
                i = 0.5
                j = 0.5
                
        for imode in range(0,5):
            decaymodes_den.Fill(imode,i)
        
        for imode in range(0,2):
            leptonmodes_den.Fill(imode,j)
                
        # Fill reconstructed info into only the right x-axis value
        # taggedTjet = 1, taggedWjet = 2, untaggedTlep = 3, untaggedWlep = 4
    
        if t.Bdecay_obs == 1:
            decaymodes_num.Fill(0.5,i)
        elif t.Bdecay_obs == 2:
            decaymodes_num.Fill(2.5,i)
        elif t.Bdecay_obs == 3:
            decaymodes_num.Fill(3.5,i)
        else:
            decaymodes_num.Fill(1.5,i)

        if t.Bdecay_obs == 1 or t.Bdecay_obs == 4:
            leptonmodes_num.Fill(0.5,j)
        else:
            leptonmodes_num.Fill(1.5,j)

    decaymodes_num.Divide(decaymodes_num, decaymodes_den, 1, 1, "B")
    leptonmodes_num.Divide(leptonmodes_num, leptonmodes_den, 1, 1, "B")

    histFile = TFile.Open("confusionPlots_Bprime1400.root", "recreate")

    decaymodes_num.Write()
    leptonmodes_num.Write()

    histFile.Write()
    histFile.Close()

## Read histograms from file
histFile = TFile.Open("confusionPlots_Bprime1400.root")

decaymodes_num = histFile.Get("B_decays")
decaymodes_alt = histFile.Get("B_decays_alt")
leptonmodes_num = histFile.Get("lepton_source")
leptonmodes_alt = histFile.Get("lepton_alt")

canv1 = TCanvas("c1","c1",800,600)
xlabels = ['t jet','untagged t','W jet','untagged W']
for ibin in range(1,decaymodes_num.GetNbinsX()+1):
    decaymodes_num.GetXaxis().SetBinLabel(ibin,xlabels[ibin-1])
    
ylabels = ['boosted t','unboosted t','boosted W','unboosted W']
for ibin in range(1,decaymodes_num.GetNbinsY()+1):
    decaymodes_num.GetYaxis().SetBinLabel(ibin,ylabels[ibin-1])
    
gStyle.SetOptStat(0)
gStyle.SetPaintTextFormat("1.2f")
canv1.SetLeftMargin(0.15);
decaymodes_num.Draw("colz texte")
canv1.SaveAs("decaymodes_1400_pNetOrig.png")
    


    
canv2 = TCanvas("c2","c2",800,600)
xlabels = ['reco W', 'reco T']
for ibin in range(1,leptonmodes_num.GetNbinsX()+1):
    leptonmodes_num.GetXaxis().SetBinLabel(ibin,xlabels[ibin-1])
    
ylabels = ['lep W', 'lep T']
for ibin in range(1,leptonmodes_num.GetNbinsY()+1):
    leptonmodes_num.GetYaxis().SetBinLabel(ibin,ylabels[ibin-1])

gStyle.SetOptStat(0)
gStyle.SetPaintTextFormat("1.2f")
leptonmodes_num.Draw("colz texte")
canv2.SaveAs("leptonmodes_1400_pNetOrig.png")

