#!/bin/sh
SCRIPT="../../../test/scripts/submitGridpackCondorJob.py"
PROC="SMS-N1N2"
JOBS="jobs"

for MNLSP in {100..400..25}; do
    for MLSP in {7.5,25,50}; do
        MODEL=${PROC}"_mN1-"${MLSP}"_mN2-"${MNLSP}
        python ${SCRIPT} ${MODEL} --cards-dir ${JOBS}/${MODEL}  --proxy /tmp/x509up_u31606 --genproductions-dir "/home/users/vdutta/genproductions/"
    done
done
