#!/bin/bash

# for local test run inside the directory with the fragment e.g. production/models/T1tttt/
# the tag can be used when there are multiple datasets per model

JOBNUM=$1
MODEL=$2
OUTDIR=$3
NEVENTS=$4
LOCAL_TEST=$5
TAG=$6

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
FRAGMENT=${MODEL}_${TAG}_fragment.py
OUTPUT=${MODEL}_${TAG}_${JOBNUM}.root
MINI=${MODEL}_${TAG}_${JOBNUM}_MiniAODv2.root
OUTDIR_EOS="store/group/phys_susy/LHE/private_samples/FSPremix80X/"${MODEL}
if [[ -z "${TAG}" ]]; then
   FRAGMENT=${MODEL}_fragment.py
   OUTPUT=${MODEL}_${JOBNUM}.root
   MINI=${MODEL}_${JOBNUM}_MiniAODv2.root
   OUTDIR_EOS="store/group/phys_susy/LHE/private_samples/FSPremix80X/"${MODEL}_${TAG}
fi
cp ../../${FRAGMENT} Configuration/GenProduction/python/

scram b
cd ../../
mkdir test
cd test
# 
# dbs:/Neutrino_E-10_gun/RunIISpring16FSPremix-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/GEN-SIM-DIGI-RAW
cmsDriver.py  Configuration/GenProduction/python/${FRAGMENT} \
--fileout file:${OUTPUT}  \
--pileup_input "file:/hadoop/cms/store/user/ana/data/Neutrino_E-10_gun_RunIISpring16FSPremix_PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1_GEN-SIM-DIGI-RAW.root"  \
--mc \
--eventcontent AODSIM \
--fast \
--customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput,Configuration/DataProcessing/Utils.addMonitoring \
--customise_commands "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(50) \n process.source.firstRun = cms.untracked.uint32(${JOBNUM})" \
--datatier AODSIM \
--conditions 80X_mcRun2_asymptotic_v12 \
--beamspot Realistic50ns13TeVCollision \
--step GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,L1Reco,RECO,HLT:@fake1 \
--datamix PreMix \
--era Run2_25ns \
--python_filename jobcfg.py \
--no_exec \
-n ${NEVENTS}

cmsRun jobcfg.py

if [[ "${LOCAL_TEST}" != 'local' ]]; then 
   lcg-cp -v -b -D srmv2 --vo cms file:`pwd`/${OUTPUT} srm://bsrm-3.t2.ucsd.edu:8443/srm/v2/server?SFN=${OUTDIR}/${OUTPUT}    
fi

cmsDriver.py step1 \
--filein file:${OUTPUT} \
--fileout file:${MINI} \
--mc \
--eventcontent MINIAODSIM \
--runUnscheduled \
--fast \
--datatier MINIAODSIM \
--conditions 80X_mcRun2_asymptotic_2016_miniAODv2_v0 \
--step PAT \
--era Run2_25ns \
--python_filename mini_cfg.py \
--no_exec \
--customise Configuration/DataProcessing/Utils.addMonitoring \
-n -1

cmsRun mini_cfg.py

if [[ "${LOCAL_TEST}" != 'local' ]]; then 
   lcg-cp -v -b -D srmv2 --vo cms file:`pwd`/${MINI} srm://bsrm-3.t2.ucsd.edu:8443/srm/v2/server?SFN=${OUTDIR}/${MINI}
   if ! [[ "${OUTDIR_EOS}" == "" ]]; then
       xrdcp ${MINI} root://eoscms.cern.ch//eos/cms/${OUTDIR_EOS}/${MINI}
   fi
   cd ../
   rm -rf CMSSW_8_0_5_patch1
   rm -rf test
fi


echo "Bye."
