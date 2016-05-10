#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="SMS-GlGl_mGl-"
JOBS="jobs"

for MGL in {800..1600..25} {1650..2300..50}; do
    python ${SCRIPT} ${MODEL}${MGL} --cards-dir ${JOBS}/${MODEL}${MGL} --genproductions-dir ${genprodir} --proxy ${vomsdir}
done
