/*

  Macro to make DJR plots. 
  Should run on EDM root file with GEN information, using FWLite. 

  Written by: Josh Bendavid
  Modified slighlty by: Nadja Strobbe

 */


#include "TFile.h"
#include "TTree.h"
#include "TH1D.h"
#include "TCanvas.h"
#include "TCut.h"
#include "TROOT.h"
#include "TChain.h"
#include <vector>

double deltaPhiVal(double phi1, double phi2) {
 
  double dphival = phi2 - phi1;
  while (dphival>=M_PI) dphival -= 2.*M_PI;
  while (dphival<-M_PI) dphival += 2.*M_PI;
  
  return dphival;
  
}

double deltaRVal(double eta1,double phi1,double eta2,double phi2) {
 
  double detaval = eta2-eta1;
  double dphival = deltaPhiVal(phi1,phi2);
  return sqrt(detaval*detaval + dphival*dphival);
  
}

void makeplot(const char *name, TTree *tree, TCut weight, const char *drawstring, const char *xlabel, int nbins, double xlow, double xhigh) {
  
  //this is for NLO with FXFX merging
//   TCut mult0 = "LHEEvent.npNLO()==0";
//   TCut mult1 = "LHEEvent.npNLO()==1";
//   TCut mult2 = "LHEEvent.npNLO()==2";
  
  //this is for LO with MLM
  TCut mult0 = "GenEvent.nMEPartons()==0";
  TCut mult1 = "GenEvent.nMEPartons()==1";
  TCut mult2 = "GenEvent.nMEPartons()==2";

  //this is for LO with MLM (plotting partons after excluding non-matched partons in wbb/vbf type processes)
//   TCut mult0 = "GenEvent.nMEPartonsFiltered()==0";
//   TCut mult1 = "GenEvent.nMEPartonsFiltered()==1";
//   TCut mult2 = "GenEvent.nMEPartonsFiltered()==2";
  
  TH1D *hall = new TH1D(TString::Format("hall_%s",name),"",nbins,xlow,xhigh);
  TH1D *hmult0 = new TH1D(TString::Format("hmult0_%s",name),"",nbins,xlow,xhigh);
  TH1D *hmult1 = new TH1D(TString::Format("hmult1_%s",name),"",nbins,xlow,xhigh);
  TH1D *hmult2 = new TH1D(TString::Format("hmult2_%s",name),"",nbins,xlow,xhigh);

  hall->SetLineColor(kBlack);
  hmult0->SetLineColor(kBlue);
  hmult1->SetLineColor(kRed);
  hmult2->SetLineColor(kMagenta);
  
  tree->Draw(TString::Format("%s>>%s",drawstring,hall->GetName()),weight,"goff");
  tree->Draw(TString::Format("%s>>%s",drawstring,hmult0->GetName()),weight*mult0,"goff");
  tree->Draw(TString::Format("%s>>%s",drawstring,hmult1->GetName()),weight*mult1,"goff");
  tree->Draw(TString::Format("%s>>%s",drawstring,hmult2->GetName()),weight*mult2,"goff");
  
  hall->GetXaxis()->SetTitle(xlabel);
  
  TCanvas* c = new TCanvas(name,name);
  c->cd();
  hall->Draw("EHIST");
  hmult0->Draw("EHISTSAME");
  hmult1->Draw("EHISTSAME");
  hmult2->Draw("EHISTSAME");
  c->SaveAs(TString::Format("%s.pdf",name));
}

void plotdjr(TString filename, const char* outputbase) {
 
  TH1::SetDefaultSumw2();
  
  TChain *tree = new TChain("Events");
  tree->Add(filename);
  
  tree->SetAlias("LHEEvent","LHEEventProduct_source__GEN.obj");
  tree->SetAlias("GenEvent","GenEventInfoProduct_generator__GEN.obj");
  tree->SetAlias("GenParticles","recoGenParticles_genParticles__GEN.obj");
  tree->SetAlias("genJets","recoGenJets_ak4GenJets__GEN.obj");  
  
  tree->SetAlias("dr0","sqrt( (genJetsCleaned[0].eta()-promptPhotons[0].eta())^2 + atan2(sin(genJetsCleaned[0].phi()-promptPhotons[0].phi()),cos(genJetsCleaned[0].phi()-promptPhotons[0].phi()))^2 )");
  tree->SetAlias("dr1","sqrt( (genJetsCleaned[1].eta()-promptPhotons[0].eta())^2 + atan2(sin(genJetsCleaned[1].phi()-promptPhotons[0].phi()),cos(genJetsCleaned[1].phi()-promptPhotons[0].phi()))^2 )");
  tree->SetAlias("dr2","sqrt( (genJetsCleaned[2].eta()-promptPhotons[0].eta())^2 + atan2(sin(genJetsCleaned[2].phi()-promptPhotons[0].phi()),cos(genJetsCleaned[2].phi()-promptPhotons[0].phi()))^2 )");
  
  TCut weight = "GenEvent.weight()";
  int nbins = 50.;
  double djrmin = -0.5;
  double djrmax = 3.;
  
  
  makeplot(TString::Format("%s_%s",outputbase,"djr0"),tree,weight,"log10(GenEvent.DJRValues_[0])","DJR 0->1",nbins,djrmin,djrmax);
  makeplot(TString::Format("%s_%s",outputbase,"djr1"),tree,weight,"log10(GenEvent.DJRValues_[1])","DJR 1->2",nbins,djrmin,djrmax);
  makeplot(TString::Format("%s_%s",outputbase,"djr2"),tree,weight,"log10(GenEvent.DJRValues_[2])","DJR 2->3",nbins,djrmin,djrmax);
  return;  
}

