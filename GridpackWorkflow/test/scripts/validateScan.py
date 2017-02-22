import sys
import ROOT as rt

def cleanstring(s):
    for c in '+-*/!@#$%^&()[]{}?\\_:=':
        s = s.replace(c,'')
    return s

#define models
class model:
    def __init__(self, nbinsx, xmin, xmax, nbinsy=1, ymin=0, ymax=0, nconfigs=500,scanTup=None):
        self.nbinsx = nbinsx
        self.xmin = xmin
        self.xmax = xmax
        self.nbinsy = nbinsy
        self.ymin = ymin
        self.ymax = ymax
        self.nconfigs = nconfigs
        self.scanTup = scanTup



models = {}
models["T5qqqqVV"] = model(34, 600, 2300, 32, 0, 1600, 500)
models["T5qqqqVV_dM20"] = model(24, 600, 1800, 26, 0, 1300, 500)
models["T5qqqqVV_dM15_mLSP-300"] = model(30, 600, 2100, 1, 300, 350, 30)
models["T5qqqqVV_dM10_mLSP-300"] = model(30, 600, 2100, 1, 300, 350, 30)
models["T5qqqqVV_dM5_mLSP-300"] = model(30, 600, 2100, 1, 300, 350, 30)
models["T5qqqqVV_dM20_ext"] = model(30, 600, 2100, 32, 0, 1600, 1000)
models["T5ZZ"] = model(20, 800, 1800, 36, 0, 1800, 500)
models["T2bb"] = model(52,300,1600,44,0,1100,500)
models["T5Wg"] = model(52,800,2100,78,150,2100,500)
models['T2qq'] = model(30,300,1800,70,0,1400,500)
models["T2bt"] = model(41,200,1225,27,0,675,308)
models["T2tt"] = model(35,350,1225,27,0,675,308)
models["T2tt_mStop1250to1500"] = model(6,1250,1501,27,0,651,84)
models["TChiStauStau_x0p5"] = model(25,100,725,13,0,325,280)
models["TChiSlepSnu_tauenriched_x0p05"] = model(25,100,725,13,0,325,280)
models["TChiSlepSnu_tauenriched_x0p95"] = model(25,100,725,13,0,325,280)
models["TChiSlepSnu_tauenriched_x0p5"] = model(25,100,725,13,0,325,280)
models["T5ttcc"] = model(44,600,1700,140,0,1400,500)
models["TChipmSlepSnu"] = model(28,100,800,24,0,600,500)
models["T6ttWW"] = model(36,300,1200,100,0,1200,500)
#models["T6ttWW"] = model(36,300,1200,48,0,1200,500)
models["TChiWG"] = model(nbinsx=41,xmin=300,xmax=1300,nconfigs=41)
models["T1ttbb"] = model(nbinsx=31,xmin=800,xmax=2300,nbinsy=33,ymin=0.,ymax=1600,nconfigs=646)
models["TChiHH_HToGG"] = model(35, 125, 1000, 1, 0.5, 1.5, 35)
models["TChiHH_HToWWZZTauTau_HToWWZZTauTau"] = model(35, 125, 1000, 1, 0.5, 1.5, 35)
models["TChiHZ_HToGG"] = model(35, 125, 1000, 1, 0.5, 1.5, 35)
models["TChiHZ_HToWWZZTauTau_ZToLL"] = model(35, 125, 1000, 1, 0.5, 1.5, 35)
models["TChiHZ_HToWWZZTauTau_ZToLL"] = model(35, 125, 1000, 1, 0.5, 1.5, 35)
models["TChiZZ_ZToLL"] = model(36, 100, 1000, 1, 0.5, 1.5, 36)
models["TChiZZ_ZToLL_ZToLL"] = model(36, 100, 1000, 1, 0.5, 1.5, 36)
models["TChipmWW"] = model(19, 100., 575.,31 , 0., 310.,264)
models["TChiNG"] = model(nbinsx=41,xmin=300,xmax=1325,nconfigs=41)
models["T2bW_X05_dM-10to80"] = model(nbinsx=23,xmin=250,xmax=801,nbinsy=56,ymin=250,ymax=801,nconfigs=184)
models["T2bW_X05_dM-10to80_2Lfilter"] = model(nbinsx=23,xmin=250,xmax=801,nbinsy=56,ymin=250,ymax=801,nconfigs=184)
models["T6ttHZ_BR-H_0p6"] = model(nbinsx=29,xmin=300.,xmax=1025.,nbinsy=106,ymin=175.,ymax=725.,nconfigs=154)
models["T8bbllnunu_XCha0p5"] = model(nbinsx=53,xmin=200.,xmax=1501.,nbinsy=27,ymin=0.,ymax=651.,nconfigs=393)
models["TChiSlepSnu_x0p5"] = model(nbinsx=25, xmin=100., xmax=1301., nbinsy=33, ymin=0., ymax=800.,nconfigs=336)
models["ttH_HToTT"] = model(nbinsx=56, xmin=350., xmax=901., nbinsy=56, ymin=350., ymax=901.,nconfigs=18)
models["tHq_HToTT"] = model(nbinsx=11, xmin=350., xmax=551., nbinsy=11, ymin=350., ymax=551.,nconfigs=11)
models["tHW_HToTT"] = model(nbinsx=11, xmin=350., xmax=551., nbinsy=11, ymin=350., ymax=551.,nconfigs=11)
models["T2qqgamma"] = model(nbinsx=7, xmin=200., xmax=501., nbinsy=71, ymin=150., ymax=501.)
models["Higgsino-N2C1"] = model(nbinsx=8, xmin=100., xmax=241., nbinsy=965, ymin=0., ymax=241.,nconfigs=48,scanTup=(("N2",1000023),("C1",1000024)))

if __name__ == '__main__':
    rt.gROOT.SetBatch()

    #get input
    if len(sys.argv) < 2:
        sys.exit("Please specify a model")
    mname = sys.argv[1]
    f = rt.TFile.Open("genbaby_"+mname+".root")
    t = f.Get("tree")
    if mname not in models:
        sys.exit("Model "+mname+" not implemented!")
    m = models[mname]

    #sanity checks
    print "Model:",mname
    print "Number of events in tree:",t.GetEntries()

    #make histograms
    # each lumiblock must be in one bin, to see whether there are lumiblocks where no events were produced
    # which would indicate a problem 
    histparams = [("20*(run-1)+lumiblock", "Lumiblock index", (2000, 0, 2000)),
                  ("mprod", "Produced particle mass", (m.nbinsx, m.xmin, m.xmax)),
                  ("mlsp", "LSP mass", (m.nbinsy, m.ymin, m.ymax)),
                  ("gen_cfgid", "Config ID", (m.nconfigs, 0, m.nconfigs)),
                  ("abs(mc_id)-1000000#abs(mc_id)>1000000", "SUSY particles in event", (30, 0, 30)),
                  ("abs(mc_id)-2000000#abs(mc_id)>2000000", "Other SUSY particles in event", (30, 0, 30)),
                  ("abs(mc_id)#abs(mc_id)<1000000", "Non-SUSY particles in event", (30, 0, 30)),
                 ]
    histparams2D = [
                  ("mlsp:mprod##colztext", "Grid", (m.nbinsx,m.xmin,m.xmax,m.nbinsy,m.ymin,m.ymax)),
                  ]

    if mname in ['T5qqqqVV','T5qqqqVV_dM20','T5qqqqVV_dM20_ext','T5ZZ','T5ttcc',
            'TChipmSlepSnu','T6ttWW','TChipmWW',
            'T5qqqqVV_dM15_mLSP-300', 'T5qqqqVV_dM5_mLSP-300', 'T5qqqqVV_dM10_mLSP-300',]:
        histparams += [
                  ("mc_mass#abs(mc_id)==24", "W Mass", (100, 0, 150)),
                  ("mc_mass#abs(mc_id)==23", "Z Mass", (100, 0, 150)),
                  ("mc_mass#abs(mc_id)==24&&mprod-mlsp<150", "W Mass (compressed points)", (100, 0, 150)),
                  ("mc_mass#abs(mc_id)==23&&mprod-mlsp<150", "Z Mass (compressed points)", (100, 0, 150)),
                  ("Sum$(abs(mc_id)==23||abs(mc_id)==24)", "Number of bosons in event", (5, 0, 5)),
                  ("ntruleps", "Lepton multiplicity", (5, 0, 5)),
                  ]

    if mname == 'T8bbllnunu_XCha0p5':
        histparams += [
            ("Sum$(abs(mc_id)==11||abs(mc_id)==13||abs(mc_id)==15)", "Number of leptons in event (e,mu,taus)", (5, 0, 5)),
            ]

    if mname == 'T5Wg':
        histparams += [
            ("mc_mass#abs(mc_id)==24&&mlsp==10", "W Mass (m_{LSP} = 10 GeV)", (60, 0, 20)),
            ("mc_mass#abs(mc_id)==24&&mlsp==25", "W Mass (m_{LSP} = 25 GeV)", (100, 0, 50)),
            ("mc_mass#abs(mc_id)==24&&mlsp==50", "W Mass (m_{LSP} = 50 GeV)", (140, 0, 70)),
            ]

    if mname == 'T5ZZ':
        histparams += [
                ("mc_mass#abs(mc_id)==23&&mlsp<90", "Z Mass (m_{NLSP} < 90 GeV)", (100, 0, 150)),
                ("mc_mass#abs(mc_id)==23&&mlsp==25", "Z Mass (m_{NLSP} = 25 GeV)", (100, 0, 150)),
                ("mc_mass#abs(mc_id)==23&&mlsp==50", "Z Mass (m_{NLSP} = 50 GeV)", (100, 0, 150)),
                ]
    if mname == 'T6ttHZ_BR-H_0p6':
        histparams += [
                ("mc_mass#abs(mc_id)==23", "Z Mass", (100, 0, 150)),
                ("mc_mass#abs(mc_id)==25", "Higgs Mass", (50, 115, 135)),
                ("ntruleps", "Lepton multiplicity", (7, 0, 7)),
                ]
    if mname == 'T2bt':
        histparams += [
                ("mc_mass#abs(mc_id)==6", "Top Mass", (100, 100, 250)),
                ]
    if mname == 'T6ttWW':
        histparams += [
                ("mc_mass#abs(mc_id)==24&&mlsp<130", "W Mass (Chargino mass < 130 GeV)",(100,0,150)),
                ("mc_mass#abs(mc_id)==6", "Top Mass", (100, 100, 250)),
                ("mc_mass#abs(mc_id)==6&&mprod-mlsp<175", "Top Mass (dM < 175)", (100, 50, 250)),
                ("mc_mass#abs(mc_id)==6&&mprod-mlsp==88", "Top Mass (dM = 88)", (100, 50, 250)),
                ("mc_mass#abs(mc_id)==6&&mprod-mlsp==100", "Top Mass (dM = 100)", (100, 50, 250)),
                ("mc_mass#abs(mc_id)==6&&mprod-mlsp==125", "Top Mass (dM = 125)", (100, 50, 250)),
                ("mc_mass#abs(mc_id)==6&&mprod-mlsp==150", "Top Mass (dM = 150)", (100, 50, 250)),
                ("mc_mass#abs(mc_id)==6&&mprod-mlsp==175", "Top Mass (dM = 175)", (100, 50, 250)),
                ("mc_mass#abs(mc_id)==6&&mprod-mlsp==200", "Top Mass (dM = 200)", (100, 50, 250)),
                ]
    if mname == 'T5ttcc':
        histparams += [
                ("mc_mass#abs(mc_id)==6", "Top Mass", (100, 100, 250)),
                ("mc_mass#abs(mc_id)==6&&mprod-mlsp==108", "Top Mass (dM = 108)", (100, 50, 250)),
                ("mc_mass#abs(mc_id)==6&&mprod-mlsp==125", "Top Mass (dM = 125)", (100, 50, 250)),
                ("mc_mass#abs(mc_id)==6&&mprod-mlsp==150", "Top Mass (dM = 150)", (100, 50, 250)),
                ("mc_mass#abs(mc_id)==6&&mprod-mlsp==175", "Top Mass (dM = 175)", (100, 50, 250)),
                ("mc_mass#abs(mc_id)==6&&mprod-mlsp==200", "Top Mass (dM = 200)", (100, 50, 250)),
                ]
    if 'TChi' in mname:
        histparams += [
                ("mc_mass#abs(mc_id)==23", "Z Mass", (100, 0, 150)),
                ("mc_mass#abs(mc_id)==25", "Higgs Mass", (100, 0, 150)),
                ("mc_id#mc_direct_mom==25", "Higgs daughters", (30, 0, 30)), # higgs daughters
                ("mc_id#mc_direct_mom==23", "Z daughters", (30, 0, 30)), # Z daughters
                ("ntruleps", "Lepton multiplicity", (5, 0, 5)),
                ]
    if 'T2bW' in mname:
        histparams += [
            ("mc_mass#abs(mc_id)==24", "W Mass", (100, 0., 40.)),
            ]

    hists = {}
    for params in histparams:
        hists[params[0]] = rt.TH1F(cleanstring(params[0]),params[1],*params[2])
    for params in histparams2D:
        hists[params[0]] = rt.TH2F(cleanstring(params[0]),params[1],*params[2])
        hists[params[0]].SetStats(0)

    #fill histograms and print
    c = rt.TCanvas("c", "c", 800, 600)
    for name,hist in hists.iteritems():
        splitname = name.split('#')
        cleanname = cleanstring(name)
        var = splitname[0]
        cut = ''
        opt = ''
        if len(splitname) > 1:
            cut = splitname[1]
        if len(splitname) > 2:
            opt = splitname[2]
        t.Draw(var+'>>'+cleanname, cut)
        hist.Draw(opt)
        c.Print(mname+'_'+cleanname+'.pdf')
