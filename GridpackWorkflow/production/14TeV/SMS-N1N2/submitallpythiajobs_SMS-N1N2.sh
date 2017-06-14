#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../../test/scripts/submitPythiaCondorJob.py"
PROC="SMS-N1N2"
JOBS="jobs"

for MNLSP in {100..400..25}; do
    for MLSP in {7.5,25,50}; do
        MODEL=${PROC}"_mN1-"${MLSP}"_mN2-"${MNLSP}
        python ${SCRIPT} ${MODEL} --in-dir /hadoop/cms/store/user/${USER}/mcProduction/LHE/${MODEL} --slha ${JOBS}/${MODEL}/${MODEL}.slha --qcut-range ${QMIN} ${QMAX} --proxy ${vomsdir}
    done
done
