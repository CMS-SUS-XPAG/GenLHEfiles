import sys
import os
import glob
from optparse import OptionParser
import subprocess
sys.path.append("./python/")
from Models import T6ttWH
from Models import T6ttHH
from Models import T1ttbb
from Models import T5tttt
from Models import T2tb
from Tools import tools

def outputFileName(inputfilename,opt,mSp,mLsp):
    labels = inputfilename.replace(".gz","").split("_")
    runlabel = "none"
    for label in labels:
        if label.find("run") != -1: runlabel = label
    
    if options.x>0:
        return "%s_%s_%ij_%i_%i_x%0.2f_%s.lhe" %(opt.energy,opt.model,opt.npartons,mSp,mLSP,opt.x,runlabel)
    elif options.mLSPfixed>0:
        return "%s/%s_%s_%ij_%i_%i_%i_%s.lhe" %(opt.outdir,opt.energy,opt.model,opt.npartons,mSp,mLSP,options.mLSPfixed,runlabel)
    else: 
        return "%s/%s_%s_%ij_%i_%i_%s.lhe" %(opt.outdir,opt.energy,opt.model,opt.npartons,mSp,mLSP,runlabel)
def setModel(model):
    if model == "T2tb": return T2tb.T2tb()
    if model == "T6ttHH": return T6ttHH.T6ttHH()
    if model == "T6ttWH": return T6ttWH.T6ttWH()
    if model == "T1ttbb": return T1ttbb.T1ttbb()
    if model == "T5tttt": return T5tttt.T5tttt()
    return "None"

if __name__ == '__main__':
    parser = tools.defineParser()
    (options,args) = parser.parse_args()

    # check that the input file list is not empty
    if len(args) <1:
        parser.print_help()
        sys.exit(-1)

    # if needed, create the output directoy
    if not os.path.exists(options.outdir): os.system("mkdir %s" %options.outdir)

    #set the model
    model = setModel(options.model)
    if options.pdgId>0: model.setPdgId(options.pdgId)
    if model == 'None':
        print "Model %s not implemented" %options.model
        sys.exit(-1)


    mGomin = int(options.mGomin)
    mGomax = int(options.mGomax)
    mGofixed = int(options.mGofixed)
    stepGo = int(options.stepGo)

    scan2D = (mGofixed>0)
    
    mStmin = int(options.mStmin)
    mStmax = int(options.mStmax)
    mStfixed = int(options.mStfixed)
    stepSt = int(options.stepSt)
    
    mLSPmin = int(options.mLSPmin)
    mLSPmax = int(options.mLSPmax)
    mLSPfixed = int(options.mLSPfixed)
    stepLSP = int(options.stepLSP)

        
    for file in args:
        if not os.path.exists(file):
            print "File %s not found" %file
            continue
        if file[-3:] == ".gz":
            os.system("gunzip %s" %file)
            file = file.replace(".gz","")
        mGo = model.getMass(file)    
        #loop over the mLSP/mSp values
        nLSP = int((options.mLSPmax-options.mLSPmin)/options.stepLSP)+1
        for i in range(0,nLSP):
            mLSP = options.mLSPmin + options.stepLSP*i
            if mGo-mLSP <= options.deltaM: continue
            nSp = int((options.mSpmax-options.mSpmin)/options.stepSp)+1
            for q in range(0,nSp):
                mSp = options.mSpmin + options.stepSp*q
                if mGo-mSp <= options.deltaM: continue
                outfile =outputFileName(file,options,mGo,mSp,mLSP)
                if options.x<0: print "Creating the LHE file %s for mGo = %f, mSp = %f, and mLSP = %f"  %(outfile,mGo,mSp,mLSP)
                else: print "Creating the LHE file %s for mGo = %f mSp = %f mLSP = %f and x = %f"  %(outfile,mGo,mSp,mLSP,options.x)
                model.setMassSpectrum(mGo,mSp,mLSP,options.x)
                model.replace(file, outputFileName(file,options,mGo,mSp,mLSP))

