#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="SMS-StopStop_mStop-"
JOBS="jobs"

for MPROD in {167..817..25} {183..833..25} {825..925..50} {1250..1400..50}; do  
    python ${SCRIPT} ${MODEL}${MPROD} --cards-dir ${JOBS}/${MODEL}${MPROD} --genproductions-dir ${genprodir} --proxy ${vomsdir}
done
