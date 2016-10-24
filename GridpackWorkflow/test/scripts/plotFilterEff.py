#!/usr/bin/python
import os, sys
import ROOT as r
r.gROOT.SetBatch(True)
r.PyConfig.IgnoreCommandLineOptions = True
from DataFormats.FWLite import Events, Handle, Lumis
import glob
from collections import OrderedDict

fileBase = "/hadoop/cms/store/user/scasasso/mcProduction/AODSIM/T2bW_X05_dM-10to80/T2bW_X05_dM-10to80_genHT-160_genMET-80_{0}.root"


def main():
    

    fileList = [fileBase.format(i) for i in range(1,101)]

    modelDict = {}

    for file in fileList:
        print '  Inspecting file {0}'.format(file)

        lumis = Lumis(file)
        events = Events(file)
        handle  = Handle('GenFilterInfo')
        label = ('genFilterEfficiencyProducer')
        handleHead = Handle('GenLumiInfoHeader')
        labelHead = ('generator')
        
        
        for i,lum in enumerate(lumis):

            lum.getByLabel(labelHead,handleHead)
            genHeader = handleHead.product()
            lum.getByLabel(label,handle)
            genFilter = handle.product()
            
            model = genHeader.configDescription()
            modelShort = "_".join(model.split("_")[-2:])

            if not modelShort in modelDict.keys():
                modelDict[modelShort] = {}
                modelDict[modelShort]["pass"] = float(genFilter.numEventsPassed())
                modelDict[modelShort]["total"] = float(genFilter.numEventsTotal())
            else:
                modelDict[modelShort]["pass"] += float(genFilter.numEventsPassed())
                modelDict[modelShort]["total"] += float(genFilter.numEventsTotal())

    oModelDict = OrderedDict(sorted(modelDict.items()))

    print "Total mass points: ",len(oModelDict.keys())

    hFilterEff = r.TH1D('hFilterEff','Gen filter efficiency',len(oModelDict.keys()),0.,float(len(oModelDict.keys())))
    count = 1
    evtsTotAll = 0
    evtsPassAll = 0
    for model,evtsDict in oModelDict.iteritems():
        eff = evtsDict["pass"]/evtsDict["total"]
        evtsTotAll += evtsDict["total"]
        evtsPassAll += evtsDict["pass"]
        # print "{0} {1:.2f}".format(model,eff)
        hFilterEff.GetXaxis().SetBinLabel(count,model)
        hFilterEff.SetBinContent(count,eff)
        count += 1

    print "Average efficiency: {0:.2f}".format(evtsPassAll/evtsTotAll)
    c = r.TCanvas("c","c")
    c.cd()
    hFilterEff.Draw()
    c.SaveAs("FilterEff.pdf")
    c.SaveAs("FilterEff.png")

            


    return True
    

if __name__ == "__main__": main()
