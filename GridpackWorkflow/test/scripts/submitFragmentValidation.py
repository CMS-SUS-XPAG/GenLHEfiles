### Script to submit Condor jobs for validation of GEN fragments at UCSD

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
parser.add_argument('--model', dest="model", help='Name of model and  a batch number if model has multiple models', required=True)
parser.add_argument('--tag', dest="tag", help='In case of multiple sets of fragments per model')
parser.add_argument('--executable', help='Path to executable that should be run', 
        default = script_dir+'/runFragmentValidation.sh')
parser.add_argument('--fragment', dest='fragment', help="Path to fragment", required=True)
parser.add_argument('--njobs', dest="njobs", type=int, help='Number of condor jobs', required=True)
parser.add_argument('--nevents', dest="nevents", type=int, help='Number of events per job', required=True)
parser.add_argument('--no-sub', dest='noSub', action='store_true', help='Do not submit jobs')
parser.add_argument('--proxy', dest="proxy", help="Path to proxy", default='/tmp/x509up_u31156')
args = parser.parse_args()


out_dir='/hadoop/cms/store/user/'+os.environ['USER']+'/mcProduction/AODSIM'

for ijob in range(args.njobs):
    outdir = out_dir+'/'+args.model
    options = [str(ijob+1), args.model, outdir, str(args.nevents),"condor"]
    submitCondorJob(args.model, args.executable, options, args.fragment, label="batch"+str(ijob+1),submit=(not args.noSub), proxy=args.proxy)
    if args.tag:
        options = [str(ijob+1), args.model, outdir, str(args.nevents),"condor",args.tag]
        submitCondorJob(args.model, args.executable, options, args.fragment, label=args.tag+"_batch"+str(ijob+1),submit=(not args.noSub), proxy=args.proxy)
            
