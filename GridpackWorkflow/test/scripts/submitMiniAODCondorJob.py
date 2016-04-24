### Script to submit Condor jobs for end-to-end (gridpack --> miniaod) production with Condor

### Author: 
### Dustin Anderson

import os
import sys
import argparse
import glob

from submitLHECondorJob import submitCondorJob

parser = argparse.ArgumentParser()
parser.add_argument('exe', help="Path to job script")
parser.add_argument('--gridpack', '-g', help="Path to gridpack", required=True)
parser.add_argument('--nevents', '-n', help="Number of events per job", type=int, default=1000)
parser.add_argument('--njobs', '-j', help="Number of condor jobs", type=int, default=1)
parser.add_argument('--out-dir', help="Output directory", dest='outdir',
        default='/hadoop/cms/store/user/'+os.environ['USER']+'/mcProduction/MINIAODSIM')
parser.add_argument('--no-sub', dest='noSub', action='store_true', help='Do not submit jobs')
args = parser.parse_args()

executable = args.exe
infile = args.gridpack
nevents = args.nevents
njobs = args.njobs
outdir=args.outdir

print "Will run",njobs,"jobs with",nevents,"events each"
print "Running this executable:",executable

for j in range(njobs):
    rseed = str(10000+j)
    print "Random seed",rseed
    options = [str(nevents), str(rseed), outdir]
    submitCondorJob('miniaod', executable, options, infile, label=str(rseed), 
            submit=(not args.noSub))
