### Open Condor log files and retrieve the cross section and matching information from each Pythia job

### Author: Dustin Anderson

import os
import argparse
import glob
import matplotlib.pyplot as plt

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inDir', help='directory containing condor log files')
    args = parser.parse_args()

    infiles = glob.glob(args.inDir+'/*.err.*')
    qcuts = []
    matcheffs = []
    matcherrs = []

    for infile in infiles:
        #parse qcut from filename
        #(filenames look like gen_<process>_<qcut>.err.<job ID>.0)
        qcut = int(infile.split('_')[-1].split('.')[0])
        found = False
        with open(infile) as f:
            for line in f:
                if line.startswith('Total'):
                    splitline = line.split('\t')
                    matcheff = splitline[-2]
                    eff,pm,err = matcheff.split(' ')
                    matcheffs.append(float(eff))
                    matcherrs.append(float(err))
                    found = True
                    break
        if found:
            qcuts.append(qcut)
        else:
            print "Couldn't retrieve matching efficiency from file",infile
    plt.errorbar(qcuts, matcheffs, yerr=matcherrs, fmt='o')
    plt.xlabel('qcut')
    plt.ylabel('Matching efficiency (%)')
    plt.show()
    plt.savefig('qcut.pdf')
