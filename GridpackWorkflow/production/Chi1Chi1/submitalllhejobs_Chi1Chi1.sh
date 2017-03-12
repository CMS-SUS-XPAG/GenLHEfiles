#!/bin/sh
SCRIPT="../../test/scripts/submitLHECondorJob.py"
MODEL="Chi1Chi1_mChi-"

for MNLSP in {100..1500..25}; do
    python ${SCRIPT} ${MODEL}${MNLSP} --in-file /hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/${MODEL}${MNLSP}/${MODEL}${MNLSP}_tarball.tar.xz
done
