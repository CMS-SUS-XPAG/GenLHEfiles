1#!/usr/bin/python
import os, sys
import ROOT as r
r.gROOT.SetBatch(True)
r.PyConfig.IgnoreCommandLineOptions = True
from DataFormats.FWLite import Events, Handle, Lumis
import glob
from collections import OrderedDict
from validateScan import models
import optparse

def parse_args():
    parser = optparse.OptionParser()
    parser.add_option('-m','--model', default=None, help="Model name as specified in the fragment.")

    options,args = parser.parse_args()
    return options


def printPlot(plot):
    
    pTag = plot.GetName().split("_")[0]
    if pTag == "h": opt = "HIST"
    elif pTag == "h2": opt = "COLZTEXT"

    name = "_".join(plot.GetName().split("_")[1:])
    cName = "c_"+name
    c = r.TCanvas(cName,cName)
    c.cd()
    plot.Draw(opt)
    c.SaveAs(name+".pdf")
    

def loop(model,m):        
    
    fileList = [fileBase.format(model,i) for i in range(1,101)]
    if len(fileList) == 0: raise ValueError("File list is empty!")

    plotScan = True
    if getattr(m,"scanTup",None) == None: 
        print "[WARNING] You have to define scanTup=((\"nameX\",pdgId),(\"nameY\",pdgId)) for model {0} in order to plot the scan.".format(model)
        plotScan = False

    # Histograms gen particles
    histos = {}
    histos["susy_pdgId_1"] = r.TH1D("h_susy_pdgId_1","SUSY particle in the event (id < 1000000)",40,0.,40.)
    histos["susy_pdgId_2"] = r.TH1D("h_susy_pdgId_2","SUSY particle in the event (id > 1000000)",40,0.,40.)
    histos["susy_scan"]    = r.TH2D("h2_susy_scan","SUSY scan",m.nbinsx,m.xmin,m.xmax,m.nbinsy,m.ymin,m.ymax)
    histos["sm_pdgId"]     = r.TH1D("h_sm_pdgId","SM particles in the event",40,0.,40.)
    histos["sm_z_mass"]    = r.TH1D("h_sm_z_mass","Mass of the Z(*) boson",120,0.,120.)
    histos["sm_w_mass"]    = r.TH1D("h_sm_w_mass","Mass of the W(*) boson",120,0.,120.)

    # Histograms lumi-block
    histos["lumi_cfgId"]   = r.TH1D("h_lumi_cfgId","Config ID",m.nconfigs,0.,float(m.nconfigs)+0.5)

    # Loop over files
    for file in fileList:
        print '  Running on file {0}'.format(file)

        lumis = Lumis(file)
        events = Events(file)
        handle = Handle ('std::vector<reco::GenParticle>')
        label = 'genParticles'
        handleHead = Handle('GenLumiInfoHeader')
        labelHead = ('generator')

        # Loop over lumi blocks
        for i,lum in enumerate(lumis):

            lum.getByLabel(labelHead,handleHead)
            genHeader = handleHead.product()

            cfgId = genHeader.randomConfigIndex()
            histos["lumi_cfgId"].Fill(cfgId)

        # Loop over events
        for iev,ev in enumerate(events):
            ev.getByLabel(label,handle)
            genps = handle.product()

            # print "Event n. ",iev

            # Loop over gen particles
            mX, mY = 0., 0. # for the 2D scan plot
            for p in genps:
                id = abs(p.pdgId())
                status = p.status()

                if (not status in range(21,25) + [1]): continue
                
                # SUSY particles
                if id > 1000000:
                    if id > 2000000: 
                        idPruned = id - 2000000
                        histos["susy_pdgId_2"].Fill(idPruned)
                    else: 
                        idPruned = id - 1000000
                        histos["susy_pdgId_1"].Fill(idPruned)
                                
                    if plotScan:
                        if id == m.scanTup[0][1] and mX == 0.: mX = p.mass()
                        elif id == m.scanTup[1][1] and mY == 0.: mY = p.mass()
                
                # SM particles
                elif id in SM_ids:
                    histos["sm_pdgId"].Fill(id)
                    if id == 23 and status == 22: histos["sm_z_mass"].Fill(p.mass())
                    if id == 24 and status == 22: histos["sm_w_mass"].Fill(p.mass())
            
            # 2-D plot of the scan
            if plotScan: 
                histos["susy_scan"].Fill(mX,mY)
                histos["susy_scan"].GetXaxis().SetTitle(m.scanTup[0][0])
                histos["susy_scan"].GetYaxis().SetTitle(m.scanTup[1][0])

    # Print plots
    for name,histo in histos.iteritems(): printPlot(histo)
    

if __name__ == "__main__": 

    fileBase = "/hadoop/cms/store/user/"+os.environ["USER"]+"/mcProduction/AODSIM/{0}/{0}_{1}.root"
    SM_ids = [23,24,25] + range(1,7) + [11,13,15] #SM particles we are interested in

    opt = parse_args()
    if opt.model not in models:
        raise ValueError("The model {0} is NOT defined in validateScan.py".format(opt.model))

    modelClass = models[opt.model]
    
    loop(opt.model,modelClass)
