import os 

# Question: A lot of the samples have _PSweights_.  The samples we were working with before didn't have this.  Is it good or bad?
# Sample Dictionaries: samples, samples_2022, samples_2022EE, samples_2023, samples_2023BPix, samples_test, samples_QCD

class sample:
    def __init__(self, prefix, year, textlist, samplename): #, color
        self.prefix = prefix
        self.year = year
        self.textlist = textlist
        self.samplename = samplename
        #self.color = color

/Tau/Run2022A-22Sep2023-v1/NANOAOD
/Tau/Run2022B-22Sep2023-v1/NANOAOD
/Tau/Run2022C-22Sep2023-v1/NANOAOD
/Tau/Run2022D-22Sep2023-v1/NANOAOD
/Tau/Run2022E-22Sep2023-v1/NANOAOD
/Tau/Run2022F-22Sep2023-v1/NANOAOD
/Tau/Run2022G-22Sep2023-v1/NANOAOD
/Tau/Run2023B-22Sep2023-v1/NANOAOD
/Tau/Run2023C-22Sep2023_v1-v2/NANOAOD
/Tau/Run2023C-22Sep2023_v2-v1/NANOAOD
/Tau/Run2023C-22Sep2023_v3-v1/NANOAOD
/Tau/Run2023C-22Sep2023_v4-v1/NANOAOD
/Tau/Run2023D-22Sep2023_v1-v1/NANOAOD
/Tau/Run2023D-22Sep2023_v2-v1/NANOAOD
/MuonEG/Run2022A-22Sep2023-v1/NANOAOD
/MuonEG/Run2022B-22Sep2023-v1/NANOAOD
/MuonEG/Run2022C-22Sep2023-v1/NANOAOD
/MuonEG/Run2022D-22Sep2023-v1/NANOAOD
/MuonEG/Run2022E-22Sep2023-v1/NANOAOD
/MuonEG/Run2022F-22Sep2023-v1/NANOAOD
/MuonEG/Run2022G-22Sep2023-v1/NANOAOD
/MuonEG/Run2023B-22Sep2023-v1/NANOAOD
/MuonEG/Run2023C-22Sep2023_v1-v1/NANOAOD
/MuonEG/Run2023C-22Sep2023_v2-v1/NANOAOD
/MuonEG/Run2023C-22Sep2023_v3-v1/NANOAOD
/MuonEG/Run2023C-22Sep2023_v4-v1/NANOAOD
/MuonEG/Run2023D-22Sep2023_v1-v1/NANOAOD
/MuonEG/Run2023D-22Sep2023_v2-v1/NANOAOD
/TprimeTprimeto2T4Tau_MT-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/TprimeTprimeto2T4Tau_MT-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM

/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM
/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM
/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM
/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM
/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM
/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM
/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM
/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM

/WWto2L2Nu-2Jets_OS_noTop_EW-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/WWto2L2Nu-2Jets_OS_noTop_EW-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/WWto2L2Nu-2Jets_OS_noTop_EW-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/WWto2L2Nu-2Jets_OS_noTop_EW-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM
/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM
/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM
/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM
/WZto3LNu-2Jets_EWK-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/WZto3LNu-2Jets_EWK-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/WZto3LNu-2Jets_EWK-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/WZto3LNu-2Jets_EWK-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/ZZto2L2Nu-2Jets_EW-QCD_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/ZZto2L2Nu-2Jets_EW-QCD_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/ZZto2L2Nu-2Jets_EW-QCD_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v3/NANOAODSIM
/ZZto2L2Nu-2Jets_EW-QCD_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/ZZto4L-2Jets_EW-QCD_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/ZZto4L-2Jets_EW-QCD_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/ZZto4L-2Jets_EW-QCD_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/ZZto4L-2Jets_EW-QCD_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM

/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-mg35x_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-mg35x_130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-mg35x_130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-mg35x_130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM
/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM
/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6_ext1-v2/NANOAODSIM
/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15_ext1-v2/NANOAODSIM

/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM
/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM
/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM
/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM
/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM
/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM
/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM
/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM
/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM
/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM
/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM


Bprime_M1000_2022 = sample("Bprime_M1000_2022", "2022", "Bprime_M1000_2022NanoList.txt", "/BprimeBtoTW_M-1000_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1000_2022EE = sample("Bprime_M1000_2022EE", "2022EE", "Bprime_M1000_2022EENanoList.txt", "/BprimeBtoTW_M-1000_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1000_2023 = sample("Bprime_M1000_2023", "2023", "Bprime_M1000_2023NanoList.txt", "/BprimeBtoTW_M-1000_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1000_2023BPix = sample("Bprime_M1000_2023BPix", "2023BPix", "Bprime_M1000_2023BPixNanoList.txt", "/BprimeBtoTW_M-1000_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M1200_2022 = sample("Bprime_M1200_2022", "2022", "Bprime_M1200_2022NanoList.txt", "/BprimeBtoTW_M-1200_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1200_2022EE = sample("Bprime_M1200_2022EE", "2022EE", "Bprime_M1200_2022EENanoList.txt", "/BprimeBtoTW_M-1200_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1200_2023 = sample("Bprime_M1200_2023", "2023", "Bprime_M1200_2023NanoList.txt", "/BprimeBtoTW_M-1200_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1200_2023BPix = sample("Bprime_M1200_2023BPix", "2023BPix", "Bprime_M1200_2023BPixNanoList.txt", "/BprimeBtoTW_M-1200_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M1300_2022 = sample("Bprime_M1300_2022", "2022", "Bprime_M1300_2022NanoList.txt", "/BprimeBtoTW_M-1300_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1300_2022EE = sample("Bprime_M1300_2022EE", "2022EE", "Bprime_M1300_2022EENanoList.txt", "/BprimeBtoTW_M-1300_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1300_2023 = sample("Bprime_M1300_2023", "2023", "Bprime_M1300_2023NanoList.txt", "/BprimeBtoTW_M-1300_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1300_2023BPix = sample("Bprime_M1300_2023BPix", "2023BPix", "Bprime_M1300_2023BPixNanoList.txt", "/BprimeBtoTW_M-1300_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M1400_2022 = sample("Bprime_M1400_2022", "2022", "Bprime_M1400_2022NanoList.txt", "/BprimeBtoTW_M-1400_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1400_2022EE = sample("Bprime_M1400_2022EE", "2022EE", "Bprime_M1400_2022EENanoList.txt", "/BprimeBtoTW_M-1400_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1400_2023 = sample("Bprime_M1400_2023", "2023", "Bprime_M1400_2023NanoList.txt", "/BprimeBtoTW_M-1400_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1400_2023BPix = sample("Bprime_M1400_2023BPix", "2023BPix", "Bprime_M1400_2023BPixNanoList.txt", "/BprimeBtoTW_M-1400_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M1500_2022 = sample("Bprime_M1500_2022", "2022", "Bprime_M1500_2022NanoList.txt", "/BprimeBtoTW_M-1500_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1500_2022EE = sample("Bprime_M1500_2022EE", "2022EE", "Bprime_M1500_2022EENanoList.txt", "/BprimeBtoTW_M-1500_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1500_2023 = sample("Bprime_M1500_2023", "2023", "Bprime_M1500_2023NanoList.txt", "/BprimeBtoTW_M-1500_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1500_2023BPix = sample("Bprime_M1500_2023BPix", "2023BPix", "Bprime_M1500_2023BPixNanoList.txt", "/BprimeBtoTW_M-1500_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M1600_2022 = sample("Bprime_M1600_2022", "2022", "Bprime_M1600_2022NanoList.txt", "/BprimeBtoTW_M-1600_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1600_2022EE = sample("Bprime_M1600_2022EE", "2022EE", "Bprime_M1600_2022EENanoList.txt", "/BprimeBtoTW_M-1600_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1600_2023 = sample("Bprime_M1600_2023", "2023", "Bprime_M1600_2023NanoList.txt", "/BprimeBtoTW_M-1600_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1600_2023BPix = sample("Bprime_M1600_2023BPix", "2023BPix", "Bprime_M1600_2023BPixNanoList.txt", "/BprimeBtoTW_M-1600_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M1700_2022 = sample("Bprime_M1700_2022", "2022", "Bprime_M1700_2022NanoList.txt", "/BprimeBtoTW_M-1700_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1700_2022EE = sample("Bprime_M1700_2022EE", "2022EE", "Bprime_M1700_2022EENanoList.txt", "/BprimeBtoTW_M-1700_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1700_2023 = sample("Bprime_M1700_2023", "2023", "Bprime_M1700_2023NanoList.txt", "/BprimeBtoTW_M-1700_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1700_2023BPix = sample("Bprime_M1700_2023BPix", "2023BPix", "Bprime_M1700_2023BPixNanoList.txt", "/BprimeBtoTW_M-1700_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M1800_2022 = sample("Bprime_M1800_2022", "2022", "Bprime_M1800_2022NanoList.txt", "/BprimeBtoTW_M-1800_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1800_2022EE = sample("Bprime_M1800_2022EE", "2022EE", "Bprime_M1800_2022EENanoList.txt", "/BprimeBtoTW_M-1800_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1800_2023 = sample("Bprime_M1800_2023", "2023", "Bprime_M1800_2023NanoList.txt", "/BprimeBtoTW_M-1800_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1800_2023BPix = sample("Bprime_M1800_2023BPix", "2023BPix", "Bprime_M1800_2023BPixNanoList.txt", "/BprimeBtoTW_M-1800_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M2000_2022 = sample("Bprime_M2000_2022", "2022", "Bprime_M2000_2022NanoList.txt", "/BprimeBtoTW_M-2000_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M2000_2022EE = sample("Bprime_M2000_2022EE", "2022EE", "Bprime_M2000_2022EENanoList.txt", "/BprimeBtoTW_M-2000_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M2000_2023 = sample("Bprime_M2000_2023", "2023", "Bprime_M2000_2023NanoList.txt", "/BprimeBtoTW_M-2000_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M2000_2023BPix = sample("Bprime_M2000_2023BPix", "2023BPix", "Bprime_M2000_2023BPixNanoList.txt", "/BprimeBtoTW_M-2000_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M2200_2022 = sample("Bprime_M2200_2022", "2022", "Bprime_M2200_2022NanoList.txt", "/BprimeBtoTW_M-2200_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M2200_2022EE = sample("Bprime_M2200_2022EE", "2022EE", "Bprime_M2200_2022EENanoList.txt", "/BprimeBtoTW_M-2200_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M2200_2023 = sample("Bprime_M2200_2023", "2023", "Bprime_M2200_2023NanoList.txt", "/BprimeBtoTW_M-2200_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M2200_2023BPix = sample("Bprime_M2200_2023BPix", "2023BPix", "Bprime_M2200_2023BPixNanoList.txt", "/BprimeBtoTW_M-2200_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M800_2022 = sample("Bprime_M800_2022", "2022", "Bprime_M800_2022NanoList.txt", "/BprimeBtoTW_M-800_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M800_2022EE  = sample("Bprime_M800_2022EE", "2022EE", "Bprime_M800_2022EENanoList.txt", "/BprimeBtoTW_M-800_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M800_2023  = sample("Bprime_M800_2023", "2023", "Bprime_M800_2023NanoList.txt", "/BprimeBtoTW_M-800_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M800_2023BPix  = sample("Bprime_M800_2023BPix", "2023BPix", "Bprime_M800_2023BPixNanoList.txt", "/BprimeBtoTW_M-800_NWALO_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

DYPT402022 = sample("DYPT402022", "2022", "DYPT402022NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-40to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
DYPT402022EE = sample("DYPT402022EE", "2022EE", "DYPT402022EENanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-40to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
DYPT402023 = sample("DYPT402023", "2023", "DYPT402023NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-40to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
DYPT402023BPix = sample("DYPT402023BPix", "2023BPix", "DYPT402023BPixNanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-40to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
DYPT1002022 = sample("DYPT1002022", "2022", "DYPT1002022NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
DYPT1002022EE = sample("DYPT1002022EE", "2022EE", "DYPT1002022EENanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
DYPT1002023 = sample("DYPT1002023", "2023", "DYPT1002023NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
DYPT1002023BPix = sample("DYPT1002023BPix", "2023BPix", "DYPT1002023BPixNanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
DYPT2002022 = sample("DYPT2002022", "2022", "DYPT2002022NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
DYPT2002022EE = sample("DYPT2002022EE", "2022EE", "DYPT2002022EENanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
DYPT2002023 = sample("DYPT2002023", "2023", "DYPT2002023NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
DYPT2002023BPix = sample("DYPT2002023BPix", "2023BPix", "DYPT2002023BPixNanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
DYPT4002022 = sample("DYPT4002022", "2022", "DYPT4002022NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
DYPT4002022EE = sample("DYPT4002022EE", "2022EE", "DYPT4002022EENanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
DYPT4002023 = sample("DYPT4002023", "2023", "DYPT4002023NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
DYPT4002023BPix = sample("DYPT4002023BPix", "2023BPix", "DYPT4002023BPixNanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
DYPT6002022 = sample("DYPT6002022", "2022", "DYPT6002022NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
DYPT6002022EE = sample("DYPT6002022EE", "2022EE", "DYPT6002022EENanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
DYPT6002023 = sample("DYPT6002023", "2023", "DYPT6002023NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
DYPT6002023BPix = sample("DYPT6002023BPix", "2023BPix", "DYPT6002023BPixNanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

QCDHT10002022  = sample("QCDHT10002022", "2022", "QCDHT10002022NanoList.txt", "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
QCDHT10002022EE     = sample("QCDHT10002022EE", "2022EE", "QCDHT10002022EENanoList.txt", "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
QCDHT10002023     = sample("QCDHT10002023", "2023", "QCDHT10002023NanoList.txt", "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
QCDHT10002023BPix     = sample("QCDHT10002023BPix", "2023BPix", "QCDHT10002023BPixNanoList.txt", "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM")
QCDHT12002022  = sample("QCDHT12002022", "2022", "QCDHT12002022NanoList.txt", "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
QCDHT12002022EE     = sample("QCDHT12002022EE", "2022EE", "QCDHT12002022EENanoList.txt", "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
QCDHT12002023     = sample("QCDHT12002023", "2023", "QCDHT12002023NanoList.txt", "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
QCDHT12002023BPix     = sample("QCDHT12002023BPix", "2023BPix", "QCDHT12002023BPixNanoList.txt", "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM")
QCDHT15002022  = sample("QCDHT15002022", "2022", "QCDHT15002022NanoList.txt", "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
QCDHT15002022EE     = sample("QCDHT15002022EE", "2022EE", "QCDHT15002022EENanoList.txt", "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
QCDHT15002023     = sample("QCDHT15002023", "2023", "QCDHT15002023NanoList.txt", "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM")
QCDHT15002023BPix     = sample("QCDHT15002023BPix", "2023BPix", "QCDHT15002023BPixNanoList.txt", "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
QCDHT20002022  = sample("QCDHT20002022", "2022", "QCDHT20002022NanoList.txt", "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
QCDHT20002022EE     = sample("QCDHT20002022EE", "2022EE", "QCDHT20002022EENanoList.txt", "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
QCDHT20002023     = sample("QCDHT20002023", "2023", "QCDHT20002023NanoList.txt", "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
QCDHT20002023BPix     = sample("QCDHT20002023BPix", "2023BPix", "QCDHT20002023BPixNanoList.txt", "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM")
QCDHT2002022   = sample("QCDHT2002022", "2022", "QCDHT2002022NanoList.txt", "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
QCDHT2002022EE      = sample("QCDHT2002022EE", "2022EE", "QCDHT2002022EENanoList.txt", "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
QCDHT2002023      = sample("QCDHT2002023", "2023", "QCDHT2002023NanoList.txt", "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
QCDHT2002023BPix      = sample("QCDHT2002023BPix", "2023BPix", "QCDHT2002023BPixNanoList.txt", "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
QCDHT4002022   = sample("QCDHT4002022", "2022", "QCDHT4002022NanoList.txt", "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
QCDHT4002022EE      = sample("QCDHT4002022EE", "2022EE", "QCDHT4002022EENanoList.txt", "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
QCDHT4002023      = sample("QCDHT4002023", "2023", "QCDHT4002023NanoList.txt", "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM")
QCDHT4002023BPix      = sample("QCDHT4002023BPix", "2023BPix", "QCDHT4002023BPixNanoList.txt", "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM")
QCDHT6002022   = sample("QCDHT6002022", "2022", "QCDHT6002022NanoList.txt", "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
QCDHT6002022EE      = sample("QCDHT6002022EE", "2022EE", "QCDHT6002022EENanoList.txt", "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
QCDHT6002023      = sample("QCDHT6002023", "2023", "QCDHT6002023NanoList.txt", "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
QCDHT6002023BPix      = sample("QCDHT6002023BPix", "2023BPix", "QCDHT6002023BPixNanoList.txt", "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
QCDHT8002022   = sample("QCDHT8002022", "2022", "QCDHT8002022NanoList.txt", "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
QCDHT8002022EE      = sample("QCDHT8002022EE", "2022EE", "QCDHT8002022EENanoList.txt", "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
QCDHT8002023      = sample("QCDHT8002023", "2023", "QCDHT8002023NanoList.txt", "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
QCDHT8002023BPix      = sample("QCDHT8002023BPix", "2023BPix", "QCDHT8002023BPixNanoList.txt", "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM")

SingleElecRun2022C = sample("SingleElecRun2022C", "2022", "SingleElecRun2022C2022NanoList.txt", "/EGamma/Run2022C-22Sep2023-v1/NANOAOD")
SingleElecRun2022D = sample("SingleElecRun2022D", "2022", "SingleElecRun2022D2022NanoList.txt", "/EGamma/Run2022D-22Sep2023-v1/NANOAOD")
SingleElecRun2022EEE  = sample("SingleElecRun2022EEE", "2022EE", "SingleElecRun2022EEE2022EENanoList.txt", "/EGamma/Run2022E-22Sep2023-v1/NANOAOD")
SingleElecRun2022EEF  = sample("SingleElecRun2022EEF", "2022EE", "SingleElecRun2022EEF2022EENanoList.txt", "/EGamma/Run2022F-22Sep2023-v1/NANOAOD")
SingleElecRun2022EEG  = sample("SingleElecRun2022EEG", "2022EE", "SingleElecRun2022EEG2022EENanoList.txt", "/EGamma/Run2022G-22Sep2023-v2/NANOAOD")
SingleElecRun2023C01  = sample("SingleElecRun2023C01", "2023", "SingleElecRun2023C012023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v1-v1/NANOAOD")
SingleElecRun2023C02  = sample("SingleElecRun2023C02", "2023", "SingleElecRun2023C022023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v2-v1/NANOAOD")
SingleElecRun2023C03  = sample("SingleElecRun2023C03", "2023", "SingleElecRun2023C032023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v3-v1/NANOAOD")
SingleElecRun2023C04  = sample("SingleElecRun2023C04", "2023", "SingleElecRun2023C042023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v4-v1/NANOAOD")
SingleElecRun2023C11  = sample("SingleElecRun2023C11", "2023", "SingleElecRun2023C112023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v1-v1/NANOAOD")
SingleElecRun2023C12  = sample("SingleElecRun2023C12", "2023", "SingleElecRun2023C122023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v2-v1/NANOAOD")
SingleElecRun2023C13  = sample("SingleElecRun2023C13", "2023", "SingleElecRun2023C132023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v3-v1/NANOAOD")
SingleElecRun2023C14  = sample("SingleElecRun2023C14", "2023", "SingleElecRun2023C142023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v4-v1/NANOAOD")
SingleElecRun2023BPixD01  = sample("SingleElecRun2023BPixD01", "2023BPix", "SingleElecRun2023BPixD012023BPixNanoList.txt", "/EGamma0/Run2023D-22Sep2023_v1-v1/NANOAOD")
SingleElecRun2023BPixD02  = sample("SingleElecRun2023BPixD02", "2023BPix", "SingleElecRun2023BPixD022023BPixNanoList.txt", "/EGamma0/Run2023D-22Sep2023_v2-v1/NANOAOD")
SingleElecRun2023BPixD11  = sample("SingleElecRun2023BPixD11", "2023BPix", "SingleElecRun2023BPixD112023BPixNanoList.txt", "/EGamma1/Run2023D-22Sep2023_v1-v1/NANOAOD")
SingleElecRun2023BPixD12  = sample("SingleElecRun2023BPixD12", "2023BPix", "SingleElecRun2023BPixD122023BPixNanoList.txt", "/EGamma1/Run2023D-22Sep2023_v2-v1/NANOAOD")

SingleMuonRun2022C = sample("SingleMuonRun2022C", "2022", "SingleMuonRun2022C2022NanoList.txt", "/Muon/Run2022C-22Sep2023-v1/NANOAOD")
SingleMuonRun2022D = sample("SingleMuonRun2022D", "2022", "SingleMuonRun2022D2022NanoList.txt", "/Muon/Run2022D-22Sep2023-v1/NANOAOD")
SingleMuonRun2022EEE  = sample("SingleMuonRun2022EEE", "2022EE", "SingleMuonRun2022EEE2022EENanoList.txt", "/Muon/Run2022E-22Sep2023-v1/NANOAOD")
SingleMuonRun2022EEF  = sample("SingleMuonRun2022EEF", "2022EE", "SingleMuonRun2022EEF2022EENanoList.txt", "/Muon/Run2022F-22Sep2023-v2/NANOAOD")
SingleMuonRun2022EEG  = sample("SingleMuonRun2022EEG", "2022EE", "SingleMuonRun2022EEG2022EENanoList.txt", "/Muon/Run2022G-22Sep2023-v1/NANOAOD")
SingleMuonRun2023C01  = sample("SingleMuonRun2023C01", "2023", "SingleMuonRun2023C012023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v1-v1/NANOAOD")
SingleMuonRun2023C02  = sample("SingleMuonRun2023C02", "2023", "SingleMuonRun2023C022023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v2-v1/NANOAOD")
SingleMuonRun2023C03  = sample("SingleMuonRun2023C03", "2023", "SingleMuonRun2023C032023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v3-v1/NANOAOD")
SingleMuonRun2023C04  = sample("SingleMuonRun2023C04", "2023", "SingleMuonRun2023C042023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v4-v1/NANOAOD")
SingleMuonRun2023C11  = sample("SingleMuonRun2023C11", "2023", "SingleMuonRun2023C112023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v1-v1/NANOAOD")
SingleMuonRun2023C12  = sample("SingleMuonRun2023C12", "2023", "SingleMuonRun2023C122023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v2-v1/NANOAOD")
SingleMuonRun2023C13  = sample("SingleMuonRun2023C13", "2023", "SingleMuonRun2023C132023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v3-v1/NANOAOD")
SingleMuonRun2023C14  = sample("SingleMuonRun2023C14", "2023", "SingleMuonRun2023C142023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v4-v2/NANOAOD")
SingleMuonRun2023BPixD01  = sample("SingleMuonRun2023BPixD01", "2023BPix", "SingleMuonRun2023BPixD012023BPixNanoList.txt", "/Muon0/Run2023D-22Sep2023_v1-v1/NANOAOD")
SingleMuonRun2023BPixD02  = sample("SingleMuonRun2023BPixD02", "2023BPix", "SingleMuonRun2023BPixD022023BPixNanoList.txt", "/Muon0/Run2023D-22Sep2023_v2-v1/NANOAOD")
SingleMuonRun2023BPixD11  = sample("SingleMuonRun2023BPixD11", "2023BPix", "SingleMuonRun2023BPixD112023BPixNanoList.txt", "/Muon1/Run2023D-22Sep2023_v1-v1/NANOAOD")
SingleMuonRun2023BPixD12  = sample("SingleMuonRun2023BPixD12", "2023BPix", "SingleMuonRun2023BPixD122023BPixNanoList.txt", "/Muon1/Run2023D-22Sep2023_v2-v1/NANOAOD")

STs2022 = sample("STs2022", "2022", "STs2022NanoList.txt", "/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
STs2022EE = sample("STs2022EE", "2022EE", "STs2022EENanoList.txt", "/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
STs2023 = sample("STs2023", "2023", "STs2023NanoList.txt", "/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
STs2023BPix = sample("STs2023BPix", "2023BPix", "STs2023BPixNanoList.txt", "/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
STbs2022 = sample("STbs2022", "2022", "STbs2022NanoList.txt", "/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
STbs2022EE = sample("STbs2022EE", "2022EE", "STbs2022EENanoList.txt", "/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
STbs2023 = sample("STbs2023", "2023", "STbs2023NanoList.txt", "/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
STbs2023BPix = sample("STbs2023BPix", "2023BPix", "STbs2023BPixNanoList.txt", "/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

STt2022 = sample("STt2022", "2022", "STt2022NanoList.txt", "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
STt2022EE = sample("STt2022EE", "2022EE", "STt2022EENanoList.txt", "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
STt2023 = sample("STt2023", "2023", "STt2023NanoList.txt", "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
STt2023BPix = sample("STt2023BPix", "2023BPix", "STt2023BPixNanoList.txt", "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
STtb2022 = sample("STtb2022", "2022", "STtb2022NanoList.txt", "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
STtb2022EE = sample("STtb2022EE", "2022EE", "STtb2022EENanoList.txt", "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
STtb2023 = sample("STtb2023", "2023", "STtb2023NanoList.txt", "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
STtb2023BPix = sample("STtb2023BPix", "2023BPix", "STtb2023BPixNanoList.txt", "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

# 2L2Nu and 4Q exist, can add if needed
STtW2022 = sample("STtW2022", "2022", "STtW2022NanoList.txt", "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
STtW2022ext = sample("STtW2022ext", "2022", "STtW2022extNanoList.txt", "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
STtW2022EE = sample("STtW2022EE", "2022EE", "STtW2022EENanoList.txt", "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
STtW2022EEext = sample("STtW2022EEext", "2022EE", "STtW2022EEextNanoList.txt", "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
STtW2023 = sample("STtW2023", "2023", "STtW2023NanoList.txt", "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
STtW2023BPix = sample("STtW2023BPix", "2023BPix", "STtW2023BPixNanoList.txt", "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
STtWb2022 = sample("STtWb2022", "2022", "STtWb2022NanoList.txt", "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
STtWb2022ext = sample("STtWb2022ext", "2022", "STtWb2022extNanoList.txt", "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
STtWb2022EE = sample("STtWb2022EE", "2022EE", "STtWb2022EENanoList.txt", "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
STtWb2022EEext = sample("STtWb2022EEext", "2022EE", "STtWb2022EEextNanoList.txt", "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
STtWb2023 = sample("STtWb2023", "2023", "STtWb2023NanoList.txt", "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
STtWb2023BPix = sample("STtWb2023BPix", "2023BPix", "STtWb2023BPixNanoList.txt", "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")

TTHB2022 = sample("TTHB2022", "2022", "TTHB2022NanoList.txt", "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM")
TTHB2022EE = sample("TTHB2022EE", "2022EE", "TTHB2022EENanoList.txt", "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
TTHB2023 = sample("TTHB2023", "2023", "TTHB2023NanoList.txt", "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM")
TTHB2023BPix = sample("TTHB2023BPix", "2023BPix", "TTHB2023BPixNanoList.txt", "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
TTHnonB2022 = sample("TTHnonB2022", "2022", "TTHnonB2022NanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM")
TTHnonB2022EE = sample("TTHnonB2022EE", "2022EE", "TTHnonB2022EENanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTHnonB2023 = sample("TTHnonB2023", "2023", "TTHnonB2023NanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
TTHnonB2023BPix = sample("TTHnonB2023BPix", "2023BPix", "TTHnonB2023BPixNanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")

#TTMT10002022 = sample("TTMT10002022", "2022", "TTMT10002022NanoList.txt", "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
#TTMT10002022EE = sample("TTMT10002022EE", "2022EE", "TTMT10002022EENanoList.txt", "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
#TTMT10002023 = sample("TTMT10002023", "2023", "TTMT10002023NanoList.txt", "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
#TTMT10002023BPix = sample("TTMT10002023BPix", "2023BPix", "TTMT10002023BPixNanoList.txt", "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
#TTMT7002022 = sample("TTMT7002022", "2022", "TTMT7002022NanoList.txt", "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
#TTMT7002022EE = sample("TTMT7002022EE", "2022EE", "TTMT7002022EENanoList.txt", "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
#TTMT7002023 = sample("TTMT7002023", "2023", "TTMT7002023NanoList.txt", "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
#TTMT7002023BPix = sample("TTMT7002023BPix", "2023BPix", "TTMT7002023BPixNanoList.txt", "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")

TTTo2L2Nu2022 = sample("TTTo2L2Nu2022", "2022", "TTTo2L2Nu2022NanoList.txt", "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTTo2L2Nu2022ext = sample("TTTo2L2Nu2022ext", "2022", "TTTo2L2Nu2022extNanoList.txt", "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
TTTo2L2Nu2022EE = sample("TTTo2L2Nu2022EE", "2022EE", "TTTo2L2Nu2022EENanoList.txt", "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTTo2L2Nu2022EEext = sample("TTTo2L2Nu2022EEext", "2022EE", "TTTo2L2Nu2022EEextNanoList.txt", "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
TTTo2L2Nu2023 = sample("TTTo2L2Nu2023", "2023", "TTTo2L2Nu2023NanoList.txt", "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
TTTo2L2Nu2023BPix = sample("TTTo2L2Nu2023BPix", "2023BPix", "TTTo2L2Nu2023BPixNanoList.txt", "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
TTToHadronic2022 = sample("TTToHadronic2022", "2022", "TTToHadronic2022NanoList.txt", "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTToHadronic2022ext = sample("TTToHadronic2022ext", "2022", "TTToHadronic2022extNanoList.txt", "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
TTToHadronic2022EE = sample("TTToHadronic2022EE", "2022EE", "TTToHadronic2022EENanoList.txt", "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTToHadronic2022EEext = sample("TTToHadronic2022EEext", "2022EE", "TTToHadronic2022EEextNanoList.txt", "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
TTToHadronic2023 = sample("TTToHadronic2023", "2023", "TTToHadronic2023NanoList.txt", "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
TTToHadronic2023BPix = sample("TTToHadronic2023BPix", "2023BPix", "TTToHadronic2023BPixNanoList.txt", "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
TTToSemiLeptonic2022 = sample("TTToSemiLeptonic2022", "2022", "TTToSemiLeptonic2022NanoList.txt", "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTToSemiLeptonic2022ext = sample("TTToSemiLeptonic2022ext", "2022", "TTToSemiLeptonic2022extNanoList.txt", "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
TTToSemiLeptonic2022EE = sample("TTToSemiLeptonic2022EE", "2022EE", "TTToSemiLeptonic2022EENanoList.txt", "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTToSemiLeptonic2022EEext = sample("TTToSemiLeptonic2022EEext", "2022EE", "TTToSemiLeptonic2022EEextNanoList.txt", "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
TTToSemiLeptonic2023 = sample("TTToSemiLeptonic2023", "2023", "TTToSemiLeptonic2023NanoList.txt", "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
TTToSemiLeptonic2023BPix = sample("TTToSemiLeptonic2023BPix", "2023BPix", "TTToSemiLeptonic2023BPixNanoList.txt", "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")

# 2023 not available yet... https://indico.cern.ch/event/1440343/ -- check back in Jan and see if it's there
# https://its.cern.ch/jira/projects/CMSTOPMCREQ/issues/CMSTOPMCREQ-15?filter=allopenissues -- looks like TTW-WtoQQ are expected...
TTWl2022 = sample("TTWl2022", "2022", "TTWl2022NanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM")
TTWl2022EE = sample("TTWl2022EE", "2022EE", "TTWl2022EENanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM")
TTWl2023 = sample("TTWl2023", "2023", "TTWl2023NanoList.txt", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
TTWl2023BPix = sample("TTWl2023BPix", "2023BPix", "TTWl2023BPixNanoList.txt", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
TTWq2022 = sample("TTWq2022", "2022", "TTWq2022NanoList.txt", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTWq2022EE = sample("TTWq2022EE", "2022EE", "TTWq2022EENanoList.txt", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTWq2023 = sample("TTWq2023", "2023", "TTWq2023NanoList.txt", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
TTWq2023BPix = sample("TTWq2023BPix", "2023BPix", "TTWq2023BPixNanoList.txt", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")

TTZM102022 = sample("TTZM102022", "2022", "TTZM102022NanoList.txt", "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTZM102022EE = sample("TTZM102022EE", "2022EE", "TTZM102022EENanoList.txt", "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTZM102023 = sample("TTZM102023", "2023", "TTZM102023NanoList.txt", "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTZM102023BPix = sample("TTZM102023BPix", "2023BPix", "TTZM102023BPixNanoList.txt", "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTZM1to102022 = sample("TTZM1to102022", "2022", "TTZM1to102022NanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTZM1to102022EE = sample("TTZM1to102022EE", "2022EE", "TTZM1to102022EENanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTZM1to102023 = sample("TTZM1to102023", "2023", "TTZM1to102023NanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTZM1to102023BPix = sample("TTZM1to102023BPix", "2023BPix", "TTZM1to102023BPixNanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

WJetsHT1002022 = sample("WJetsHT1002022", "2022", "WJetsHT1002022NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM")
WJetsHT1002022EE = sample("WJetsHT1002022EE", "2022EE", "WJetsHT1002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
WJetsHT1002023 = sample("WJetsHT1002023", "2023", "WJetsHT1002023NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WJetsHT1002023BPix = sample("WJetsHT1002023BPix", "2023BPix", "WJetsHT1002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
WJetsHT15002022 = sample("WJetsHT15002022", "2022", "WJetsHT15002022NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WJetsHT15002022EE = sample("WJetsHT15002022EE", "2022EE", "WJetsHT15002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WJetsHT15002023 = sample("WJetsHT15002023", "2023", "WJetsHT15002023NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM")
WJetsHT15002023BPix = sample("WJetsHT15002023BPix", "2023BPix", "WJetsHT15002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
WJetsHT25002022 = sample("WJetsHT25002022", "2022", "WJetsHT25002022NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WJetsHT25002022EE = sample("WJetsHT25002022EE", "2022EE", "WJetsHT25002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WJetsHT25002023 = sample("WJetsHT25002023", "2023", "WJetsHT25002023NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM")
WJetsHT25002023BPix = sample("WJetsHT25002023BPix", "2023BPix", "WJetsHT25002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM") #invalid
WJetsHT4002022 = sample("WJetsHT4002022", "2022", "WJetsHT4002022NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM")
WJetsHT4002022EE = sample("WJetsHT4002022EE", "2022EE", "WJetsHT4002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
WJetsHT4002023 = sample("WJetsHT4002023", "2023", "WJetsHT4002023NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WJetsHT4002023BPix = sample("WJetsHT4002023BPix", "2023BPix", "WJetsHT4002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
WJetsHT8002022 = sample("WJetsHT8002022", "2022", "WJetsHT8002022NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WJetsHT8002022EE = sample("WJetsHT8002022EE", "2022EE", "WJetsHT8002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WJetsHT8002023 = sample("WJetsHT8002023", "2023", "WJetsHT8002023NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v5/NANOAODSIM")
WJetsHT8002023BPix = sample("WJetsHT8002023BPix", "2023BPix", "WJetsHT8002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
WJetsM120HT1002022 = sample("WJetsM120HT1002022", "2022", "WJetsM120HT1002022NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WJetsM120HT1002022EE = sample("WJetsM120HT1002022EE", "2022EE", "WJetsM120HT1002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WJetsM120HT1002023 = sample("WJetsM120HT1002023", "2023", "WJetsM120HT1002023NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM")
WJetsM120HT1002023BPix = sample("WJetsM120HT1002023BPix", "2023BPix", "WJetsM120HT1002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
WJetsM120HT15002022 = sample("WJetsM120HT15002022", "2022", "WJetsM120HT15002022NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WJetsM120HT15002022EE = sample("WJetsM120HT15002022EE", "2022EE", "WJetsM120HT15002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WJetsM120HT15002023 = sample("WJetsM120HT15002023", "2023", "WJetsM120HT15002023NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM")
WJetsM120HT15002023BPix = sample("WJetsM120HT15002023BPix", "2023BPix", "WJetsM120HT15002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
WJetsM120HT25002022 = sample("WJetsM120HT25002022", "2022", "WJetsM120HT25002022NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WJetsM120HT25002022EE = sample("WJetsM120HT25002022EE", "2022EE", "WJetsM120HT25002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WJetsM120HT25002023 = sample("WJetsM120HT25002023", "2023", "WJetsM120HT25002023NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM")
WJetsM120HT25002023BPix = sample("WJetsM120HT25002023BPix", "2023BPix", "WJetsM120HT25002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
WJetsM120HT4002022 = sample("WJetsM120HT4002022", "2022", "WJetsM120HT4002022NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WJetsM120HT4002022EE = sample("WJetsM120HT4002022EE", "2022EE", "WJetsM120HT4002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WJetsM120HT4002023 = sample("WJetsM120HT4002023", "2023", "WJetsM120HT4002023NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM")
WJetsM120HT4002023BPix = sample("WJetsM120HT4002023BPix", "2023BPix", "WJetsM120HT4002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM") #invalid
WJetsM120HT8002022 = sample("WJetsM120HT8002022", "2022", "WJetsM120HT8002022NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WJetsM120HT8002022EE = sample("WJetsM120HT8002022EE", "2022EE", "WJetsM120HT8002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WJetsM120HT8002023 = sample("WJetsM120HT8002023", "2023", "WJetsM120HT8002023NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM")
WJetsM120HT8002023BPix = sample("WJetsM120HT8002023BPix", "2023BPix", "WJetsM120HT8002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v3/NANOAODSIM")

# 4Q exists, could add if needed
WW2L2022 = sample("WW2L2022", "2022", "WW2L2022NanoList.txt", "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WW2L2022ext = sample("WW2L2022ext", "2022", "WW2L2022extNanoList.txt", "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
WW2L2022EE = sample("WW2L2022EE", "2022EE", "WW2L2022EENanoList.txt", "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WW2L2022EEext = sample("WW2L2022EEext", "2022EE", "WW2L2022EEextNanoList.txt", "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
WW2L2023 = sample("WW2L2023", "2023", "WW2L2023NanoList.txt", "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v4/NANOAODSIM")
WW2L2023BPix = sample("WW2L2023BPix", "2023BPix", "WW2L2023BPixNanoList.txt", "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
WW1L2022 = sample("WW1L2022", "2022", "WW1L2022NanoList.txt", "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WW1L2022ext = sample("WW1L2022ext", "2022", "WW1L2022extNanoList.txt", "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
WW1L2022EE = sample("WW1L2022EE", "2022EE", "WW1L2022EENanoList.txt", "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WW1L2022EEext = sample("WW1L2022EEext", "2022EE", "WW1L2022EEextNanoList.txt", "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
WW1L2023 = sample("WW1L2023", "2023", "WW1L2023NanoList.txt", "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM")
WW1L2023BPix = sample("WW1L2023BPix", "2023BPix", "WW1L2023BPixNanoList.txt", "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
WZ2L2022 = sample("WZ2L2022", "2022", "WZ2L2022NanoList.txt", "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WZ2L2022ext = sample("WZ2L2022ext", "2022", "WZ2L2022extNanoList.txt", "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
WZ2L2022EE = sample("WZ2L2022EE", "2022EE", "WZ2L2022EENanoList.txt", "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WZ2L2022EEext = sample("WZ2L2022EEext", "2022EE", "WZ2L2022EEextNanoList.txt", "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
WZ2L2023 = sample("WZ2L2023", "2023", "WZ2L2023NanoList.txt", "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM")
WZ2L2023BPix = sample("WZ2L2023BPix", "2023BPix", "WZ2L2023BPixNanoList.txt", "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")
WZ1L2022 = sample("WZ1L2022", "2022", "WZ1L2022NanoList.txt", "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WZ1L2022ext = sample("WZ1L2022ext", "2022", "WZ1L2022extNanoList.txt", "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
WZ1L2022EE = sample("WZ1L2022EE", "2022EE", "WZ1L2022EENanoList.txt", "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WZ1L2022EEext = sample("WZ1L2022EEext", "2022EE", "WZ1L2022EEextNanoList.txt", "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
WZ1L2023 = sample("WZ1L2023", "2023", "WZ1L2023NanoList.txt", "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WZ1L2023BPix = sample("WZ1L2023BPix", "2023BPix", "WZ1L2023BPixNanoList.txt", "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")

# 2L2Nu exists, could add if needed
ZZ2022 = sample("ZZ2022", "2022", "ZZ2022NanoList.txt", "/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
ZZ2022ext = sample("ZZ2022ext", "2022", "ZZ2022extNanoList.txt", "/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
ZZ2022EE = sample("ZZ2022EE", "2022EE", "ZZ2022EENanoList.txt", "/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
ZZ2022EEext = sample("ZZ2022EEext", "2022EE", "ZZ2022EEextNanoList.txt", "/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
ZZ2023 = sample("ZZ2023", "2023", "ZZ2023NanoList.txt", "/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM")
ZZ2023BPix = sample("ZZ2023BPix", "2023BPix", "ZZ2023BPixNanoList.txt", "/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")

samples_data = {
    "SingleElecRun2022C":      SingleElecRun2022C,      
    "SingleElecRun2022D":      SingleElecRun2022D,      
    "SingleElecRun2022EEE":    SingleElecRun2022EEE,    
    "SingleElecRun2022EEF":    SingleElecRun2022EEF,    
    "SingleElecRun2022EEG":    SingleElecRun2022EEG,    
    "SingleElecRun2023C01":    SingleElecRun2023C01,    
    "SingleElecRun2023C02":    SingleElecRun2023C02,    
    "SingleElecRun2023C03":    SingleElecRun2023C03,    
    "SingleElecRun2023C04":    SingleElecRun2023C04,    
    "SingleElecRun2023C11":    SingleElecRun2023C11,    
    "SingleElecRun2023C12":    SingleElecRun2023C12,    
    "SingleElecRun2023C13":    SingleElecRun2023C13,    
    "SingleElecRun2023C14":    SingleElecRun2023C14,    
    "SingleElecRun2023BPixD01":SingleElecRun2023BPixD01,
    "SingleElecRun2023BPixD02":SingleElecRun2023BPixD02,
    "SingleElecRun2023BPixD11":SingleElecRun2023BPixD11,
    "SingleElecRun2023BPixD12":SingleElecRun2023BPixD12,
    "SingleMuonRun2022C":      SingleMuonRun2022C,      
    "SingleMuonRun2022D":      SingleMuonRun2022D,      
    "SingleMuonRun2022EEE":    SingleMuonRun2022EEE,    
    "SingleMuonRun2022EEF":    SingleMuonRun2022EEF,    
    "SingleMuonRun2022EEG":    SingleMuonRun2022EEG,    
    "SingleMuonRun2023C01":    SingleMuonRun2023C01,    
    "SingleMuonRun2023C02":    SingleMuonRun2023C02,    
    "SingleMuonRun2023C03":    SingleMuonRun2023C03,    
    "SingleMuonRun2023C04":    SingleMuonRun2023C04,    
    "SingleMuonRun2023C11":    SingleMuonRun2023C11,    
    "SingleMuonRun2023C12":    SingleMuonRun2023C12,    
    "SingleMuonRun2023C13":    SingleMuonRun2023C13,    
    "SingleMuonRun2023C14":    SingleMuonRun2023C14,    
    "SingleMuonRun2023BPixD01":SingleMuonRun2023BPixD01,
    "SingleMuonRun2023BPixD02":SingleMuonRun2023BPixD02,
    "SingleMuonRun2023BPixD11":SingleMuonRun2023BPixD11,
    "SingleMuonRun2023BPixD12":SingleMuonRun2023BPixD12,
}

samples={
    "Bprime_M1000_2022":    Bprime_M1000_2022,    
    "Bprime_M1000_2022EE":  Bprime_M1000_2022EE,  
    "Bprime_M1000_2023":    Bprime_M1000_2023,    
    "Bprime_M1000_2023BPix":Bprime_M1000_2023BPix,
    "Bprime_M1200_2022":    Bprime_M1200_2022,    
    "Bprime_M1200_2022EE":  Bprime_M1200_2022EE,  
    "Bprime_M1200_2023":    Bprime_M1200_2023,    
    "Bprime_M1200_2023BPix":Bprime_M1200_2023BPix,
    "Bprime_M1300_2022":    Bprime_M1300_2022,    
    "Bprime_M1300_2022EE":  Bprime_M1300_2022EE,  
    "Bprime_M1300_2023":    Bprime_M1300_2023,    
    "Bprime_M1300_2023BPix":Bprime_M1300_2023BPix,
    "Bprime_M1400_2022":    Bprime_M1400_2022,    
    "Bprime_M1400_2022EE":  Bprime_M1400_2022EE,  
    "Bprime_M1400_2023":    Bprime_M1400_2023,    
    "Bprime_M1400_2023BPix":Bprime_M1400_2023BPix,
    "Bprime_M1500_2022":    Bprime_M1500_2022,    
    "Bprime_M1500_2022EE":  Bprime_M1500_2022EE,  
    "Bprime_M1500_2023":    Bprime_M1500_2023,    
    "Bprime_M1500_2023BPix":Bprime_M1500_2023BPix,
    "Bprime_M1600_2022":    Bprime_M1600_2022,    
    "Bprime_M1600_2022EE":  Bprime_M1600_2022EE,  
    "Bprime_M1600_2023":    Bprime_M1600_2023,    
    "Bprime_M1600_2023BPix":Bprime_M1600_2023BPix,
    "Bprime_M1700_2022":    Bprime_M1700_2022,    
    "Bprime_M1700_2022EE":  Bprime_M1700_2022EE,  
    "Bprime_M1700_2023":    Bprime_M1700_2023,    
    "Bprime_M1700_2023BPix":Bprime_M1700_2023BPix,
    "Bprime_M1800_2022":    Bprime_M1800_2022,    
    "Bprime_M1800_2022EE":  Bprime_M1800_2022EE,  
    "Bprime_M1800_2023":    Bprime_M1800_2023,    
    "Bprime_M1800_2023BPix":Bprime_M1800_2023BPix,
    "Bprime_M2000_2022":    Bprime_M2000_2022,    
    "Bprime_M2000_2022EE":  Bprime_M2000_2022EE,  
    "Bprime_M2000_2023":    Bprime_M2000_2023,    
    "Bprime_M2000_2023BPix":Bprime_M2000_2023BPix,
    "Bprime_M2200_2022":    Bprime_M2200_2022,    
    "Bprime_M2200_2022EE":  Bprime_M2200_2022EE,  
    "Bprime_M2200_2023":    Bprime_M2200_2023,    
    "Bprime_M2200_2023BPix":Bprime_M2200_2023BPix,
    "Bprime_M800_2022":     Bprime_M800_2022,     
    "Bprime_M800_2022EE ":  Bprime_M800_2022EE ,  
    "Bprime_M800_2023":     Bprime_M800_2023,     
    "Bprime_M800_2023BPix": Bprime_M800_2023BPix, 
    "DYPT402022":     DYPT402022,     
    "DYPT402022EE":   DYPT402022EE,   
    "DYPT402023":     DYPT402023,     
    "DYPT402023BPix": DYPT402023BPix, 
    "DYPT1002022":    DYPT1002022,    
    "DYPT1002022EE":  DYPT1002022EE,  
    "DYPT1002023":    DYPT1002023,    
    "DYPT1002023BPix":DYPT1002023BPix,
    "DYPT2002022":    DYPT2002022,    
    "DYPT2002022EE":  DYPT2002022EE,  
    "DYPT2002023":    DYPT2002023,    
    "DYPT2002023BPix":DYPT2002023BPix,
    "DYPT4002022":    DYPT4002022,    
    "DYPT4002022EE":  DYPT4002022EE,  
    "DYPT4002023":    DYPT4002023,    
    "DYPT4002023BPix":DYPT4002023BPix,
    "DYPT6002022":    DYPT6002022,    
    "DYPT6002022EE":  DYPT6002022EE,  
    "DYPT6002023":    DYPT6002023,    
    "DYPT6002023BPix":DYPT6002023BPix,
    "QCDHT10002022 ":   QCDHT10002022 ,   
    "QCDHT10002022EE":  QCDHT10002022EE,  
    "QCDHT10002023":    QCDHT10002023,    
    "QCDHT10002023BPix":QCDHT10002023BPix,
    "QCDHT12002022":    QCDHT12002022,    
    "QCDHT12002022EE":  QCDHT12002022EE,  
    "QCDHT12002023":    QCDHT12002023,    
    "QCDHT12002023BPix":QCDHT12002023BPix,
    "QCDHT15002022":    QCDHT15002022,    
    "QCDHT15002022EE":  QCDHT15002022EE,  
    "QCDHT15002023":    QCDHT15002023,    
    "QCDHT15002023BPix":QCDHT15002023BPix,
    "QCDHT20002022":    QCDHT20002022,    
    "QCDHT20002022EE":  QCDHT20002022EE,  
    "QCDHT20002023":    QCDHT20002023,    
    "QCDHT20002023BPix":QCDHT20002023BPix,
    "QCDHT2002022":     QCDHT2002022,     
    "QCDHT2002022EE":   QCDHT2002022EE,   
    "QCDHT2002023":     QCDHT2002023,     
    "QCDHT2002023BPix": QCDHT2002023BPix, 
    "QCDHT4002022":     QCDHT4002022,     
    "QCDHT4002022EE":   QCDHT4002022EE,   
    "QCDHT4002023":     QCDHT4002023,     
    "QCDHT4002023BPix": QCDHT4002023BPix, 
    "QCDHT6002022":     QCDHT6002022,     
    "QCDHT6002022EE":   QCDHT6002022EE,   
    "QCDHT6002023":     QCDHT6002023,     
    "QCDHT6002023BPix": QCDHT6002023BPix, 
    "QCDHT8002022":     QCDHT8002022,     
    "QCDHT8002022EE":   QCDHT8002022EE,   
    "QCDHT8002023":     QCDHT8002023,     
    "QCDHT8002023BPix": QCDHT8002023BPix, 
    "TTHB2022":       TTHB2022,       
    "TTHB2022EE":     TTHB2022EE,     
    "TTHB2023":       TTHB2023,       
    "TTHB2023BPix":   TTHB2023BPix,   
    "TTHnonB2022":    TTHnonB2022,    
    "TTHnonB2022EE":  TTHnonB2022EE,  
    "TTHnonB2023":    TTHnonB2023,    
    "TTHnonB2023BPix":TTHnonB2023BPix,
    "TTTo2L2Nu2022":            TTTo2L2Nu2022,            
    "TTTo2L2Nu2022ext":         TTTo2L2Nu2022ext,         
    "TTTo2L2Nu2022EE":          TTTo2L2Nu2022EE,          
    "TTTo2L2Nu2022EEext":       TTTo2L2Nu2022EEext,       
    "TTTo2L2Nu2023":            TTTo2L2Nu2023,            
    "TTTo2L2Nu2023BPix":        TTTo2L2Nu2023BPix,        
    "TTToHadronic2022":         TTToHadronic2022,         
    "TTToHadronic2022ext":      TTToHadronic2022ext,      
    "TTToHadronic2022EE":       TTToHadronic2022EE,       
    "TTToHadronic2022EEext":    TTToHadronic2022EEext,    
    "TTToHadronic2023":         TTToHadronic2023,         
    "TTToHadronic2023BPix":     TTToHadronic2023BPix,     
    "TTToSemiLeptonic2022":     TTToSemiLeptonic2022,     
    "TTToSemiLeptonic2022ext":  TTToSemiLeptonic2022ext,  
    "TTToSemiLeptonic2022EE":   TTToSemiLeptonic2022EE,   
    "TTToSemiLeptonic2022EEext":TTToSemiLeptonic2022EEext,
    "TTToSemiLeptonic2023":     TTToSemiLeptonic2023,     
    "TTToSemiLeptonic2023BPix": TTToSemiLeptonic2023BPix, 
    "TTWl2022":         TTWl2022,         
    "TTWl2022EE":       TTWl2022EE,       
    "TTWl2023":         TTWl2023,         
    "TTWl2023BPix":     TTWl2023BPix,     
    "TTWq2022":         TTWq2022,         
    "TTWq2022EE":       TTWq2022EE,       
    "TTWq2023":         TTWq2023,         
    "TTWq2023BPix":     TTWq2023BPix,     
    "TTZM102022":       TTZM102022,       
    "TTZM102022EE":     TTZM102022EE,     
    "TTZM102023":       TTZM102023,       
    "TTZM102023BPix":   TTZM102023BPix,   
    "TTZM1to102022":    TTZM1to102022,    
    "TTZM1to102022EE":  TTZM1to102022EE,  
    "TTZM1to102023":    TTZM1to102023,    
    "TTZM1to102023BPix":TTZM1to102023BPix,
    "WW2L2022":     WW2L2022,     
    "WW2L2022ext":  WW2L2022ext,  
    "WW2L2022EE":   WW2L2022EE,   
    "WW2L2022EEext":WW2L2022EEext,
    "WW2L2023":     WW2L2023,     
    "WW2L2023BPix": WW2L2023BPix, 
    "WW1L2022":     WW1L2022,     
    "WW1L2022ext":  WW1L2022ext,  
    "WW1L2022EE":   WW1L2022EE,   
    "WW1L2022EEext":WW1L2022EEext,
    "WW1L2023":     WW1L2023,     
    "WW1L2023BPix": WW1L2023BPix, 
    "WZ2L2022":     WZ2L2022,     
    "WZ2L2022ext":  WZ2L2022ext,  
    "WZ2L2022EE":   WZ2L2022EE,   
    "WZ2L2022EEext":WZ2L2022EEext,
    "WZ2L2023":     WZ2L2023,     
    "WZ2L2023BPix": WZ2L2023BPix, 
    "WZ1L2022":     WZ1L2022,     
    "WZ1L2022ext":  WZ1L2022ext,  
    "WZ1L2022EE":   WZ1L2022EE,   
    "WZ1L2022EEext":WZ1L2022EEext,
    "WZ1L2023":     WZ1L2023,     
    "WZ1L2023BPix": WZ1L2023BPix, 
    "ZZ2022":       ZZ2022,       
    "ZZ2022ext":    ZZ2022ext,    
    "ZZ2022EE":     ZZ2022EE,     
    "ZZ2022EEext":  ZZ2022EEext,  
    "ZZ2023":       ZZ2023,       
    "ZZ2023BPix":   ZZ2023BPix,   

}


