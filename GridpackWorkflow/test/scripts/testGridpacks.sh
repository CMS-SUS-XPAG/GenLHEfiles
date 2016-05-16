#!/usr/local/bin/bash

### Script for testing gridpacks with 100 events, interactively

MODEL=$1
MIN=$2
MAX=$3
STEP=$4

NEVENTS=100
GRIDPACKDIR=/hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/
RANDOM_SEED=15

source /cvmfs/cms.cern.ch/cmsset_default.sh  
export SCRAM_ARCH=slc6_amd64_gcc481
echo $HOSTNAME

echo "Setting up a CMSSW release..."
eval `scramv1 project CMSSW CMSSW_7_1_20_patch3`
cd CMSSW_7_1_20_patch3/src
eval `scramv1 runtime -sh`
eval "scramv1 build clean"
eval "scramv1 build"

NGRIDPACKS=0
for (( MASS=${MIN}; MASS<=${MAX}; MASS+=${STEP} )); do
# if variable step, it's easier to just enter it manually    
# for MASS in {300..900..25} {950..1300..50}; do 
    NGRIDPACKS+=1
    mkdir test
    cd test
    
    echo "Unpacking tarball: "${MODEL}${MASS}
    tar -xaf ${GRIDPACKDIR}/${MODEL}${MASS}/${MODEL}${MASS}_tarball.tar.xz  
    echo "Running event generation: "${MODEL}${MASS}
    ./runcmsgrid.sh $NEVENTS $RANDOM_SEED $(getconf _NPROCESSORS_ONLN) | tee test.log
    
    mv cmsgrid_final.lhe ${GRIDPACKDIR}/${MODEL}${MASS}/${MODEL}${MASS}_test${NEVENTS}.lhe
    mv test.log ${GRIDPACKDIR}/${MODEL}${MASS}/${MODEL}${MASS}_tarball_test.log
    cd ..
    rm -rf test
done

PROD=`(grep "<event" /hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/${MODEL}*/*lhe |wc -l)`
echo "Produced ${PROD} LHE events from ${NGRIDPACKS} gridpacks."

echo "Bye."
