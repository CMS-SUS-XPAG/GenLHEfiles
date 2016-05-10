#!/bin/sh
source setup.sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
JOBS="jobs"
MODEL="SMS-TStauStau_mStau-"

for MNLSP in {100..450..25}; do
    python ${SCRIPT} ${MODEL}${MNLSP} --cards-dir ${JOBS}/${MODEL}${MNLSP} --genproductions-dir ${genprodir} --proxy ${vomsdir}
done
