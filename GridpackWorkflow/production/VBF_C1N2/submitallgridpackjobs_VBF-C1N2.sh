#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="VBF-C1N2_mChi-"
JOBS="jobs"

# for MNLSP in {100..500..25}; do
for MNLSP in 200; do
    python ${SCRIPT} ${MODEL}${MNLSP} --cards-dir ${JOBS}/${MODEL}${MNLSP} --proxy /tmp/x509up_u31582 --genproductions-dir "/home/users/ana/genproductions/"
done
