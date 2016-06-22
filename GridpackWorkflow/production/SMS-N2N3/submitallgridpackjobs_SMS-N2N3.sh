#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="SMS-N2N3_mN-"
JOBS="jobs"

for MNLSP in 127; do
    python ${SCRIPT} ${MODEL}${MNLSP} --cards-dir ${JOBS}/${MODEL}${MNLSP}  --proxy /tmp/x509up_u31582 --genproductions-dir "/home/users/ana/genproductions/"
done
