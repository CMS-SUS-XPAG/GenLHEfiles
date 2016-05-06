#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/submitPythiaCondorJob.py"
MODEL="Chi1Chi1_mChi-"
JOBS="jobs"

for MNLSP in {100..800..50}; do
    python ${SCRIPT} ${MODEL}${MNLSP} --in-dir /hadoop/cms/store/user/${USER}/mcProduction/LHE/${MODEL}${MNLSP} --slha ${JOBS}/${MODEL}${MNLSP}/${MODEL}${MNLSP}.slha --qcut-range ${QMIN} ${QMAX}
done
