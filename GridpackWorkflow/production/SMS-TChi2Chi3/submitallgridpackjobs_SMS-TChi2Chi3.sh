#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="SMS-TChi2Chi3_mChi-"
JOBS="jobs"

for MNLSP in {100..1000..25}; do
    python ${SCRIPT} ${MODEL}${MNLSP} --cards-dir ${JOBS}/${MODEL}${MNLSP} --genproductions-dir ${genprodir} --proxy ${vomsdir}
done
