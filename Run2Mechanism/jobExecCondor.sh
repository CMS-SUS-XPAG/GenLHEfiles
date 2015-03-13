#!/bin/bash

#
# variables from arguments string in jdl
#

echo "Starting job on " `date` #Only to display the starting of production date
echo "Running on " `uname -a` #Only to display the machine where the job is running
echo "System release " `cat /etc/redhat-release` #And the system release
echo "CMSSW on Condor"

CMSSWVER=$1
OUTDIR=$2
PROCNAME=$3
CUSTOMCARD=$4

echo ""
echo "parameter set:"
echo "CMSSWVER:   $CMSSWVER"
echo "OUTDIR:     $OUTDIR"
echo "PROCNAME:   $PROCNAME"
echo "CUSTOMCARD: $CUSTOMCARD"

tar -xzf ${CMSSWVER}.tar.gz
cd ${CMSSWVER}
scram b ProjectRename
source /cvmfs/cms.cern.ch/cmsset_default.sh
# cmsenv
eval `scramv1 runtime -sh`
cd -

# environment variables for generator and run directory
source setupGenEnv.sh

# cardfiles location
CARDSDIR=${RUNBASEDIR}/cards

# run madgraph
# last argument specifies that the script is running in Condor
${RUNBASEDIR}/SUSY_generation.sh ${CARDSDIR} ${OUTDIR} ${PROCNAME} ${CUSTOMCARD} 1


