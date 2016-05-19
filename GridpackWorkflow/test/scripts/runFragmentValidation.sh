#!/bin/bash

JOBNUM=$1
DATASET=$2
OUTDIR=$3
NEVENTS=$4

source /cvmfs/cms.cern.ch/cmsset_default.sh 
export SCRAM_ARCH=slc6_amd64_gcc530
if [ -r CMSSW_8_0_5_patch1/src ] ; then 
 echo release CMSSW_8_0_5_patch1 already exists
else
scram p CMSSW CMSSW_8_0_5_patch1
fi
cd CMSSW_8_0_5_patch1/src
eval `scram runtime -sh`

mkdir -p Configuration/GenProduction/python/
cp ../../fragment.py Configuration/GenProduction/python/

scram b
cd ../../
mkdir test
cd test

OUTPUT=${DATASET}_${JOBNUM}.root

cmsDriver.py Configuration/GenProduction/python/fragment.py \
--fileout file:${OUTPUT}  \
--eventcontent AODSIM \
--conditions 80X_mcRun2_asymptotic_v12 \
--customise_commands "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(50) \n process.source.firstRun = cms.untracked.uint32(${JOBNUM}) \n process.generator.initialSeed = cms.untracked.uint32(${JOBNUM})" \
--step GEN \
--python_filename jobcfg.py \
--no_exec \
-n ${NEVENTS}

cmsRun jobcfg.py

lcg-cp -v -b -D srmv2 --vo cms file:`pwd`/${OUTPUT} srm://bsrm-3.t2.ucsd.edu:8443/srm/v2/server?SFN=${OUTDIR}/${OUTPUT}

cd ../
rm -rf CMSSW_8_0_5_patch1
rm -rf test

echo "Bye."
