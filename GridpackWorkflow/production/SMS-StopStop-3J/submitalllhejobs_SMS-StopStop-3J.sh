#!/bin/sh
SCRIPT="../../test/scripts/submitLHECondorJob.py"
MODEL="SMS-StopStop-3J_mStop-"

for MPROD in {200,225,325}; do
    python ${SCRIPT} ${MODEL}${MPROD} --in-file /hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/${MODEL}${MPROD}/${MODEL}${MPROD}_tarball.tar.xz  --proxy ${vomsdir} --nevents 20000 --njobs 5
done


