### Script to submit Condor jobs for Pythia hadronization at UCSD

### Authors: 
### Ana Ovcharova
### Dustin Anderson

import os
import sys
import argparse
import glob

from submitLHECondorJob import submitCondorJob

script_dir = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument('proc', help="Name of physics model")
parser.add_argument('--in-dir', '-i', dest='inDir', help="Path to input file directory", required=True)
parser.add_argument('--slha', help="Path to slha file/fragment", required=True)
parser.add_argument('--qcut-range', dest='qcutRange', nargs=2, type=int, default=[50,100], 
        help="Range of qcuts to scan over")
parser.add_argument('--qcut-list', dest='qcutList', nargs='+', type=int, default=[], 
        help="List of qcuts to scan over")
parser.add_argument('--qcut-step', dest='qcutStep', type=int, default=2)
parser.add_argument('--nJetMax', help="nJetMax argument in the fragment", default=2)
parser.add_argument('--no-sub', dest='noSub', action='store_true', help='Do not submit jobs')
parser.add_argument('--proxy', dest="proxy", help="Path to proxy", default=os.environ["X509_USER_PROXY"])
parser.add_argument('--executable', help='Path to executable that should be run', 
        default = script_dir+'/runPythiaJob.sh')
args = parser.parse_args()

proc = args.proc
inDir = args.inDir
slha = args.slha
executable = args.executable
qcutRange = range(args.qcutRange[0], args.qcutRange[1]+1, args.qcutStep)
qcutList = args.qcutList
nJetMax = args.nJetMax

#get files
inFilesList = ["root://cmsxrootd.fnal.gov/"+fl.split("/hadoop/cms")[-1] for fl in glob.glob(inDir+'/*.lhe')]
infile = ','.join(inFilesList)

out_dir='/hadoop/cms/store/user/'+os.environ['USER']+'/mcProduction/RAWSIM'

print "Will use Pythia to shower LHE events from files:",infile

if len(qcutList)>0: qcutRange=qcutList

for qcut in qcutRange:
    outdir = out_dir+'/'+proc
    outfile = '_'.join(['GEN',proc,str(qcut)+'.root'])
    options = [proc, os.path.basename(slha), str(qcut), outdir,infile,str(nJetMax)]
    submitCondorJob(proc, executable, options, slha, label=str(qcut), #outputToTransfer=outfile,
            submit=(not args.noSub), proxy=args.proxy)
