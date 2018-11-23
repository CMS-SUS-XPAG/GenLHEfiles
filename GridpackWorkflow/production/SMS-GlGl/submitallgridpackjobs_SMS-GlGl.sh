#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="SMS-GlGl_mGl-"
JOBS="jobs"
genprodir="/home/users/dspitzba/SUSYsignalProduction/genproductions/"

#for MGL in {600..750..50} {800..1600..25} {1650..2300..50}; do
for MGL in {600..2800..25}; do
    python ${SCRIPT} ${MODEL}${MGL} --cards-dir ${JOBS}/${MODEL}${MGL} --genproductions-dir ${genprodir}
done
