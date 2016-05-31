### Script to submit Condor jobs for end-to-end (gridpack --> miniaod) production with Condor

### Author: 
### Dustin Anderson

import os
import sys
import argparse
import glob
import random

from submitLHECondorJob import submitCondorJob

parser = argparse.ArgumentParser()
parser.add_argument('exe', help="Path to job script")
parser.add_argument('--gridpack', '-g', help="Path to gridpack", required=True)
parser.add_argument('--nevents', '-n', help="Number of events per job", type=int, default=1000)
parser.add_argument('--njobs', '-j', help="Number of condor jobs", type=int, default=1)
parser.add_argument('--out-dir', help="Output directory", dest='outdir',
        default='/hadoop/cms/store/user/'+os.environ['USER']+'/mcProduction/MINIAODSIM')
parser.add_argument('--out-dir-eos', help="Output directory (EOS)", dest='outdirEos',
        default="")
parser.add_argument('--no-sub', dest='noSub', action='store_true', help='Do not submit jobs')
parser.add_argument('--pu-input', dest="puOpt", help="Specify how to retrieve the PU dataset: 'dbs', 'local_safe'", default='dbs')
parser.add_argument('--proxy', dest="proxy", help="Path to proxy", default='/tmp/x509up_u31156')
parser.add_argument('--rseed-start', dest='rseedStart', help='Initial value for random seed', 
        type=int, default=10000)
args = parser.parse_args()

executable = args.exe
infile = args.gridpack
nevents = args.nevents
njobs = args.njobs
outdir=args.outdir
outdirEos=args.outdirEos
rseedStart = args.rseedStart

print "Will run",njobs,"jobs with",nevents,"events each"
print "Running this executable:",executable

for j in range(njobs):
    rseed = str(rseedStart+j)
    print "Random seed",rseed
    if args.puOpt == "dbs": puInputStr = "dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIIWinter15GS-MCRUN2_71_V1-v1/GEN-SIM"
    elif args.puOpt == "local_safe": 
        puFilesAll = glob.glob("/hadoop/cms/phedex/store/mc/RunIIWinter15GS/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM/MCRUN2_71_V1-v1/*/*")
        puFiles = random.sample(puFilesAll,10)
        puFiles = ["file:"+i for i in puFiles]
        puInputStr = "{0}".format(",".join(puFiles))
    options = [str(nevents), str(rseed), outdir, puInputStr, outdirEos]
    submitCondorJob('miniaod', executable, options, infile, label=str(rseed), 
            submit=(not args.noSub),proxy=args.proxy)
