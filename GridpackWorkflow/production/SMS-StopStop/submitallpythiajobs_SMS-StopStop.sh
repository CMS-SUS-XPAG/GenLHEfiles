#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/submitPythiaCondorJob.py"
MODEL="SMS-StopStop_mStop-"
JOBS="jobs"

for MPROD in {100..1200..100}; do
    python ${SCRIPT} ${MODEL}${MPROD} --in-dir /hadoop/cms/store/user/${USER}/mcProduction/LHE/${MODEL}${MPROD} --slha ${JOBS}/${MODEL}${MPROD}/${MODEL}${MPROD}.slha --qcut-range ${QMIN} ${QMAX} --proxy ${vomsdir}
done
