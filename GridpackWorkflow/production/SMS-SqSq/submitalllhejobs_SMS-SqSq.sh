#!/bin/sh
SCRIPT="../../test/scripts/submitLHECondorJob.py"
MODEL="SMS-SqSq_mSq-"

for MPROD in {300..1600..100}; do
    python ${SCRIPT} ${MODEL}${MPROD} --in-file /hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/${MODEL}${MPROD}/${MODEL}${MPROD}_tarball.tar.xz  --proxy ${vomsdir} --nevents 50000 --njobs 2
done


