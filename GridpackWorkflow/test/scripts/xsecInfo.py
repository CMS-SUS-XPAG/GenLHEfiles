### Open Condor log files and retrieve the cross section and matching information for each mass point

### Author: Dustin Anderson

import os
import argparse
import glob

from parseProcessInfo import parseCrossSectionAndMatchingEfficiency

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('proc', help='physics process name')
    parser.add_argument('mass', help='sparticle masses to consider', nargs='+', type=int)
    parser.add_argument('--qcut', help='qcut to use', required=True, type=int)
    args = parser.parse_args()

    proc = args.proc
    mass = args.mass
    qcut = args.qcut

    masses = []
    xsecs = []
    xsecerrs = []
    matcheffs = []
    matcherrs = []

    for m in mass:
        #get all log files for this mass point
        #(filenames look like gen_<process>_<qcut>.err.<job ID>.0)
        fnames = glob.glob('gen_%s-%d_%d.err.*.0'%(proc,m,qcut))
        fnames.sort(key=os.path.getmtime, reverse=True)
        #look in all such files -- take the first one that yields a value
        found = False
        for f in fnames:
            xsec,xsecerr,eff,efferr = parseCrossSectionAndMatchingEfficiency(f)
            if eff is not None:
                masses.append(m)
                xsecs.append(xsec)
                xsecerrs.append(xsecerr)
                matcheffs.append(eff)
                matcherrs.append(efferr)
                found = True
                break
        if not found:
            print "Didn't find cross section information for mass",m
    print "Mass | Cross Section | Uncertainty | Matching Efficiency | Uncertainty"
    for i in range(len(xsecs)):
        print masses[i],xsecs[i],xsecerrs[i],matcheffs[i],matcherrs[i]

