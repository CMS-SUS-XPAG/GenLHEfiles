//*****************************************************//
//Estimating the number of events for a given SMS model//
//*****************************************************//
#include "TText.h"
#include "TH2F.h"
#include "TCanvas.h"
#include "TBox.h"
#include <vector>
#include "tdrstyle.C"
#include "TLegend.h"
#include <fstream>
#include <iostream>
#include <vector>
#include "TLatex.h"
#include "TLine.h"
#include "TGraph.h"
#include "TLatex.h"



//---------------------------------Storage of cross sections-----------------------------------------//
std::vector<Int_t> Mglgl;
std::vector<Float_t> Xsecglgl;
std::vector<Float_t> Uncglgl;

std::vector<Int_t> Msqsq;
std::vector<Float_t> Xsecsqsq;
std::vector<Float_t> Uncsqsq;

std::vector<Int_t> Msbsb;
std::vector<Float_t> Xsecsbsb;
std::vector<Float_t> Uncsbsb;

std::vector<Int_t> Mchineu;
std::vector<Float_t> Xsecchineu;
std::vector<Float_t> Uncchineu;

std::vector<Int_t> Mglsq;
std::vector<Float_t> Xsecglsq;
std::vector<Float_t> Uncglsq;

Float_t Lref = 50; //in fb^-1

//------------------------------------------Functions------------------------------------------------//
void loadCrossSectionglgl(string);
Float_t crossSectionglgl(Int_t);
void loadCrossSectionsqsq(string);
Float_t crossSectionsqsq(Int_t);
void loadCrossSectionsbsb(string);
Float_t crossSectionsbsb(Int_t);
void loadCrossSectionchineu(string);
Float_t crossSectionchineu(Int_t);

Int_t T2qq();
Int_t T2qq2();
Int_t T6ttWW();
Int_t T6ttWW2();
Int_t T6bbllslepton();
Int_t T6qqWW();
Int_t T6qqWW2();
Int_t TChiWZ();
Int_t TChiSlepSnu();
Int_t TCoNLSP();
Int_t T1TTTTExtended();
Int_t T1TTTTExtended_v2();
Int_t T1TTBB();
Int_t T1TTBB_v2();
Int_t T1BBBB();
Int_t T1BBBB();
Int_t T1qqqq();
Int_t T1qqqq_v2();
Int_t T5VV();
Int_t T5ZZ();
Int_t T5VV_v2();
Int_t T5qqqqWW_v1();
Int_t T5qqqqWW_v2();
Int_t T5qqqqWZ();
Int_t T5tttt_MGLU1500();
Int_t T5tttt_MGLU1500_v2();
Int_t T5tttt_DM175();
Int_t T5tttt_DM175_v2();
Int_t T5ttcc();
Int_t T5ttcc_v2();
Int_t T7btW();
Int_t T5Zg();
Int_t T5Wg();
Int_t T5Wg_v2();
Int_t T5gg();
Int_t T5gg_v2();
Int_t T6gg();
Int_t T6gg_v2();
Int_t T2bb();
Int_t T2tb();
Int_t T2bW();
Int_t T6ttWW();
Int_t T2TT();
//Int_t T2TTstrip();

void go();
//----------------------------------------End Functions----------------------------------------------//



void go() {

  setTDRStyle();

  loadCrossSectionglgl("glu-glu.dat");
  loadCrossSectionsqsq("sq-sq.dat");
  loadCrossSectionsbsb("stop-stop.dat");
  loadCrossSectionchineu("char-neu.dat");

  //##########Gluino-Gluino production###################//

  Int_t nT1TTTTExtended = T1TTTTExtended();
  Int_t nT1TTTTExtended = T1TTTTExtended_v2();
  Int_t nT1TTBB = T1TTBB();
  Int_t nT1TTBB = T1TTBB_v2();
  
  Int_t nT1BBBB = T1BBBB();
  Int_t nT1BBBB = T1BBBB_v2();
  
  Int_t nT1qqqq = T1qqqq();
  Int_t nT1qqqq = T1qqqq_v2();
  
  Int_t nT5VV = T5VV();
  Int_t nT5VV = T5VV_v2();
  
  Int_t nT5ZZ = T5ZZ();
  
    
  //Int_t nT5qqqqWW = T5qqqqWW_v1();
  Int_t nT5qqqqWW = T5qqqqWW_v2();
  
  Int_t nT5qqqqWZ = T5qqqqWZ();
  
  Int_t nT5tttt_MGLU1500 = T5tttt_MGLU1500();
  //Int_t nT5tttt_MGLU1500 = T5tttt_MGLU1500_v2();
  
  Int_t nT5tttt_DM175 = T5tttt_DM175();
  //Int_t nT5tttt_DM175 = T5tttt_DM175()_v2;
  
  Int_t nT5ttcc = T5ttcc();
  //Int_t nT5ttcc = T5ttcc_v2();
  
  Int_t nT5Wg = T5Wg();
  //Int_t nT5Wg = T5Wg_v2();
  
  Int_t nT5gg = T5gg();
  //Int_t nT5gg = T5gg_v2();

  Int_t nT5Zg = T5Zg();

  //##########Squark-Squark production###################//
  Int_t nT2qq = T2qq();
  Int_t nT2qq2 = T2qq2();

  Int_t nT6qqWW = T6qqWW();
  Int_t nT6qqWW2 = T6qqWW2();
  
  Int_t nT6gg = T6gg();
  //Int_t nT6gg = T6gg_v2();
  

  //##########Third generation production###################//
  Int_t nT2bb = T2bb();
  
  Int_t nT2tb = T2tb();
  
  Int_t nT2bW = T2bW();

  Int_t nT2TT = T2TT();
    
  Int_t nT2TTstrip = T2TTstrip();

  Int_t nT6ttWW = T6ttWW();
  
  Int_t nT6ttWW2 = T6ttWW2();

  Int_t nT6bbllslepton = T6bbllslepton();

  //##########Electroweak production###################//
  Int_t nTChiWZ = TChiWZ();

  Int_t nTChiSlepSnu = TChiSlepSnu();

  Int_t nTConNLSP = TCoNLSP();

}



Int_t T2qq() {

  bool considerXsec = true;

  Int_t msqMin = 300;
  Int_t msqMax = 1600;
  Int_t mLSPMax = 1100;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T2qqc", "T2qqc");
  TH2F *h = new TH2F("T2qqh", "", msqMax/step, 0, msqMax, msqMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(sq) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T2qq");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);

  for(Int_t m_sq = msqMin; m_sq < msqMax; m_sq += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_sq - 100 && m_LSP < mLSPMax; m_LSP += 2*step) {
      TBox *box = new TBox(m_sq, m_LSP, m_sq+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionsqsq(m_sq);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
      if(considerXsec && NEvents > 50000) std::cout << m_sq << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_sq << " " << m_LSP << " 50000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");

  for(Int_t m_sq = msqMin; m_sq < msqMax; m_sq += 2*step) {
    for(Int_t m_LSP = m_sq - 100; m_LSP < m_sq && m_LSP > 0 && m_LSP < mLSPMax; m_LSP += 2*step) {
      TBox *box = new TBox(m_sq, m_LSP, m_sq+2*step, m_LSP+2*step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionsqsq(m_sq);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
      if(considerXsec && NEvents > 100000) std::cout << m_sq << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_sq << " " << m_LSP << " 100000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 100K", "F");
 

 
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  can->SaveAs("T2qq.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

Int_t T2qq2() {

  bool considerXsec = true;

  Int_t msqMin = 200;
  Int_t msqMax = 1600;
  Int_t mLSPMax = 1100;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T2qqc", "T2qqc");
  TH2F *h = new TH2F("T2qqh", "", msqMax/step, 0, msqMax, msqMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(sq) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T2qq");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);

  for(Int_t m_sq = msqMin; m_sq < msqMax; m_sq += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_sq - 100 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if(m_sq <= 700 && m_LSP <= 200) continue;
      TBox *box = new TBox(m_sq, m_LSP, m_sq+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionsqsq(m_sq);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  for(Int_t m_sq = msqMin; m_sq < msqMax; m_sq += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_sq - 100 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if(!(m_sq <= 700 && m_LSP <= 200)) continue;
      TBox *box = new TBox(m_sq, m_LSP, m_sq+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionsqsq(m_sq)/8.;
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");

  for(Int_t m_sq = msqMin; m_sq < msqMax; m_sq += 2*step) {
    for(Int_t m_LSP = m_sq - 100; m_LSP < m_sq && m_LSP > 0 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if(m_sq <= 700 && m_LSP <= 200) continue;
      TBox *box = new TBox(m_sq, m_LSP, m_sq+2*step, m_LSP+2*step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionsqsq(m_sq);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  for(Int_t m_sq = msqMin; m_sq < msqMax; m_sq += 2*step) {
    for(Int_t m_LSP = m_sq - 100; m_LSP < m_sq && m_LSP > 0 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if(!(m_sq <= 700 && m_LSP <= 200)) continue;
      TBox *box = new TBox(m_sq, m_LSP, m_sq+2*step, m_LSP+2*step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionsqsq(m_sq/8.);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 100K", "F");
 

 
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  can->SaveAs("T2qq2.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}



Int_t T6ttWW() {

  Float_t Lref = 25; //in fb^-1
  bool considerXsec = true;

  Int_t mgluMin = 300;
  Int_t mgluMax = 1000;
  Int_t mLSPMax = 900;
  Int_t step = 25;

  TCanvas *can = new TCanvas("T6ttWWc", "T6ttWWc");
  TH2F *h = new TH2F("T6ttWWc", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 1200);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(sbottom) [GeV]");
  h->GetYaxis()->SetTitle("M(Chargino) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T6ttWW M(LSP)=50 GeV");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 75; m_LSP < 150; m_LSP += step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionsbsb(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
      if(considerXsec && NEvents > 100000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 100000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 100K", "F");
  
  
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = m_glu-100; m_LSP < m_glu && m_LSP < mLSPMax ; m_LSP += step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionsbsb(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
      if(considerXsec && NEvents > 100000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 100000 " << std::endl;
    }
  }

  for(Int_t m_glu = 325; m_glu < mgluMax; m_glu += 2*step) {
    Int_t m_LSP = m_glu-125;
    TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
    box->SetFillColor(kGreen-7);
    boxes.push_back(box);
    float xsec = crossSectionsbsb(m_glu);
    Float_t NEvents = xsec * Lref * 1000;
    if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
    else totalNumberOfEvents += 100000;
    if(considerXsec && NEvents > 100000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
    else                                 std::cout << m_glu << " " << m_LSP << " 100000 " << std::endl;
  }

  


  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 150; m_LSP < m_glu-100 && m_LSP < mLSPMax ; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionsbsb(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
      if(considerXsec && NEvents > 100000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 100000 " << std::endl;
    }
  }
   
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 100K", "F");


  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(100, 650, textNP);
  TText *NE = new TText(100, 550, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  can->SaveAs("T6ttWW.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;


} 

Int_t T6ttWW2() {

  Float_t Lref = 25; //in fb^-1
  bool considerXsec = true;


  Int_t mgluMin = 300;
  Int_t mgluMax = 1000;
  Int_t mLSPMax = 900;
  Int_t step = 25;

  TCanvas *can = new TCanvas("T6ttWW2c", "T6ttWW2c");
  TH2F *h = new TH2F("T6ttWW2c", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 1200);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(sbottom) [GeV]");
  h->GetYaxis()->SetTitle("M(Chargino) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T6ttWW M(Chargino)-M(LSP)=20 GeV");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
  
 for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = m_glu-100; m_LSP < m_glu-25 && m_LSP < mLSPMax ; m_LSP += step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionsbsb(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 100K", "F");

  for(Int_t m_glu = 325; m_glu < mgluMax; m_glu += 2*step) {
    Int_t m_LSP = m_glu-125;
    TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
    box->SetFillColor(kGreen-7);
    boxes.push_back(box);
    float xsec = crossSectionsbsb(m_glu);
    Float_t NEvents = xsec * Lref * 1000;
    if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
    else totalNumberOfEvents += 100000;
  }
  


  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-100 && m_LSP < mLSPMax ; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionsbsb(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
   
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 100K", "F");

 
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(100, 650, textNP);
  TText *NE = new TText(100, 550, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  can->SaveAs("T6ttWW2.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

} 

Int_t T6bbllslepton() {

  Float_t Lref = 25; //in fb^-1
  bool considerXsec = true;


  Int_t mgluMin = 400;
  Int_t mgluMax = 900;
  Int_t mLSPMax = 900;
  Int_t step = 25;

  TCanvas *can = new TCanvas("T6bbllsleptonc", "T6bbllsleptoncc");
  TH2F *h = new TH2F("T6bbllslepton", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 1200);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(sbottom) [GeV]");
  h->GetYaxis()->SetTitle("M(Chi20) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T6bbllslepton");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
  
 for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < 300 && m_LSP < mLSPMax ; m_LSP += step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionsbsb(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 50K", "F");

  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 300; m_LSP < m_glu && m_LSP < mLSPMax ; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionsbsb(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");

 
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(100, 650, textNP);
  TText *NE = new TText(100, 550, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  can->SaveAs("T6bbllslepton.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

} 

Int_t T6qqWW() {

  Float_t Lref = 25; //in fb^-1
  bool considerXsec = false;

  Int_t mgluMin = 300;
  Int_t mgluMax = 1500;
  Int_t mLSPMax = 900;
  Int_t step = 25;

  TCanvas *can = new TCanvas("T6qqWWc", "T6qqWWc");
  TH2F *h = new TH2F("T6qqWWc", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 1600);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(squark) [GeV]");
  h->GetYaxis()->SetTitle("M(Chargino) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T6qqWW M(LSP)=50 GeV");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 75; m_LSP < 150; m_LSP += step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionsbsb(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 20000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 20000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 20K", "F");
  
  
 for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = m_glu-100; m_LSP < m_glu && m_LSP < mLSPMax ; m_LSP += step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionsbsb(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 20000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 20000;
    }
  }

  for(Int_t m_glu = 325; m_glu < mgluMax; m_glu += 2*step) {
    Int_t m_LSP = m_glu-125;
    if(m_LSP>=900) continue;
    TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
    box->SetFillColor(kGreen-7);
    boxes.push_back(box);
    float xsec = crossSectionsbsb(m_glu);
    Float_t NEvents = xsec * Lref * 1000;
    if(considerXsec && NEvents > 20000) totalNumberOfEvents += NEvents;   
    else totalNumberOfEvents += 20000;
  }

  


  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 150; m_LSP < m_glu-100 && m_LSP < mLSPMax ; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionsbsb(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 20000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 20000;
    }
  }
   
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 20K", "F");


  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(100, 950, textNP);
  TText *NE = new TText(100, 850, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  can->SaveAs("T6qqWW.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;


} 

Int_t T6qqWW2() {

  Float_t Lref = 25; //in fb^-1
  bool considerXsec = false;

  setTDRStyle();
  char name[] = "sq-sq.dat";

  Int_t mgluMin = 300;
  Int_t mgluMax = 1500;
  Int_t mLSPMax = 900;
  Int_t step = 25;

  TCanvas *can = new TCanvas("T6qqWWc", "T6qqWWc");
  TH2F *h = new TH2F("T6qqWW", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 1600);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(squark) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T6qqWW M(Chargino) - M(LSP) = 20 GeV");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
  
 for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-250 && m_LSP < mLSPMax ; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionsqsq(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 20000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 20000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 20K", "F");


  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = m_glu-250; m_LSP < m_glu-25 && m_LSP < mLSPMax ; m_LSP += step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionsqsq(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 20000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 20000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 20K", "F");


 
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(100, 950, textNP);
  TText *NE = new TText(100, 850, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  can->SaveAs("T6qqWW2.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}



Int_t TChiWZ() {

  Float_t Lref = 25; //in fb^-1
  bool considerXsec = true;

  Int_t mgluMin = 100;
  Int_t mgluMax = 600;
  Int_t mLSPMax = 400;
  Int_t step = 25;

  TCanvas *can = new TCanvas("TChiWZc", "TChiWZc");
  TH2F *h = new TH2F("TChiWZ", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 1200);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(chargino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "TChiWZ");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
  
 for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu && m_LSP < mLSPMax ; m_LSP += step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionchineu(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 50K", "F");

  // extra DM=10 region
  for(Int_t m_glu = mgluMin; m_glu < mgluMax && m_glu-10 < mLSPMax; m_glu += step) {
    TBox *box = new TBox(m_glu, m_glu-10, m_glu+step, m_glu-10+step);
    box->SetFillColor(kGreen-7);
    boxes.push_back(box);
    float xsec = crossSectionchineu(m_glu);
    Float_t NEvents = xsec * Lref * 1000;
    if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
    else totalNumberOfEvents += 50000;
  }

 
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(100, 650, textNP);
  TText *NE = new TText(100, 550, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  can->SaveAs("TChiWZ.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

} 

Int_t TChiSlepSnu() {

  Float_t Lref = 25; //in fb^-1
  bool considerXsec = true;

  Int_t mgluMin = 100;
  Int_t mgluMax = 900;
  Int_t mLSPMax = 700;
  Int_t step = 25;

  TCanvas *can = new TCanvas("TChiSlepSnuc", "TChiSlepSnuc");
  TH2F *h = new TH2F("TChiSlepSnu", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 1200);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(chargino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "TChiSlepSnu");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
  
 for(Int_t m_glu = mgluMin; m_glu < 200; m_glu += step) {
    for(Int_t m_LSP = m_glu-100; m_LSP < m_glu && m_LSP < mLSPMax ; m_LSP += step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionchineu(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 20000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 20000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 20K", "F");


  for(Int_t m_glu = 125; m_glu < 200; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-100 && m_LSP < mLSPMax ; m_LSP += step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionchineu(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 20000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 20000;
    }
  }

  for(Int_t m_glu = 200; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = m_glu-175; m_LSP < m_glu && m_LSP < mLSPMax ; m_LSP += step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionchineu(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 20000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 20000;
    }
  }

  for(Int_t m_glu = 200; m_glu < mgluMax; m_glu += 2*step) {
    Int_t m_LSP = m_glu-200; 
    TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
    box->SetFillColor(kGreen-7);
    boxes.push_back(box);
    float xsec = crossSectionchineu(m_glu);
    Float_t NEvents = xsec * Lref * 1000;
    if(considerXsec && NEvents > 20000) totalNumberOfEvents += NEvents;   
    else totalNumberOfEvents += 20000;
  }

  for(Int_t m_glu = 225; m_glu < mgluMax-50; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-175 && m_LSP < mLSPMax ; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionchineu(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 20000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 20000;
    }
  }

  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 20K", "F");

 
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(100, 650, textNP);
  TText *NE = new TText(100, 550, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  can->SaveAs("TSlepSnu.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

} 

Int_t TCoNLSP() {

  Float_t Lref = 25; //in fb^-1
  bool considerXsec = false;


  Int_t mgluMin = 700;
  Int_t mgluMax = 2000;
  Int_t mLSPMax = 3000;
  Int_t step = 25;

  TCanvas *can = new TCanvas("TCoNLSPc", "TCoNLSPc");
  TH2F *h = new TH2F("TCoNLSP", "", mgluMax/step, mgluMin, mgluMax, mgluMax/step, 2000, 5000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(chargino) [GeV]");
  h->GetYaxis()->SetTitle("M(gluino) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "TCoNLSP");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
  
  for(Int_t m_glu = mgluMin; m_glu < 1400; m_glu += step) {
    for(Int_t m_LSP = 2000; m_LSP < mLSPMax ; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+2*step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionchineu(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 5000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 5000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x50 GeV^{2}, 5K", "F");


  for(Int_t m_glu = 1400; m_glu < 2000; m_glu += 4*step) {
    for(Int_t m_LSP = 2000; m_LSP < mLSPMax ; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+2*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionchineu(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 5000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 5000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x50 GeV^{2}, 5K", "F");


 
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(900, 3650, textNP);
  TText *NE = new TText(900, 3550, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  can->SaveAs("TCoNLSP.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

} 



Int_t T1TTTTExtended() {

  bool considerXsec = true;


  Int_t mgluMin = 600;
  Int_t mgluMax = 2050;
  Int_t mLSPMax = 1500;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T1TTTTc", "T1TTTTc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T1TTTTh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.42, 0.92, "T1tttt");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


 //Diagonal low
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-200 && m_LSP < 1200; m_LSP += step) {
      if( !(m_glu % 50 == 0) && m_LSP < m_glu-425) continue; 
      if( (m_glu % 50 == 0) && m_LSP < m_glu-400) continue; 
      //if( m_LSP < m_glu-375) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
      if(considerXsec && NEvents > 150000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 150000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 150K", "F");

 //Diagonal high
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 1200; m_LSP < m_glu-200 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if( !(m_glu % 50 == 0) && m_LSP < m_glu-425) continue; 
      if( (m_glu % 50 == 0) && m_LSP < m_glu-400) continue; 
      //if( m_LSP < m_glu-375) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kGreen-3);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
      if(considerXsec && NEvents > 150000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 150000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 150K", "F");

  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < 1000; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < 200; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
      if(considerXsec && NEvents > 100000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 100000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 100K", "F");


  //Other regions; mglu < 1600
  for(Int_t m_glu = mgluMin; m_glu < 1600; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-400 && m_LSP < mLSPMax; m_LSP += 2*step) {
      //if( m_LSP < m_glu-375) continue; 
      if(m_glu < 1000 && m_LSP < 200) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
      if(considerXsec && NEvents > 100000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 100000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 100K", "F");

  //Other regions; mglu >= 1600
  for(Int_t m_glu = 1600; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-400 && m_LSP < mLSPMax; m_LSP += 2*step) {
      //if( m_LSP < m_glu-375) continue; 
      if(m_glu < 1000 && m_LSP < 200) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kViolet);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
      if(considerXsec && NEvents > 50000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 50000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");

 
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  // Add lines showing the diagonals
  can->Update();
  TLine line1 = TLine(0+175*2,0,2050,2050-175*2);
  line1.SetLineColor(kGray+2);
  line1.SetLineWidth(2);
  line1.SetLineStyle(2);
  line1.Draw("same");
  TLatex *line1t = new TLatex(340, 30, "m_{#tilde{g}} - m_{LSP} = 2*m_{t}");
  line1t->SetTextSize(0.02);
  line1t->SetTextAngle(45);
  line1t->Draw();

  TLine line2 = TLine(0+85*2,0,2050,2050-85*2);
  line2.SetLineColor(kGray+2);
  line2.SetLineWidth(2);
  line2.SetLineStyle(2);
  line2.Draw("same");
  TLatex *line2t = new TLatex(150, 30, "m_{#tilde{g}} - m_{LSP} = 2*(m_{W} + m_{b})");
  line2t->SetTextSize(0.02);
  line2t->SetTextAngle(45);
  line2t->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();


  can->SaveAs("T1tttt.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

// ============================================================================

Int_t T1TTTTExtended_v2() {

  bool considerXsec = true;


  Int_t mgluMin = 600;
  Int_t mgluMax = 2050;
  Int_t mLSPMax = 1500;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T1TTTTc", "T1TTTTc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T1TTTTh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.55, 0.4, 0.92, "T1tttt");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


 //Diagonal low
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-200 && m_LSP < 1200; m_LSP += step) {
      if( !(m_glu % 50 == 0) && m_LSP < m_glu-425) continue; 
      if( (m_glu % 50 == 0) && m_LSP < m_glu-400) continue; 
      //if( m_LSP < m_glu-375) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 150K", "F");

 //Diagonal high
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 1200; m_LSP < m_glu-200 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if( !(m_glu % 50 == 0) && m_LSP < m_glu-425) continue; 
      if( (m_glu % 50 == 0) && m_LSP < m_glu-400) continue; 
      //if( m_LSP < m_glu-375) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kGreen-3);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 150K", "F");

  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < 1000; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < 200; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 100K", "F");


  //Other regions; mglu < 1600, mLSP < 400
  for(Int_t m_glu = mgluMin; m_glu < 1600; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-400 && m_LSP < 400; m_LSP += 4*step) {
      //if( m_LSP < m_glu-375) continue; 
      if(m_glu < 1000 && m_LSP < 200) continue;
      if( m_glu - m_LSP < 500) continue; 
      //if( !(m_glu % 50 == 0) && m_LSP < m_glu-400) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+4*step);
      box->SetFillColor(kBlue-4);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x100 GeV^{2}, 100K", "F");

  //Other regions; mglu < 1600, mlSP > 400
  for(Int_t m_glu = mgluMin; m_glu < 1600; m_glu += 2*step) {
    for(Int_t m_LSP = 400; m_LSP < m_glu-400 && m_LSP < mLSPMax; m_LSP += 2*step) {
      //if( m_LSP < m_glu-375) continue; 
      if(m_glu < 1000 && m_LSP < 200) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  //Other regions; mglu < 1600, mlSP > 400, remainders
  {
    TBox *box = new TBox(650, 200, 650+2*step, 200+2*step);
    box->SetFillColor(kBlue-7);
    boxes.push_back(box);
    float xsec = crossSectionglgl(650);
    Float_t NEvents = xsec * Lref * 1000;
    if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
    else totalNumberOfEvents += 100000;
  }
  {
    TBox *box = new TBox(750, 300, 750+2*step, 300+2*step);
    box->SetFillColor(kBlue-7);
    boxes.push_back(box);
    float xsec = crossSectionglgl(750);
    Float_t NEvents = xsec * Lref * 1000;
    if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
    else totalNumberOfEvents += 100000;
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 100K", "F");

  //Other regions; mglu >= 1600, mLSP < 400
  for(Int_t m_glu = 1600; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-400 && m_LSP < 400; m_LSP += 4*step) {
      //if( m_LSP < m_glu-375) continue; 
      if(m_glu < 1000 && m_LSP < 200) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+4*step);
      box->SetFillColor(kViolet);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x100 GeV^{2}, 50K", "F");
 
  //Other regions; mglu >= 1600, mLSP > 400
  for(Int_t m_glu = 1600; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 400; m_LSP < m_glu-400 && m_LSP < mLSPMax; m_LSP += 2*step) {
      //if( m_LSP < m_glu-375) continue; 
      if(m_glu < 1000 && m_LSP < 200) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kViolet-4);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");
 
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  // Add lines showing the diagonals
  can->Update();
  TLine line1 = TLine(0+175*2,0,2050,2050-175*2);
  line1.SetLineColor(kGray+2);
  line1.SetLineWidth(2);
  line1.SetLineStyle(2);
  line1.Draw("same");
  TLatex *line1t = new TLatex(340, 30, "m_{#tilde{g}} - m_{LSP} = 2*m_{t}");
  line1t->SetTextSize(0.02);
  line1t->SetTextAngle(45);
  line1t->Draw();

  TLine line2 = TLine(0+85*2,0,2050,2050-85*2);
  line2.SetLineColor(kGray+2);
  line2.SetLineWidth(2);
  line2.SetLineStyle(2);
  line2.Draw("same");
  TLatex *line2t = new TLatex(150, 30, "m_{#tilde{g}} - m_{LSP} = 2*(m_{W} + m_{b})");
  line2t->SetTextSize(0.02);
  line2t->SetTextAngle(45);
  line2t->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 930, textNP);
  TText *NE = new TText(210, 830, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  can->SaveAs("T1tttt_v2.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

// ============================================================================

Int_t T1BBBB() {

  bool considerXsec = true;


  Int_t mgluMin = 600;
  Int_t mgluMax = 2050;
  Int_t mLSPMax = 1500;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T1BBBBc", "T1BBBBc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T1BBBBh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.42, 0.92, "T1bbbb");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


 //Diagonal low
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu && m_LSP < 1200; m_LSP += step) {
      if( !(m_glu % 50 == 0) && m_LSP < m_glu-225) continue; 
      if( (m_glu % 50 == 0) && m_LSP < m_glu-200) continue; 
      //if( m_LSP < m_glu-375) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
      if(considerXsec && NEvents > 150000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 150000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 150K", "F");

 //Diagonal high
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 1200; m_LSP < m_glu && m_LSP < mLSPMax; m_LSP += 2*step) {
      if( !(m_glu % 50 == 0) && m_LSP < m_glu-225) continue; 
      if( (m_glu % 50 == 0) && m_LSP < m_glu-200) continue; 
      //if( m_LSP < m_glu-375) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kGreen-3);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
      if(considerXsec && NEvents > 150000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 150000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 150K", "F");

  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < 1300; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < 400; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
      if(considerXsec && NEvents > 50000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 50000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");


  //Other regions
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-200 && m_LSP < mLSPMax; m_LSP += 2*step) {
      //if( m_LSP < m_glu-375) continue; 
      if(m_glu < 1300 && m_LSP < 400) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
      if(considerXsec && NEvents > 50000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 50000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");

  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  


  can->SaveAs("T1bbbb.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

// ============================================================================

Int_t T1BBBB_v2() {

  bool considerXsec = true;


  Int_t mgluMin = 600;
  Int_t mgluMax = 2050;
  Int_t mLSPMax = 1500;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T1BBBBc", "T1BBBBc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T1BBBBh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.42, 0.92, "T1bbbb");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


 //Diagonal low
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu && m_LSP < 1200; m_LSP += step) {
      if( !(m_glu % 50 == 0) && m_LSP < m_glu-225) continue; 
      if( (m_glu % 50 == 0) && m_LSP < m_glu-200) continue; 
      //if( m_LSP < m_glu-375) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 100K", "F");

 //Diagonal high
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 1200; m_LSP < m_glu && m_LSP < mLSPMax; m_LSP += 2*step) {
      if( !(m_glu % 50 == 0) && m_LSP < m_glu-225) continue; 
      if( (m_glu % 50 == 0) && m_LSP < m_glu-200) continue; 
      //if( m_LSP < m_glu-375) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kGreen-3);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 100K", "F");

  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < 1300; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < 400; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");


  //Other regions, mLSP < 400
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-200 && m_LSP < 400; m_LSP += 4*step) {
      //if( m_LSP < m_glu-375) continue; 
      if(m_glu < 1300 && m_LSP < 400) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+4*step);
      box->SetFillColor(kBlue-4);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x100 GeV^{2}, 50K", "F");

  //Other regions, mLSP > 400
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 400; m_LSP < m_glu-200 && m_LSP < mLSPMax; m_LSP += 2*step) {
      //if( m_LSP < m_glu-375) continue; 
      if(m_glu < 1300 && m_LSP < 400) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");

  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  can->SaveAs("T1bbbb_v2.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

// ============================================================================

Int_t T1TTBB() {

  bool considerXsec = true;


  Int_t mgluMin = 600;
  Int_t mgluMax = 2050;
  Int_t mLSPMax = 1500;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T1TTBBc", "T1TTBBc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T1TTBBh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.42, 0.92, "T1ttbb");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


 //Diagonal low
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-200 && m_LSP < 1200; m_LSP += step) {
      if( !(m_glu % 50 == 0) && m_LSP < m_glu-425) continue; 
      if( (m_glu % 50 == 0) && m_LSP < m_glu-400) continue; 
      if( m_LSP < m_glu-425) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
      if(considerXsec && NEvents > 150000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 150000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 150K", "F");

 //Diagonal high
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 1200; m_LSP < m_glu-200 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if( !(m_glu % 50 == 0) && m_LSP < m_glu-425) continue; 
      if( (m_glu % 50 == 0) && m_LSP < m_glu-400) continue; 
      //if( m_LSP < m_glu-375) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kGreen-3);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
      if(considerXsec && NEvents > 150000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 150000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 150K", "F");

  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < 1300; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < 400 && m_glu - m_LSP > 400; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
      if(considerXsec && NEvents > 50000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 50000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");


  //Other regions
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-400 && m_LSP < mLSPMax; m_LSP += 2*step) {
      //if( m_LSP < m_glu-375) continue; 
      if(m_glu < 1300 && m_LSP < 400 && m_glu - m_LSP > 400) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
      if(considerXsec && NEvents > 50000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 50000 " << std::endl;
    }
  }
  //Other regions; remainders
  {
    TBox *box = new TBox(650, 200, 650+2*step, 200+2*step);
    box->SetFillColor(kBlue-7);
    boxes.push_back(box);
    float xsec = crossSectionglgl(650);
    Float_t NEvents = xsec * Lref * 1000;
    if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
    else totalNumberOfEvents += 50000;
    if(considerXsec && NEvents > 50000) std::cout << "650" << " " << "200" << " " << NEvents << std::endl;
    else                                 std::cout << "650" << " " << "200" << " 50000 " << std::endl;

  }
  {
    TBox *box = new TBox(750, 300, 750+2*step, 300+2*step);
    box->SetFillColor(kBlue-7);
    boxes.push_back(box);
    float xsec = crossSectionglgl(750);
    Float_t NEvents = xsec * Lref * 1000;
    if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
    else totalNumberOfEvents += 50000;
    if(considerXsec && NEvents > 50000) std::cout << "650" << " " << "200" << " " << NEvents << std::endl;
    else                                 std::cout << "650" << " " << "200" << " 50000 " << std::endl;
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");

 
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  // Add lines showing the diagonals
  can->Update();
  TLine line1 = TLine(0+175*2,0,2050,2050-175*2);
  line1.SetLineColor(kGray+2);
  line1.SetLineWidth(2);
  line1.SetLineStyle(2);
  line1.Draw("same");
  TLatex *line1t = new TLatex(340, 30, "m_{#tilde{g}} - m_{LSP} = 2*m_{t}");
  line1t->SetTextSize(0.02);
  line1t->SetTextAngle(45);
  line1t->Draw();

  TLine line2 = TLine(0+85*2,0,2050,2050-85*2);
  line2.SetLineColor(kGray+2);
  line2.SetLineWidth(2);
  line2.SetLineStyle(2);
  line2.Draw("same");
  TLatex *line2t = new TLatex(150, 30, "m_{#tilde{g}} - m_{LSP} = 2*(m_{W} + m_{b})");
  line2t->SetTextSize(0.02);
  line2t->SetTextAngle(45);
  line2t->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  can->SaveAs("T1ttbb.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

// ============================================================================

Int_t T1TTBB_v2() {

  bool considerXsec = true;


  Int_t mgluMin = 600;
  Int_t mgluMax = 2050;
  Int_t mLSPMax = 1500;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T1TTBBc", "T1TTBBc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T1TTBBh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.42, 0.92, "T1ttbb");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


 //Diagonal low
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-200 && m_LSP < 1200; m_LSP += step) {
      if( !(m_glu % 50 == 0) && m_LSP < m_glu-425) continue; 
      if( (m_glu % 50 == 0) && m_LSP < m_glu-400) continue; 
      if( m_LSP < m_glu-425) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 150K", "F");

 //Diagonal high
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 1200; m_LSP < m_glu-200 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if( !(m_glu % 50 == 0) && m_LSP < m_glu-425) continue; 
      if( (m_glu % 50 == 0) && m_LSP < m_glu-400) continue; 
      //if( m_LSP < m_glu-375) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kGreen-3);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 150K", "F");

  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < 1300; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < 400 && m_glu - m_LSP > 400; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");


  //Other regions, mLSP < 400
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-400 && m_LSP < 400; m_LSP += 4*step) {
      //if( m_LSP < m_glu-375) continue; 
      if(m_glu < 1300 && m_LSP < 400 && m_glu - m_LSP > 400) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+4*step);
      box->SetFillColor(kBlue-4);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x100 GeV^{2}, 50K", "F");
  //Other regions, mLSP > 400
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 400; m_LSP < m_glu-400 && m_LSP < mLSPMax; m_LSP += 2*step) {
      //if( m_LSP < m_glu-375) continue; 
      if(m_glu < 1300 && m_LSP < 400 && m_glu - m_LSP > 400) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  //Other regions; remainders
  {
    TBox *box = new TBox(650, 200, 650+2*step, 200+2*step);
    box->SetFillColor(kBlue-7);
    boxes.push_back(box);
    float xsec = crossSectionglgl(650);
    Float_t NEvents = xsec * Lref * 1000;
    if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
    else totalNumberOfEvents += 50000;
  }
  {
    TBox *box = new TBox(750, 300, 750+2*step, 300+2*step);
    box->SetFillColor(kBlue-7);
    boxes.push_back(box);
    float xsec = crossSectionglgl(750);
    Float_t NEvents = xsec * Lref * 1000;
    if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
    else totalNumberOfEvents += 50000;
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");

 
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  // Add lines showing the diagonals
  can->Update();
  TLine line1 = TLine(0+175*2,0,2050,2050-175*2);
  line1.SetLineColor(kGray+2);
  line1.SetLineWidth(2);
  line1.SetLineStyle(2);
  line1.Draw("same");
  TLatex *line1t = new TLatex(340, 30, "m_{#tilde{g}} - m_{LSP} = 2*m_{t}");
  line1t->SetTextSize(0.02);
  line1t->SetTextAngle(45);
  line1t->Draw();

  TLine line2 = TLine(0+85*2,0,2050,2050-85*2);
  line2.SetLineColor(kGray+2);
  line2.SetLineWidth(2);
  line2.SetLineStyle(2);
  line2.Draw("same");
  TLatex *line2t = new TLatex(150, 30, "m_{#tilde{g}} - m_{LSP} = 2*(m_{W} + m_{b})");
  line2t->SetTextSize(0.02);
  line2t->SetTextAngle(45);
  line2t->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  


  can->SaveAs("T1ttbb_v2.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}


// ============================================================================

Int_t T1qqqq() {

  bool considerXsec = true;


  Int_t mgluMin = 600;
  Int_t mgluMax = 2050;
  Int_t mLSPMax = 1300;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T1qqqqc", "T1qqqqc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T1qqqqh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T1qqqq");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < 1200; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-200 && m_LSP < 400; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
      if(considerXsec && NEvents > 50000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 50000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");


  //Diagonal
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu && m_LSP < mLSPMax; m_LSP += step) {
      //if( !(m_glu % 50 == 0) && m_LSP < m_glu-225) continue; 
      //if( (m_glu % 50 == 0) && m_LSP < m_glu-200) continue; 
      if(m_LSP < m_glu-200) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
      if(considerXsec && NEvents > 100000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 100000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 100K", "F");
  
  // rest
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-200 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if(m_LSP < 400 && m_glu < 1200) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
      if(considerXsec && NEvents > 50000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 50000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");


   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  
  can->SaveAs("T1qqqq.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}


// ============================================================================

Int_t T1qqqq_v2() {

  bool considerXsec = true;


  Int_t mgluMin = 600;
  Int_t mgluMax = 2050;
  Int_t mLSPMax = 1300;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T1qqqqc", "T1qqqqc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T1qqqqh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T1qqqq");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < 1200; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-200 && m_LSP < 400; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");


  //Diagonal
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu && m_LSP < mLSPMax; m_LSP += step) {
      //if( !(m_glu % 50 == 0) && m_LSP < m_glu-225) continue; 
      //if( (m_glu % 50 == 0) && m_LSP < m_glu-200) continue; 
      if(m_LSP < m_glu-200) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 100K", "F");
  
  // rest
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 400; m_LSP < m_glu-200 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if(m_LSP < 400 && m_glu < 1200) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");


  // rest
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-200 && m_LSP < 400; m_LSP += 4*step) {
      if(m_LSP < 400 && m_glu < 1200) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+4*step);
      box->SetFillColor(kBlue-4);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x100 GeV^{2}, 50K", "F");


   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  
  can->SaveAs("T1qqqq_v2.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}


// ============================================================================

Int_t T5VV() {

  bool considerXsec = true;


  Int_t mgluMin = 600;
  Int_t mgluMax = 2050;
  Int_t mLSPMax = 1300;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T5VVc", "T5VVc");
  TH2F *h = new TH2F("T5VVh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5VV");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < 1200; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-100 && m_LSP < 400; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
      if(considerXsec && NEvents > 50000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                std::cout << m_glu << " " << m_LSP << " 50000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");

  //Diagonal
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-100 && m_LSP < mLSPMax; m_LSP += step) {
      if(m_LSP < m_glu-250) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
      if(considerXsec && NEvents > 150000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 150000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 150K", "F");
  
  // rest
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-250 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if( m_LSP < 400 && m_glu < 1200) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
      if(considerXsec && NEvents > 50000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 50000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");
  
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  
  can->SaveAs("T5VV.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

// ============================================================================
Int_t T5VV_v2() {

  bool considerXsec = true;

  Int_t mgluMin = 600;
  Int_t mgluMax = 2050;
  Int_t mLSPMax = 1300;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T5VVc", "T5VVc");
  TH2F *h = new TH2F("T5VVh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5VV");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < 1200; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-100 && m_LSP < 400; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");

  //Diagonal
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-100 && m_LSP < mLSPMax; m_LSP += step) {
      if(m_LSP < m_glu-250) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 150K", "F");
  
  // rest
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 400; m_LSP < m_glu-250 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if( m_LSP < 400 && m_glu < 1200) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");
  
  // rest
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-250 && m_LSP < 400; m_LSP += 4*step) {
      if( m_LSP < 400 && m_glu < 1200) continue; 
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+4*step);
      box->SetFillColor(kBlue-4);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x100 GeV^{2}, 50K", "F");
  
  

  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  
  can->SaveAs("T5VV_v2.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

// ============================================================================

Int_t T5qqqqWW_v1() {

  bool considerXsec = false;


  Int_t mgluMin = 600;
  Int_t mgluMax = 1750;
  Int_t mLSPMax = 1200;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T5qqqqWWc", "T5qqqqWWc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T5qqqqWWh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5qqqqWW lepton filter");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);

  /*
  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < 1200; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-100 && m_LSP < 400; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");
  */
  //Diagonal
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-50 && m_LSP < mLSPMax; m_LSP += step) {
      if(m_LSP < m_glu-350) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 10000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 10000;
      if(considerXsec && NEvents > 10000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 10000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 10K", "F");
  
  // rest
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-350 && m_LSP < mLSPMax; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 10000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 10000;
      if(considerXsec && NEvents > 10000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 10000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 10K", "F");
  

  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  
  can->SaveAs("T5qqqqWW_v1.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

// ============================================================================

Int_t T5qqqqWW_v2() {

  bool considerXsec = false;


  Int_t mgluMin = 600;
  Int_t mgluMax = 1750;
  Int_t mLSPMax = 1200;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T5qqqqWWc", "T5qqqqWWc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T5qqqqWWh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5qqqqWW lepton filter");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);

  /*
  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < 1200; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-100 && m_LSP < 400; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");
  */
  //Diagonal
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-50 && m_LSP < mLSPMax; m_LSP += step) {
      if(m_LSP < m_glu-250) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 10000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 10000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 10K", "F");
  
  // rest
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-250 && m_LSP < mLSPMax; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 10000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 10000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 10K", "F");
  

  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  
  can->SaveAs("T5qqqqWW_v2.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

// ============================================================================

Int_t T5qqqqWZ() {

  bool considerXsec = false;


  Int_t mgluMin = 600;
  Int_t mgluMax = 1600;
  Int_t mLSPMax = 1200;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T5qqqqWWc", "T5qqqqWWc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T5qqqqWWh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5qqqqWZ lepton filter");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);

  /*
  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < 1200; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-100 && m_LSP < 400; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");
  */
  //Diagonal
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-100 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if(m_LSP < m_glu-350) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 10000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 10000;
      if(considerXsec && NEvents > 10000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 10000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 10K", "F");
  
  // rest
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-350 && m_LSP < mLSPMax; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 10000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 10000;
      if(considerXsec && NEvents > 10000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 10000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 10K", "F");
  

  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  
  can->SaveAs("T5qqqqWZ.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

// ============================================================================

Int_t T5ZZ() {

  bool considerXsec = true;


  Int_t mgluMin = 600;
  Int_t mgluMax = 1600;
  Int_t mLSPMax = 900;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T5ZZc", "T5ZZc");
  TH2F *h = new TH2F("T5ZZh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(neutralino) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5ZZ");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
   
  for(Int_t m_glu = 600; m_glu < 800; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-100; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
      if(considerXsec && NEvents > 50000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 50000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");

  for(Int_t m_glu = 800; m_glu < 1600; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-100; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
      if(considerXsec && NEvents > 50000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 50000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");

   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  
  can->SaveAs("T5ZZ.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

// ============================================================================

Int_t T5tttt_DM175() {

  bool considerXsec = false;


  Int_t mgluMin = 600;
  Int_t mgluMax = 1750;
  Int_t mLSPMax = 1325;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T5ttttc", "T5ttttc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T5tttth", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, mgluMax);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5tttt DM=175");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  // compressed region
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-270 && m_LSP < mLSPMax; m_LSP += step) {
      if (m_glu - m_LSP > 370) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
      if(considerXsec && NEvents > 100000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 100000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 100K", "F");

  // excluded
  for(Int_t m_glu = mgluMin; m_glu < 900; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < 200; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
      if(considerXsec && NEvents > 100000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 100000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 100K", "F");


  //bulk
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-370 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if (m_LSP < 200 && m_glu < 900) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
      if(considerXsec && NEvents > 100000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 100000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 100K", "F");


   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  // Add lines showing the diagonals
  can->Update();
  TLine line1 = TLine(0+175*2,0,1750,1750-175*2);
  line1.SetLineColor(kGray+2);
  line1.SetLineWidth(2);
  line1.SetLineStyle(2);
  line1.Draw("same");
  TLatex *line1t = new TLatex(450, 30, "m_{#tilde{g}} - m_{#tilde{t}} = m_{t}");
  line1t->SetTextSize(0.02);
  line1t->SetTextAngle(45);
  line1t->Draw();

  TLine line2 = TLine(0+85+175,0,1750,1750-85-175);
  line2.SetLineColor(kGray+2);
  line2.SetLineWidth(2);
  line2.SetLineStyle(2);
  line2.Draw("same");
  TLatex *line2t = new TLatex(250, 30, "m_{#tilde{g}} - m_{#tilde{t}} = m_{W} + m_{b}");
  line2t->SetTextSize(0.02);
  line2t->SetTextAngle(45);
  line2t->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(110, 1130, textNP);
  TText *NE = new TText(110, 1030, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  can->SaveAs("T5tttt_dm175.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

// ============================================================================

Int_t T5tttt_DM175_v2() {

  bool considerXsec = false;


  Int_t mgluMin = 600;
  Int_t mgluMax = 1800;
  Int_t mLSPMax = 1325;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T5ttttc", "T5ttttc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T5tttth", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, mgluMax);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5tttt DM=175");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  // compressed region
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-270 && m_LSP < mLSPMax; m_LSP += step) {
      if (m_glu - m_LSP > 370) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 100K", "F");

  // excluded
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < mLSPMax && m_LSP < m_glu-470; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 100K", "F");


  //bulk
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-370 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if( !(m_glu % 100 == 0) && m_LSP < m_glu-470) continue; 
      if( (m_glu % 100 == 0) && m_LSP < m_glu-420) continue; 
      //if (m_LSP < m_glu - 470) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 100K", "F");


   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  // Add lines showing the diagonals
  can->Update();
  TLine line1 = TLine(0+175*2,0,1750,1750-175*2);
  line1.SetLineColor(kGray+2);
  line1.SetLineWidth(2);
  line1.SetLineStyle(2);
  line1.Draw("same");
  TLatex *line1t = new TLatex(450, 30, "m_{#tilde{g}} - m_{#tilde{t}} = m_{t}");
  line1t->SetTextSize(0.02);
  line1t->SetTextAngle(45);
  line1t->Draw();

  TLine line2 = TLine(0+85+175,0,1750,1750-85-175);
  line2.SetLineColor(kGray+2);
  line2.SetLineWidth(2);
  line2.SetLineStyle(2);
  line2.Draw("same");
  TLatex *line2t = new TLatex(250, 30, "m_{#tilde{g}} - m_{#tilde{t}} = m_{W} + m_{b}");
  line2t->SetTextSize(0.02);
  line2t->SetTextAngle(45);
  line2t->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(110, 1130, textNP);
  TText *NE = new TText(110, 1030, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  can->SaveAs("T5tttt_dm175_v2.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

Int_t T5tttt_MGLU1500() {

  bool considerXsec = false;


  Int_t mgluMin = 100;
  Int_t mgluMax = 1450;
  Int_t mLSPMax = 1100;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T5tttt_mglu1500c", "T5tttt_mglu1500c");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T5tttt_mglu1500h", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, mgluMax);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(stop) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5tttt M(gluino) = 1500 GeV");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  // compressed region
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-90 && m_LSP < mLSPMax; m_LSP += step) {
      if (m_glu - m_LSP > 225) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
      if(considerXsec && NEvents > 100000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 100000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 100K", "F");

  //bulk
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-225 && m_LSP < mLSPMax; m_LSP += 2*step) {
      //if (m_LSP < 200 && m_glu < 900) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
      if(considerXsec && NEvents > 50000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 50000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");
  

   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  // Add lines showing the diagonals
  can->Update();
  TLine line1 = TLine(0+175,0,1450,1450-175);
  line1.SetLineColor(kGray+2);
  line1.SetLineWidth(2);
  line1.SetLineStyle(2);
  line1.Draw("same");
  TLatex *line1t = new TLatex(1275, 1125, "m_{#tilde{t}} - m_{LSP} = m_{t}");
  line1t->SetTextSize(0.02);
  line1t->SetTextAngle(45);
  line1t->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(110, 930, textNP);
  TText *NE = new TText(110, 830, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  can->SaveAs("T5tttt_mglu1500.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

// ============================================================================

Int_t T5tttt_MGLU1500_v2() {

  bool considerXsec = false;


  Int_t mgluMin = 100;
  Int_t mgluMax = 1450;
  Int_t mLSPMax = 1100;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T5tttt_mglu1500c", "T5tttt_mglu1500c");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T5tttt_mglu1500h", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, mgluMax);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(stop) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5tttt M(gluino) = 1500 GeV");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  // compressed region
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-90 && m_LSP < mLSPMax; m_LSP += step) {
      if (m_glu - m_LSP > 225) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 100K", "F");
  
  // excluded
  for(Int_t m_glu = 900; m_glu < 1400; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu - 800; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");
  
  
  //bulk
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-225 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if (m_glu % 100 == 0 && m_glu >= 900 && m_glu < 1400 && m_LSP < m_glu - 800) continue;
      if (m_glu % 100 != 0 && m_glu >= 900 && m_glu < 1400 && m_LSP < m_glu - 850) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");
  
  
   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  // Add lines showing the diagonals
  can->Update();
  TLine line1 = TLine(0+175,0,1450,1450-175);
  line1.SetLineColor(kGray+2);
  line1.SetLineWidth(2);
  line1.SetLineStyle(2);
  line1.Draw("same");
  TLatex *line1t = new TLatex(1275, 1125, "m_{#tilde{t}} - m_{LSP} = m_{t}");
  line1t->SetTextSize(0.02);
  line1t->SetTextAngle(45);
  line1t->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(110, 930, textNP);
  TText *NE = new TText(110, 830, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  can->SaveAs("T5tttt_mglu1500_v2.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

// ============================================================================

Int_t T5ttcc() {

  bool considerXsec = false;


  Int_t mgluMin = 600;
  Int_t mgluMax = 1750;
  Int_t mLSPMax = 1400;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T5ttccc", "T5ttccc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T5ttcch", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, mgluMax);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5ttcc");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  // compressed region
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-110 && m_LSP < mLSPMax; m_LSP += step) {
      if (m_glu - m_LSP > 210) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
      if(considerXsec && NEvents > 100000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 100000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 100K", "F");

  
  // excluded
  for(Int_t m_glu = mgluMin; m_glu < 1000; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < 400; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
      if(considerXsec && NEvents > 50000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 50000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");

  // less structure
  for(Int_t m_glu = 1000; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 100; m_LSP < 400; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+4*step);
      box->SetFillColor(kBlue-4);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
      if(considerXsec && NEvents > 100000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 100000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x100 GeV^{2}, 100K", "F");

  
  //bulk
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-210 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if (m_LSP < 400 && m_glu < 1000) continue;
      if (m_LSP < 400 && m_LSP >= 100) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
      if(considerXsec && NEvents > 100000) std::cout << m_glu << " " << m_LSP << " " << NEvents << std::endl;
      else                                 std::cout << m_glu << " " << m_LSP << " 100000 " << std::endl;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 100K", "F");
  

   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  // Add lines showing the diagonals
  can->Update();
  TLine line1 = TLine(0+175+20,0,1750,1750-175-20);
  line1.SetLineColor(kGray+2);
  line1.SetLineWidth(2);
  line1.SetLineStyle(2);
  line1.Draw("same");
  TLatex *line1t = new TLatex(280, 30, "m_{#tilde{g}} - m_{#tilde{t}} = m_{t}");
  line1t->SetTextSize(0.02);
  line1t->SetTextAngle(45);
  line1t->Draw();

  TLine line2 = TLine(0+85+20,0,1750,1750-85-20);
  line2.SetLineColor(kGray+2);
  line2.SetLineWidth(2);
  line2.SetLineStyle(2);
  line2.Draw("same");
  TLatex *line2t = new TLatex(100, 30, "m_{#tilde{g}} - m_{#tilde{t}} = m_{W} + m_{b}");
  line2t->SetTextSize(0.02);
  line2t->SetTextAngle(45);
  line2t->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(110, 930, textNP);
  TText *NE = new TText(110, 830, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  
  can->SaveAs("T5ttcc.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

// ============================================================================

Int_t T5ttcc_v2() {

  bool considerXsec = false;


  Int_t mgluMin = 600;
  Int_t mgluMax = 1750;
  Int_t mLSPMax = 1400;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T5ttccc", "T5ttccc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T5ttcch", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, mgluMax);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5ttcc");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  // compressed region
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-110 && m_LSP < mLSPMax; m_LSP += step) {
      if (m_glu - m_LSP > 210) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 100K", "F");

  
  // excluded
  for(Int_t m_glu = mgluMin; m_glu < 1000; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < 400; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");

  // less structure
  for(Int_t m_glu = 1000; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 100; m_LSP < 400; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+4*step);
      box->SetFillColor(kBlue-4);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x100 GeV^{2}, 50K", "F");

  
  //bulk
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-210 && m_LSP < mLSPMax; m_LSP += 2*step) {
      if (m_LSP < 400 && m_glu < 1000) continue;
      if (m_LSP < 400 && m_LSP >= 100) continue;
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");
  

   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(110, 930, textNP);
  TText *NE = new TText(110, 830, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  
  can->SaveAs("T5ttcc_v2.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

Int_t T7btW() {

  bool considerXsec = true;


  Int_t mgluMin = 900;
  Int_t mgluMax = 1500;
  Int_t mLSPMax = 900;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T7btWc", "T7btWc");
  TH2F *h = new TH2F("T7btWh", "", mgluMax/step, mgluMin, mgluMax, mgluMax/step, 500, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(sbottom) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T7btW");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < mgluMax; m_glu += step) {
    for(Int_t m_LSP = 500; m_LSP < m_glu-170; m_LSP += step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+step);
      box->SetFillColor(kGreen-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 150K", "F");


   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(925, 1230, textNP);
  TText *NE = new TText(925, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  
  can->SaveAs("T7btW.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}


Int_t T5Wg() {

  bool considerXsec = true;


  Int_t mgluMin = 800;
  Int_t mgluMax = 1600;
  Int_t mLSPMax = 900;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T5Wgc", "T5Wgc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T5Wgh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(neutralino) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5Wg");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.03);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
   
  for(Int_t m_glu = 800; m_glu < 1000; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");

  for(Int_t m_glu = 1000; m_glu < 1600; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 150K", "F");

   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  
  can->SaveAs("T5Wg.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}


Int_t T5gg() {

  bool considerXsec = true;

  Int_t mgluMin = 1000;
  Int_t mgluMax = 2000;
  Int_t mLSPMax = 1000;
  Int_t step = 50;
  TCanvas *can = new TCanvas("T5ggc", "T5ggc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T5ggh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, mgluMax);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(neutralino) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5gg");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.03);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
   
  for(Int_t m_glu = 1000; m_glu < 1250; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 150K", "F");

  // rest 
  for(Int_t m_glu = 1300; m_glu <= mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-80; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x100 GeV^{2}, 150K", "F");

   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  
  can->SaveAs("T5gg.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

Int_t T5Zg() {

  bool considerXsec = true;


  Int_t mgluMin = 800;
  Int_t mgluMax = 1600;
  Int_t mLSPMax = 900;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T5Zgc", "TZWgc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T5Zgh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(neutralino) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5Zg");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.03);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
   
  for(Int_t m_glu = 800; m_glu < mgluMax; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 100K", "F");
   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  
  can->SaveAs("T5Zg.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}


// ============================================================================

Int_t T6gg() {

  bool considerXsec = true;


  Int_t mgluMin = 1200;
  Int_t mgluMax = 2000;
  Int_t mLSPMax = 1000;
  Int_t step = 50;
  TCanvas *can = new TCanvas("T6ggc", "T5ggc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T6ggh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, mgluMax);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(neutralino) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T6gg");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.03);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
   
  for(Int_t m_glu = mgluMin; m_glu < 1450; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionsqsq(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 140000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 150K", "F");

  // rest 
  for(Int_t m_glu = 1500; m_glu <= mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-80; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionsqsq(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 150000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x100 GeV^{2}, 150K", "F");

   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  
  can->SaveAs("T6gg.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}



// ============================================================================

Int_t T5Wg_v2() {

  bool considerXsec = true;

  Int_t mgluMin = 800;
  Int_t mgluMax = 1600;
  Int_t mLSPMax = 900;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T5Wgc", "T5Wgc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T5Wgh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 2000);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(neutralino) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5Wg");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.03);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
   
  for(Int_t m_glu = 800; m_glu < 1000; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 100K", "F");

  for(Int_t m_glu = 1000; m_glu < 1600; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 100K", "F");

   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  
  can->SaveAs("T5Wg_100k.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}


Int_t T5gg_v2() {

  bool considerXsec = true;

  Int_t mgluMin = 1000;
  Int_t mgluMax = 2000;
  Int_t mLSPMax = 1000;
  Int_t step = 50;
  TCanvas *can = new TCanvas("T5ggc", "T5ggc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T5ggh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, mgluMax);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(neutralino) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T5gg");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.03);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
   
  for(Int_t m_glu = 1000; m_glu < 1250; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 100K", "F");

  // rest 
  for(Int_t m_glu = 1300; m_glu <= mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-80; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionglgl(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x100 GeV^{2}, 100K", "F");

   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  
  can->SaveAs("T5gg_100k.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

// ============================================================================

Int_t T6gg_v2() {

  bool considerXsec = true;

  Int_t mgluMin = 1200;
  Int_t mgluMax = 2000;
  Int_t mLSPMax = 1000;
  Int_t step = 50;
  TCanvas *can = new TCanvas("T6ggc", "T5ggc");
  can->SetRightMargin(0.05);
  TH2F *h = new TH2F("T6ggh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, mgluMax);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(gluino) [GeV]");
  h->GetYaxis()->SetTitle("M(neutralino) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T6gg");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.03);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
   
  for(Int_t m_glu = mgluMin; m_glu < 1450; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionsqsq(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 100K", "F");

  // rest 
  for(Int_t m_glu = 1500; m_glu <= mgluMax; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-80; m_LSP += 2*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+step, m_LSP+2*step);
      box->SetFillColor(kBlue-7);
      boxes.push_back(box);
      float xsec = crossSectionsqsq(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 100000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x100 GeV^{2}, 100K", "F");

   
  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  
  can->SaveAs("T6gg_100k.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;
  
  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

Int_t T2bb() {

  bool considerXsec = true;

  Int_t mgluMin = 300;
  Int_t mgluMax = 1300;
  Int_t mLSPMax = 900;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T2bbc", "T2bbc");
  TH2F *h = new TH2F("T2bbh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 1200);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(sbottom) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T2bb");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
  for(Int_t m_glu = mgluMin; m_glu < 600; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < 100; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionsbsb(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");


 //Diagonal
  for(Int_t m_glu = mgluMin; m_glu < 400; m_glu += step) {
    for(Int_t m_LSP = 100; m_LSP < m_glu && m_LSP < 600; m_LSP += step) {
  //    if( m_LSP < m_glu-250) continue;
      for(Int_t incx = 0; incx < 1; incx++) {
        for(Int_t incy = 0; incy < 1; incy++) {
          TBox *box = new TBox(m_glu+incx*step, m_LSP+incy*step, m_glu+(incx+1)*step, m_LSP+(incy+1)*step);
          box->SetFillColor(kGreen-7);
          boxes.push_back(box);
          float xsec = crossSectionsbsb(m_glu);
          Float_t NEvents = xsec * Lref * 1000;
          if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;
          else totalNumberOfEvents += 150000;
        }
      }
    }
  }
  
    
    
    for(Int_t m_glu = 400; m_glu < 500; m_glu += step) {
        for(Int_t m_LSP = 200; m_LSP < m_glu && m_LSP < 600; m_LSP += step) {
            //    if( m_LSP < m_glu-250) continue;
            for(Int_t incx = 0; incx < 1; incx++) {
                for(Int_t incy = 0; incy < 1; incy++) {
                    TBox *box = new TBox(m_glu+incx*step, m_LSP+incy*step, m_glu+(incx+1)*step, m_LSP+(incy+1)*step);
                    box->SetFillColor(kGreen-7);
                    boxes.push_back(box);
                    float xsec = crossSectionsbsb(m_glu);
                    Float_t NEvents = xsec * Lref * 1000;
                    if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;
                    else totalNumberOfEvents += 150000;
                }
            }
        }
    }

    
    for(Int_t m_glu = 500; m_glu < 600; m_glu += step) {
        for(Int_t m_LSP = 100; m_LSP < m_glu && m_LSP < 600; m_LSP += step) {
               if( m_LSP < 300) continue;
            for(Int_t incx = 0; incx < 1; incx++) {
                for(Int_t incy = 0; incy < 1; incy++) {
                    TBox *box = new TBox(m_glu+incx*step, m_LSP+incy*step, m_glu+(incx+1)*step, m_LSP+(incy+1)*step);
                    box->SetFillColor(kGreen-7);
                    boxes.push_back(box);
                    float xsec = crossSectionsbsb(m_glu);
                    Float_t NEvents = xsec * Lref * 1000;
                    if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;
                    else totalNumberOfEvents += 150000;
                }
            }
        }
    }

    
    
    for(Int_t m_glu = 600; m_glu < 700; m_glu += step) {
        for(Int_t m_LSP = 100; m_LSP < m_glu && m_LSP < 600; m_LSP += step) {
                if( m_LSP < m_glu-250) continue;
            for(Int_t incx = 0; incx < 1; incx++) {
                for(Int_t incy = 0; incy < 1; incy++) {
                    TBox *box = new TBox(m_glu+incx*step, m_LSP+incy*step, m_glu+(incx+1)*step, m_LSP+(incy+1)*step);
                    box->SetFillColor(kGreen-7);
                    boxes.push_back(box);
                    float xsec = crossSectionsbsb(m_glu);
                    Float_t NEvents = xsec * Lref * 1000;
                    if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;
                    else totalNumberOfEvents += 150000;
                }
            }
        }
    }

    for(Int_t m_glu = 700; m_glu < 800; m_glu += step) {
        for(Int_t m_LSP = 100; m_LSP < m_glu && m_LSP < 600; m_LSP += step) {
               if( m_LSP < m_glu-250) continue;
            for(Int_t incx = 0; incx < 1; incx++) {
                for(Int_t incy = 0; incy < 1; incy++) {
                    TBox *box = new TBox(m_glu+incx*step, m_LSP+incy*step, m_glu+(incx+1)*step, m_LSP+(incy+1)*step);
                    box->SetFillColor(kGreen-7);
                    boxes.push_back(box);
                    float xsec = crossSectionsbsb(m_glu);
                    Float_t NEvents = xsec * Lref * 1000;
                    if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;
                    else totalNumberOfEvents += 150000;
                }
            }
        }
    }

    
    leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 150K", "F");

   
  for(Int_t m_glu = 400; m_glu < 600; m_glu += 4*step) {
    for(Int_t m_LSP = 100; m_LSP < m_glu-200 && m_LSP < 600; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionsbsb(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;
      else totalNumberOfEvents += 500000;
    }
  }


  for(Int_t m_glu = 600; m_glu < 1100; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-200 && m_LSP < 600; m_LSP += 4*step) {
      for(Int_t incx = 0; incx < 2; incx++) {
        for(Int_t incy = 0; incy < 2; incy++) {
          TBox *box = new TBox(m_glu+incx*2*step, m_LSP+incy*2*step, m_glu+(incx+1)*2*step, m_LSP+(incy+1)*2*step);
          box->SetFillColor(kBlue-7);
          boxes.push_back(box);
          float xsec = crossSectionsbsb(m_glu);
          Float_t NEvents = xsec * Lref * 1000;
          if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;
          else totalNumberOfEvents += 50000;
        }
      }
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");


  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(100, 800, textNP);
  TText *NE = new TText(100, 700, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  can->SaveAs("T2bb.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;

  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;


}

Int_t T2tb() {

  bool considerXsec = true;

  Int_t mgluMin = 300;
  Int_t mgluMax = 1200;
  Int_t mLSPMax = 900;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T2tbc", "T2tbc");
  TH2F *h = new TH2F("T2tbh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 1200);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(stop) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T2tb");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
  for(Int_t m_glu = 400; m_glu < 600; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-300; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionsbsb(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");


 //Diagonal
 for(Int_t m_glu = 200; m_glu < 400; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-100 && m_LSP < 500; m_LSP += step) {
     // if( m_LSP < m_glu-350) continue;
      for(Int_t incx = 0; incx < 1; incx++) {
        for(Int_t incy = 0; incy < 1; incy++) {
          TBox *box = new TBox(m_glu+incx*step, m_LSP+incy*step, m_glu+(incx+1)*step, m_LSP+(incy+1)*step);
          box->SetFillColor(kGreen-7);
          boxes.push_back(box);
          float xsec = crossSectionsbsb(m_glu);
          Float_t NEvents = xsec * Lref * 1000;
          if(considerXsec && NEvents > 150000 && NEvents<5e05) totalNumberOfEvents += NEvents;
          else totalNumberOfEvents += 150000;
        }
      }
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 150K", "F");
    
    
    
    //Diagonal
    for(Int_t m_glu = 400; m_glu < 500; m_glu += step) {
        for(Int_t m_LSP = 100; m_LSP < m_glu-100 && m_LSP < 500; m_LSP += step) {
            // if( m_LSP < m_glu-350) continue;
            for(Int_t incx = 0; incx < 1; incx++) {
                for(Int_t incy = 0; incy < 1; incy++) {
                    TBox *box = new TBox(m_glu+incx*step, m_LSP+incy*step, m_glu+(incx+1)*step, m_LSP+(incy+1)*step);
                    box->SetFillColor(kGreen-7);
                    boxes.push_back(box);
                    float xsec = crossSectionsbsb(m_glu);
                    Float_t NEvents = xsec * Lref * 1000;
                    if(considerXsec && NEvents > 150000 && NEvents<5e05) totalNumberOfEvents += NEvents;
                    else totalNumberOfEvents += 150000;
                }
            }
        }
    }

    
    
    //Diagonal
    for(Int_t m_glu = 500; m_glu < 600; m_glu += step) {
        for(Int_t m_LSP = 200; m_LSP < m_glu-100 && m_LSP < 500; m_LSP += step) {
            // if( m_LSP < m_glu-350) continue;
            for(Int_t incx = 0; incx < 1; incx++) {
                for(Int_t incy = 0; incy < 1; incy++) {
                    TBox *box = new TBox(m_glu+incx*step, m_LSP+incy*step, m_glu+(incx+1)*step, m_LSP+(incy+1)*step);
                    box->SetFillColor(kGreen-7);
                    boxes.push_back(box);
                    float xsec = crossSectionsbsb(m_glu);
                    Float_t NEvents = xsec * Lref * 1000;
                    if(considerXsec && NEvents > 150000 && NEvents<5e05) totalNumberOfEvents += NEvents;
                    else totalNumberOfEvents += 150000;
                }
            }
        }
    }
    

    
    //Diagonal
    for(Int_t m_glu = 600; m_glu < 700; m_glu += step) {
        for(Int_t m_LSP = 300; m_LSP < m_glu-100 && m_LSP < 500; m_LSP += step) {
            // if( m_LSP < m_glu-350) continue;
            for(Int_t incx = 0; incx < 1; incx++) {
                for(Int_t incy = 0; incy < 1; incy++) {
                    TBox *box = new TBox(m_glu+incx*step, m_LSP+incy*step, m_glu+(incx+1)*step, m_LSP+(incy+1)*step);
                    box->SetFillColor(kGreen-7);
                    boxes.push_back(box);
                    float xsec = crossSectionsbsb(m_glu);
                    Float_t NEvents = xsec * Lref * 1000;
                    if(considerXsec && NEvents > 150000 && NEvents<5e05) totalNumberOfEvents += NEvents;
                    else totalNumberOfEvents += 150000;
                }
            }
        }
    }
    

    
 
    
    


  for(Int_t m_glu = 700; m_glu < 1100; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < 500; m_LSP += 4*step) {
      for(Int_t incx = 0; incx < 2; incx++) {
        for(Int_t incy = 0; incy < 2; incy++) {
          TBox *box = new TBox(m_glu+incx*2*step, m_LSP+incy*2*step, m_glu+(incx+1)*2*step, m_LSP+(incy+1)*2*step);
          box->SetFillColor(kBlue-7);
          boxes.push_back(box);
          float xsec = crossSectionsbsb(m_glu);
          Float_t NEvents = xsec * Lref * 1000;
          if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;
          else totalNumberOfEvents += 50000;
        }
      }
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");

  for(Int_t m_glu = 600; m_glu < 700; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < 300; m_LSP += 4*step) {
      for(Int_t incx = 0; incx < 2; incx++) {
        for(Int_t incy = 0; incy < 2; incy++) {
          TBox *box = new TBox(m_glu+incx*2*step, m_LSP+incy*2*step, m_glu+(incx+1)*2*step, m_LSP+(incy+1)*2*step);
          box->SetFillColor(kBlue-7);
          boxes.push_back(box);
          float xsec = crossSectionsbsb(m_glu);
          Float_t NEvents = xsec * Lref * 1000;
          if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;
          else totalNumberOfEvents += 50000;
        }
      }
    }
  }


  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(100, 800, textNP);
  TText *NE = new TText(100, 700, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  can->SaveAs("T2tb.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;

  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;


}



Int_t T2bW() {

  bool considerXsec = true;

  Int_t mgluMin = 100;
  Int_t mgluMax = 1200;
  Int_t mLSPMax = 900;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T2bW", "T2bW");
  TH2F *h = new TH2F("T2bWh", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 1200);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(stop) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T2bW");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
  for(Int_t m_glu = 300; m_glu < 600; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-300; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionsbsb(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000 && NEvents<5e05) totalNumberOfEvents += NEvents;
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");


 //Diagonal
  for(Int_t m_glu = 0; m_glu < 400; m_glu += step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-100 ; m_LSP += step) {
    //  if( m_LSP < m_glu-325) continue;
        //if (m_glu<100 || m_glu>325) continue;
      for(Int_t incx = 0; incx < 1; incx++) {
        for(Int_t incy = 0; incy < 1; incy++) {
          TBox *box = new TBox(m_glu+incx*step, m_LSP+incy*step, m_glu+(incx+1)*step, m_LSP+(incy+1)*step);
          box->SetFillColor(kGreen-7);
          boxes.push_back(box);
          float xsec = crossSectionsbsb(m_glu);
          Float_t NEvents = xsec * Lref * 1000;
          if(considerXsec && NEvents > 150000 && NEvents<5e05) totalNumberOfEvents += NEvents;
          else totalNumberOfEvents += 150000;
        }
      }
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 150K", "F");
    
    
    for(Int_t m_glu = 400; m_glu < 500; m_glu += step) {
        for(Int_t m_LSP = 100; m_LSP < 300 ; m_LSP += step) {
          //  if( m_LSP < m_glu-325) continue;
          //  if (m_glu<100 || m_glu>325) continue;
            for(Int_t incx = 0; incx < 1; incx++) {
                for(Int_t incy = 0; incy < 1; incy++) {
                    TBox *box = new TBox(m_glu+incx*step, m_LSP+incy*step, m_glu+(incx+1)*step, m_LSP+(incy+1)*step);
                    box->SetFillColor(kGreen-7);
                    boxes.push_back(box);
                    float xsec = crossSectionsbsb(m_glu);
                    Float_t NEvents = xsec * Lref * 1000;
                    if(considerXsec && NEvents > 150000 && NEvents<5e05) totalNumberOfEvents += NEvents;
                    else totalNumberOfEvents += 150000;
                }
            }
        }
    }
    
    
    for(Int_t m_glu = 500; m_glu < 600; m_glu += step) {
        for(Int_t m_LSP = 200; m_LSP < 300 ; m_LSP += step) {
            //  if( m_LSP < m_glu-325) continue;
            //  if (m_glu<100 || m_glu>325) continue;
            for(Int_t incx = 0; incx < 1; incx++) {
                for(Int_t incy = 0; incy < 1; incy++) {
                    TBox *box = new TBox(m_glu+incx*step, m_LSP+incy*step, m_glu+(incx+1)*step, m_LSP+(incy+1)*step);
                    box->SetFillColor(kGreen-7);
                    boxes.push_back(box);
                    float xsec = crossSectionsbsb(m_glu);
                    Float_t NEvents = xsec * Lref * 1000;
                    if(considerXsec && NEvents > 150000 && NEvents<5e05) totalNumberOfEvents += NEvents;
                    else totalNumberOfEvents += 150000;
                }
            }
        }
    }

    
    
    for(Int_t m_glu = 400; m_glu < 700; m_glu += step) {
        for(Int_t m_LSP = 300; m_LSP < 400 ; m_LSP += step) {
              if( m_LSP > m_glu-125) continue;
            //  if (m_glu<100 || m_glu>325) continue;
            for(Int_t incx = 0; incx < 1; incx++) {
                for(Int_t incy = 0; incy < 1; incy++) {
                    TBox *box = new TBox(m_glu+incx*step, m_LSP+incy*step, m_glu+(incx+1)*step, m_LSP+(incy+1)*step);
                    box->SetFillColor(kGreen-7);
                    boxes.push_back(box);
                    float xsec = crossSectionsbsb(m_glu);
                    Float_t NEvents = xsec * Lref * 1000;
                    if(considerXsec && NEvents > 150000 && NEvents<5e05) totalNumberOfEvents += NEvents;
                    else totalNumberOfEvents += 150000;
                }
            }
        }
    }

    
    
    
  for(Int_t m_glu = 700; m_glu < 1000; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < 400; m_LSP += 4*step) {
      for(Int_t incx = 0; incx < 2; incx++) {
        for(Int_t incy = 0; incy < 2; incy++) {
          TBox *box = new TBox(m_glu+incx*2*step, m_LSP+incy*2*step, m_glu+(incx+1)*2*step, m_LSP+(incy+1)*2*step);
          box->SetFillColor(kBlue-7);
          boxes.push_back(box);
          float xsec = crossSectionsbsb(m_glu);
          Float_t NEvents = xsec * Lref * 1000;
          if(considerXsec && NEvents > 50000 && NEvents<5e05) totalNumberOfEvents += NEvents;
          else totalNumberOfEvents += 50000;
        }
      }
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");

  for(Int_t m_glu = 600; m_glu < 700; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < 300; m_LSP += 4*step) {
      for(Int_t incx = 0; incx < 2; incx++) {
        for(Int_t incy = 0; incy < 2; incy++) {
          TBox *box = new TBox(m_glu+incx*2*step, m_LSP+incy*2*step, m_glu+(incx+1)*2*step, m_LSP+(incy+1)*2*step);
          box->SetFillColor(kBlue-7);
          boxes.push_back(box);
          float xsec = crossSectionsbsb(m_glu);
          Float_t NEvents = xsec * Lref * 1000;
          if(considerXsec && NEvents > 50000 && NEvents<5e05) totalNumberOfEvents += NEvents;
          else totalNumberOfEvents += 50000;
        }
      }
    }
  }



  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(100, 800, textNP);
  TText *NE = new TText(100, 700, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  can->SaveAs("T2bW.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;

  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;


}



/*
Int_t T6ttWW() {

  bool considerXsec = true;


  Int_t mgluMin = 400;
  Int_t mgluMax = 900;
  Int_t mLSPMax = 700;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T6ttWWc", "T6ttWWc");
  TH2F *h = new TH2F("T6ttWWc", "", mgluMax/step, 0, mgluMax, mgluMax/step, 0, 1200);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(sbottom) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T6ttWW");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);


  //Excluded region
 for(Int_t m_glu = 400; m_glu < 600; m_glu += 4*step) {
    for(Int_t m_LSP = 0; m_LSP < 200; m_LSP += 4*step) {
      TBox *box = new TBox(m_glu, m_LSP, m_glu+4*step, m_LSP+4*step);
      box->SetFillColor(kRed-7);
      boxes.push_back(box);
      float xsec = crossSectionsbsb(m_glu);
      Float_t NEvents = xsec * Lref * 1000;
      if(considerXsec && NEvents > 50000) totalNumberOfEvents += NEvents;   
      else totalNumberOfEvents += 50000;
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "100x100 GeV^{2}, 50K", "F");

  for(Int_t m_glu = 400; m_glu < 800; m_glu += 2*step) {
    for(Int_t m_LSP = 200; m_LSP < m_glu-150 && m_LSP < 700; m_LSP += 2*step) {
      if( m_LSP < m_glu-200) continue; 
      for(Int_t incx = 0; incx < 2; incx++) {
        for(Int_t incy = 0; incy < 2; incy++) {
          TBox *box = new TBox(m_glu+incx*step, m_LSP+incy*step, m_glu+(incx+1)*step, m_LSP+(incy+1)*step);
          box->SetFillColor(kGreen-7);
          boxes.push_back(box);
          float xsec = crossSectionsbsb(m_glu);
          Float_t NEvents = xsec * Lref * 1000;
          if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;
          else totalNumberOfEvents += 150000;
        }
      }
    }
  }
  leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 150K", "F");

 for(Int_t m_glu = 450; m_glu < 600; m_glu += 2*step) {
    for(Int_t m_LSP = 200; m_LSP < m_glu-200 && m_LSP < 700; m_LSP += 2*step) {
       TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
       box->SetFillColor(kBlue-7);
       boxes.push_back(box);
       float xsec = crossSectionsbsb(m_glu);
       Float_t NEvents = xsec * Lref * 1000;
       if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;
       else totalNumberOfEvents += 100000;
    }
  } 
  leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 100K", "F");

  for(Int_t m_glu = 600; m_glu < 900; m_glu += 2*step) {
    for(Int_t m_LSP = 0; m_LSP < m_glu-200 && m_LSP < 700; m_LSP += 2*step) {
       TBox *box = new TBox(m_glu, m_LSP, m_glu+2*step, m_LSP+2*step);
       box->SetFillColor(kBlue-7);
       boxes.push_back(box);
       float xsec = crossSectionsbsb(m_glu);
       Float_t NEvents = xsec * Lref * 1000;
       if(considerXsec && NEvents > 100000) totalNumberOfEvents += NEvents;
       else totalNumberOfEvents += 100000;
    }
  } 

  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(100, 650, textNP);
  TText *NE = new TText(100, 550, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  

  can->SaveAs("T6ttWW.png");

  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete can;

  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;


} 
*/

Int_t T2TT() {

  bool considerXsec = true;


  Int_t mstopMin = 100;
  Int_t mstopMax = 1200;
  Int_t mLSPMax = 1000;
  Int_t step = 25;
  TCanvas *can = new TCanvas("T2TTc", "T2TTc");
  TH2F *h = new TH2F("T2TTh", "", mstopMax/step, 0, mstopMax, mstopMax/step, 0, mLSPMax);
  h->GetXaxis()->SetLabelSize(0.03);
  h->GetYaxis()->SetLabelSize(0.03);
  h->GetXaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleSize(0.04);
  h->GetYaxis()->SetTitleOffset(1.4);
  h->GetXaxis()->SetTitle("M(stop) [GeV]");
  h->GetYaxis()->SetTitle("M(LSP) [GeV]");

  vector<TBox *> boxes;  
  Int_t totalNumberOfEvents = 0;  

  TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T2TT");
  leg->SetFillColor(kWhite);
  leg->SetTextFont(42);
  leg->SetTextSize(0.028);
  leg->SetLineWidth(0);
  leg->SetBorderSize(0);

  //Low stop mass
  // bulk region
    
    for(Int_t m_stop = 250; m_stop < 600; m_stop += 2*step) {
        for(Int_t m_LSP = 0; m_LSP < m_stop-200 && m_LSP < 500; m_LSP += 2*step) {
            TBox *box = new TBox(m_stop, m_LSP, m_stop+2*step, m_LSP+2*step);
            box->SetFillColor(kBlue-7);
            boxes.push_back(box);
            float xsec = crossSectionsbsb(m_stop);
            Float_t NEvents = xsec * Lref * 1000;
            if(considerXsec && NEvents > 50000 && NEvents < 1e6) totalNumberOfEvents += NEvents;
            else if(considerXsec && NEvents > 1e6) totalNumberOfEvents += 1000000;
            else totalNumberOfEvents += 50000;
            if(considerXsec && NEvents > 50000) std::cout << m_stop << " " << m_LSP << " " << NEvents << std::endl;
            else if(considerXsec && NEvents > 1e6) std::cout << m_stop << " " << m_LSP << " 1000000" << std::endl;
            else                                 std::cout << m_stop << " " << m_LSP << " 50000 " << std::endl;
        }
    }
    leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 50K", "F");
 
    
    // heavy stop region
    for(Int_t m_stop = 600; m_stop < 1000; m_stop += 2*step) {
        for(Int_t m_LSP = 0; m_LSP < 500; m_LSP += 2*step) {
            TBox *box = new TBox(m_stop, m_LSP, m_stop+2*step, m_LSP+2*step);
            box->SetFillColor(kRed-7);
            boxes.push_back(box);
            float xsec = crossSectionsbsb(m_stop);
            Float_t NEvents = xsec * Lref * 1000;
            if(considerXsec && NEvents > 100000 && NEvents < 1e6) totalNumberOfEvents += NEvents;
            else if(considerXsec && NEvents > 1e6) totalNumberOfEvents += 1000000;
            else totalNumberOfEvents += 100000;
            if(considerXsec && NEvents > 100000) std::cout << m_stop << " " << m_LSP << " " << NEvents << std::endl;
            else if(considerXsec && NEvents > 1e6) std::cout << m_stop << " " << m_LSP << " 1000000" << std::endl;
            else                                 std::cout << m_stop << " " << m_LSP << " 100000 " << std::endl;
        }
    }
    leg->AddEntry(boxes[boxes.size()-1], "50x50 GeV^{2}, 100K", "F");
    
     //1rst diagonal
    for(Int_t m_stop = 100; m_stop < 575; m_stop += step) {
        for(Int_t m_LSP = 0;  m_LSP < m_stop-50 && m_LSP<mLSPMax; m_LSP += step) {
        
            if(m_LSP < m_stop-200 ) continue;
            for(Int_t cx = 0; cx < 2; cx++) {
              for(Int_t cy = 0; cy < 2; cy++) {
                TBox *box = new TBox(m_stop+cx*step, m_LSP+cy*step, m_stop+(cx+1)*step, m_LSP+(cy+1)*step);
                box->SetFillColor(kGreen-7);
                boxes.push_back(box);
                float xsec = crossSectionsbsb(m_stop);
                Float_t NEvents = xsec * Lref * 1000;
              //  if(considerXsec && NEvents > 5e05) totalNumberOfEvents += 5e05;
                if(considerXsec && NEvents > 150000 && NEvents < 1e6) totalNumberOfEvents += NEvents;
                else if(considerXsec && NEvents > 1e6) totalNumberOfEvents += 1000000;
                else totalNumberOfEvents += 150000;
                if(considerXsec && NEvents > 150000) std::cout << m_stop << " " << m_LSP << " " << NEvents << std::endl;
                else if(considerXsec && NEvents > 1e6) std::cout << m_stop << " " << m_LSP << " 1000000" << std::endl;
                else                                 std::cout << m_stop << " " << m_LSP << " 150000 " << std::endl;
             }
          }
        }
    }
    leg->AddEntry(boxes[boxes.size()-1], "25x25 GeV^{2}, 150K", "F");

    /*
    for(Int_t m_stop = 100; m_stop < 500; m_stop += 2*step) {
        for(Int_t m_LSP = 0;  m_LSP < m_stop-80 && m_LSP<mLSPMax; m_LSP += 2*step) {
        
            if(m_LSP < m_stop-100) continue;
            for(Int_t cx = 0; cx < 2; cx++) {
              for(Int_t cy = 0; cy < 2; cy++) {
                TBox *box = new TBox(m_stop+cx*step, m_LSP+cy*step, m_stop+(cx+1)*step, m_LSP+(cy+1)*step);
                box->SetFillColor(kGreen-7);
                boxes.push_back(box);
                float xsec = crossSectionsbsb(m_stop);
                Float_t NEvents = xsec * Lref * 1000;
                if(considerXsec && NEvents > 150000) totalNumberOfEvents += NEvents;
                else totalNumberOfEvents += 150000;
             }
          }
        }
    }
 */
 

  can->cd();
  h->Draw();
  for(Size_t c = 0; c < boxes.size(); c++) {
    boxes[c]->Draw("l");
  }
  leg->Draw();

  TGraph *graph = new TGraph(2);
  graph->SetName("Graph");
  graph->SetTitle("Graph");
  graph->SetFillColor(1);
    
  graph->SetLineColor(kBlue);
  graph->SetLineStyle(2);
  graph->SetLineWidth(3);
  graph->SetMarkerStyle(20);
  graph->SetPoint(0,100,20);
  graph->SetPoint(1,2000,1920);
  graph->Draw("l, same");
    
  TLatex *tex3 = new TLatex(300,135,"m_{#tilde{t}_{1}} < m_{#tilde{#chi}_{0}^{1}} + m_{t}  ");
  tex3->SetTextAngle(46);
  tex3->SetLineWidth(2);
  tex3->SetTextColor(50);
  tex3->SetTextSize(0.035);
    
  tex3->Draw("same");
    
  TLatex *tex4 = new TLatex(230,200,"m_{#tilde{t}_{1}} < m_{#tilde{#chi}_{0}^{1}} + m_{W} +m_{b}  ");
  tex4->SetTextAngle(46);
  tex4->SetLineWidth(2);
  tex4->SetTextColor(50);
  tex4->SetTextSize(0.035);
    
  tex4->Draw("same");

  TGraph *graph2 = new TGraph(2);
  graph2->SetName("Graph");
  graph2->SetTitle("Graph");
  graph2->SetFillColor(1);
  graph2->SetMarkerStyle(20);
  graph2->SetPoint(0,175,0);
  graph2->SetPoint(1,2000,2000-175);
  graph2->Draw("l, same");

    
    
  char textNP[200];
  sprintf(textNP, "# of mass points: %d", boxes.size());
  char textNE[200];
  sprintf(textNE, "# of events: %d", totalNumberOfEvents);

  TText *NP = new TText(210, 1230, textNP);
  TText *NE = new TText(210, 1130, textNE);
  NP->SetTextSize(0.03);
  NE->SetTextSize(0.03);
  NP->Draw();
  NE->Draw();
  
  TLatex *tex = new TLatex(50,650,textNP);
  tex->SetLineWidth(2);
  tex->SetTextSize(0.03);
  tex->Draw("same");
  TLatex  *tex2 = new TLatex(50,550,textNE);
  tex2->SetLineWidth(2);
  tex2->SetTextSize(0.03);
  tex2->Draw("same");
    
  can->SaveAs("T2tt.png");

  delete tex;
  delete tex2; 
  delete tex3; 
  delete tex4; 
  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete graph;
  delete graph2;
  delete can;

  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());
  
  return totalNumberOfEvents;


}



/*
Int_t T2TTstrip() {
    
    bool considerXsec = true;
    
    Int_t mstopMin = 100;
    Int_t mstopMax = 1200;
    Int_t mLSPMax = 1000;
    Int_t step = 1;
    TCanvas *can = new TCanvas("T2TTc", "T2TTc");
    TH2F *h = new TH2F("T2TTh", "", mstopMax/step, 0, mstopMax, mstopMax/step, 0, mLSPMax);
    h->GetXaxis()->SetLabelSize(0.03);
    h->GetYaxis()->SetLabelSize(0.03);
    h->GetXaxis()->SetTitleSize(0.04);
    h->GetYaxis()->SetTitleSize(0.04);
    h->GetYaxis()->SetTitleOffset(1.4);
    h->GetXaxis()->SetTitle("M(stop) [GeV]");
    h->GetYaxis()->SetTitle("M(LSP) [GeV]");
    
    vector<TBox *> boxes;
    Int_t totalNumberOfEvents = 0;
    
    TLegend *leg = new TLegend(0.2, 0.7, 0.4, 0.9, "T2TT");
    leg->SetFillColor(kWhite);
    leg->SetTextFont(42);
    leg->SetTextSize(0.028);
    leg->SetLineWidth(0);
    leg->SetBorderSize(0);
    
    //Low stop mass
    // bulk region
    
    for(Int_t m_stop = 100; m_stop < 220; m_stop++) {
    //    for(Int_t m_LSP = 0; m_LSP < 11  m_LSP ++) {
            
          //  if (m_stop == 160 || m_stop==170 || m_stop== 175 || m_stop== 180 || m_stop== 190
         //       || m_stop== 200 || m_stop== 210) {
                
         //       if (m_LSP==1 || m_LSP==10){
            
         //   TBox *box = new TBox(m_stop, m_LSP, m_stop+2*step, m_LSP+2*step);
          //  box->SetFillColor(kBlue-7);
          //  boxes.push_back(box);
            Float_t NEvents = 2500000;
            
                    totalNumberOfEvents += NEvents;
       // }
   // }
            
    //    }
    }
    
    leg->AddEntry(boxes[boxes.size()-1], "Strip 2.5 M", "F");
    
    
    can->cd();
    h->Draw();
    for(Size_t c = 0; c < boxes.size(); c++) {
        boxes[c]->Draw("l");
    }
    leg->Draw();
    
    TGraph *graph = new TGraph(2);
    graph->SetName("Graph");
    graph->SetTitle("Graph");
    graph->SetFillColor(1);
    
    graph->SetLineColor(kBlue);
    graph->SetLineStyle(2);
    graph->SetLineWidth(3);
    graph->SetMarkerStyle(20);
    graph->SetPoint(0,100,20);
    graph->SetPoint(1,2000,1920);
    graph->Draw("l, same");
    
    TLatex *tex = new TLatex(300,135,"m_{#tilde{t}_{1}} < m_{#tilde{#chi}_{0}^{1}} + m_{t}  ");
    tex->SetTextAngle(46);
    tex->SetLineWidth(2);
    tex->SetTextColor(50);
    tex->SetTextSize(0.035);
    
    tex->Draw("same");
    
    TLatex *tex2 = new TLatex(230,200,"m_{#tilde{t}_{1}} < m_{#tilde{#chi}_{0}^{1}} + m_{W} +m_{b}  ");
    tex2->SetTextAngle(46);
    tex2->SetLineWidth(2);
    tex2->SetTextColor(50);
    tex2->SetTextSize(0.035);
    
    tex2->Draw("same");
    
    
    TGraph *graph2 = new TGraph(2);
    graph2->SetName("Graph");
    graph2->SetTitle("Graph");
    graph2->SetFillColor(1);
    graph2->SetMarkerStyle(20);
    graph2->SetPoint(0,175,0);
    graph2->SetPoint(1,2000,2000-175);
    graph2->Draw("l, same");
    
    
    
    char textNP[200];
    sprintf(textNP, "# of mass points: %d", boxes.size());
    char textNE[200];
    sprintf(textNE, "# of events: %d", totalNumberOfEvents);
    
    TText *NP = new TText(210, 1230, textNP);
    TText *NE = new TText(210, 1130, textNE);
    NP->SetTextSize(0.03);
    NE->SetTextSize(0.03);
    NP->Draw();
    NE->Draw();
    
    TLatex *tex3 = new TLatex(50,650,textNP);
    tex3->SetLineWidth(2);
    tex3->SetTextSize(0.03);
    
    tex3->Draw("same");
    TLatex *tex4 = new TLatex(50,550,textNE);
    tex4->SetLineWidth(2);
    tex4->SetTextSize(0.03);
    tex4->Draw("same");
    
    
  can->SaveAs("T2ttstrip.png");   
 
  delete NP;
  delete NE;
  delete h;
  delete leg;
  delete graph;
  delete graph2;
  delete tex;
  delete tex2;
  delete tex3;
  delete tex4;
  delete can;

  for(unsigned int c = 0; c < boxes.size(); c++) {
    delete boxes[c];
  }
  boxes.erase(boxes.begin(), boxes.end());

  return totalNumberOfEvents;

}

*/





//----------------------------------------Helper functions-------------------------------------------//
void loadCrossSectionglgl(string name) {

  ifstream f(name.c_str());
  while(!f.eof()) {
    Int_t m;
    Float_t xsec, unc;
    f >> m >> xsec >> unc;
    if(f.eof()) break;
    Mglgl.push_back(m);
    Xsecglgl.push_back(xsec);
    Uncglgl.push_back(unc);
  }
  f.close();
}

void loadCrossSectionsqsq(string name) {

  ifstream f(name.c_str());
  while(!f.eof()) {
    Int_t m;
    Float_t xsec, unc;
    f >> m >> xsec >> unc;
    if(f.eof()) break;
    Msqsq.push_back(m);
    Xsecsqsq.push_back(xsec);
    Uncsqsq.push_back(unc);
  }
  f.close();
}

void loadCrossSectionsbsb(string name) {

  ifstream f(name.c_str());
  while(!f.eof()) {
    Int_t m;
    Float_t xsec, unc;
    f >> m >> xsec >> unc;
    if(f.eof()) break;
    Msbsb.push_back(m);
    Xsecsbsb.push_back(xsec);
    Uncsbsb.push_back(unc);
  }
  f.close();
}

void loadCrossSectionchineu(string name) {

  ifstream f(name.c_str());
  while(!f.eof()) {
    Int_t m;
    Float_t xsec, unc;
    f >> m >> xsec >> unc;
    if(f.eof()) break;
    Mchineu.push_back(m);
    Xsecchineu.push_back(xsec);
    Uncchineu.push_back(unc);
  }
  f.close();
}


Float_t crossSectionglgl(Int_t m) {
  for(Size_t c = 0; c < Mglgl.size(); c++) {
    if(Mglgl[c] == m) return Xsecglgl[c];
  }
  return 0;
}

Float_t crossSectionsqsq(Int_t m) {
  for(Size_t c = 0; c < Msqsq.size(); c++) {
    if(Msqsq[c] == m) return Xsecsqsq[c];
  }
  return 0;
}

Float_t crossSectionsbsb(Int_t m) {
  for(Size_t c = 0; c < Msbsb.size(); c++) {
    if(Msbsb[c] == m) return Xsecsbsb[c];
  }
  return 0;
}


Float_t crossSectionchineu(Int_t m) {
  for(Size_t c = 0; c < Mchineu.size(); c++) {
    if(Mchineu[c] == m) return Xsecchineu[c];
  }
  return 0;
}

//---------------------------------------------------End------------------------------------------------------//


