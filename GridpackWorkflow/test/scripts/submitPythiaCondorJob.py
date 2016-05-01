### Script to submit Condor jobs for Pythia hadronization at UCSD

### Authors: 
### Ana Ovcharova
### Dustin Anderson

import os
import sys
import argparse
import glob

from submitLHECondorJob import submitCondorJob

parser = argparse.ArgumentParser()
parser.add_argument('proc', help="Name of physics model")
parser.add_argument('--in-dir', '-i', dest='inDir', help="Path to input file directory", required=True)
parser.add_argument('--slha', help="Path to slha file/fragment", required=True)
parser.add_argument('--qcut-range', dest='qcutRange', nargs=2, type=int, default=[50,100], 
        help="Range of qcuts to scan over")
parser.add_argument('--no-sub', dest='noSub', action='store_true', help='Do not submit jobs')
parser.add_argument('--proxy', dest="proxy", help="Path to proxy", default='/tmp/x509up_u31156')
args = parser.parse_args()

proc = args.proc
inDir = args.inDir
slha = args.slha
qcutRange = range(args.qcutRange[0], args.qcutRange[1]+1, 2)

#get files
inFilesList = glob.glob(inDir+'/*.lhe')
infile = ','.join(inFilesList)+','+slha

script_dir = os.path.dirname(os.path.realpath(__file__))
executable = script_dir+'/runPythiaJob.sh'
out_dir='/hadoop/cms/store/user/'+os.environ['USER']+'/mcProduction/RAWSIM'

print "Will use Pythia to shower LHE events from files:",infile

for qcut in qcutRange:
    outdir = out_dir+'/'+proc
    outfile = '_'.join(['GEN',proc,str(qcut)+'.root'])
    options = [proc, os.path.basename(slha), str(qcut), outdir]
    submitCondorJob(proc, executable, options, infile, label=str(qcut), #outputToTransfer=outfile,
            submit=(not args.noSub), proxy=args.proxy)
