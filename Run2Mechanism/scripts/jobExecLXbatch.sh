#!/bin/bash

echo "Starting job on " `date` #Only to display the starting of production date
echo "Running on " `uname -a` #Only to display the machine where the job is running
echo "System release " `cat /etc/redhat-release` #And the system release

cd CMSDIR
# cmsenv
eval `scramv1 runtime -sh`
cd -

# environment variables for generator and run directory
source RUNDIR/scripts/setupGenEnv.sh

# cardfiles location
CARDSDIR=${RUNBASEDIR}/cards

# run madgraph
${RUNBASEDIR}/SUSY_generation.sh CARDSDIR OUTDIR PROCNAME CUSTOMCARD


