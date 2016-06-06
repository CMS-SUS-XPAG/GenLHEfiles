import sys
import ROOT as rt

def cleanstring(s):
    for c in '+-*/!@#$%^&()[]{}?\\_:=':
        s = s.replace(c,'')
    return s

#define models
class model:
    def __init__(self, nbinsx, xmin, xmax, nbinsy, ymin, ymax, nconfigs):
        self.nbinsx = nbinsx
        self.xmin = xmin
        self.xmax = xmax
        self.nbinsy = nbinsy
        self.ymin = ymin
        self.ymax = ymax
        self.nconfigs = nconfigs

models = {}
models["T5qqqqVV"] = model(34, 600, 2300, 32, 0, 1600, 500)
models["T5qqqqVV_dM20"] = model(24, 600, 1800, 26, 0, 1300, 500)
models["T5ZZ"] = model(20, 800, 1800, 36, 0, 1800, 500)
models["T2bb"] = model(52,300,1600,44,0,1100,500)
models["T5Wg"] = model(52,800,2100,78,150,2100,500)
models['T2qq'] = model(30,300,1800,70,0,1400,500)
models["T2bt"] = model(41,200,1225,27,0,675,308)
models["T2tt"] = model(35,350,1225,27,0,675,308)
models["TChiStauStau_x0p5"] = model(25,100,725,13,0,325,280)
models["T5ttcc"] = model(44,600,1700,140,0,1400,500)
models["TChipmSlepSnu"] = model(28,100,800,24,0,600,500)
models["T6ttWW"] = model(36,300,1200,48,0,1200,500)

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
                 ]
    histparams2D = [
                  ("mlsp:mprod##colztext", "Grid", (m.nbinsx,m.xmin,m.xmax,m.nbinsy,m.ymin,m.ymax)),
                  ]

    if mname in ['T5qqqqVV','T5qqqqVV_dM20','T5ZZ','T5ttcc','TChipmSlepSnu','T6ttWW']:
        histparams += [
                  ("mc_mass#abs(mc_id)==24", "W Mass", (100, 0, 150)),
                  ("mc_mass#abs(mc_id)==23", "Z Mass", (100, 0, 150)),
                  ("mc_mass#abs(mc_id)==24&&mprod-mlsp<150", "W Mass (compressed points)", (100, 0, 150)),
                  ("mc_mass#abs(mc_id)==23&&mprod-mlsp<150", "Z Mass (compressed points)", (100, 0, 150)),
                  ("Sum$(abs(mc_id)==23||abs(mc_id)==24)", "Number of bosons in event", (5, 0, 5)),
                  ("ntruleps", "Lepton multiplicity", (5, 0, 5)),
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
    if mname == 'T2bt':
        histparams += [
                ("mc_mass#abs(mc_id)==6", "Top Mass", (100, 100, 250)),
                ]
    if mname == 'T6ttWW':
        histparams += [
                ("mc_mass#abs(mc_id)==24&&mlsp<130", "W Mass (Chargino mass < 130 GeV)",(100,0,150))
                ]

    hists = {}
    for params in histparams:
        hists[params[0]] = rt.TH1F(cleanstring(params[0]),params[1],*params[2])
    for params in histparams2D:
        hists[params[0]] = rt.TH2F(cleanstring(params[0]),params[1],*params[2])

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
