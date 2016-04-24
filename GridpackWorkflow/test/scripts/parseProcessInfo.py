### Open Condor log files and retrieve the cross section and matching information from each Pythia job

### Author: Dustin Anderson

import os
import argparse
import glob
import matplotlib.pyplot as plt

def parseCrossSectionAndMatchingEfficiency(fname):
    with open(fname) as f:
        for line in f:
            if line.startswith('Total'):
                splitline = line.split('\t')
                eff,pm,efferr = splitline[-2].split(' ')
                xsec,pm,xsecerr = splitline[-4].split(' ')
                return float(xsec),float(xsecerr),float(eff),float(efferr)
    print "Warning in parseMatchingEfficiencyAndUncertainty: didn't find matching efficiency!"
    return None,None,None,None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inDir', help='directory containing condor log files')
    args = parser.parse_args()

    infiles = glob.glob(args.inDir+'/*.err.*')
    qcuts = []
    xsecs = []
    xsecerrs = []
    matcheffs = []
    matcherrs = []

    for infile in infiles:
        #parse qcut from filename
        #(filenames look like gen_<process>_<qcut>.err.<job ID>.0)
        qcut = int(infile.split('_')[-1].split('.')[0])
        found = False
        xsec,xsecerr,eff,efferr = parseCrossSectionAndMatchingEfficiency(infile)
        if eff:
            xsecs.append(xsec)
            xsecerrs.append(xsecerr)
            matcheffs.append(eff)
            matcherrs.append(efferr)
            qcuts.append(qcut)
    #plot cross section
    plt.errorbar(qcuts, xsecs, yerr=xsecerrs, fmt='o')
    plt.xlabel('qcut')
    plt.ylabel('Cross section after matching (pb)')
    plt.show()
    plt.savefig('xsec.pdf')
    #plot matching efficiency
    plt.errorbar(qcuts, matcheffs, yerr=matcherrs, fmt='o')
    plt.xlabel('qcut')
    plt.ylabel('Matching efficiency (%)')
    plt.show()
    plt.savefig('qcut.pdf')


