#!/bin/sh
SCRIPT="../../test/scripts/submitLHECondorJob.py"
MODEL="SMS-TStauStau_mStau-"

for MNLSP in {100..1300..25}; do
    python ${SCRIPT} ${MODEL}${MNLSP} --in-file /hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/${MODEL}${MNLSP}/${MODEL}${MNLSP}_tarball.tar.xz
done
