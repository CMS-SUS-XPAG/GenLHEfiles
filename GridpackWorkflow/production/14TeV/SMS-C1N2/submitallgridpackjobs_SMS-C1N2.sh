#!/bin/sh
SCRIPT="../../../test/scripts/submitGridpackCondorJob.py"
MODEL="SMS-C1N2_mC1-"
JOBS="jobs"

for MNLSP in {300,400} ; do
    python ${SCRIPT} ${MODEL}${MNLSP} --cards-dir ${JOBS}/${MODEL}${MNLSP} --proxy /tmp/x509up_u31606 --genproductions-dir "/home/users/vdutta/genproductions/"
done
