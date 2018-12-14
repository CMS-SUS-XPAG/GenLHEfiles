### Make many DJR plots at once
### (files in the input directory should have names of the form GEN_<process>_<qcut>.root)

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

def wrapper(args):
    print "Will do edmPickMerge for the following files"
    infile_path, files, qcut, proc  = args
    print files
    filelist = [file.replace('/hadoop/cms','') for file in files]
    outfile = 'GEN_'+proc+'_'+str(qcut)+'.root'
    os.system('edmCopyPickMerge inputFiles='+','.join(filelist)+' outputFile='+outfile)
    os.system('mv '+outfile+' '+infile_path+'/'+outfile)
    #results[qcut:infile_path+'/'+outfile]
    return (qcut, infile_path+'/'+outfile)

def parseQcuts(proc, infile_path):
    #get files from input directory and read the qcuts from the filenames
    infiles = glob.glob(infile_path+'/GEN_'+proc+'*.root')
    qcuts = {}

    #get the qcut from each input filename
    for infile in infiles:
        try:
            qcut = os.path.basename(infile).split('_')[-1].replace('.root','')
            if qcuts.has_key(int(qcut)):
                qcuts[int(qcut)].append(infile)
            else:
                qcuts[int(qcut)] = [infile]
            print "qcut",qcut,"from file",infile
        except IndexError:
            print "Unable to parse qcut from filename:",infile

    #merge multiple input files for the same qcut value
    jobs = []
    merged = []
    results = {}

    for qcut,files in qcuts.iteritems():
        outfile = 'GEN_'+proc+'_'+str(qcut)+'.root'
        jobs.append((infile_path, files, qcut, proc))
        merged.append((qcut, infile_path+'/'+outfile))
    

    #print jobs[0][0]
    #print jobs[0][1]
    #print jobs[0][2]
    #print jobs[0][3]


    from multiprocessing import Pool
    pool = Pool(processes=6)
    res = pool.map(wrapper, jobs)
    pool.close()
    pool.join()

    #for r in results.keys():
    #    print "Adding merged files to list:", r, results[r]
    #    merged.append((r, results[r]))

    #sort by qcut
    merged.sort(key=itemgetter(0))
    return merged

def makeDJRPlots(f, proc, qcuts, texOnly=False, qmin=0, qmax=200, njetmax=2):
    #load libraries
    gSystem.Load("libFWCoreFWLite.so")
    FWLiteEnabler.enable()
    gSystem.Load("libDataFormatsFWLite.so")
    gSystem.Load("libDataFormatsPatCandidates.so")
    gROOT.LoadMacro(os.path.join(os.path.abspath('.').split('GridpackWorkflow')[0],'GridpackWorkflow/test/scripts/plotdjr.C')) # probably not the most beautiful way to get the right plotdjr.C macro
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
        if iqcut > qmax or iqcut < qmin: continue
        qcut = str(iqcut) 
        fout = proc+"_"+qcut
        if not texOnly: #create the pdf
            print 'making DJR plots with input',fin,'and output',fout
            plotdjr(fin, fout)

        #include in TeX file
        f.write("\\begin{frame} \n")
        f.write("\\frametitle{"+proc.replace("_"," ") +" qCut = "+ qcut+"} \n")
        if njetmax < 3:
            f.write("\\includegraphics[width=0.5\\textwidth]{"+proc+"_"+qcut+"_djr0.pdf} \n")
            f.write("\\includegraphics[width=0.5\\textwidth]{"+proc+"_"+qcut+"_djr1.pdf}\\\\ \n")
        else:
            f.write("\\includegraphics[width=0.5\\textwidth]{"+proc+"_"+qcut+"_djr0.pdf} \n")
            f.write("\\includegraphics[width=0.5\\textwidth]{"+proc+"_"+qcut+"_djr1.pdf}\\\\ \n")
            f.write("\\includegraphics[width=0.5\\textwidth]{"+proc+"_"+qcut+"_djr2.pdf} \n")
            f.write("\\includegraphics[width=0.5\\textwidth]{"+proc+"_"+qcut+"_djr3.pdf}\\\\ \n")
        f.write("\\end{frame} \n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('proc', help='physics process')
    parser.add_argument('directory', help='path to dir containing input files')
    parser.add_argument('--tex-only', dest='texOnly', action='store_true', 
            help='only write latex document, skip making pdfs')
    parser.add_argument('--qcut-range', dest='qcutRange', nargs=2, type=int, default=[50,100], 
            help="Range of qcuts to consider")
    parser.add_argument('--nJetMax', help="nJetMax argument in the fragment", default=2)
    args = parser.parse_args()

    proc = args.proc
    infile_path = args.directory
    qcuts = parseQcuts(proc, infile_path)
    qmin = args.qcutRange[0]
    qmax = args.qcutRange[1]
    njetmax = args.nJetMax

    fname = "plots_"+proc+".tex"
    f = open(fname,'w')
    f.write("\\documentclass{beamer}\n")
    f.write("\\beamertemplatenavigationsymbolsempty\n")
    f.write("\\usepackage{graphicx}\n")
    f.write("\\begin{document}\n")
    makeDJRPlots(f, proc, qcuts, texOnly=args.texOnly, qmin=qmin, qmax=qmax, njetmax=njetmax)
    f.write("\\end{document}\n")
    f.close()
    subprocess.call(['pdflatex', fname])
