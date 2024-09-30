import os 

# Question: A lot of the samples have _PSweights_.  The samples we were working with before didn't have this.  Is it good or bad?
# Sample Dictionaries: samples, samples_2016APVUL, samples_2016UL, samples_2017UL, samples_2018UL, samples_test, samples_QCD

class sample:
    def __init__(self, prefix, year, textlist, samplename): #, color
        self.prefix = prefix
        self.year = year
        self.textlist = textlist
        self.samplename = samplename
        #self.color = color


Bprime_M1000_2016APVUL = sample("Bprime_M1000_2016APVUL", "2016APV", "Bprime_M1000_2016APVULNanoList.txt", "/BprimeBtoTW_M-1000_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M1000_2016UL = sample("Bprime_M1000_2016UL", "2016", "Bprime_M1000_2016ULNanoList.txt", "/BprimeBtoTW_M-1000_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M1000_2017UL = sample("Bprime_M1000_2017UL", "2017", "Bprime_M1000_2017ULNanoList.txt", "/BprimeBtoTW_M-1000_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
Bprime_M1000_2018UL = sample("Bprime_M1000_2018UL", "2018", "Bprime_M1000_2018ULNanoList.txt", "/BprimeBtoTW_M-1000_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M1200_2016APVUL = sample("Bprime_M1200_2016APVUL", "2016APV", "Bprime_M1200_2016APVULNanoList.txt", "/BprimeBtoTW_M-1200_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M1200_2016UL = sample("Bprime_M1200_2016UL", "2016", "Bprime_M1200_2016ULNanoList.txt", "/BprimeBtoTW_M-1200_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M1200_2017UL = sample("Bprime_M1200_2017UL", "2017", "Bprime_M1200_2017ULNanoList.txt", "/BprimeBtoTW_M-1200_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
Bprime_M1200_2018UL = sample("Bprime_M1200_2018UL", "2018", "Bprime_M1200_2018ULNanoList.txt", "/BprimeBtoTW_M-1200_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M1300_2016APVUL = sample("Bprime_M1300_2016APVUL", "2016APV", "Bprime_M1300_2016APVULNanoList.txt", "/BprimeBtoTW_M-1300_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M1300_2016UL = sample("Bprime_M1300_2016UL", "2016", "Bprime_M1300_2016ULNanoList.txt", "/BprimeBtoTW_M-1300_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M1300_2017UL = sample("Bprime_M1300_2017UL", "2017", "Bprime_M1300_2017ULNanoList.txt", "/BprimeBtoTW_M-1300_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
Bprime_M1300_2018UL = sample("Bprime_M1300_2018UL", "2018", "Bprime_M1300_2018ULNanoList.txt", "/BprimeBtoTW_M-1300_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M1400_2016APVUL = sample("Bprime_M1400_2016APVUL", "2016APV", "Bprime_M1400_2016APVULNanoList.txt", "/BprimeBtoTW_M-1400_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M1400_2016UL = sample("Bprime_M1400_2016UL", "2016", "Bprime_M1400_2016ULNanoList.txt", "/BprimeBtoTW_M-1400_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M1400_2017UL = sample("Bprime_M1400_2017UL", "2017", "Bprime_M1400_2017ULNanoList.txt", "/BprimeBtoTW_M-1400_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
Bprime_M1400_2018UL = sample("Bprime_M1400_2018UL", "2018", "Bprime_M1400_2018ULNanoList.txt", "/BprimeBtoTW_M-1400_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M1500_2016APVUL = sample("Bprime_M1500_2016APVUL", "2016APV", "Bprime_M1500_2016APVULNanoList.txt", "/BprimeBtoTW_M-1500_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M1500_2016UL = sample("Bprime_M1500_2016UL", "2016", "Bprime_M1500_2016ULNanoList.txt", "/BprimeBtoTW_M-1500_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M1500_2017UL = sample("Bprime_M1500_2017UL", "2017", "Bprime_M1500_2017ULNanoList.txt", "/BprimeBtoTW_M-1500_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
Bprime_M1500_2018UL = sample("Bprime_M1500_2018UL", "2018", "Bprime_M1500_2018ULNanoList.txt", "/BprimeBtoTW_M-1500_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M1600_2016APVUL = sample("Bprime_M1600_2016APVUL", "2016APV", "Bprime_M1600_2016APVULNanoList.txt", "/BprimeBtoTW_M-1600_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M1600_2016UL = sample("Bprime_M1600_2016UL", "2016", "Bprime_M1600_2016ULNanoList.txt", "/BprimeBtoTW_M-1600_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M1600_2017UL = sample("Bprime_M1600_2017UL", "2017", "Bprime_M1600_2017ULNanoList.txt", "/BprimeBtoTW_M-1600_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
Bprime_M1600_2018UL = sample("Bprime_M1600_2018UL", "2018", "Bprime_M1600_2018ULNanoList.txt", "/BprimeBtoTW_M-1600_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M1700_2016APVUL = sample("Bprime_M1700_2016APVUL", "2016APV", "Bprime_M1700_2016APVULNanoList.txt", "/BprimeBtoTW_M-1700_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M1700_2016UL = sample("Bprime_M1700_2016UL", "2016", "Bprime_M1700_2016ULNanoList.txt", "/BprimeBtoTW_M-1700_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M1700_2017UL = sample("Bprime_M1700_2017UL", "2017", "Bprime_M1700_2017ULNanoList.txt", "/BprimeBtoTW_M-1700_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
Bprime_M1700_2018UL = sample("Bprime_M1700_2018UL", "2018", "Bprime_M1700_2018ULNanoList.txt", "/BprimeBtoTW_M-1700_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M1800_2016APVUL = sample("Bprime_M1800_2016APVUL", "2016APV", "Bprime_M1800_2016APVULNanoList.txt", "/BprimeBtoTW_M-1800_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M1800_2016UL = sample("Bprime_M1800_2016UL", "2016", "Bprime_M1800_2016ULNanoList.txt", "/BprimeBtoTW_M-1800_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M1800_2017UL = sample("Bprime_M1800_2017UL", "2017", "Bprime_M1800_2017ULNanoList.txt", "/BprimeBtoTW_M-1800_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
Bprime_M1800_2018UL = sample("Bprime_M1800_2018UL", "2018", "Bprime_M1800_2018ULNanoList.txt", "/BprimeBtoTW_M-1800_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M2000_2016APVUL = sample("Bprime_M2000_2016APVUL", "2016APV", "Bprime_M2000_2016APVULNanoList.txt", "/BprimeBtoTW_M-2000_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M2000_2016UL = sample("Bprime_M2000_2016UL", "2016", "Bprime_M2000_2016ULNanoList.txt", "/BprimeBtoTW_M-2000_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M2000_2017UL = sample("Bprime_M2000_2017UL", "2017", "Bprime_M2000_2017ULNanoList.txt", "/BprimeBtoTW_M-2000_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
Bprime_M2000_2018UL = sample("Bprime_M2000_2018UL", "2018", "Bprime_M2000_2018ULNanoList.txt", "/BprimeBtoTW_M-2000_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M2200_2016APVUL = sample("Bprime_M2200_2016APVUL", "2016APV", "Bprime_M2200_2016APVULNanoList.txt", "/BprimeBtoTW_M-2200_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M2200_2016UL = sample("Bprime_M2200_2016UL", "2016", "Bprime_M2200_2016ULNanoList.txt", "/BprimeBtoTW_M-2200_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M2200_2017UL = sample("Bprime_M2200_2017UL", "2017", "Bprime_M2200_2017ULNanoList.txt", "/BprimeBtoTW_M-2200_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
Bprime_M2200_2018UL = sample("Bprime_M2200_2018UL", "2018", "Bprime_M2200_2018ULNanoList.txt", "/BprimeBtoTW_M-2200_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
Bprime_M800_2016APVUL = sample("Bprime_M800_2016APVUL", "2016APV", "Bprime_M800_2016APVULNanoList.txt", "/BprimeBtoTW_M-800_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
Bprime_M800_2016UL  = sample("Bprime_M800_2016UL", "2016", "Bprime_M800_2016ULNanoList.txt", "/BprimeBtoTW_M-800_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
Bprime_M800_2017UL  = sample("Bprime_M800_2017UL", "2017", "Bprime_M800_2017ULNanoList.txt", "/BprimeBtoTW_M-800_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
Bprime_M800_2018UL  = sample("Bprime_M800_2018UL", "2018", "Bprime_M800_2018ULNanoList.txt", "/BprimeBtoTW_M-800_NWALO_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
DYMHT12002016APVUL = sample("DYMHT12002016APVUL", "2016APV", "DYMHT12002016APVULNanoList.txt", "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
DYMHT12002016UL = sample("DYMHT12002016UL", "2016", "DYMHT12002016ULNanoList.txt", "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
DYMHT12002017UL = sample("DYMHT12002017UL", "2017", "DYMHT12002017ULNanoList.txt", "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
DYMHT12002018UL = sample("DYMHT12002018UL", "2018", "DYMHT12002018ULNanoList.txt", "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
DYMHT2002016APVUL = sample("DYMHT2002016APVUL", "2016APV", "DYMHT2002016APVULNanoList.txt", "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
DYMHT2002016UL = sample("DYMHT2002016UL", "2016", "DYMHT2002016ULNanoList.txt", "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
DYMHT2002017UL = sample("DYMHT2002017UL", "2017", "DYMHT2002017ULNanoList.txt", "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
DYMHT2002018UL = sample("DYMHT2002018UL", "2018", "DYMHT2002018ULNanoList.txt", "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
DYMHT25002016APVUL = sample("DYMHT25002016APVUL", "2016APV", "DYMHT25002016APVULNanoList.txt", "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
DYMHT25002016UL = sample("DYMHT25002016UL", "2016", "DYMHT25002016ULNanoList.txt", "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
DYMHT25002017UL = sample("DYMHT25002017UL", "2017", "DYMHT25002017ULNanoList.txt", "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
DYMHT25002018UL = sample("DYMHT25002018UL", "2018", "DYMHT25002018ULNanoList.txt", "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
DYMHT4002016APVUL = sample("DYMHT4002016APVUL", "2016APV", "DYMHT4002016APVULNanoList.txt", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
DYMHT4002016UL = sample("DYMHT4002016UL", "2016", "DYMHT4002016ULNanoList.txt", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
DYMHT4002017UL = sample("DYMHT4002017UL", "2017", "DYMHT4002017ULNanoList.txt", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
DYMHT4002018UL = sample("DYMHT4002018UL", "2018", "DYMHT4002018ULNanoList.txt", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
DYMHT6002016APVUL = sample("DYMHT6002016APVUL", "2016APV", "DYMHT6002016APVULNanoList.txt", "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
DYMHT6002016UL = sample("DYMHT6002016UL", "2016", "DYMHT6002016ULNanoList.txt", "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
DYMHT6002017UL = sample("DYMHT6002017UL", "2017", "DYMHT6002017ULNanoList.txt", "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
DYMHT6002018UL = sample("DYMHT6002018UL", "2018", "DYMHT6002018ULNanoList.txt", "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
DYMHT8002016APVUL = sample("DYMHT8002016APVUL", "2016APV", "DYMHT8002016APVULNanoList.txt", "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
DYMHT8002016UL = sample("DYMHT8002016UL", "2016", "DYMHT8002016ULNanoList.txt", "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
DYMHT8002017UL = sample("DYMHT8002017UL", "2017", "DYMHT8002017ULNanoList.txt", "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
DYMHT8002018UL = sample("DYMHT8002018UL", "2018", "DYMHT8002018ULNanoList.txt", "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
JetHTRun2016APVB    = sample("JetHTRun2016APVB", "2016APV", "JetHTRun2016APVBNanoList.txt", "/JetHT/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
JetHTRun2016APVC    = sample("JetHTRun2016APVC", "2016APV", "JetHTRun2016APVCNanoList.txt", "/JetHT/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
JetHTRun2016APVD    = sample("JetHTRun2016APVD", "2016APV", "JetHTRun2016APVDNanoList.txt", "/JetHT/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
JetHTRun2016APVE    = sample("JetHTRun2016APVE", "2016APV", "JetHTRun2016APVENanoList.txt", "/JetHT/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
JetHTRun2016APVF    = sample("JetHTRun2016APVF", "2016APV", "JetHTRun2016APVFNanoList.txt", "/JetHT/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
JetHTRun2016F       = sample("JetHTRun2016F", "2016", "JetHTRun2016FNanoList.txt", "/JetHT/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2016G       = sample("JetHTRun2016G", "2016", "JetHTRun2016GNanoList.txt", "/JetHT/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2016H       = sample("JetHTRun2016H", "2016", "JetHTRun2016HNanoList.txt", "/JetHT/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2017B       = sample("JetHTRun2017B", "2017", "JetHTRun2017BNanoList.txt", "/JetHT/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2017C       = sample("JetHTRun2017C", "2017", "JetHTRun2017CNanoList.txt", "/JetHT/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2017D       = sample("JetHTRun2017D", "2017", "JetHTRun2017DNanoList.txt", "/JetHT/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2017E       = sample("JetHTRun2017E", "2017", "JetHTRun2017ENanoList.txt", "/JetHT/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2017F       = sample("JetHTRun2017F", "2017", "JetHTRun2017FNanoList.txt", "/JetHT/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2018A       = sample("JetHTRun2018A", "2018", "JetHTRun2018ANanoList.txt", "/JetHT/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD")
JetHTRun2018B       = sample("JetHTRun2018B", "2018", "JetHTRun2018BNanoList.txt", "/JetHT/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2018C       = sample("JetHTRun2018C", "2018", "JetHTRun2018CNanoList.txt", "/JetHT/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD")
JetHTRun2018D       = sample("JetHTRun2018D", "2018", "JetHTRun2018DNanoList.txt", "/JetHT/Run2018D-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD")
QCDHT10002016APVUL  = sample("QCDHT10002016APVUL", "2016APV", "QCDHT10002016APVULNanoList.txt", "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
QCDHT10002016UL     = sample("QCDHT10002016UL", "2016", "QCDHT10002016ULNanoList.txt", "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
QCDHT10002017UL     = sample("QCDHT10002017UL", "2017", "QCDHT10002017ULNanoList.txt", "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
QCDHT10002018UL     = sample("QCDHT10002018UL", "2018", "QCDHT10002018ULNanoList.txt", "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
QCDHT15002016APVUL  = sample("QCDHT15002016APVUL", "2016APV", "QCDHT15002016APVULNanoList.txt", "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
QCDHT15002016UL     = sample("QCDHT15002016UL", "2016", "QCDHT15002016ULNanoList.txt", "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
QCDHT15002017UL     = sample("QCDHT15002017UL", "2017", "QCDHT15002017ULNanoList.txt", "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
QCDHT15002018UL     = sample("QCDHT15002018UL", "2018", "QCDHT15002018ULNanoList.txt", "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
QCDHT20002016APVUL  = sample("QCDHT20002016APVUL", "2016APV", "QCDHT20002016APVULNanoList.txt", "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
QCDHT20002016UL     = sample("QCDHT20002016UL", "2016", "QCDHT20002016ULNanoList.txt", "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
QCDHT20002017UL     = sample("QCDHT20002017UL", "2017", "QCDHT20002017ULNanoList.txt", "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
QCDHT20002018UL     = sample("QCDHT20002018UL", "2018", "QCDHT20002018ULNanoList.txt", "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
QCDHT2002016APVUL   = sample("QCDHT2002016APVUL", "2016APV", "QCDHT2002016APVULNanoList.txt", "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
QCDHT2002016UL      = sample("QCDHT2002016UL", "2016", "QCDHT2002016ULNanoList.txt", "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
QCDHT2002017UL      = sample("QCDHT2002017UL", "2017", "QCDHT2002017ULNanoList.txt", "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
QCDHT2002018UL      = sample("QCDHT2002018UL", "2018", "QCDHT2002018ULNanoList.txt", "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
QCDHT3002016APVUL   = sample("QCDHT3002016APVUL", "2016APV", "QCDHT3002016APVULNanoList.txt", "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
QCDHT3002016UL      = sample("QCDHT3002016UL", "2016", "QCDHT3002016ULNanoList.txt", "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
QCDHT3002017UL      = sample("QCDHT3002017UL", "2017", "QCDHT3002017ULNanoList.txt", "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
QCDHT3002018UL      = sample("QCDHT3002018UL", "2018", "QCDHT3002018ULNanoList.txt", "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
QCDHT5002016APVUL   = sample("QCDHT5002016APVUL", "2016APV", "QCDHT5002016APVULNanoList.txt", "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
QCDHT5002016UL      = sample("QCDHT5002016UL", "2016", "QCDHT5002016ULNanoList.txt", "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
QCDHT5002017UL      = sample("QCDHT5002017UL", "2017", "QCDHT5002017ULNanoList.txt", "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
QCDHT5002018UL      = sample("QCDHT5002018UL", "2018", "QCDHT5002018ULNanoList.txt", "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
QCDHT7002016APVUL   = sample("QCDHT7002016APVUL", "2016APV", "QCDHT7002016APVULNanoList.txt", "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
QCDHT7002016UL      = sample("QCDHT7002016UL", "2016", "QCDHT7002016ULNanoList.txt", "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
QCDHT7002017UL      = sample("QCDHT7002017UL", "2017", "QCDHT7002017ULNanoList.txt", "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
QCDHT7002018UL      = sample("QCDHT7002018UL", "2018", "QCDHT7002018ULNanoList.txt", "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
SingleElecRun2016APVA = sample("SingleElecRun2016APVA", "2016APV", "SingleElecRun2016APVA2016APVULNanoList.txt", "/SingleElectron/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleElecRun2016APVB = sample("SingleElecRun2016APVB", "2016APV", "SingleElecRun2016APVB2016APVULNanoList.txt", "/SingleElectron/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleElecRun2016APVC = sample("SingleElecRun2016APVC", "2016APV", "SingleElecRun2016APVC2016APVULNanoList.txt", "/SingleElectron/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleElecRun2016APVD = sample("SingleElecRun2016APVD", "2016APV", "SingleElecRun2016APVD2016APVULNanoList.txt", "/SingleElectron/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleElecRun2016APVE = sample("SingleElecRun2016APVE", "2016APV", "SingleElecRun2016APVE2016APVULNanoList.txt", "/SingleElectron/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleElecRun2016APVF = sample("SingleElecRun2016APVF", "2016APV", "SingleElecRun2016APVF2016APVULNanoList.txt", "/SingleElectron/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleElecRun2016F  = sample("SingleElecRun2016F", "2016", "SingleElecRun2016F2016ULNanoList.txt", "/SingleElectron/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2016G  = sample("SingleElecRun2016G", "2016", "SingleElecRun2016G2016ULNanoList.txt", "/SingleElectron/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2016H  = sample("SingleElecRun2016H", "2016", "SingleElecRun2016H2016ULNanoList.txt", "/SingleElectron/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2017B  = sample("SingleElecRun2017B", "2017", "SingleElecRun2017B2017ULNanoList.txt", "/SingleElectron/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2017C  = sample("SingleElecRun2017C", "2017", "SingleElecRun2017C2017ULNanoList.txt", "/SingleElectron/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2017D  = sample("SingleElecRun2017D", "2017", "SingleElecRun2017D2017ULNanoList.txt", "/SingleElectron/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2017E  = sample("SingleElecRun2017E", "2017", "SingleElecRun2017E2017ULNanoList.txt", "/SingleElectron/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2017F  = sample("SingleElecRun2017F", "2017", "SingleElecRun2017F2017ULNanoList.txt", "/SingleElectron/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2018A  = sample("SingleElecRun2018A", "2018", "SingleElecRun2018A2018ULNanoList.txt", "/EGamma/Run2018A-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2018B  = sample("SingleElecRun2018B", "2018", "SingleElecRun2018B2018ULNanoList.txt", "/EGamma/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2018C  = sample("SingleElecRun2018C", "2018", "SingleElecRun2018C2018ULNanoList.txt", "/EGamma/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleElecRun2018D  = sample("SingleElecRun2018D", "2018", "SingleElecRun2018D2018ULNanoList.txt", "/EGamma/Run2018D-UL2018_MiniAODv2_NanoAODv9-v3/NANOAOD")
SingleMuonRun2016APVA = sample("SingleMuonRun2016APVA", "2016APV", "SingleMuonRun2016APVA2016APVULNanoList.txt", "/SingleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleMuonRun2016APVB = sample("SingleMuonRun2016APVB", "2016APV", "SingleMuonRun2016APVB2016APVULNanoList.txt", "/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleMuonRun2016APVC = sample("SingleMuonRun2016APVC", "2016APV", "SingleMuonRun2016APVC2016APVULNanoList.txt", "/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleMuonRun2016APVD = sample("SingleMuonRun2016APVD", "2016APV", "SingleMuonRun2016APVD2016APVULNanoList.txt", "/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleMuonRun2016APVE = sample("SingleMuonRun2016APVE", "2016APV", "SingleMuonRun2016APVE2016APVULNanoList.txt", "/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleMuonRun2016APVF = sample("SingleMuonRun2016APVF", "2016APV", "SingleMuonRun2016APVF2016APVULNanoList.txt", "/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD")
SingleMuonRun2016F  = sample("SingleMuonRun2016F", "2016", "SingleMuonRun2016F2016ULNanoList.txt", "/SingleMuon/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleMuonRun2016G  = sample("SingleMuonRun2016G", "2016", "SingleMuonRun2016G2016ULNanoList.txt", "/SingleMuon/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleMuonRun2016H  = sample("SingleMuonRun2016H", "2016", "SingleMuonRun2016H2016ULNanoList.txt", "/SingleMuon/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD")
SingleMuonRun2017B  = sample("SingleMuonRun2017B", "2017", "SingleMuonRun2017B2017ULNanoList.txt", "/SingleMuon/Run2017B-UL2017_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD")
SingleMuonRun2017C  = sample("SingleMuonRun2017C", "2017", "SingleMuonRun2017C2017ULNanoList.txt", "/SingleMuon/Run2017C-UL2017_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD")
SingleMuonRun2017D  = sample("SingleMuonRun2017D", "2017", "SingleMuonRun2017D2017ULNanoList.txt", "/SingleMuon/Run2017D-UL2017_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD")
SingleMuonRun2017E  = sample("SingleMuonRun2017E", "2017", "SingleMuonRun2017E2017ULNanoList.txt", "/SingleMuon/Run2017E-UL2017_MiniAODv2_NanoAODv9_GT36-v2/NANOAOD")
SingleMuonRun2017F  = sample("SingleMuonRun2017F", "2017", "SingleMuonRun2017F2017ULNanoList.txt", "/SingleMuon/Run2017F-UL2017_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD")
SingleMuonRun2018A  = sample("SingleMuonRun2018A", "2018", "SingleMuonRun2018A2018ULNanoList.txt", "/SingleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD")
SingleMuonRun2018B  = sample("SingleMuonRun2018B", "2018", "SingleMuonRun2018B2018ULNanoList.txt", "/SingleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD")
SingleMuonRun2018C  = sample("SingleMuonRun2018C", "2018", "SingleMuonRun2018C2018ULNanoList.txt", "/SingleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD")
SingleMuonRun2018D  = sample("SingleMuonRun2018D", "2018", "SingleMuonRun2018D2018ULNanoList.txt", "/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD")
STs2016APVUL = sample("STs2016APVUL", "2016APV", "STs2016APVULNanoList.txt", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
STs2016UL = sample("STs2016UL", "2016", "STs2016ULNanoList.txt", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
STs2017UL = sample("STs2017UL", "2017", "STs2017ULNanoList.txt", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
STs2018UL = sample("STs2018UL", "2018", "STs2018ULNanoList.txt", "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
STt2016APVUL = sample("STt2016APVUL", "2016APV", "STt2016APVULNanoList.txt", "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
STt2016UL = sample("STt2016UL", "2016", "STt2016ULNanoList.txt", "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
STt2017UL = sample("STt2017UL", "2017", "STt2017ULNanoList.txt", "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
STt2018UL = sample("STt2018UL", "2018", "STt2018ULNanoList.txt", "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
STtb2016APVUL = sample("STtb2016APVUL", "2016APV", "STtb2016APVULNanoList.txt", "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
STtb2016UL = sample("STtb2016UL", "2016", "STtb2016ULNanoList.txt", "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
STtb2017UL = sample("STtb2017UL", "2017", "STtb2017ULNanoList.txt", "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
STtb2018UL = sample("STtb2018UL", "2018", "STtb2018ULNanoList.txt", "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
STtW2016APVUL = sample("STtW2016APVUL", "2016APV", "STtW2016APVULNanoList.txt", "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
STtW2016UL = sample("STtW2016UL", "2016", "STtW2016ULNanoList.txt", "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
STtW2017UL = sample("STtW2017UL", "2017", "STtW2017ULNanoList.txt", "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
STtW2018UL = sample("STtW2018UL", "2018", "STtW2018ULNanoList.txt", "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
STtWb2016APVUL = sample("STtWb2016APVUL", "2016APV", "STtWb2016APVULNanoList.txt", "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
STtWb2016UL = sample("STtWb2016UL", "2016", "STtWb2016ULNanoList.txt", "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
STtWb2017UL = sample("STtWb2017UL", "2017", "STtWb2017ULNanoList.txt", "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
STtWb2018UL = sample("STtWb2018UL", "2018", "STtWb2018ULNanoList.txt", "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
TTHB2016APVUL = sample("TTHB2016APVUL", "2016APV", "TTHB2016APVULNanoList.txt", "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
TTHB2016UL = sample("TTHB2016UL", "2016", "TTHB2016ULNanoList.txt", "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
TTHB2017UL = sample("TTHB2017UL", "2017", "TTHB2017ULNanoList.txt", "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
TTHB2018UL = sample("TTHB2018UL", "2018", "TTHB2018ULNanoList.txt", "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
TTHnonB2016APVUL = sample("TTHnonB2016APVUL", "2016APV", "TTHnonB2016APVULNanoList.txt", "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
TTHnonB2016UL = sample("TTHnonB2016UL", "2016", "TTHnonB2016ULNanoList.txt", "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
TTHnonB2017UL = sample("TTHnonB2017UL", "2017", "TTHnonB2017ULNanoList.txt", "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
TTHnonB2018UL = sample("TTHnonB2018UL", "2018", "TTHnonB2018ULNanoList.txt", "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
TTMT10002016APVUL = sample("TTMT10002016APVUL", "2016APV", "TTMT10002016APVULNanoList.txt", "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
TTMT10002016UL = sample("TTMT10002016UL", "2016", "TTMT10002016ULNanoList.txt", "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTMT10002017UL = sample("TTMT10002017UL", "2017", "TTMT10002017ULNanoList.txt", "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
TTMT10002018UL = sample("TTMT10002018UL", "2018", "TTMT10002018ULNanoList.txt", "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
TTMT7002016APVUL = sample("TTMT7002016APVUL", "2016APV", "TTMT7002016APVULNanoList.txt", "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
TTMT7002016UL = sample("TTMT7002016UL", "2016", "TTMT7002016ULNanoList.txt", "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTMT7002017UL = sample("TTMT7002017UL", "2017", "TTMT7002017ULNanoList.txt", "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
TTMT7002018UL = sample("TTMT7002018UL", "2018", "TTMT7002018ULNanoList.txt", "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
TTTo2L2Nu2016APVUL = sample("TTTo2L2Nu2016APVUL", "2016APV", "TTTo2L2Nu2016APVULNanoList.txt", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
TTTo2L2Nu2016UL = sample("TTTo2L2Nu2016UL", "2016", "TTTo2L2Nu2016ULNanoList.txt", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTTo2L2Nu2017UL = sample("TTTo2L2Nu2017UL", "2017", "TTTo2L2Nu2017ULNanoList.txt", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
TTTo2L2Nu2018UL = sample("TTTo2L2Nu2018UL", "2018", "TTTo2L2Nu2018ULNanoList.txt", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
TTToHadronic2016APVUL = sample("TTToHadronic2016APVUL", "2016APV", "TTToHadronic2016APVULNanoList.txt", "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
TTToHadronic2016UL = sample("TTToHadronic2016UL", "2016", "TTToHadronic2016ULNanoList.txt", "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTToHadronic2017UL = sample("TTToHadronic2017UL", "2017", "TTToHadronic2017ULNanoList.txt", "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
TTToHadronic2018UL = sample("TTToHadronic2018UL", "2018", "TTToHadronic2018ULNanoList.txt", "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
TTToSemiLeptonic2016APVUL = sample("TTToSemiLeptonic2016APVUL", "2016APV", "TTToSemiLeptonic2016APVULNanoList.txt", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
TTToSemiLeptonic2016UL = sample("TTToSemiLeptonic2016UL", "2016", "TTToSemiLeptonic2016ULNanoList.txt", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTToSemiLeptonic2017UL = sample("TTToSemiLeptonic2017UL", "2017", "TTToSemiLeptonic2017ULNanoList.txt", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
TTToSemiLeptonic2018UL = sample("TTToSemiLeptonic2018UL", "2018", "TTToSemiLeptonic2018ULNanoList.txt", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
TTWl2016APVUL = sample("TTWl2016APVUL", "2016APV", "TTWl2016APVULNanoList.txt", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
TTWl2016UL = sample("TTWl2016UL", "2016", "TTWl2016ULNanoList.txt", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTWl2017UL = sample("TTWl2017UL", "2017", "TTWl2017ULNanoList.txt", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
TTWl2018UL = sample("TTWl2018UL", "2018", "TTWl2018ULNanoList.txt", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
TTWq2016APVUL = sample("TTWq2016APVUL", "2016APV", "TTWq2016APVULNanoList.txt", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
TTWq2016UL = sample("TTWq2016UL", "2016", "TTWq2016ULNanoList.txt", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTWq2017UL = sample("TTWq2017UL", "2017", "TTWq2017ULNanoList.txt", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
TTWq2018UL = sample("TTWq2018UL", "2018", "TTWq2018ULNanoList.txt", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
TTZM102016APVUL = sample("TTZM102016APVUL", "2016APV", "TTZM102016APVULNanoList.txt", "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
TTZM102016UL = sample("TTZM102016UL", "2016", "TTZM102016ULNanoList.txt", "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTZM102017UL = sample("TTZM102017UL", "2017", "TTZM102017ULNanoList.txt", "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
TTZM102018UL = sample("TTZM102018UL", "2018", "TTZM102018ULNanoList.txt", "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
TTZM1to102016APVUL = sample("TTZM1to102016APVUL", "2016APV", "TTZM1to102016APVULNanoList.txt", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTZM1to102016UL = sample("TTZM1to102016UL", "2016", "TTZM1to102016ULNanoList.txt", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTZM1to102017UL = sample("TTZM1to102017UL", "2017", "TTZM1to102017ULNanoList.txt", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
TTZM1to102018UL = sample("TTZM1to102018UL", "2018", "TTZM1to102018ULNanoList.txt", "/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
WJetsHT12002016APVUL = sample("WJetsHT12002016APVUL", "2016APV", "WJetsHT12002016APVULNanoList.txt", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
WJetsHT12002016UL = sample("WJetsHT12002016UL", "2016", "WJetsHT12002016ULNanoList.txt", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
WJetsHT12002017UL = sample("WJetsHT12002017UL", "2017", "WJetsHT12002017ULNanoList.txt", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
WJetsHT12002018UL = sample("WJetsHT12002018UL", "2018", "WJetsHT12002018ULNanoList.txt", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
WJetsHT1200ext2018UL = sample("WJetsHT1200ext2018UL", "2018", "WJetsHT1200ext2018ULNanoList.txt", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM")
WJetsHT2002016APVUL = sample("WJetsHT2002016APVUL", "2016APV", "WJetsHT2002016APVULNanoList.txt", "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
WJetsHT2002016UL = sample("WJetsHT2002016UL", "2016", "WJetsHT2002016ULNanoList.txt", "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
WJetsHT2002017UL = sample("WJetsHT2002017UL", "2017", "WJetsHT2002017ULNanoList.txt", "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
WJetsHT2002018UL = sample("WJetsHT2002018UL", "2018", "WJetsHT2002018ULNanoList.txt", "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
WJetsHT25002016APVUL = sample("WJetsHT25002016APVUL", "2016APV", "WJetsHT25002016APVULNanoList.txt", "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM")
WJetsHT25002016UL = sample("WJetsHT25002016UL", "2016", "WJetsHT25002016ULNanoList.txt", "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM")
WJetsHT25002017UL = sample("WJetsHT25002017UL", "2017", "WJetsHT25002017ULNanoList.txt", "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM")
WJetsHT25002018UL = sample("WJetsHT25002018UL", "2018", "WJetsHT25002018ULNanoList.txt", "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM")
WJetsHT4002016APVUL = sample("WJetsHT4002016APVUL", "2016APV", "WJetsHT4002016APVULNanoList.txt", "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
WJetsHT4002016UL = sample("WJetsHT4002016UL", "2016", "WJetsHT4002016ULNanoList.txt", "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
WJetsHT4002017UL = sample("WJetsHT4002017UL", "2017", "WJetsHT4002017ULNanoList.txt", "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
WJetsHT4002018UL = sample("WJetsHT4002018UL", "2018", "WJetsHT4002018ULNanoList.txt", "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
WJetsHT400ext2018UL = sample("WJetsHT400ext2018UL", "2018", "WJetsHT400ext2018ULNanoList.txt", "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM")
WJetsHT6002016APVUL = sample("WJetsHT6002016APVUL", "2016APV", "WJetsHT6002016APVULNanoList.txt", "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
WJetsHT6002016UL = sample("WJetsHT6002016UL", "2016", "WJetsHT6002016ULNanoList.txt", "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
WJetsHT6002017UL = sample("WJetsHT6002017UL", "2017", "WJetsHT6002017ULNanoList.txt", "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
WJetsHT6002018UL = sample("WJetsHT6002018UL", "2018", "WJetsHT6002018ULNanoList.txt", "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
WJetsHT600ext2018UL = sample("WJetsHT600ext2018UL", "2018", "WJetsHT600ext2018ULNanoList.txt", "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM")
WJetsHT8002016APVUL = sample("WJetsHT8002016APVUL", "2016APV", "WJetsHT8002016APVULNanoList.txt", "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
WJetsHT8002016UL = sample("WJetsHT8002016UL", "2016", "WJetsHT8002016ULNanoList.txt", "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
WJetsHT8002017UL = sample("WJetsHT8002017UL", "2017", "WJetsHT8002017ULNanoList.txt", "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v3/NANOAODSIM")
WJetsHT8002018UL = sample("WJetsHT8002018UL", "2018", "WJetsHT8002018ULNanoList.txt", "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
WJetsHT800ext2018UL = sample("WJetsHT800ext2018UL", "2018", "WJetsHT800ext2018ULNanoList.txt", "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM")
WW2016APVUL = sample("WW2016APVUL", "2016APV", "WW2016APVULNanoList.txt", "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
WW2016UL = sample("WW2016UL", "2016", "WW2016ULNanoList.txt", "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
WW2017UL = sample("WW2017UL", "2017", "WW2017ULNanoList.txt", "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
WW2018UL = sample("WW2018UL", "2018", "WW2018ULNanoList.txt", "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
WZ2016APVUL = sample("WZ2016APVUL", "2016APV", "WZ2016APVULNanoList.txt", "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
WZ2016UL = sample("WZ2016UL", "2016", "WZ2016ULNanoList.txt", "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
WZ2017UL = sample("WZ2017UL", "2017", "WZ2017ULNanoList.txt", "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
WZ2018UL = sample("WZ2018UL", "2018", "WZ2018ULNanoList.txt", "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")
ZZ2016APVUL = sample("ZZ2016APVUL", "2016APV", "ZZ2016APVULNanoList.txt", "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
ZZ2016UL = sample("ZZ2016UL", "2016", "ZZ2016ULNanoList.txt", "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
ZZ2017UL = sample("ZZ2017UL", "2017", "ZZ2017ULNanoList.txt", "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
ZZ2018UL = sample("ZZ2018UL", "2018", "ZZ2018ULNanoList.txt", "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM")

samples_data = {
    "SingleElecRun2016APVB":SingleElecRun2016APVB,
    "SingleElecRun2016APVC":SingleElecRun2016APVC,
    "SingleElecRun2016APVD":SingleElecRun2016APVD,
    "SingleElecRun2016APVE":SingleElecRun2016APVE,
    "SingleElecRun2016APVF":SingleElecRun2016APVF,
    "SingleElecRun2016F":SingleElecRun2016F,
    "SingleElecRun2016G":SingleElecRun2016G,
    "SingleElecRun2016H":SingleElecRun2016H,
    "SingleElecRun2017B":SingleElecRun2017B,
    "SingleElecRun2017C":SingleElecRun2017C,
    "SingleElecRun2017D":SingleElecRun2017D,
    "SingleElecRun2017E":SingleElecRun2017E,
    "SingleElecRun2017F":SingleElecRun2017F,
    "SingleElecRun2018A":SingleElecRun2018A,
    "SingleElecRun2018B":SingleElecRun2018B,
    "SingleElecRun2018C":SingleElecRun2018C,
    "SingleElecRun2018D":SingleElecRun2018D,
    "SingleMuonRun2016APVB":SingleMuonRun2016APVB,
    "SingleMuonRun2016APVC":SingleMuonRun2016APVC,
    "SingleMuonRun2016APVD":SingleMuonRun2016APVD,
    "SingleMuonRun2016APVE":SingleMuonRun2016APVE,
    "SingleMuonRun2016APVF":SingleMuonRun2016APVF,
    "SingleMuonRun2016F":SingleMuonRun2016F,
    "SingleMuonRun2016G":SingleMuonRun2016G,
    "SingleMuonRun2016H":SingleMuonRun2016H,
    "SingleMuonRun2017B":SingleMuonRun2017B,
    "SingleMuonRun2017C":SingleMuonRun2017C,
    "SingleMuonRun2017D":SingleMuonRun2017D,
    "SingleMuonRun2017E":SingleMuonRun2017E,
    "SingleMuonRun2017F":SingleMuonRun2017F,
    "SingleMuonRun2018A":SingleMuonRun2018A,
    "SingleMuonRun2018B":SingleMuonRun2018B,
    "SingleMuonRun2018C":SingleMuonRun2018C,
    "SingleMuonRun2018D":SingleMuonRun2018D,
}

samples={
    "Bprime_M1000_2016APVUL":Bprime_M1000_2016APVUL,
    "Bprime_M1000_2016UL":Bprime_M1000_2016UL,
    "Bprime_M1000_2017UL":Bprime_M1000_2017UL,
    "Bprime_M1000_2018UL":Bprime_M1000_2018UL,
    "Bprime_M1200_2016APVUL":Bprime_M1200_2016APVUL,
    "Bprime_M1200_2016UL":Bprime_M1200_2016UL,
    "Bprime_M1200_2017UL":Bprime_M1200_2017UL,
    "Bprime_M1200_2018UL":Bprime_M1200_2018UL,
    "Bprime_M1300_2016APVUL":Bprime_M1300_2016APVUL,
    "Bprime_M1300_2016UL":Bprime_M1300_2016UL,
    "Bprime_M1300_2017UL":Bprime_M1300_2017UL,
    "Bprime_M1300_2018UL":Bprime_M1300_2018UL,
    "Bprime_M1400_2016APVUL":Bprime_M1400_2016APVUL,
    "Bprime_M1400_2016UL":Bprime_M1400_2016UL,
    "Bprime_M1400_2017UL":Bprime_M1400_2017UL,
    "Bprime_M1400_2018UL":Bprime_M1400_2018UL,
    "Bprime_M1500_2016APVUL":Bprime_M1500_2016APVUL,
    "Bprime_M1500_2016UL":Bprime_M1500_2016UL,
    "Bprime_M1500_2017UL":Bprime_M1500_2017UL,
    "Bprime_M1500_2018UL":Bprime_M1500_2018UL,
    "Bprime_M1600_2016APVUL":Bprime_M1600_2016APVUL,
    "Bprime_M1600_2016UL":Bprime_M1600_2016UL,
    "Bprime_M1600_2017UL":Bprime_M1600_2017UL,
    "Bprime_M1600_2018UL":Bprime_M1600_2018UL,
    "Bprime_M1700_2016APVUL":Bprime_M1700_2016APVUL,
    "Bprime_M1700_2016UL":Bprime_M1700_2016UL,
    "Bprime_M1700_2017UL":Bprime_M1700_2017UL,
    "Bprime_M1700_2018UL":Bprime_M1700_2018UL,
    "Bprime_M1800_2016APVUL":Bprime_M1800_2016APVUL,
    "Bprime_M1800_2016UL":Bprime_M1800_2016UL,
    "Bprime_M1800_2017UL":Bprime_M1800_2017UL,
    "Bprime_M1800_2018UL":Bprime_M1800_2018UL,
    "Bprime_M2000_2016APVUL":Bprime_M2000_2016APVUL,
    "Bprime_M2000_2016UL":Bprime_M2000_2016UL,
    "Bprime_M2000_2017UL":Bprime_M2000_2017UL,
    "Bprime_M2000_2018UL":Bprime_M2000_2018UL,
    "Bprime_M2200_2016APVUL":Bprime_M2200_2016APVUL,
    "Bprime_M2200_2016UL":Bprime_M2200_2016UL,
    "Bprime_M2200_2017UL":Bprime_M2200_2017UL,
    "Bprime_M2200_2018UL":Bprime_M2200_2018UL,
    "Bprime_M800_2016APVUL":Bprime_M800_2016APVUL,
    "Bprime_M800_2016UL":Bprime_M800_2016UL,
    "Bprime_M800_2017UL":Bprime_M800_2017UL,
    "Bprime_M800_2018UL":Bprime_M800_2018UL,
    "DYMHT12002016APVUL":DYMHT12002016APVUL,
    "DYMHT12002016UL":DYMHT12002016UL,
    "DYMHT12002017UL":DYMHT12002017UL,
    "DYMHT12002018UL":DYMHT12002018UL,
    "DYMHT2002016APVUL":DYMHT2002016APVUL,
    "DYMHT2002016UL":DYMHT2002016UL,
    "DYMHT2002017UL":DYMHT2002017UL,
    "DYMHT2002018UL":DYMHT2002018UL,
    "DYMHT25002016APVUL":DYMHT25002016APVUL,
    "DYMHT25002016UL":DYMHT25002016UL,
    "DYMHT25002017UL":DYMHT25002017UL,
    "DYMHT25002018UL":DYMHT25002018UL,
    "DYMHT4002016APVUL":DYMHT4002016APVUL,
    "DYMHT4002016UL":DYMHT4002016UL,
    "DYMHT4002017UL":DYMHT4002017UL,
    "DYMHT4002018UL":DYMHT4002018UL,
    "DYMHT6002016APVUL":DYMHT6002016APVUL,
    "DYMHT6002016UL":DYMHT6002016UL,
    "DYMHT6002017UL":DYMHT6002017UL,
    "DYMHT6002018UL":DYMHT6002018UL,
    "DYMHT8002016APVUL":DYMHT8002016APVUL,
    "DYMHT8002016UL":DYMHT8002016UL,
    "DYMHT8002017UL":DYMHT8002017UL,
    "DYMHT8002018UL":DYMHT8002018UL,
    # "JetHTRun2016APVB":JetHTRun2016APVB,
    # "JetHTRun2016APVC":JetHTRun2016APVC,
    # "JetHTRun2016APVD":JetHTRun2016APVD,
    # "JetHTRun2016APVE":JetHTRun2016APVE,
    # "JetHTRun2016APVF":JetHTRun2016APVF,
    # "JetHTRun2016F":JetHTRun2016F,
    # "JetHTRun2016G":JetHTRun2016G,
    # "JetHTRun2016H":JetHTRun2016H,
    # "JetHTRun2017B":JetHTRun2017B,
    # "JetHTRun2017C":JetHTRun2017C,
    # "JetHTRun2017D":JetHTRun2017D,
    # "JetHTRun2017E":JetHTRun2017E,
    # "JetHTRun2017F":JetHTRun2017F,
    # "JetHTRun2018A":JetHTRun2018A,
    # "JetHTRun2018B":JetHTRun2018B,
    # "JetHTRun2018C":JetHTRun2018C,
    # "JetHTRun2018D":JetHTRun2018D,
    "QCDHT10002016APVUL":QCDHT10002016APVUL,
    "QCDHT10002016UL":QCDHT10002016UL,
    "QCDHT10002017UL":QCDHT10002017UL,
    "QCDHT10002018UL":QCDHT10002018UL,
    "QCDHT15002016APVUL":QCDHT15002016APVUL,
    "QCDHT15002016UL":QCDHT15002016UL,
    "QCDHT15002017UL":QCDHT15002017UL,
    "QCDHT15002018UL":QCDHT15002018UL,
    "QCDHT20002016APVUL":QCDHT20002016APVUL,
    "QCDHT20002016UL":QCDHT20002016UL,
    "QCDHT20002017UL":QCDHT20002017UL,
    "QCDHT20002018UL":QCDHT20002018UL,
    "QCDHT2002016APVUL":QCDHT2002016APVUL,
    "QCDHT2002016UL":QCDHT2002016UL,
    "QCDHT2002017UL":QCDHT2002017UL,
    "QCDHT2002018UL":QCDHT2002018UL,
    "QCDHT3002016APVUL":QCDHT3002016APVUL,
    "QCDHT3002016UL":QCDHT3002016UL,
    "QCDHT3002017UL":QCDHT3002017UL,
    "QCDHT3002018UL":QCDHT3002018UL,
    "QCDHT5002016APVUL":QCDHT5002016APVUL,
    "QCDHT5002016UL":QCDHT5002016UL,
    "QCDHT5002017UL":QCDHT5002017UL,
    "QCDHT5002018UL":QCDHT5002018UL,
    "QCDHT7002016APVUL":QCDHT7002016APVUL,
    "QCDHT7002016UL":QCDHT7002016UL,
    "QCDHT7002017UL":QCDHT7002017UL,
    "QCDHT7002018UL":QCDHT7002018UL,
    "SingleElecRun2016APVB":SingleElecRun2016APVB,
    "SingleElecRun2016APVC":SingleElecRun2016APVC,
    "SingleElecRun2016APVD":SingleElecRun2016APVD,
    "SingleElecRun2016APVE":SingleElecRun2016APVE,
    "SingleElecRun2016APVF":SingleElecRun2016APVF,
    "SingleElecRun2016F":SingleElecRun2016F,
    "SingleElecRun2016G":SingleElecRun2016G,
    "SingleElecRun2016H":SingleElecRun2016H,
    "SingleElecRun2017B":SingleElecRun2017B,
    "SingleElecRun2017C":SingleElecRun2017C,
    "SingleElecRun2017D":SingleElecRun2017D,
    "SingleElecRun2017E":SingleElecRun2017E,
    "SingleElecRun2017F":SingleElecRun2017F,
    "SingleElecRun2018A":SingleElecRun2018A,
    "SingleElecRun2018B":SingleElecRun2018B,
    "SingleElecRun2018C":SingleElecRun2018C,
    "SingleElecRun2018D":SingleElecRun2018D,
    "SingleMuonRun2016APVB":SingleMuonRun2016APVB,
    "SingleMuonRun2016APVC":SingleMuonRun2016APVC,
    "SingleMuonRun2016APVD":SingleMuonRun2016APVD,
    "SingleMuonRun2016APVE":SingleMuonRun2016APVE,
    "SingleMuonRun2016APVF":SingleMuonRun2016APVF,
    "SingleMuonRun2016F":SingleMuonRun2016F,
    "SingleMuonRun2016G":SingleMuonRun2016G,
    "SingleMuonRun2016H":SingleMuonRun2016H,
    "SingleMuonRun2017B":SingleMuonRun2017B,
    "SingleMuonRun2017C":SingleMuonRun2017C,
    "SingleMuonRun2017D":SingleMuonRun2017D,
    "SingleMuonRun2017E":SingleMuonRun2017E,
    "SingleMuonRun2017F":SingleMuonRun2017F,
    "SingleMuonRun2018A":SingleMuonRun2018A,
    "SingleMuonRun2018B":SingleMuonRun2018B,
    "SingleMuonRun2018C":SingleMuonRun2018C,
    "SingleMuonRun2018D":SingleMuonRun2018D,
    "STs2016APVUL":STs2016APVUL,
    "STs2016UL":STs2016UL,
    "STs2017UL":STs2017UL,
    "STs2018UL":STs2018UL,
    "STt2016APVUL":STt2016APVUL,
    "STt2016UL":STt2016UL,
    "STt2017UL":STt2017UL,
    "STt2018UL":STt2018UL,
    "STtb2016APVUL":STtb2016APVUL,
    "STtb2016UL":STtb2016UL,
    "STtb2017UL":STtb2017UL,
    "STtb2018UL":STtb2018UL,
    "STtW2016APVUL":STtW2016APVUL,
    "STtW2016UL":STtW2016UL,
    "STtW2017UL":STtW2017UL,
    "STtW2018UL":STtW2018UL,
    "STtWb2016APVUL":STtWb2016APVUL,
    "STtWb2016UL":STtWb2016UL,
    "STtWb2017UL":STtWb2017UL,
    "STtWb2018UL":STtWb2018UL,
    "TTHB2016APVUL":TTHB2016APVUL,
    "TTHB2016UL":TTHB2016UL,
    "TTHB2017UL":TTHB2017UL,
    "TTHB2018UL":TTHB2018UL,
    "TTHnonB2016APVUL":TTHnonB2016APVUL,
    "TTHnonB2016UL":TTHnonB2016UL,
    "TTHnonB2017UL":TTHnonB2017UL,
    "TTHnonB2018UL":TTHnonB2018UL,
    "TTMT10002016APVUL":TTMT10002016APVUL,
    "TTMT10002016UL":TTMT10002016UL,
    "TTMT10002017UL":TTMT10002017UL,
    "TTMT10002018UL":TTMT10002018UL,
    "TTMT7002016APVUL":TTMT7002016APVUL,
    "TTMT7002016UL":TTMT7002016UL,
    "TTMT7002017UL":TTMT7002017UL,
    "TTMT7002018UL":TTMT7002018UL,
    "TTTo2L2Nu2016APVUL":TTTo2L2Nu2016APVUL,
    "TTTo2L2Nu2016UL":TTTo2L2Nu2016UL,
    "TTTo2L2Nu2017UL":TTTo2L2Nu2017UL,
    "TTTo2L2Nu2018UL":TTTo2L2Nu2018UL,
    "TTToHadronic2016APVUL":TTToHadronic2016APVUL,
    "TTToHadronic2016UL":TTToHadronic2016UL,
    "TTToHadronic2017UL":TTToHadronic2017UL,
    "TTToHadronic2018UL":TTToHadronic2018UL,
    "TTToSemiLeptonic2016APVUL":TTToSemiLeptonic2016APVUL,
    "TTToSemiLeptonic2016UL":TTToSemiLeptonic2016UL,
    "TTToSemiLeptonic2017UL":TTToSemiLeptonic2017UL,
    "TTToSemiLeptonic2018UL":TTToSemiLeptonic2018UL,
    "TTWl2016APVUL":TTWl2016APVUL,
    "TTWl2016UL":TTWl2016UL,
    "TTWl2017UL":TTWl2017UL,
    "TTWl2018UL":TTWl2018UL,
    "TTWq2016APVUL":TTWq2016APVUL,
    "TTWq2016UL":TTWq2016UL,
    "TTWq2017UL":TTWq2017UL,
    "TTWq2018UL":TTWq2018UL,
    "TTZM102016APVUL":TTZM102016APVUL,
    "TTZM102016UL":TTZM102016UL,
    "TTZM102017UL":TTZM102017UL,
    "TTZM102018UL":TTZM102018UL,
    "TTZM1to102016APVUL":TTZM1to102016APVUL,
    "TTZM1to102016UL":TTZM1to102016UL,
    "TTZM1to102017UL":TTZM1to102017UL,
    "TTZM1to102018UL":TTZM1to102018UL,
    "WJetsHT12002016APVUL":WJetsHT12002016APVUL,
    "WJetsHT12002016UL":WJetsHT12002016UL,
    "WJetsHT12002017UL":WJetsHT12002017UL,
    "WJetsHT12002018UL":WJetsHT12002018UL,
    "WJetsHT1200ext2018UL":WJetsHT1200ext2018UL,
    "WJetsHT2002016APVUL":WJetsHT2002016APVUL,
    "WJetsHT2002016UL":WJetsHT2002016UL,
    "WJetsHT2002017UL":WJetsHT2002017UL,
    "WJetsHT2002018UL":WJetsHT2002018UL,
    "WJetsHT25002016APVUL":WJetsHT25002016APVUL,
    "WJetsHT25002016UL":WJetsHT25002016UL,
    "WJetsHT25002017UL":WJetsHT25002017UL,
    "WJetsHT25002018UL":WJetsHT25002018UL,
    "WJetsHT4002016APVUL":WJetsHT4002016APVUL,
    "WJetsHT4002016UL":WJetsHT4002016UL,
    "WJetsHT4002017UL":WJetsHT4002017UL,
    "WJetsHT4002018UL":WJetsHT4002018UL,
    "WJetsHT400ext2018UL":WJetsHT400ext2018UL,
    "WJetsHT6002016APVUL":WJetsHT6002016APVUL,
    "WJetsHT6002016UL":WJetsHT6002016UL,
    "WJetsHT6002017UL":WJetsHT6002017UL,
    "WJetsHT6002018UL":WJetsHT6002018UL,
    "WJetsHT600ext2018UL":WJetsHT600ext2018UL,
    "WJetsHT8002016APVUL":WJetsHT8002016APVUL,
    "WJetsHT8002016UL":WJetsHT8002016UL,
    "WJetsHT8002017UL":WJetsHT8002017UL,
    "WJetsHT8002018UL":WJetsHT8002018UL,
    "WJetsHT800ext2018UL":WJetsHT800ext2018UL,
    "WW2016APVUL":WW2016APVUL,
    "WW2016UL":WW2016UL,
    "WW2017UL":WW2017UL,
    "WW2018UL":WW2018UL,
    "WZ2016APVUL":WZ2016APVUL,
    "WZ2016UL":WZ2016UL,
    "WZ2017UL":WZ2017UL,
    "WZ2018UL":WZ2018UL,
    "ZZ2016APVUL":ZZ2016APVUL,
    "ZZ2016UL":ZZ2016UL,
    "ZZ2017UL":ZZ2017UL,
    "ZZ2018UL":ZZ2018UL,
}

samples_2016APVUL = {
    
    "DYMHT12002016APVUL":DYMHT12002016APVUL,
    "DYMHT2002016APVUL":DYMHT2002016APVUL,
    "DYMHT25002016APVUL":DYMHT25002016APVUL,
    "DYMHT4002016APVUL":DYMHT4002016APVUL,
    "DYMHT6002016APVUL":DYMHT6002016APVUL,
    "DYMHT8002016APVUL":DYMHT8002016APVUL,
    # "JetHTRun2016APVB":JetHTRun2016APVB,
    # "JetHTRun2016APVC":JetHTRun2016APVC,
    # "JetHTRun2016APVD":JetHTRun2016APVD,
    # "JetHTRun2016APVE":JetHTRun2016APVE,
    # "JetHTRun2016APVF":JetHTRun2016APVF,
    "QCDHT10002016APVUL":QCDHT10002016APVUL,
    "QCDHT15002016APVUL":QCDHT15002016APVUL,
    "QCDHT20002016APVUL":QCDHT20002016APVUL,
    "QCDHT2002016APVUL":QCDHT2002016APVUL,
    "QCDHT3002016APVUL":QCDHT3002016APVUL,
    "QCDHT5002016APVUL":QCDHT5002016APVUL,
    "QCDHT7002016APVUL":QCDHT7002016APVUL,
    "SingleElecRun2016APVB":SingleElecRun2016APVB,
    "SingleElecRun2016APVC":SingleElecRun2016APVC,
    "SingleElecRun2016APVD":SingleElecRun2016APVD,
    "SingleElecRun2016APVE":SingleElecRun2016APVE,
    "SingleElecRun2016APVF":SingleElecRun2016APVF,
    "SingleMuonRun2016APVB":SingleMuonRun2016APVB,
    "SingleMuonRun2016APVC":SingleMuonRun2016APVC,
    "SingleMuonRun2016APVD":SingleMuonRun2016APVD,
    "SingleMuonRun2016APVE":SingleMuonRun2016APVE,
    "SingleMuonRun2016APVF":SingleMuonRun2016APVF,
    "STs2016APVUL":STs2016APVUL,
    "STt2016APVUL":STt2016APVUL,
    "STtb2016APVUL":STtb2016APVUL,
    "STtW2016APVUL":STtW2016APVUL,
    "STtWb2016APVUL":STtWb2016APVUL,
    "TTHB2016APVUL":TTHB2016APVUL,
    "TTHnonB2016APVUL":TTHnonB2016APVUL,
    "TTMT10002016APVUL":TTMT10002016APVUL,
    "TTMT7002016APVUL":TTMT7002016APVUL,
    "TTTo2L2Nu2016APVUL":TTTo2L2Nu2016APVUL,
    "TTToHadronic2016APVUL":TTToHadronic2016APVUL,
    "TTToSemiLeptonic2016APVUL":TTToSemiLeptonic2016APVUL,
    "TTWl2016APVUL":TTWl2016APVUL,
    "TTWq2016APVUL":TTWq2016APVUL,
    "TTZM102016APVUL":TTZM102016APVUL,
    "TTZM1to102016APVUL":TTZM1to102016APVUL,
    "WJetsHT12002016APVUL":WJetsHT12002016APVUL,
    "WJetsHT2002016APVUL":WJetsHT2002016APVUL,
    "WJetsHT25002016APVUL":WJetsHT25002016APVUL,
    "WJetsHT4002016APVUL":WJetsHT4002016APVUL,
    "WJetsHT6002016APVUL":WJetsHT6002016APVUL,
    "WJetsHT8002016APVUL":WJetsHT8002016APVUL,
    "WW2016APVUL":WW2016APVUL,
    "WZ2016APVUL":WZ2016APVUL,
    "ZZ2016APVUL":ZZ2016APVUL,

}

samples_2016UL = {
    "Bprime_M1000_2016UL":Bprime_M1000_2016UL,
    "Bprime_M1200_2016UL":Bprime_M1200_2016UL,
    "Bprime_M1300_2016UL":Bprime_M1300_2016UL,
    "Bprime_M1400_2016UL":Bprime_M1400_2016UL,
    "Bprime_M1500_2016UL":Bprime_M1500_2016UL,
    "Bprime_M1600_2016UL":Bprime_M1600_2016UL,
    "Bprime_M1700_2016UL":Bprime_M1700_2016UL,
    "Bprime_M1800_2016UL":Bprime_M1800_2016UL,
    "Bprime_M2000_2016UL":Bprime_M2000_2016UL,
    "Bprime_M2200_2016UL":Bprime_M2200_2016UL,
    "Bprime_M800_2016UL":Bprime_M800_2016UL,
    "DYMHT12002016UL":DYMHT12002016UL,
    "DYMHT2002016UL":DYMHT2002016UL,
    "DYMHT25002016UL":DYMHT25002016UL,
    "DYMHT4002016UL":DYMHT4002016UL,
    "DYMHT6002016UL":DYMHT6002016UL,
    "DYMHT8002016UL":DYMHT8002016UL,
    # "JetHTRun2016F":JetHTRun2016F,
    # "JetHTRun2016G":JetHTRun2016G,
    # "JetHTRun2016H":JetHTRun2016H,
    "QCDHT10002016UL":QCDHT10002016UL,
    "QCDHT15002016UL":QCDHT15002016UL,
    "QCDHT20002016UL":QCDHT20002016UL,
    "QCDHT2002016UL":QCDHT2002016UL,
    "QCDHT3002016UL":QCDHT3002016UL,
    "QCDHT5002016UL":QCDHT5002016UL,
    "QCDHT7002016UL":QCDHT7002016UL,
    "SingleElecRun2016F":SingleElecRun2016F,
    "SingleElecRun2016G":SingleElecRun2016G,
    "SingleElecRun2016H":SingleElecRun2016H,
    "SingleMuonRun2016F":SingleMuonRun2016F,
    "SingleMuonRun2016G":SingleMuonRun2016G,
    "SingleMuonRun2016H":SingleMuonRun2016H,
    "STs2016UL":STs2016UL,
    "STt2016UL":STt2016UL,
    "STtb2016UL":STtb2016UL,
    "STtW2016UL":STtW2016UL,
    "STtWb2016UL":STtWb2016UL,
    "TTHB2016UL":TTHB2016UL,
    "TTHnonB2016UL":TTHnonB2016UL,
    "TTMT10002016UL":TTMT10002016UL,
    "TTMT7002016UL":TTMT7002016UL,
    "TTTo2L2Nu2016UL":TTTo2L2Nu2016UL,
    "TTToHadronic2016UL":TTToHadronic2016UL,
    "TTToSemiLeptonic2016UL":TTToSemiLeptonic2016UL,
    "TTWl2016UL":TTWl2016UL,
    "TTWq2016UL":TTWq2016UL,
    "TTZM102016UL":TTZM102016UL,
    "TTZM1to102016UL":TTZM1to102016UL,
    "WJetsHT12002016UL":WJetsHT12002016UL,
    "WJetsHT2002016UL":WJetsHT2002016UL,
    "WJetsHT25002016UL":WJetsHT25002016UL,
    "WJetsHT4002016UL":WJetsHT4002016UL,
    "WJetsHT6002016UL":WJetsHT6002016UL,
    "WJetsHT8002016UL":WJetsHT8002016UL,
    "WW2016UL":WW2016UL,
    "WZ2016UL":WZ2016UL,
    "ZZ2016UL":ZZ2016UL,
}

samples_2017UL = {
    "Bprime_M1000_2017UL":Bprime_M1000_2017UL,
    "Bprime_M1200_2017UL":Bprime_M1200_2017UL,
    "Bprime_M1300_2017UL":Bprime_M1300_2017UL,
    "Bprime_M1400_2017UL":Bprime_M1400_2017UL,
    "Bprime_M1500_2017UL":Bprime_M1500_2017UL,
    "Bprime_M1600_2017UL":Bprime_M1600_2017UL,
    "Bprime_M1700_2017UL":Bprime_M1700_2017UL,
    "Bprime_M1800_2017UL":Bprime_M1800_2017UL,
    "Bprime_M2000_2017UL":Bprime_M2000_2017UL,
    "Bprime_M2200_2017UL":Bprime_M2200_2017UL,
    "Bprime_M800_2017UL":Bprime_M800_2017UL,
    "DYMHT12002017UL":DYMHT12002017UL,
    "DYMHT2002017UL":DYMHT2002017UL,
    "DYMHT25002017UL":DYMHT25002017UL,
    "DYMHT4002017UL":DYMHT4002017UL,
    "DYMHT6002017UL":DYMHT6002017UL,
    "DYMHT8002017UL":DYMHT8002017UL,
    # "JetHTRun2017B":JetHTRun2017B,
    # "JetHTRun2017C":JetHTRun2017C,
    # "JetHTRun2017D":JetHTRun2017D,
    # "JetHTRun2017E":JetHTRun2017E,
    # "JetHTRun2017F":JetHTRun2017F,
    "QCDHT10002017UL":QCDHT10002017UL,
    "QCDHT15002017UL":QCDHT15002017UL,
    "QCDHT20002017UL":QCDHT20002017UL,
    "QCDHT2002017UL":QCDHT2002017UL,
    "QCDHT3002017UL":QCDHT3002017UL,
    "QCDHT5002017UL":QCDHT5002017UL,
    "QCDHT7002017UL":QCDHT7002017UL,
    "SingleElecRun2017B":SingleElecRun2017B,
    "SingleElecRun2017C":SingleElecRun2017C,
    "SingleElecRun2017D":SingleElecRun2017D,
    "SingleElecRun2017E":SingleElecRun2017E,
    "SingleElecRun2017F":SingleElecRun2017F,
    "SingleMuonRun2017B":SingleMuonRun2017B,
    "SingleMuonRun2017C":SingleMuonRun2017C,
    "SingleMuonRun2017D":SingleMuonRun2017D,
    "SingleMuonRun2017E":SingleMuonRun2017E,
    "SingleMuonRun2017F":SingleMuonRun2017F,
    "STs2017UL":STs2017UL,
    "STt2017UL":STt2017UL,
    "STtb2017UL":STtb2017UL,
    "STtW2017UL":STtW2017UL,
    "STtWb2017UL":STtWb2017UL,
    "TTHB2017UL":TTHB2017UL,
    "TTHnonB2017UL":TTHnonB2017UL,
    "TTMT10002017UL":TTMT10002017UL,
    "TTMT7002017UL":TTMT7002017UL,
    "TTTo2L2Nu2017UL":TTTo2L2Nu2017UL,
    "TTToHadronic2017UL":TTToHadronic2017UL,
    "TTToSemiLeptonic2017UL":TTToSemiLeptonic2017UL,
    "TTWl2017UL":TTWl2017UL,
    "TTWq2017UL":TTWq2017UL,
    "TTZM102017UL":TTZM102017UL,
    "TTZM1to102017UL":TTZM1to102017UL,
    "WJetsHT12002017UL":WJetsHT12002017UL,
    "WJetsHT2002017UL":WJetsHT2002017UL,
    "WJetsHT25002017UL":WJetsHT25002017UL,
    "WJetsHT4002017UL":WJetsHT4002017UL,
    "WJetsHT6002017UL":WJetsHT6002017UL,
    "WJetsHT8002017UL":WJetsHT8002017UL,
    "WW2017UL":WW2017UL,
    "WZ2017UL":WZ2017UL,
    "ZZ2017UL":ZZ2017UL,
}

samples_2018UL = {
    # "JetHTRun2018A":JetHTRun2018A,
    # "JetHTRun2018B":JetHTRun2018B,
    # "JetHTRun2018C":JetHTRun2018C,
    # "JetHTRun2018D":JetHTRun2018D,
    "SingleElecRun2018A":SingleElecRun2018A,
    "SingleElecRun2018B":SingleElecRun2018B,
    "SingleElecRun2018C":SingleElecRun2018C,
    "SingleElecRun2018D":SingleElecRun2018D,
    "SingleMuonRun2018A":SingleMuonRun2018A,
    "SingleMuonRun2018B":SingleMuonRun2018B,
    "SingleMuonRun2018C":SingleMuonRun2018C,
    "SingleMuonRun2018D":SingleMuonRun2018D,
    "Bprime_M1000_2018UL":Bprime_M1000_2018UL,
    "Bprime_M1200_2018UL":Bprime_M1200_2018UL,
    "Bprime_M1300_2018UL":Bprime_M1300_2018UL,
    "Bprime_M1400_2018UL":Bprime_M1400_2018UL,
    "Bprime_M1500_2018UL":Bprime_M1500_2018UL,
    "Bprime_M1600_2018UL":Bprime_M1600_2018UL,
    "Bprime_M1700_2018UL":Bprime_M1700_2018UL,
    "Bprime_M1800_2018UL":Bprime_M1800_2018UL,
    "Bprime_M2000_2018UL":Bprime_M2000_2018UL,
    "Bprime_M2200_2018UL":Bprime_M2200_2018UL,
    "Bprime_M800_2018UL":Bprime_M800_2018UL,
    "DYMHT12002018UL":DYMHT12002018UL,
    "DYMHT2002018UL":DYMHT2002018UL,
    "DYMHT25002018UL":DYMHT25002018UL,
    "DYMHT4002018UL":DYMHT4002018UL,
    "DYMHT6002018UL":DYMHT6002018UL,
    "DYMHT8002018UL":DYMHT8002018UL,
    "QCDHT10002018UL":QCDHT10002018UL,
    "QCDHT15002018UL":QCDHT15002018UL,
    "QCDHT20002018UL":QCDHT20002018UL,
    "QCDHT2002018UL":QCDHT2002018UL,
    "QCDHT3002018UL":QCDHT3002018UL,
    "QCDHT5002018UL":QCDHT5002018UL,
    "QCDHT7002018UL":QCDHT7002018UL,
    "STs2018UL":STs2018UL,
    "STt2018UL":STt2018UL,
    "STtb2018UL":STtb2018UL,
    "STtW2018UL":STtW2018UL,
    "STtWb2018UL":STtWb2018UL,
    "TTHB2018UL":TTHB2018UL,
    "TTHnonB2018UL":TTHnonB2018UL,
    "TTMT10002018UL":TTMT10002018UL,
    "TTMT7002018UL":TTMT7002018UL,
    "TTTo2L2Nu2018UL":TTTo2L2Nu2018UL,
    "TTToHadronic2018UL":TTToHadronic2018UL,
    "TTToSemiLeptonic2018UL":TTToSemiLeptonic2018UL,
    "TTWl2018UL":TTWl2018UL,
    "TTWq2018UL":TTWq2018UL,
    "TTZM102018UL":TTZM102018UL,
    "TTZM1to102018UL":TTZM1to102018UL,
    "WJetsHT12002018UL":WJetsHT12002018UL,
    "WJetsHT2002018UL":WJetsHT2002018UL,
    "WJetsHT25002018UL":WJetsHT25002018UL,
    "WJetsHT4002018UL":WJetsHT4002018UL,
    "WJetsHT6002018UL":WJetsHT6002018UL,
    "WJetsHT8002018UL":WJetsHT8002018UL,
    "WW2018UL":WW2018UL,
    "WZ2018UL":WZ2018UL,
    "ZZ2018UL":ZZ2018UL,
}


samples_BPrime = {
    #"Bprime_M800_2018UL":Bprime_M800_2018UL,
    "Bprime_M1400_2018UL":Bprime_M1400_2018UL,
    #"Bprime_M2000_2018UL":Bprime_M2000_2018UL,
}

samples_WJets = {
    "WJetsHT12002018UL":WJetsHT12002018UL,
    "WJetsHT1200ext2018UL":WJetsHT1200ext2018UL,
    "WJetsHT4002018UL":WJetsHT4002018UL,
    "WJetsHT400ext2018UL":WJetsHT400ext2018UL,
    "WJetsHT6002018UL":WJetsHT6002018UL,
    "WJetsHT600ext2018UL":WJetsHT600ext2018UL,
    "WJetsHT8002017UL":WJetsHT8002017UL,
    "WJetsHT800ext2018UL":WJetsHT800ext2018UL,
}
samples_redo = {
    "SingleElecRun2018B":SingleElecRun2018B,
    "SingleElecRun2018C":SingleElecRun2018C,
    #"SingleElecRun2018D":SingleElecRun2018D,
    #"TTMT10002016APVUL":TTMT10002016APVUL,
    #"TTMT7002016APVUL":TTMT7002016APVUL,
}

samples_trig = {
    "TTTo2L2Nu2016APVUL":TTTo2L2Nu2016APVUL,
    "TTTo2L2Nu2016UL":TTTo2L2Nu2016UL,
    "TTTo2L2Nu2017UL":TTTo2L2Nu2017UL,
    "TTTo2L2Nu2018UL":TTTo2L2Nu2018UL,
    # "SingleElecRun2016APVB":SingleElecRun2016APVB,
    # "SingleElecRun2016APVC":SingleElecRun2016APVC,
    # "SingleElecRun2016APVD":SingleElecRun2016APVD,
    # "SingleElecRun2016APVE":SingleElecRun2016APVE,
    # "SingleElecRun2016APVF":SingleElecRun2016APVF,
    # "SingleElecRun2016F":SingleElecRun2016F,
    # "SingleElecRun2016G":SingleElecRun2016G,
    # "SingleElecRun2016H":SingleElecRun2016H,
    # "SingleElecRun2017B":SingleElecRun2017B,
    # "SingleElecRun2017C":SingleElecRun2017C,
    # "SingleElecRun2017D":SingleElecRun2017D,
    # "SingleElecRun2017E":SingleElecRun2017E,
    # "SingleElecRun2017F":SingleElecRun2017F,
    # "SingleElecRun2018A":SingleElecRun2018A,
    # "SingleElecRun2018B":SingleElecRun2018B,
    # "SingleElecRun2018C":SingleElecRun2018C,
    # "SingleElecRun2018D":SingleElecRun2018D,
    "SingleMuonRun2016APVB":SingleMuonRun2016APVB,
    "SingleMuonRun2016APVC":SingleMuonRun2016APVC,
    "SingleMuonRun2016APVD":SingleMuonRun2016APVD,
    "SingleMuonRun2016APVE":SingleMuonRun2016APVE,
    "SingleMuonRun2016APVF":SingleMuonRun2016APVF,
    "SingleMuonRun2016F":SingleMuonRun2016F,
    "SingleMuonRun2016G":SingleMuonRun2016G,
    "SingleMuonRun2016H":SingleMuonRun2016H,
    "SingleMuonRun2017B":SingleMuonRun2017B,
    "SingleMuonRun2017C":SingleMuonRun2017C,
    "SingleMuonRun2017D":SingleMuonRun2017D,
    "SingleMuonRun2017E":SingleMuonRun2017E,
    "SingleMuonRun2017F":SingleMuonRun2017F,
    "SingleMuonRun2018A":SingleMuonRun2018A,
    "SingleMuonRun2018B":SingleMuonRun2018B,
    "SingleMuonRun2018C":SingleMuonRun2018C,
    "SingleMuonRun2018D":SingleMuonRun2018D,
}

