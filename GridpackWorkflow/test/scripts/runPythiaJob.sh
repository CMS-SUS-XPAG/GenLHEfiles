#### !/usr/local/bin/bash

### Script to shower LHE events using Pythia
### Intended for use with Condor at UCSD

### Authors:
### Ana Ovcharova
### Dustin Anderson

PROCESS=$1
SLHA=$2
QCUT=$3
OUTDIR=$4
INFILES=$5
NJETMAX=$6


echo "Process:"
echo $PROCESS

# INFILES=""
# for f in $( ls ${PROCESS}_*.lhe ); do
#     INFILES="file:${f},"$INFILES
# done
# INFILES=${INFILES%?}
echo "Input files:"
echo $INFILES

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
eval `scramv1 project CMSSW CMSSW_7_1_20_patch3`
cp $SLHA CMSSW_7_1_20_patch3/src
cd CMSSW_7_1_20_patch3/src
eval `scramv1 runtime -sh`

echo "Prepare fragment..."
mkdir -p Configuration/GenProduction/python

echo "SLHA fragment from $SLHA"
SLHAFRAG=$( cat $SLHA )

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
            'JetMatching:nJetMax = $NJETMAX', #number of partons in born matrix element for highest multiplicity                             
            'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching 
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
    ),
    SLHATableForPythia8 = cms.string(\"\"\"
        $SLHAFRAG
    \"\"\"),
)" > Configuration/GenProduction/python/genfragment.py

eval "scramv1 build clean"
eval "scramv1 build"

echo "Fragment:"
cat Configuration/GenProduction/python/genfragment.py

#             SHOWER
#--------------------------------
GENFILE='GEN_'${PROCESS}'_'${QCUT}'.root'

echo "--------------> Let's begin... SHOWER"
echo "cmsDriver.py Configuration/GenProduction/python/genfragment.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions auto:run2_mc --step GEN --filein ${INFILES} --fileout file:${GENFILE} -n -1"
cmsDriver.py \
  Configuration/GenProduction/python/genfragment.py \
  --mc \
  --eventcontent RAWSIM \
  --datatier GEN-SIM \
  --conditions auto:run2_mc \
  --step GEN \
  --filein ${INFILES} \
  --fileout file:${GENFILE} \
  -n -1

echo "Hadronization finished. Copy output..."
lcg-cp -v -b -D srmv2 --vo cms file:`pwd`/${GENFILE} srm://bsrm-3.t2.ucsd.edu:8443/srm/v2/server?SFN=${OUTDIR}/${GENFILE}
#cp $GENFILE $WORKDIR #for copying file back to submission directory

echo "ls in cmssw src dir"
ls

#cleanup
cd $WORKDIR
echo "ls in workdir"
ls
rm -rf CMSSW_7_1_20_patch3

echo "Bye."
