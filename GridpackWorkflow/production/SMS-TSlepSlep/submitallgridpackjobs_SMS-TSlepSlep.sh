#!/bin/sh
source setup.sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
JOBS="jobs"
MODEL="SMS-TSlepSlep_mSlep-"

for MNLSP in {100..1000..25}; do
#    if [ $MNLSP -eq 100 ]; then
    python ${SCRIPT} ${MODEL}${MNLSP} --cards-dir ${JOBS}/${MODEL}${MNLSP} --genproductions-dir ${genprodir} --proxy ${vomsdir}
#    fi
done
