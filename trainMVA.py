# %%
### Imports
import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import importlib
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from keras import backend as K
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.layers import Input, Dense, Concatenate
from tensorflow.keras.models import Model, Sequential, load_model
import importlib
from sklearn.preprocessing import StandardScaler

from ROOT import TTree, TH1D, TFile
from root_numpy import tree2array
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn import svm, metrics, preprocessing
from plot_confusion_matrix import plot_confusion_matrix
import copy, time, os, sys, math, random, itertools
from sklearn import neural_network
from sklearn.linear_model import SGDClassifier
from sklearn import tree
from sklearn.metrics import roc_curve
from sklearn.externals import joblib
from sklearn.metrics import classification_report, f1_score, recall_score, precision_score, accuracy_score

# %% 
### Define helper functions
def millify(n):
   n = float(n)
   millnames = ['','k','M','G','T']
   millidx = max(0,min(len(millnames)-1,
                       int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

   return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

def arch2tuple(n):
   layers, nodes = n.split('x',2)
   tup = (int(nodes),)
   out =()
   for x in range(int(layers)-1):
      out = out + tup
   return (out)

# %% 
### Read in arguments
start_time = time.time()
arch = '3x10'
maxtest = 15000
outdir = sys.argv[1]
vararray = int(sys.argv[2])
testnum = int(sys.argv[3])
year = str(sys.argv[4])
if year == 'all': maxtest = 30000

# %%
### Set up logging
# TODO
outdir = outdir + '/'
if testnum == 1:
   ofile = open(outdir+"BB_output_Jan21_"+year+".txt","a+")
   ofile.write('\ntest, vararray, Testing Score (Accuracy), tt-as-BB, BB-as-BB, Precision, Recall, F-Score \n')
else:
   time.sleep(2)
   ofile = open(outdir+"BB_output_Jan21_"+year+".txt","a+")
   ofile.write('\n')
ofile.write(str(testnum)+", ")
ofile.write(str(vararray)+", ")

# %% 
### Signal selection
Bprime = 1.0
Bprime2 = 1.8
test1100 = False #use if Bprime = 1800

# %%
### Configure output
outStr = '_'+year+'BB_'+str(arch)+'_' + str(millify(maxtest)) +'test_vars'+str(vararray)+'_Test'+str(testnum)
print 'Outstr:',outStr,'Outdir:',outdir
if not os.path.exists(outdir): os.system('mkdir '+outdir)

# %% 
### Define input variables

# TODO
## List of possible variables for the MVA
varList = ['dnnJ_1','dnnJ_2','jetPt_1','jetPt_3','sdMass_1','sdMass_3','tau21_3','AK4HT','t_pt','t_mass','t_dRWb','AK4HTpMETpLepPt','corr_met_MultiLepCalc','NJets_JetSubCalc', 'NJetsDeepFlavwithSF_JetSubCalc','NJetsAK8_JetSubCalc','minDR_leadAK8otherAK8'] 
#'jetPt_2','sdMass_2','dnnJ_3', removed for bad data/bkg agreement  #'tau21_1','tau21_2', removed since not used before

if year == '2016':
   # varList = ['dnnJ_1','dnnJ_2','dnnJ_3','jetPt_1','jetPt_3','sdMass_1','tau21_3','AK4HT','t_pt','t_mass','t_dRWb','AK4HTpMETpLepPt','corr_met_MultiLepCalc','NJets_JetSubCalc', 'NJetsDeepFlavwithSF_JetSubCalc','NJetsAK8_JetSubCalc','minDR_leadAK8otherAK8'] 
   varList = ['dpak8_J_1', 'dpak8_J_2', 'FatJet_pt_1', 'FatJet_pt_2', 'FatJet_sdMass_1', 'FatJet_sdMass_2', 'AK4HT', 'pnT_1', 'pnT_2', 'pnT_3', 'pnH_1', 'pnH_2', 'pnH_3', 'pnZ_1', 'pnZ_2', 'pnZ_3', 'pnW_1','pnW_2', 'pnW_3', 'NJetsDeepFlavwithSF', 'Bprime_eta', 'Bprime_phi']
   #'jetPt_2','sdMass_2','sdMass_3', removed for bad data/bkg agreement  #'tau21_1','tau21_2', removed since not used before
elif year == '2018':
   varList = ['dnnJ_1','dnnJ_2','dnnJ_3','jetPt_1','jetPt_3','sdMass_3','tau21_3','AK4HT','t_pt','t_mass','t_dRWb','AK4HTpMETpLepPt','corr_met_MultiLepCalc','NJets_JetSubCalc', 'NJetsDeepFlavwithSF_JetSubCalc','NJetsAK8_JetSubCalc','minDR_leadAK8otherAK8'] 
   #'jetPt_2','sdMass_2','sdMass_1', removed for bad data/bkg agreement  #'tau21_1','tau21_2', removed since not used before
elif year == 'all':
   varList = ['dnnJ_1','dnnJ_2','dnnJ_3','jetPt_1','jetPt_3','sdMass_1','sdMass_3','tau21_3','AK4HT','t_pt','t_mass','t_dRWb','AK4HTpMETpLepPt','corr_met_MultiLepCalc','NJets_JetSubCalc', 'NJetsDeepFlavwithSF_JetSubCalc','NJetsAK8_JetSubCalc','minDR_leadAK8otherAK8'] 

# %%
### Perform permuations calculations
## Make a big list of lists of different lengths and combinations
# TODO
combos = []
for size in range(7,len(varList)):
   thissize = list(itertools.combinations(varList,size))
   for item in thissize:
      ## Some sanity checks for vars we know for sure we want to include
      if 'dnnJ_1' not in item: continue
      if 'dnnJ_2' not in item and 'dnnJ_3' not in item: continue
      if 'AK4HT' not in item: continue
      if 'corr_met_MultiLepCalc' not in item and 'AK4HTpMETpLepPt' not in item: continue
      if 'NJetsDeepFlavwithSF_JetSubCalc' not in item and 'NJets_JetSubCalc' not in item: continue
      if 't_mass' not in item and 't_pt' not in item: continue
      if 't_dRWb' not in item and 'minDR_leadAK8otherAK8' not in item: continue
      combos.append(item)
combos.append(varList)

if year == 'all':
   combos = []
   for size in range(12,14):
      thissize = list(itertools.combinations(varList,size))
      for item in thissize:
         ## Some sanity checks for vars we know for sure we want to include
         if 'dnnJ_1' not in item: continue
         if 'dnnJ_2' not in item: continue
         if 'dnnJ_3' not in item: continue
         if 'AK4HT' not in item: continue
         if 'AK4HTpMETpLepPt' not in item: continue
         if 'NJetsDeepFlavwithSF_JetSubCalc' not in item: continue
         if 'NJets_JetSubCalc' not in item: continue
         if 't_mass' not in item and 't_pt' not in item: continue
         if 'minDR_leadAK8otherAK8' not in item: continue
         combos.append(item)
   #combos.append(varList)

   # combos = []
   # for size in range(10,len(varList)):
   #    thissize = list(itertools.combinations(varList,size))
   #    for item in thissize:
   #       ## Some sanity checks for vars we know for sure we want to include
   #       if 'dnnJ_1' not in item: continue
   #       if 'dnnJ_2' not in item: continue
   #       if 'AK4HT' not in item: continue
   #       if 'AK4HTpMETpLepPt' not in item: continue
   #       if 'NJetsDeepFlavwithSF_JetSubCalc' not in item: continue
   #       if 'NJets_JetSubCalc' not in item: continue
   #       if 't_mass' not in item and 't_pt' not in item: continue
   #       if 'minDR_leadAK8otherAK8' not in item: continue
   #       combos.append(item)
   # combos.append(varList)

# %%
### Select input for training and testing
# TODO
vars = list(combos[vararray])
print 'Vars = ',vars

indexKill = range(0,len(varList))
for item in vars:
   indexKill.remove(varList.index(item))

inStr = '_'+year+'BB_'+str(arch)+'_' + str(millify(maxtest)) +'test'
allmystuff = np.load(outdir+'Arrays'+inStr+'.npz')

trainData = (allmystuff['trainData']).tolist()
trainLabel = (allmystuff['trainLabel']).tolist()
testData = (allmystuff['testData']).tolist()
testLabel = (allmystuff['testLabel']).tolist()
testWJets = (allmystuff['testWJets']).tolist()
testTTToSemiLep = (allmystuff['testTTToSemilep']).tolist()
testTprime = (allmystuff['testTprime']).tolist()
testTprime2 = (allmystuff['testTprime2']).tolist()

## Get rid of the variables we aren't using this time
for i in range(0,len(trainData)):
   for j in sorted(indexKill, reverse = True):
      del trainData[i][j]
for i in range(0,len(testData)):
   for j in sorted(indexKill, reverse = True):
      del testData[i][j]
for i in range(0,len(testWJets)):
   for j in sorted(indexKill, reverse = True):
      del testWJets[i][j]
      del testTprime[i][j]
      del testTprime2[i][j]
      del testTTToSemiLep[i][j]

# %% 
### Perform scaling
print 'Building the scaler...'
scaler = preprocessing.StandardScaler().fit(trainData)
print 'Transforming...'
trainData = scaler.transform(trainData)
testData = scaler.transform(testData)
testTprime2 = scaler.transform(testTprime2)
testTprime = scaler.transform(testTprime)
testTTToSemiLep = scaler.transform(testTTToSemiLep)
testWJets = scaler.transform(testWJets)

# %%
# TODO
### Train _____ 
print('Training...')
mlp = neural_network.MLPClassifier(hidden_layer_sizes=arch2tuple(arch), activation='relu',early_stopping=True)
mlp.fit(trainData, trainLabel)
# %%
### Get scores for training and test data
print 'Test data score =',mlp.score(testData, testLabel)
print 'Train data score =',mlp.score(trainData, trainLabel)
ofile.write(str(round(mlp.score(testData, testLabel),5)) + ", ")

# %%
### Plotting model evaluation data
## Plot a confusion matrix
cm = metrics.confusion_matrix(mlp.predict(testData), testLabel)
plt.figure()
targetNames = [r'$\mathrm{W+jets}$',r'$\mathrm{t\bar{t}}$',r'$\mathrm{T\overline{T}}$']
plot_confusion_matrix(cm.T, targetNames, normalize=True)

cm = (cm.T).astype('float') / (cm.T).sum(axis=1)[:, np.newaxis]

ofile.write(str(round(cm[1][2],5)) + ", " + str(round(cm[2][2],5)) + ", ")

threshold = 0.78
if year == 'all': threshold = 0.83
if mlp.score(testData,testLabel) > threshold:

   plt.savefig(outdir+'confusion'+outStr+'.png')

   ## Draw training sample loss curve
   losscurve = mlp.loss_curve_
   plt.figure()
   plt.xlabel('iterations')
   plt.ylabel('training loss')
   plt.plot(losscurve)
   plt.savefig(outdir+'trainloss'+outStr+'.png')
   plt.close()
   
   ## Draw validation sample (10% of the training data) score
   testscore = mlp.validation_scores_
   plt.figure()
   plt.xlabel('iterations')
   plt.ylabel('validation score')
   plt.plot(testscore)
   plt.savefig(outdir+'valscore'+outStr+'.png')
   plt.close()
   
   ## Predict the scores for non-training events
   probsWJets = mlp.predict_proba(testWJets)
   probsTTToSemiLep = mlp.predict_proba(testTTToSemiLep)
   probsTprime = mlp.predict_proba(testTprime)
   probsTprime2 = mlp.predict_proba(testTprime2)
   probs = [probsWJets, probsTTToSemiLep, probsTprime]
   if test1100: probs = [probsWJets, probsTTToSemiLep, probsTprime2]

   ## Plot the scores
   plt.close()
   plt.figure()
   plt.xlabel('Predicted W boson score',horizontalalignment='right',x=1.0,size=14)
   plt.ylabel('Events per bin',horizontalalignment='right',y=1.0,size=14)
   plt.title('CMS Simulation',loc='left',size=18)
   plt.title('Work in progress',loc='right',size=14,style='italic')
   plt.ylim([0.01,10.**4])
   plt.hist(probsWJets.T[0], bins=20, range=(0,1), label=r'$\mathrm{W+jets}$', color='g', histtype='step',normed=True, log=True)
   plt.hist(probsTTToSemiLep.T[0], bins=20, range=(0,1), label=r'$\mathrm{t\bar{t}}$', color='y', histtype='step',normed=True, log=True)
   plt.hist(probsTprime.T[0], bins=20, range=(0,1), label=r'$\mathrm{B\overline{B}\,('+str(Tprime)+'\,TeV)}$', color='m', histtype='step',normed=True, log=True)
   plt.hist(probsTprime2.T[0], bins=20, range=(0,1), label=r'$\mathrm{B\overline{B}\,('+str(Tprime2)+'\,TeV)}$', color='c', histtype='step',normed=True, log=True)
   plt.legend(loc='best')
   plt.savefig(outdir+'score_WJet'+outStr+'.png')
   
   plt.close()
   plt.figure()
   plt.xlabel('Predicted top quark score',horizontalalignment='right',x=1.0,size=14)
   plt.ylabel('Events per bin',horizontalalignment='right',y=1.0,size=14)
   plt.title('CMS Simulation',loc='left',size=18)
   plt.title('Work in progress',loc='right',size=14,style='italic')
   plt.ylim([0.01,10.**4])
   plt.hist(probsWJets.T[1], bins=20, range=(0,1), label=r'$\mathrm{W+jets}$', color='g', histtype='step',normed=True, log=True)
   plt.hist(probsTTToSemiLep.T[1], bins=20, range=(0,1), label=r'$\mathrm{t\bar{t}}$', color='y', histtype='step',normed=True, log=True)
   plt.hist(probsTprime.T[1], bins=20, range=(0,1), label=r'$\mathrm{B\overline{B}\,('+str(Tprime)+'\,TeV)}$', color='m', histtype='step',normed=True, log=True)
   plt.hist(probsTprime2.T[1], bins=20, range=(0,1), label=r'$\mathrm{B\overline{B}\,('+str(Tprime2)+'\,TeV)}$', color='c', histtype='step',normed=True, log=True)
   plt.legend(loc='best')
   plt.savefig(outdir+'score_TTToSemiLep'+outStr+'.png')
   
   plt.close()
   plt.figure()
   plt.xlabel('Predicted B quark score',horizontalalignment='right',x=1.0,size=14)
   plt.ylabel('Events per bin',horizontalalignment='right',y=1.0,size=14)
   plt.title('CMS Simulation',loc='left',size=18)
   plt.title('Work in progress',loc='right',size=14,style='italic')
   plt.ylim([0.01,10.**4])
   plt.hist(probsWJets.T[2], bins=20, range=(0,1), label=r'$\mathrm{W+jets}$', color='g', histtype='step',normed=True, log=True)
   plt.hist(probsTTToSemiLep.T[2], bins=20, range=(0,1), label=r'$\mathrm{t\bar{t}}$', color='y', histtype='step',normed=True, log=True)
   plt.hist(probsTprime.T[2], bins=20, range=(0,1), label=r'$\mathrm{B\overline{B}\,('+str(Tprime)+'\,TeV)}$', color='m', histtype='step',normed=True, log=True)
   plt.hist(probsTprime2.T[2], bins=20, range=(0,1), label=r'$\mathrm{B\overline{B}\,('+str(Tprime2)+'\,TeV)}$', color='c', histtype='step',normed=True, log=True)
   plt.legend(loc='best')
   plt.savefig(outdir+'score_Bprime'+outStr+'.png')

   ## Print important things to files and the screen
   classRep = open('ClassificationReportsBB.txt', 'a+')
   cRep = classification_report(testLabel,mlp.predict(testData),target_names=['Wjets', 'ttbar', 'BBbar'], digits = 6)
   classRep.write('\n================================\n     Test #:' + str(testnum) +'\n================================\n' + cRep)
   classRep.close(

# %%
### Save outputs and close
prec = precision_score(testLabel, mlp.predict(testData), average='weighted')
recall = recall_score(testLabel, mlp.predict(testData), average='weighted')
fscore = f1_score(testLabel, mlp.predict(testData), average='weighted')
   
## save the output of the network
joblib.dump(mlp, outdir+'Dnn_mlp_3bin'+outStr+'.pkl')
joblib.dump(scaler, outdir+'Dnn_scaler_3bin'+outStr+'.pkl')

ofile.write(str(round(prec,5)) + ', ' + str(round(recall,5)) + ', ' + str(round(fscore,5))+ '\n')
ofile.close()

print 'Done'
print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))