### Script to submit Condor jobs for LHE event generation and showering at UCSD

### Authors:
### Ana Ovcharova
### Dustin Anderson

import os
import sys
import argparse
import shutil

from submitLHECondorJob import submitCondorJob

script_dir = os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('proc', help="Names of physics model")
    parser.add_argument('--fragment', '-f', help='Path to gen fragment', required=True)
    parser.add_argument('--qcut-range', dest='qcutRange', nargs=2, type=int, default=[50,100], 
        help="Range of qcuts to scan over")
    parser.add_argument('--qcut-list', dest='qcutList', nargs='+', type=int, default=[], 
        help="List of qcuts to scan over")
    parser.add_argument('--qcut-step', dest='qcutStep', type=int, default=2)
    parser.add_argument('--nJetMax', help="nJetMax argument in the fragment", default=2)
    parser.add_argument('--nevents', '-n', help="Number of events per job", type=int, default=25000)
    parser.add_argument('--njobs', '-j', help="Number of condor jobs", type=int, default=1)
    parser.add_argument('--no-sub', dest='noSub', action='store_true', help='Do not submit jobs')
    parser.add_argument('--proxy', dest="proxy", help="Path to proxy", default=os.environ["X509_USER_PROXY"])
    parser.add_argument('--rseed-start', dest='rseedStart', help='Initial value for random seed', 
            type=int, default=500)
    parser.add_argument('--executable', help='Path to executable that should be run', 
        default = script_dir+'/runLHEPythiaJob.sh')
    args = parser.parse_args()

    proc = args.proc
    fragment = args.fragment
    nevents = args.nevents
    njobs = args.njobs
    rseedStart = args.rseedStart
    executable = args.executable
    qcutRange = range(args.qcutRange[0], args.qcutRange[1]+1, args.qcutStep)
    qcutList = args.qcutList
    nJetMax = args.nJetMax


    script_dir = os.path.dirname(os.path.realpath(__file__))
    #executable = script_dir+'/runLHEPythiaJob.sh'
    out_dir='/hadoop/cms/store/user/'+os.environ['USER']+'/mcProduction/RAWSIM/'
    print "Will generate LHE events using tarball and shower them using Pythia"

    #need to transfer gen fragment
    fragfile = os.path.basename(fragment)

    logDir = os.path.join("logs",proc)
    if not os.path.isdir(logDir):
        os.makedirs(logDir)
    else:
        shutil.rmtree(logDir)
        os.makedirs(logDir)


    outdir = out_dir+'/'+proc

    if len(qcutList)>0: qcutRange=qcutList

    for qcut in qcutRange:
        print "QCut", qcut
        for j in range(0,njobs):
            rseed = str(rseedStart+j)
            print "Random seed",rseed
            options = [proc, str(nevents), fragfile, str(qcut), str(nJetMax), outdir, str(j+1)]
            print "Options:",(' '.join(options))
            submitCondorJob(proc, executable, options+[rseed], fragment, 
                label=str(qcut)+'_'+rseed, submit=(not args.noSub), proxy=args.proxy)
