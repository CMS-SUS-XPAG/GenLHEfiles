### Script to submit Condor jobs for end-to-end (gridpack --> miniaod) production with Condor

### Author: 
### Mia Liu

import os
import sys
import argparse
import glob
import random

from submitLHECondorJob import submitCondorJob
script_dir = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser()
#parser.add_argument('exe', help="Path to job script")
parser.add_argument('--model', dest="model", help='Name of model and  a batch number if model has multiple models', required=True)
parser.add_argument('--tag', dest="tag", help='In case of multiple sets of fragments per model')
parser.add_argument('--executable', help='Path to executable that should be run', 
        default = script_dir+'/runFullSimMiniAODv2.sh')
parser.add_argument('--full', dest='full', action='store_true', help="Run also FSPremix and MiniAOD step.")
parser.add_argument('--fragment', dest='fragment', help="Path to fragment", required=True)
parser.add_argument('--njobs', dest="njobs", type=int, help='Number of condor jobs', required=True)
parser.add_argument('--nevents', dest="nevents", type=int, help='Number of events per job', required=True)
parser.add_argument('--out-dir', help="Output directory", dest='outdir',
        default='/hadoop/cms/store/user/'+os.environ['USER']+'/mcProduction/MINIAODSIM')
parser.add_argument('--out-dir-eos', help="Output directory (EOS)", dest='outdirEos',
        default="")
parser.add_argument('--no-sub', dest='noSub', action='store_true', help='Do not submit jobs')
parser.add_argument('--proxy', dest="proxy", help="Path to proxy", default='/tmp/x509up_u31156')
parser.add_argument('--rseed-start', dest='rseedStart', help='Initial value for random seed', 
        type=int, default=1)
args = parser.parse_args()

exefile = args.executable
nevents = args.nevents
njobs = args.njobs
outdir=args.outdir
outdirEos=args.outdirEos
rseedStart = args.rseedStart

out_dir='/hadoop/cms/store/user/'+os.environ['USER']+'/mcProduction/MINIAODSIM'
print "Will run",njobs,"jobs with",nevents,"events each"
for ijob in range(2000,2000+args.njobs):
    outdir = out_dir+'/'+args.model
    rseed = str(rseedStart+ijob)
    if args.tag:
        options = [str(ijob+1),args.model, outdir, str(args.nevents),rseed,"condor",args.tag]
        submitCondorJob(args.model, exefile, options, args.fragment, label=args.tag+"_batch"+str(ijob+1),submit=(not args.noSub), proxy=args.proxy)
    else:
        options = [str(ijob+1), args.model, outdir, str(args.nevents),rseed,"condor"]
        submitCondorJob(args.model, exefile, options, args.fragment, label="batch"+str(ijob+1),submit=(not args.noSub), proxy=args.proxy)
