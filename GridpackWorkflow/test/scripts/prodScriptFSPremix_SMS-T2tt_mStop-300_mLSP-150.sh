#!/bin/bash

NEVENTS=$1
RANDOM_SEED=$2
OUTDIR=$3
OUTDIR_EOS=$4


GRIDPACK_PATH=$PWD

PROCESS="SMS-T2tt_mStop-300"
STOP_MASS="300"
MODEL="# model T2tt-2bd_300_150"
TAG="_mLSP-150"
# STOP_DECAY=\
"DECAY   1000006     1.00000000E+00   # stop1 decays
     0.00000000E+00    3     1000022         5      24
     1.00000000E+00    2     1000022         6"
QCUT=57

source /code/osgcode/cmssoft/cmsset_default.sh
# on lxplus only
# export X509_USER_PROXY=$HOME/private/personal/voms_proxy.cert

export SCRAM_ARCH=slc6_amd64_gcc481
if [ -r CMSSW_7_1_20_patch3/src ] ; then 
 echo release CMSSW_7_1_20_patch3 already exists
else
scram p CMSSW CMSSW_7_1_20_patch3
fi
cd CMSSW_7_1_20_patch3/src
eval `scram runtime -sh`

scram b

tar -xaf ${GRIDPACK_PATH}/${PROCESS}_tarball.tar.xz

echo "Running event generation..."
./runcmsgrid.sh $NEVENTS $RANDOM_SEED $(getconf _NPROCESSORS_ONLN)
cd ../../

awk '/<MGGenerationInfo/{n++}{print >"test"n".lhe"}' CMSSW_7_1_20_patch3/src/cmsgrid_final.lhe
rm -rf CMSSW_7_1_20_patch3/src/*
rm test.lhe

echo \
"<LesHouchesEvents version=\"3.0\">
<header>
<MGVersion>
# MG/ME version    : 2.2.2
</MGVersion>
<MG5ProcCard>
import model mssm
define p u u~ d d~ s s~ c c~ b b~ g
define j p
define q p
generate p p > go go  @1
add process p p >  go go j  @2
add process p p > go go j j @3
# Specify process(es) to run
#slepton-slepton
<MGProcCard>
# Begin PROCESS # This is TAG. Do not modify this line
pp>T1tttt    @0       # First Process
# End PROCESS  # This is TAG. Do not modify this line
</MGProcCard>
</MG5ProcCard>
<slha>
#
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
        25     1.00000000E+03
        35     1.00000000E+03
        36     1.00000000E+03
        37     1.00000000E+03
        6      1.72500000E+02
   1000001     100000.0          # ~d_L
   2000001     1.00000000E+05   # ~d_R
   1000002     100000.0          # ~u_L
   2000002     1.00000000E+05   # ~u_R
   1000003     100000.0          # ~s_L
   2000003     1.00000000E+05   # ~s_R
   1000004     100000.0          # ~c_L
   2000004     1.00000000E+05   # ~c_R
   1000005     1.00000000E+05   # ~b_1
   2000005     1.10000000E+05   # ~b_2
   1000006     $STOP_MASS       # ~t_1
   2000006     1.10000000E+05   # ~t_2
   1000011     1.00000000E+04   # ~e_L
   2000011     1.00000000E+04   # ~e_R
   1000012     1.00000000E+04   # ~nu_eL
   1000013     1.00000000E+04   # ~mu_L
   2000013     1.00000000E+04   # ~mu_R
   1000014     1.00000000E+04   # ~nu_muL
   1000015     1.00000000E+04   # ~tau_1
   2000015     1.00000000E+04   # ~tau_2
   1000016     1.00000000E+04   # ~nu_tauL
   1000021     1.00000000E+04   # ~g
   1000022     150.             # ~chi_10
   1000023     1.00000000E+04   # ~chi_20
   1000025     1.00000000E+04   # ~chi_30
   1000035     1.00000000E+04   # ~chi_40
   1000024     1.00000000E+04   # ~chi_1+
   1000037     1.00000000E+04   # ~chi_2+
#
#
#
#         PDG            Width
DECAY         6     1.134E+00        # top decays
DECAY   2000006     0.00000000E+00   # stop2 decays
DECAY   1000005     0.00000000E+00   # sbottom1 decays
DECAY   2000005     0.00000000E+00   # sbottom2 decays
#
#         PDG            Width
DECAY   1000011     0.00000000E+00   # selectron_L decays
DECAY   2000011     0.00000000E+00   # selectron_R decays
DECAY   1000013     0.00000000E+00   # smuon_L decays
DECAY   2000013     0.00000000E+00   # smuon_R decays
DECAY   1000015     0.00000000E+00   # stau_1 decays
DECAY   2000015     0.00000000E+00   # stau_2 decays
#
#         PDG            Width
DECAY   1000012     0.00000000E+00   # snu_elL decays
DECAY   1000014     0.00000000E+00   # snu_muL decays
DECAY   1000016     0.00000000E+00   # snu_tauL decays
$STOP_DECAY
DECAY   1000021     0.00000000E+00   # gluino decays
DECAY   1000022     0.00000000E+00   # neutralino1 decays

</slha>

<MGRunCard>
   1   = ickkw   ! turning matching on/off for multi-jet sample
  30   = xqcut   ! minimum kt jet measure between partons
</MGRunCard>
" >> undecayed.lhe

cat test1.lhe >> undecayed.lhe

sed -i "s|<scales pt_clust_1|$MODEL\n<scales pt_clust_1|g" undecayed.lhe

echo "Running pLHE step..."
cmsDriver.py \
    step1 --filein file:undecayed.lhe \
    --fileout file:${PROCESS}_plhe.root \
    --mc --eventcontent LHE --datatier LHE \
    --conditions MCRUN2_71_V1::All \
    --step NONE --python_filename plhe_driver.py \
    --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n -1 || exit $? ; 
cmsRun -e -j plhe_driver_rt.xml plhe_driver.py || exit $? ; 

rm -rf  CMSSW_7_1_20_patch3

echo "Now showering..."

export SCRAM_ARCH=slc6_amd64_gcc491
if [ -r CMSSW_7_4_4/src ] ; then 
 echo release CMSSW_7_4_4 already exists
else
scram p CMSSW CMSSW_7_4_4
fi
cd CMSSW_7_4_4/src
eval `scram runtime -sh`

mkdir -p Configuration/GenProduction/python

echo \
"import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter(\"Pythia8HadronizerFilter\",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'JetMatching:setMad = off',
            'JetMatching:scheme = 1',
            'JetMatching:merge = on',
            'JetMatching:jetAlgorithm = 2',
            'JetMatching:etaJetMax = 5.',
            'JetMatching:coneRadius = 1.',
            'JetMatching:slowJetPower = 1',
            'JetMatching:qCut = $QCUT.', #this is the actual merging scale                        
            'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
            'JetMatching:nJetMax = 2', #number of partons in born matrix element for highest multiplicity         
            'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching  
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
    )
)" > Configuration/GenProduction/python/genfragment.py

scram b
cd ../../
cmsDriver.py Configuration/GenProduction/python/genfragment.py \
	     --filein file:${PROCESS}_plhe.root \
	     --fileout file:${PROCESS}_AODSIM.root  \
	     --pileup_input "dbs:/Neutrino_E-10_gun/RunIISpring15PrePremix-MCRUN2_74_V9-v1/GEN-SIM-DIGI-RAW" \
	     --mc --eventcontent AODSIM --fast \
	     --customise SLHCUpgradeSimulations/Configuration/postLS1CustomsPreMixing.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring \
             --customise_command "process.source.setRunNumber = cms.untracked.uint32($RANDOM_SEED)" \
	     --datatier AODSIM --conditions MCRUN2_74_V9 --beamspot NominalCollision2015 \
	     --step GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2:pdigi_valid,DATAMIX,L1,L1Reco,RECO,HLT:@frozen25ns \
	     --magField 38T_PostLS1 --datamix PreMix \
	     --python_filename fspremix_driver.py --no_exec -n -1 || exit $? ; 
cmsRun -e -j fspremix_rt.xml fspremix_driver.py || exit $? ; 

rm -rf CMSSW_7_4_4

echo "Making MINIAODSIM..."
  
export SCRAM_ARCH=slc6_amd64_gcc491
if [ -r CMSSW_7_4_14/src ] ; then 
 echo release CMSSW_7_4_14 already exists
else
scram p CMSSW CMSSW_7_4_14
fi
cd CMSSW_7_4_14/src
eval `scram runtime -sh`

scram b
cd ../../
cmsDriver.py step1 --filein file:${PROCESS}_AODSIM.root \
	     --fileout file:${PROCESS}${TAG}_madgraphMLM-pythia8_RunIISpring15MiniAODv2-FastAsympt25ns_74X_MINIAODSIM_${RANDOM_SEED}.root \
	     --mc --eventcontent MINIAODSIM --runUnscheduled --fast \
	     --customise SLHCUpgradeSimulations/Configuration/postLS1CustomsPreMixing.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring \
	     --datatier MINIAODSIM --conditions 74X_mcRun2_asymptotic_v2 \
	     --step PAT --python_filename mini_driver.py --no_exec -n -1 || exit $? ; 
cmsRun -e -j mini_rt.xml mini_driver.py || exit $? ;

echo "Copy MiniAODv2 to eos and hadoop"

lcg-cp -b -D srmv2 --vo cms -t 2400 --verbose file:${PROCESS}${TAG}_madgraphMLM-pythia8_RunIISpring15MiniAODv2-FastAsympt25ns_74X_MINIAODSIM_${RANDOM_SEED}.root srm://bsrm-3.t2.ucsd.edu:8443/srm/v2/server?SFN=${OUTDIR}/${PROCESS/T2tt/T2tt-2bd}${TAG}_madgraphMLM-pythia8_RunIISpring15MiniAODv2-FastAsympt25ns_74X_MINIAODSIM_${RANDOM_SEED}.root

if ! [[ "${OUTDIR_EOS}" == "" ]]; then
    xrdcp ${PROCESS}${TAG}_madgraphMLM-pythia8_RunIISpring15MiniAODv2-FastAsympt25ns_74X_MINIAODSIM_${RANDOM_SEED}.root root://eoscms.cern.ch//eos/cms/${OUTDIR_EOS}/${PROCESS/T2tt/T2tt-2bd}${TAG}_madgraphMLM-pythia8_RunIISpring15MiniAODv2-FastAsympt25ns_74X_MINIAODSIM_${RANDOM_SEED}.root
fi

rm -rf CMSSW_7_4_14
rm *root *lhe *xml *py *txt

echo "Bye."
