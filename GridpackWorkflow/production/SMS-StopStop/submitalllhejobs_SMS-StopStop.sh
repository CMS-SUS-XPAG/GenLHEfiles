#!/bin/sh
SCRIPT="../../test/scripts/submitLHECondorJob.py"
MODEL="SMS-StopStop_mStop-"

for MPROD in {100..1400..100}; do
    python ${SCRIPT} ${MODEL}${MPROD} --in-file /hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/${MODEL}${MPROD}/${MODEL}${MPROD}_tarball.tar.xz  --proxy ${vomsdir} --nevents 20000 --njobs 5
done


