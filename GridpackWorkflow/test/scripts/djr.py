### Make many DJR plots at once
### (files in the input directory should have names of the form GEN_<process>_<qcut>_<random seed>.root)

### Authors: 
### Ana Ovcharova
### Dustin Anderson

import os
import sys
import subprocess
import glob 
import argparse
from operator import itemgetter
from ROOT import *

def parseQcuts(proc, infile_path):
    #get files from input directory and read the qcuts from the filenames
    infiles = glob.glob(infile_path+'/GEN_'+proc+'*.root')
    qcuts = []

    #get the qcut from each input filename
    for infile in infiles:
        try:
            qcut = os.path.basename(infile).split('_')[-1].replace('.root','')
            qcuts.append((int(qcut),infile))
            print "qcut",qcut,"from file",infile
        except IndexError:
            print "Unable to parse qcut from filename:",infile

    #sort by qcut
    qcuts.sort(key=itemgetter(0))

    return qcuts

def makeDJRPlots(f, proc, qcuts, texOnly=False):
    #load libraries
    gSystem.Load("libFWCoreFWLite.so")
    AutoLibraryLoader.enable()
    gSystem.Load("libDataFormatsFWLite.so")
    gSystem.Load("libDataFormatsPatCandidates.so")
    gROOT.LoadMacro(os.environ['CMSSW_BASE']+"/src/plotdjr.C")
    gROOT.SetBatch(kTRUE)

    #TeX header
    print "Plotting DJR for",proc
    f.write("\\begin{frame} \n")
    f.write("\\begin{center} \n")
    f.write(proc.replace("_"," ") +" \n")
    f.write("\\end{center} \n")
    f.write("\\end{frame} \n")

    #plot for each qcut
    for (iqcut,fin) in qcuts:
        qcut = str(iqcut) 
        fout = proc+"_"+qcut
        if not texOnly: #create the pdf
            plotdjr(fin, fout)

        #include in TeX file
        f.write("\\begin{frame} \n")
        f.write("\\frametitle{"+proc.replace("_"," ") +" qCut = "+ qcut+"} \n")
        f.write("\\includegraphics[width=0.5\\textwidth]{"+proc+"_"+qcut+"_djr0.pdf} \n")
        f.write("\\includegraphics[width=0.5\\textwidth]{"+proc+"_"+qcut+"_djr1.pdf}\\\\ \n")
        #f.write("\\includegraphics[width=0.5\\textwidth]{"+proc+"_"+qcut+"_djr2.pdf} \n")
        #f.write("\\includegraphics[width=0.5\\textwidth]{"+proc+"_"+qcut+"_djr3.pdf}\\\\ \n")
        f.write("\\end{frame} \n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('proc', help='physics process')
    parser.add_argument('directory', help='path to dir containing input files')
    parser.add_argument('--tex-only', dest='texOnly', action='store_true', 
            help='only write latex document, skip making pdfs')
    args = parser.parse_args()

    proc = args.proc
    infile_path = args.directory
    qcuts = parseQcuts(proc, infile_path)

    fname = "plots_"+proc+".tex"
    f = open(fname,'w')
    f.write("\\documentclass{beamer}\n")
    f.write("\\beamertemplatenavigationsymbolsempty\n")
    f.write("\\usepackage{graphicx}\n")
    f.write("\\begin{document}\n")
    makeDJRPlots(f, proc, qcuts, texOnly=args.texOnly)
    f.write("\\end{document}\n")
    f.close()
    subprocess.call(['pdflatex', fname])
