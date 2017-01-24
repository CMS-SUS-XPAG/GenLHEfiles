#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="tHq"
JOBS="jobs"

for MPROD in {350..550..20}; do  
    python ${SCRIPT} ${MODEL}_mH-${MPROD} --cards-dir ${JOBS}/${MODEL}_mH-${MPROD} --genproductions-dir ${genprodir} --proxy ${vomsdir}
done
