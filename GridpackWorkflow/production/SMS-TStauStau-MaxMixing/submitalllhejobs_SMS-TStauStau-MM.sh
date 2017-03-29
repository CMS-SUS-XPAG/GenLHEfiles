#!/bin/sh
SCRIPT="../../test/scripts/submitLHECondorJob.py"
PROC="SMS-TStauStau-MM"
vomsdir="/tmp/x509up_u31606"
MLSP=1

for MNLSP in {90..90..1} {100..400..50};do
    MODEL=${PROC}"_mStau-"${MNLSP}"_mLSP-"${MLSP}
    python ${SCRIPT} ${MODEL} --in-file /hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/${MODEL}/${MODEL}_tarball.tar.xz --proxy ${vomsdir}
done
