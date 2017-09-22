#!/bin/sh
SCRIPT="../../../test/scripts/submitGridpackCondorJob.py"
MODEL="SMS-C2N4_mC2-"
JOBS="jobs"

for MNLSP in {400..1000..50} ; do
    python ${SCRIPT} ${MODEL}${MNLSP} --cards-dir ${JOBS}/${MODEL}${MNLSP} --proxy /tmp/x509up_u31606 --genproductions-dir "/home/users/vdutta/genproductions/"
done
