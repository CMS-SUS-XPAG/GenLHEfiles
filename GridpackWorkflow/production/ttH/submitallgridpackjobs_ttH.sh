#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="ttH"
JOBS="jobs"

for MPROD in {350..550..20} {600..900..50}; do  
    python ${SCRIPT} ${MODEL}_mH-${MPROD} --cards-dir ${JOBS}/${MODEL}_mH-${MPROD} --genproductions-dir ${genprodir} --proxy ${vomsdir}
done
