#### !/usr/local/bin/bash

### Script to generate LHE events and shower them using Pythia
### Intended for use with Condor at UCSD

### Authors:
### Ana Ovcharova
### Dustin Anderson

PROCESS=$1
NEVENTS=$2
FRAGMENT=$3
QCUT=$4
NJETMAX=$5
OUTDIR=$6
NJOB=$7
RANDOM_SEED=$8

CMSSW_REL="CMSSW_9_3_1"

echo "Process:"
echo $PROCESS

WORKDIR=$(pwd)
echo "Working directory: "
echo $WORKDIR
echo "ls in working dir: "
ls

echo "Output directory set to: "
echo $OUTDIR

source /cvmfs/cms.cern.ch/cmsset_default.sh  
export SCRAM_ARCH=slc6_amd64_gcc630
echo $SCRAM_ARCH
echo $HOSTNAME
echo "Setting up a CMSSW release..."
eval `scramv1 project CMSSW ${CMSSW_REL}`
cp $FRAGMENT ${CMSSW_REL}/src
cd ${CMSSW_REL}/src
eval `scramv1 runtime -sh`

echo "Prepare fragment..."
mkdir -p Configuration/GenProduction/python
sed "s/%QCUT%/${QCUT}/ ;s/%NJETMAX%/${NJETMAX}/" $FRAGMENT > Configuration/GenProduction/python/genfragment.py

eval "scramv1 build clean"
eval "scramv1 build"

echo $PWD
ls

echo "-----------> Let's begin...EVENT GENERATION"

echo "Fragment:"
cat Configuration/GenProduction/python/genfragment.py

#             SHOWER
#--------------------------------
GENFILE='GEN_'${PROCESS}'_'${RANDOM_SEED}'_'${QCUT}'.root'


echo "--------------> Let's begin... SHOWER"
cmsDriver.py \
  Configuration/GenProduction/python/genfragment.py \
  --mc \
  --eventcontent RAWSIM,LHE \
  --datatier GEN-SIM,LHE \
  --conditions 93X_mc2017_realistic_v3 \
  --step LHE,GEN,SIM \
  --nThreads 8 \
  --fileout file:${GENFILE} \
  --beamspot Realistic25ns13TeVEarly2017Collision \
  --geometry DB:Extended \
  --era Run2_2017 \
  --python_filename LHEGS_cfg.py \
  --no_exec \
  -n $NEVENTS 

echo "process.RandomNumberGeneratorService.generator.initialSeed = $RANDOM_SEED" >> LHEGS_cfg.py
echo "process.RandomNumberGeneratorService.externalLHEProducer.initialSeed = $RANDOM_SEED" >> LHEGS_cfg.py
echo "process.source.firstRun = cms.untracked.uint32($NJOB)" >> LHEGS_cfg.py

echo $PWD
ls

cmsRun LHEGS_cfg.py


echo "Hadronization finished. Copy output..."
gfal-copy -p -f -t 4200 ${GENFILE} gsiftp://gftp.t2.ucsd.edu/${OUTDIR}/${GENFILE} --checksum ADLER32


echo "ls in cmssw src dir"
ls

#cleanup
cd $WORKDIR
echo "ls in workdir"
ls
rm -rf ${CMSSW_REL}

echo "Bye."

