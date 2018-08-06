#!/bin/bash

JOBNUM=$1
MODEL=$2
OUTDIR=$3
NEVENTS=$4
RANDOMSEED=$5
LOCAL_TEST=$6
TAG=$7

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
if [ -r CMSSW_9_3_6/src ] ; then
 echo release CMSSW_9_3_6 already exists
else
scram p CMSSW CMSSW_9_3_6
fi
cd CMSSW_9_3_6/src
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
cmsDriver.py  Configuration/GenProduction/python/${FRAGMENT} \
--fileout file:${OUTPUT} \
--mc \
--eventcontent RAWSIM,LHE \
--conditions 93X_mc2017_realistic_v3 \
--beamspot Realistic25ns13TeVEarly2017Collision \
--geometry DB:Extended \
--era Run2_2017 \
--customise Configuration/DataProcessing/Utils.addMonitoring \
--customise_commands "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(50) \n process.source.firstRun = cms.untracked.uint32(${JOBNUM}) \n process.RandomNumberGeneratorService.externalLHEProducer.initialSeed = ${RANDOMSEED}" \
--datatier GEN-SIM,LHE \
--step LHE,GEN,SIM \
--datamix PreMix \
--python_filename jobcfg.py \
--no_exec \
-n ${NEVENTS}
#--magField 38T_PostLS1 \

#--customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring \
cmsRun -e -j gensim.xml jobcfg.py
XML=gensim.xml
echo "getting stats from "${XML}
grep "TotalEvents" ${XML}
grep "Timing-tstoragefile-write-totalMegabytes"  ${XML}
grep "PeakValueRss" ${XML}
grep "AvgEventTime" ${XML}
grep "AvgEventCPU"  ${XML}
grep "TotalJobCPU"  ${XML}
grep "EventThroughput" ${XML}

if [[ "${LOCAL_TEST}" != 'local' ]]; then 
   gfal-copy -p -f -t 4200 --verbose file:`pwd`/${OUTPUT} srm://bsrm-3.t2.ucsd.edu:8443/srm/v2/server?SFN=${OUTDIR}/${OUTPUT}    
fi

cd ..

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
if [ -r CMSSW_9_4_6_patch1/src ] ; then
 echo release CMSSW_9_4_6_patch1 already exists
else
scram p CMSSW CMSSW_9_4_6_patch1
fi
cd CMSSW_9_4_6_patch1/src

eval `scram runtime -sh`
cd ../../
cd test
#"dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MCv2_correctPU_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW" 
cmsDriver.py step1 --filein file:${OUTPUT} --fileout file:step1.root --mc --pileup_input "file:/hadoop/cms/store/user/mliu/2017pu.root" --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v11 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --datamix PreMix --era Run2_2017 --python_filename drpremix_step1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n -1

cmsRun -e -j drpremix_step1.xml  drpremix_step1_cfg.py
cmsDriver.py step2 --filein file:step1.root --fileout file:step1_RECO.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 94X_mc2017_realistic_v11 --step RAW2DIGI,RECO,RECOSIM,EI --era Run2_2017 --python_filename drpremix_step2_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n -1

cmsRun -e -j drpremix_step2.xml  drpremix_step2_cfg.py

cmsDriver.py step1 --fileout file:${MINI} --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 94X_mc2017_realistic_v14 --step PAT  --scenario pp --era Run2_2017,run2_miniAOD_94XFall17 --python_filename mini_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n -1
cmsRun -e -j mini.xml mini_cfg.py

XML=drpremix_step1.xml 
echo "getting stats from "${XML}
grep "TotalEvents" ${XML}
grep "Timing-tstoragefile-write-totalMegabytes"  ${XML}
grep "PeakValueRss" ${XML}
grep "AvgEventTime" ${XML}
grep "AvgEventCPU"  ${XML}
grep "TotalJobCPU"  ${XML}
grep "EventThroughput" ${XML}
XML=drpremix_step2.xml 
echo "getting stats from "${XML}
grep "TotalEvents" ${XML}
grep "Timing-tstoragefile-write-totalMegabytes"  ${XML}
grep "PeakValueRss" ${XML}
grep "AvgEventTime" ${XML}
grep "AvgEventCPU"  ${XML}
grep "TotalJobCPU"  ${XML}
grep "EventThroughput" ${XML}
XML=mini.xml 
echo "getting stats from "${XML}
grep "TotalEvents" ${XML}
grep "Timing-tstoragefile-write-totalMegabytes"  ${XML}
grep "PeakValueRss" ${XML}
grep "AvgEventTime" ${XML}
grep "AvgEventCPU"  ${XML}
grep "TotalJobCPU"  ${XML}
grep "EventThroughput" ${XML}
export LD_PRELOAD=/usr/lib64/gfal2-plugins//libgfal_plugin_xrootd.so 

if [[ "${LOCAL_TEST}" != 'local' ]]; then 
   gfal-copy --verbose file://`pwd`/${MINI} srm://bsrm-3.t2.ucsd.edu:8443/srm/v2/server?SFN=${OUTDIR}/${MINI}
#   if ! [[ "${OUTDIR_EOS}" == "" ]]; then
#       xrdcp ${MINI} root://eoscms.cern.ch//eos/cms/${OUTDIR_EOS}/${MINI}
#   fi
   cd ../
   rm -rf CMSSW_8_0_21
   rm -rf test
fi

echo "Bye."
