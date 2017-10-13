### Script to submit Condor jobs for LHE event generation and showering at UCSD

### Authors:
### Ana Ovcharova
### Dustin Anderson

import os
import sys
import argparse
import shutil

from submitLHECondorJob import submitCondorJob

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('proc', help="Names of physics model")
    parser.add_argument('--in-file', '-i', dest='infile', help="Full path to input tarball", required=True)
    parser.add_argument('--fragment', '-f', help='Path to gen fragment', required=True)
    parser.add_argument('--nevents', '-n', help="Number of events per job", type=int, default=25000)
    parser.add_argument('--njobs', '-j', help="Number of condor jobs", type=int, default=1)
    parser.add_argument('--no-sub', dest='noSub', action='store_true', help='Do not submit jobs')
    args = parser.parse_args()

    proc = args.proc
    infile = args.infile
    fragment = args.fragment
    nevents = args.nevents
    njobs = args.njobs

    script_dir = os.path.dirname(os.path.realpath(__file__))
    executable = script_dir+'/runLHEPythiaJob.sh'
    out_dir='/hadoop/cms/store/user/'+os.environ['USER']+'/mcProduction/devel/'
    print "Will generate LHE events using tarball",infile,"and shower them using Pythia"

    #need to transfer input tarball and gen fragment
    infiles = infile+','+fragment
    fragfile = os.path.basename(fragment)

    logDir = os.path.join("logs",proc)
    if not os.path.isdir(logDir):
        os.makedirs(logDir)
    else:
        shutil.rmtree(logDir)
        os.makedirs(logDir)


    outdir = out_dir+'/'+proc
    options = [proc, str(nevents), fragfile, outdir]
    print "Options:",(' '.join(options))
    for j in range(0,njobs):
        rseed = str(500+j)
        print "Random seed",rseed
        submitCondorJob(proc, executable, options+[rseed], infiles, 
                label=rseed+(fragfile.replace('.py','')), submit=(not args.noSub))
