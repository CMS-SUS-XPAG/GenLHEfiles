#### !/usr/local/bin/bash

### Script to generate LHE events from a gridpack
### Intended for use with Condor at UCSD

### Authors:
### Ana Ovcharova
### Dustin Anderson

PROCESS=$1
NEVENTS=$2
OUTDIR=$3
RANDOM_SEED=$4

echo "Process"
echo $PROCESS

WORKDIR=$(pwd)
echo "Working directory: "
echo $WORKDIR

echo "Output directory set to: "
echo $OUTDIR

source /cvmfs/cms.cern.ch/cmsset_default.sh  
export SCRAM_ARCH=slc6_amd64_gcc481
echo $SCRAM_ARCH
echo $HOSTNAME
echo "Setting up a CMSSW release..."
eval `scramv1 project CMSSW CMSSW_7_1_30`
cd CMSSW_7_1_30/src
eval `scramv1 runtime -sh`

eval "scramv1 build clean"
eval "scramv1 build"

echo "-----------> Let's begin...EVENT GENERATION"

echo "Unpacking gridpack tarball..."
tar -xaf $WORKDIR/${PROCESS}_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz                                                    

echo "Running event generation..."
./runcmsgrid.sh $NEVENTS $RANDOM_SEED $(getconf _NPROCESSORS_ONLN)

echo "Generation finished. Copy output..."
#lcg-cp -v -b -D srmv2 --vo cms file:cmsgrid_final.lhe srm://bsrm-3.t2.ucsd.edu:8443/srm/v2/server?SFN=${OUTDIR}/${PROCESS}_${RANDOM_SEED}.lhe
gfal-copy -p -f -t 4200 cmsgrid_final.lhe gsiftp://gftp.t2.ucsd.edu/${OUTDIR}/${PROCESS}_${RANDOM_SEED}.lhe --checksum ADLER32
#cp cmsgrid_final.lhe ${WORKDIR}/${PROCESS}_${RANDOM_SEED}.lhe #for copying file back to submission directory

echo "ls in cmssw src dir"
ls

#cleanup
cd $WORKDIR
echo "ls in workdir"
ls
rm -rf CMSSW_7_1_30

echo "Bye."
