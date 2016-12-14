#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="SMS-StopStop-3J_mStop-"
JOBS="jobs"

for MPROD in {200,225,325}; do
    python ${SCRIPT} ${MODEL}${MPROD} --cards-dir ${JOBS}/${MODEL}${MPROD} --genproductions-dir ${genprodir} --proxy ${vomsdir}
done
