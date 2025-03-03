void plotDeepFlav(TString mass){

  // ADJUST ALL THE YEARS to 2022 and 2023...
  // CAN UNCOMMENT THE CHUNKS FOR MEDIUM TAGGING
  
  // 2016APV Loose
  TFile *_file0 = TFile::Open("RDF_BprimeBtoTW_M-"+mass+"_NWALO_TuneCP5_13TeV-madgraph-pythia8_2016APV_DeepJetEff.root");
  TH1D *num = (TH1D*)_file0->Get("BEffLoose_Nptbins_b");
  TH1D *den = (TH1D*)_file0->Get("BEff_Dptbins_b");
  num->Divide(num,den,1.0,1.0,"B");

  cout << "B FLAVOR Loose 2016APV" << endl;
  for(int i = 1; i < num->GetNbinsX()+1; i++){printf("pT > %f, eff = %f\n",num->GetBinLowEdge(i),num->GetBinContent(i));}

  TH1D *numC = (TH1D*)_file0->Get("BEffLoose_Nptbins_c");
  TH1D *denC = (TH1D*)_file0->Get("BEff_Dptbins_c");
  numC->Divide(numC,denC,1.0,1.0,"B");

  cout << "C FLAVOR Loose 2016APV" << endl;
  for(int i = 1; i < numC->GetNbinsX()+1; i++){printf("pT > %f, fake = %f\n",numC->GetBinLowEdge(i),numC->GetBinContent(i));}

  TH1D *numL = (TH1D*)_file0->Get("BEffLoose_Nptbins_udsg");
  TH1D *denL = (TH1D*)_file0->Get("BEff_Dptbins_udsg");
  numL->Divide(numL,denL,1.0,1.0,"B");

  cout << "L FLAVOR Loose 2016APV" << endl;
  for(int i = 1; i < numL->GetNbinsX()+1; i++){printf("pT > %f, fake = %f\n",numL->GetBinLowEdge(i),numL->GetBinContent(i));}

  TCanvas *c1 = new TCanvas("c1","c1",800,600);
  gStyle->SetOptStat(0);
  num->GetYaxis()->SetRangeUser(0.0,1.0);
  num->GetYaxis()->SetTitle("Efficiency of DeepJet Loose");
  num->GetXaxis()->SetTitle("AK4 jet p_{T} [GeV]");
  num->SetLineWidth(2);
  num->SetMarkerStyle(20);
  num->SetMarkerColor(kBlack);
  num->SetLineColor(kBlack);
  numC->SetLineWidth(2);
  numC->SetMarkerStyle(20);
  numC->SetMarkerColor(kBlue);
  numC->SetLineColor(kBlue);
  numL->SetLineWidth(2);
  numL->SetMarkerStyle(20);
  numL->SetMarkerColor(kRed);
  numL->SetLineColor(kRed);
  num->Draw();
  numC->Draw("same");
  numL->Draw("same");
  TLegend *leg = new TLegend(0.7,0.7,0.98,0.98);
  leg->AddEntry(num,"b quarks","pl");
  leg->AddEntry(numC,"c quarks","pl");
  leg->AddEntry(numL,"udsg","pl");
  leg->Draw();
  c1->SaveAs("DeepFlavLoose_2016APV_"+mass+".png");
  c1->SaveAs("DeepFlavLoose_2016APV_"+mass+".pdf");
  c1->SaveAs("DeepFlavLoose_2016APV_"+mass+".root");

  //  // 2016APV Medium
  // TFile *_file0 = TFile::Open("RDF_BprimeBtoTW_M-"+mass+"_NWALO_TuneCP5_13TeV-madgraph-pythia8_2016APV_DeepJetEff.root");
  // num = (TH1D*)_file0->Get("BEffMed_Nptbins_b");
  // den = (TH1D*)_file0->Get("BEff_Dptbins_b");
  // num->Divide(num,den,1.0,1.0,"B");

  // cout << "B FLAVOR Med 2016APV" << endl;
  // for(int i = 1; i < num->GetNbinsX()+1; i++){printf("pT > %f, eff = %f\n",num->GetBinLowEdge(i),num->GetBinContent(i));}

  // numC = (TH1D*)_file0->Get("BEffMed_Nptbins_c");
  // denC = (TH1D*)_file0->Get("BEff_Dptbins_c");
  // numC->Divide(numC,denC,1.0,1.0,"B");

  // cout << "C FLAVOR Med 2016APV" << endl;
  // for(int i = 1; i < numC->GetNbinsX()+1; i++){printf("pT > %f, fake = %f\n",numC->GetBinLowEdge(i),numC->GetBinContent(i));}

  // numL = (TH1D*)_file0->Get("BEffMed_Nptbins_udsg");
  // denL = (TH1D*)_file0->Get("BEff_Dptbins_udsg");
  // numL->Divide(numL,denL,1.0,1.0,"B");

  // cout << "L FLAVOR Med 2016APV" << endl;
  // for(int i = 1; i < numL->GetNbinsX()+1; i++){printf("pT > %f, fake = %f\n",numL->GetBinLowEdge(i),numL->GetBinContent(i));}

  // c1 = new TCanvas("c1","c1",800,600);
  // gStyle->SetOptStat(0);
  // num->GetYaxis()->SetRangeUser(0.0,1.0);
  // num->GetYaxis()->SetTitle("Efficiency of DeepJet Med");
  // num->GetXaxis()->SetTitle("AK4 jet p_{T} [GeV]");
  // num->SetLineWidth(2);
  // num->SetMarkerStyle(20);
  // num->SetMarkerColor(kBlack);
  // num->SetLineColor(kBlack);
  // numC->SetLineWidth(2);
  // numC->SetMarkerStyle(20);
  // numC->SetMarkerColor(kBlue);
  // numC->SetLineColor(kBlue);
  // numL->SetLineWidth(2);
  // numL->SetMarkerStyle(20);
  // numL->SetMarkerColor(kRed);
  // numL->SetLineColor(kRed);
  // num->Draw();
  // numC->Draw("same");
  // numL->Draw("same");
  // leg = new TLegend(0.7,0.7,0.98,0.98);
  // leg->AddEntry(num,"b quarks","pl");
  // leg->AddEntry(numC,"c quarks","pl");
  // leg->AddEntry(numL,"udsg","pl");
  // leg->Draw();
  // c1->SaveAs("DeepFlavMed_2016APV_"+mass+".png");
  // c1->SaveAs("DeepFlavMed_2016APV_"+mass+".pdf");
  // c1->SaveAs("DeepFlavMed_2016APV_"+mass+".root");

  // 2016 Loose
  TFile *_file3 = TFile::Open("RDF_BprimeBtoTW_M-"+mass+"_NWALO_TuneCP5_13TeV-madgraph-pythia8_2016_DeepJetEff.root");
  num = (TH1D*)_file3->Get("BEffLoose_Nptbins_b");
  den = (TH1D*)_file3->Get("BEff_Dptbins_b");
  num->Divide(num,den,1.0,1.0,"B");

  cout << "B FLAVOR Loose 2016" << endl;
  for(int i = 1; i < num->GetNbinsX()+1; i++){printf("pT > %f, eff = %f\n",num->GetBinLowEdge(i),num->GetBinContent(i));}

  numC = (TH1D*)_file3->Get("BEffLoose_Nptbins_c");
  denC = (TH1D*)_file3->Get("BEff_Dptbins_c");
  numC->Divide(numC,denC,1.0,1.0,"B");

  cout << "C FLAVOR Loose 2016" << endl;
  for(int i = 1; i < numC->GetNbinsX()+1; i++){printf("pT > %f, fake = %f\n",numC->GetBinLowEdge(i),numC->GetBinContent(i));}

  numL = (TH1D*)_file3->Get("BEffLoose_Nptbins_udsg");
  denL = (TH1D*)_file3->Get("BEff_Dptbins_udsg");
  numL->Divide(numL,denL,1.0,1.0,"B");

  cout << "L FLAVOR Loose 2016" << endl;
  for(int i = 1; i < numL->GetNbinsX()+1; i++){printf("pT > %f, fake = %f\n",numL->GetBinLowEdge(i),numL->GetBinContent(i));}

  c1 = new TCanvas("c1","c1",800,600);
  gStyle->SetOptStat(0);
  num->GetYaxis()->SetRangeUser(0.0,1.0);
  num->GetYaxis()->SetTitle("Efficiency of DeepJet Loose");
  num->GetXaxis()->SetTitle("AK4 jet p_{T} [GeV]");
  num->SetLineWidth(2);
  num->SetMarkerStyle(20);
  num->SetMarkerColor(kBlack);
  num->SetLineColor(kBlack);
  numC->SetLineWidth(2);
  numC->SetMarkerStyle(20);
  numC->SetMarkerColor(kBlue);
  numC->SetLineColor(kBlue);
  numL->SetLineWidth(2);
  numL->SetMarkerStyle(20);
  numL->SetMarkerColor(kRed);
  numL->SetLineColor(kRed);
  num->Draw();
  numC->Draw("same");
  numL->Draw("same");
  leg = new TLegend(0.7,0.7,0.98,0.98);
  leg->AddEntry(num,"b quarks","pl");
  leg->AddEntry(numC,"c quarks","pl");
  leg->AddEntry(numL,"udsg","pl");
  leg->Draw();
  c1->SaveAs("DeepFlavLoose_2016_"+mass+".png");
  c1->SaveAs("DeepFlavLoose_2016_"+mass+".pdf");
  c1->SaveAs("DeepFlavLoose_2016_"+mass+".root");

  //  // 2016 Medium
  // num = (TH1D*)_file0->Get("BEffMed_Nptbins_b");
  // den = (TH1D*)_file0->Get("BEff_Dptbins_b");
  // num->Divide(num,den,1.0,1.0,"B");

  // cout << "B FLAVOR Med 2016" << endl;
  // for(int i = 1; i < num->GetNbinsX()+1; i++){printf("pT > %f, eff = %f\n",num->GetBinLowEdge(i),num->GetBinContent(i));}

  // numC = (TH1D*)_file0->Get("BEffMed_Nptbins_c");
  // denC = (TH1D*)_file0->Get("BEff_Dptbins_c");
  // numC->Divide(numC,denC,1.0,1.0,"B");

  // cout << "C FLAVOR Med 2016" << endl;
  // for(int i = 1; i < numC->GetNbinsX()+1; i++){printf("pT > %f, fake = %f\n",numC->GetBinLowEdge(i),numC->GetBinContent(i));}

  // numL = (TH1D*)_file0->Get("BEffMed_Nptbins_udsg");
  // denL = (TH1D*)_file0->Get("BEff_Dptbins_udsg");
  // numL->Divide(numL,denL,1.0,1.0,"B");

  // cout << "L FLAVOR Med 2016" << endl;
  // for(int i = 1; i < numL->GetNbinsX()+1; i++){printf("pT > %f, fake = %f\n",numL->GetBinLowEdge(i),numL->GetBinContent(i));}

  // num->GetYaxis()->SetRangeUser(0.0,1.0);
  // num->GetYaxis()->SetTitle("Efficiency of DeepJet Medium");
  // num->GetXaxis()->SetTitle("AK4 jet p_{T} [GeV]");
  // num->SetLineWidth(2);
  // num->SetMarkerStyle(20);
  // num->SetMarkerColor(kBlack);
  // num->SetLineColor(kBlack);
  // numC->SetLineWidth(2);
  // numC->SetMarkerStyle(20);
  // numC->SetMarkerColor(kBlue);
  // numC->SetLineColor(kBlue);
  // numL->SetLineWidth(2);
  // numL->SetMarkerStyle(20);
  // numL->SetMarkerColor(kRed);
  // numL->SetLineColor(kRed);
  // num->Draw();
  // numC->Draw("same");
  // numL->Draw("same");
  // leg->Draw();
  // c1->SaveAs("DeepFlavMed_2016.png");
  // c1->SaveAs("DeepFlavMed_2016.pdf");
  // c1->SaveAs("DeepFlavMed_2016.root");

  // 2017 Loose
  TFile *_file1 = TFile::Open("RDF_BprimeBtoTW_M-"+mass+"_NWALO_TuneCP5_13TeV-madgraph-pythia8_2017_DeepJetEff.root");
  num = (TH1D*)_file1->Get("BEffLoose_Nptbins_b");
  den = (TH1D*)_file1->Get("BEff_Dptbins_b");
  num->Divide(num,den,1.0,1.0,"B");

  cout << "B FLAVOR Loose 2017" << endl;
  for(int i = 1; i < num->GetNbinsX()+1; i++){printf("pT > %f, eff = %f\n",num->GetBinLowEdge(i),num->GetBinContent(i));}

  numC = (TH1D*)_file1->Get("BEffLoose_Nptbins_c");
  denC = (TH1D*)_file1->Get("BEff_Dptbins_c");
  numC->Divide(numC,denC,1.0,1.0,"B");

  cout << "C FLAVOR Loose 2017" << endl;
  for(int i = 1; i < numC->GetNbinsX()+1; i++){printf("pT > %f, fake = %f\n",numC->GetBinLowEdge(i),numC->GetBinContent(i));}

  numL = (TH1D*)_file1->Get("BEffLoose_Nptbins_udsg");
  denL = (TH1D*)_file1->Get("BEff_Dptbins_udsg");
  numL->Divide(numL,denL,1.0,1.0,"B");

  cout << "L FLAVOR Loose 2017" << endl;
  for(int i = 1; i < numL->GetNbinsX()+1; i++){printf("pT > %f, fake = %f\n",numL->GetBinLowEdge(i),numL->GetBinContent(i));}

  num->GetYaxis()->SetRangeUser(0.0,1.0);
  num->GetYaxis()->SetTitle("Efficiency of DeepJet Loose");
  num->GetXaxis()->SetTitle("AK4 jet p_{T} [GeV]");
  num->SetLineWidth(2);
  num->SetMarkerStyle(20);
  num->SetMarkerColor(kBlack);
  num->SetLineColor(kBlack);
  numC->SetLineWidth(2);
  numC->SetMarkerStyle(20);
  numC->SetMarkerColor(kBlue);
  numC->SetLineColor(kBlue);
  numL->SetLineWidth(2);
  numL->SetMarkerStyle(20);
  numL->SetMarkerColor(kRed);
  numL->SetLineColor(kRed);
  num->Draw();
  numC->Draw("same");
  numL->Draw("same");
  leg->Draw();
  c1->SaveAs("DeepFlavLoose_2017_"+mass+".png");
  c1->SaveAs("DeepFlavLoose_2017_"+mass+".pdf");
  c1->SaveAs("DeepFlavLoose_2017_"+mass+".root");

  //  // 2017 Medium
  // num = (TH1D*)_file1->Get("BEffMed_Nptbins_b");
  // den = (TH1D*)_file1->Get("BEff_Dptbins_b");
  // num->Divide(num,den,1.0,1.0,"B");

  // cout << "B FLAVOR Med 2017" << endl;
  // for(int i = 1; i < num->GetNbinsX()+1; i++){printf("pT > %f, eff = %f\n",num->GetBinLowEdge(i),num->GetBinContent(i));}

  // numC = (TH1D*)_file1->Get("BEffMed_Nptbins_c");
  // denC = (TH1D*)_file1->Get("BEff_Dptbins_c");
  // numC->Divide(numC,denC,1.0,1.0,"B");

  // cout << "C FLAVOR Med 2017" << endl;
  // for(int i = 1; i < numC->GetNbinsX()+1; i++){printf("pT > %f, fake = %f\n",numC->GetBinLowEdge(i),numC->GetBinContent(i));}

  // numL = (TH1D*)_file1->Get("BEffMed_Nptbins_udsg");
  // denL = (TH1D*)_file1->Get("BEff_Dptbins_udsg");
  // numL->Divide(numL,denL,1.0,1.0,"B");

  // cout << "L FLAVOR Med 2017" << endl;
  // for(int i = 1; i < numL->GetNbinsX()+1; i++){printf("pT > %f, fake = %f\n",numL->GetBinLowEdge(i),numL->GetBinContent(i));}

  // num->GetYaxis()->SetRangeUser(0.0,1.0);
  // num->GetYaxis()->SetTitle("Efficiency of DeepJet Medium");
  // num->GetXaxis()->SetTitle("AK4 jet p_{T} [GeV]");
  // num->SetLineWidth(2);
  // num->SetMarkerStyle(20);
  // num->SetMarkerColor(kBlack);
  // num->SetLineColor(kBlack);
  // numC->SetLineWidth(2);
  // numC->SetMarkerStyle(20);
  // numC->SetMarkerColor(kBlue);
  // numC->SetLineColor(kBlue);
  // numL->SetLineWidth(2);
  // numL->SetMarkerStyle(20);
  // numL->SetMarkerColor(kRed);
  // numL->SetLineColor(kRed);
  // num->Draw();
  // numC->Draw("same");
  // numL->Draw("same");
  // leg->Draw();
  // c1->SaveAs("DeepFlavMed_2017.png");
  // c1->SaveAs("DeepFlavMed_2017.pdf");
  // c1->SaveAs("DeepFlavMed_2017.root");

  // 2018 Loose
  TFile *_file2 = TFile::Open("RDF_BprimeBtoTW_M-"+mass+"_NWALO_TuneCP5_13TeV-madgraph-pythia8_2018_DeepJetEff.root");
  num = (TH1D*)_file2->Get("BEffLoose_Nptbins_b");
  den = (TH1D*)_file2->Get("BEff_Dptbins_b");
  num->Divide(num,den,1.0,1.0,"B");

  cout << "B FLAVOR Loose 2018" << endl;
  for(int i = 1; i < num->GetNbinsX()+1; i++){printf("pT > %f, eff = %f\n",num->GetBinLowEdge(i),num->GetBinContent(i));}

  numC = (TH1D*)_file2->Get("BEffLoose_Nptbins_c");
  denC = (TH1D*)_file2->Get("BEff_Dptbins_c");
  numC->Divide(numC,denC,1.0,1.0,"B");

  cout << "C FLAVOR Loose 2018" << endl;
  for(int i = 1; i < numC->GetNbinsX()+1; i++){printf("pT > %f, fake = %f\n",numC->GetBinLowEdge(i),numC->GetBinContent(i));}

  numL = (TH1D*)_file2->Get("BEffLoose_Nptbins_udsg");
  denL = (TH1D*)_file2->Get("BEff_Dptbins_udsg");
  numL->Divide(numL,denL,1.0,1.0,"B");

  cout << "L FLAVOR Loose 2018" << endl;
  for(int i = 1; i < numL->GetNbinsX()+1; i++){printf("pT > %f, fake = %f\n",numL->GetBinLowEdge(i),numL->GetBinContent(i));}

  num->GetYaxis()->SetRangeUser(0.0,1.0);
  num->GetYaxis()->SetTitle("Efficiency of DeepJet Loose");
  num->GetXaxis()->SetTitle("AK4 jet p_{T} [GeV]");
  num->SetLineWidth(2);
  num->SetMarkerStyle(20);
  num->SetMarkerColor(kBlack);
  num->SetLineColor(kBlack);
  numC->SetLineWidth(2);
  numC->SetMarkerStyle(20);
  numC->SetMarkerColor(kBlue);
  numC->SetLineColor(kBlue);
  numL->SetLineWidth(2);
  numL->SetMarkerStyle(20);
  numL->SetMarkerColor(kRed);
  numL->SetLineColor(kRed);
  num->Draw();
  numC->Draw("same");
  numL->Draw("same");
  leg->Draw();
  c1->SaveAs("DeepFlavLoose_2018_"+mass+".png");
  c1->SaveAs("DeepFlavLoose_2018_"+mass+".pdf");
  c1->SaveAs("DeepFlavLoose_2018_"+mass+".root");

  //  // 2018 Medium
  // num = (TH1D*)_file2->Get("BEffMed_Nptbins_b");
  // den = (TH1D*)_file2->Get("BEff_Dptbins_b");
  // num->Divide(num,den,1.0,1.0,"B");

  // cout << "B FLAVOR Med 2018" << endl;
  // for(int i = 1; i < num->GetNbinsX()+1; i++){printf("pT > %f, eff = %f\n",num->GetBinLowEdge(i),num->GetBinContent(i));}

  // numC = (TH1D*)_file2->Get("BEffMed_Nptbins_c");
  // denC = (TH1D*)_file2->Get("BEff_Dptbins_c");
  // numC->Divide(numC,denC,1.0,1.0,"B");

  // cout << "C FLAVOR Med 2018" << endl;
  // for(int i = 1; i < numC->GetNbinsX()+1; i++){printf("pT > %f, fake = %f\n",numC->GetBinLowEdge(i),numC->GetBinContent(i));}

  // numL = (TH1D*)_file2->Get("BEffMed_Nptbins_udsg");
  // denL = (TH1D*)_file2->Get("BEff_Dptbins_udsg");
  // numL->Divide(numL,denL,1.0,1.0,"B");

  // cout << "L FLAVOR Med 2018" << endl;
  // for(int i = 1; i < numL->GetNbinsX()+1; i++){printf("pT > %f, fake = %f\n",numL->GetBinLowEdge(i),numL->GetBinContent(i));}

  // num->GetYaxis()->SetRangeUser(0.0,1.0);
  // num->GetYaxis()->SetTitle("Efficiency of DeepJet Medium");
  // num->GetXaxis()->SetTitle("AK4 jet p_{T} [GeV]");
  // num->SetLineWidth(2);
  // num->SetMarkerStyle(20);
  // num->SetMarkerColor(kBlack);
  // num->SetLineColor(kBlack);
  // numC->SetLineWidth(2);
  // numC->SetMarkerStyle(20);
  // numC->SetMarkerColor(kBlue);
  // numC->SetLineColor(kBlue);
  // numL->SetLineWidth(2);
  // numL->SetMarkerStyle(20);
  // numL->SetMarkerColor(kRed);
  // numL->SetLineColor(kRed);
  // num->Draw();
  // numC->Draw("same");
  // numL->Draw("same");
  // leg->Draw();
  // c1->SaveAs("DeepFlavMed_2018.png");
  // c1->SaveAs("DeepFlavMed_2018.pdf");
  // c1->SaveAs("DeepFlavMed_2018.root");



}
