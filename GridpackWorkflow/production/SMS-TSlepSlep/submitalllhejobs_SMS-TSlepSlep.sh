#!/bin/sh
SCRIPT="../../test/scripts/submitLHECondorJob.py"
MODEL="SMS-TSlepSlep_mSlep-"
vomsdir="/tmp/x509up_u31606"

for MNLSP in {100..1000..25}; do
    python ${SCRIPT} ${MODEL}${MNLSP} --in-file /hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/${MODEL}${MNLSP}/${MODEL}${MNLSP}_tarball.tar.xz --proxy ${vomsdir}
done
