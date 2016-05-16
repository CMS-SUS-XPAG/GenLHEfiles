#!/bin/sh
SCRIPT="../../test/scripts/submitLHECondorJob.py"
MODEL="SMS-StopStop_mStop-"

for MPROD in {100..1200..100}; do
    python ${SCRIPT} ${MODEL}${MPROD} --in-file /hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/${MODEL}${MPROD}/${MODEL}${MPROD}_tarball.tar.xz  --proxy ${vomsdir} --nevents 100000
done


