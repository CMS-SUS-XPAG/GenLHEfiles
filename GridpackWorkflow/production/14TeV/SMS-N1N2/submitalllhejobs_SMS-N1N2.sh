#!/bin/sh
SCRIPT="../../../test/scripts/submitLHECondorJob.py"
PROC="SMS-N1N2"

for MNLSP in {100..400..25}; do
    for MLSP in {7.5,25,50}; do
        MODEL=${PROC}"_mN1-"${MLSP}"_mN2-"${MNLSP}
        python ${SCRIPT} ${MODEL} --in-file /hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/${MODEL}/${MODEL}_tarball.tar.xz --proxy ${vomsdir}
    done
done
