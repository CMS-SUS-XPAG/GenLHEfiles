#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/submitPythiaCondorJob.py"
MODEL="SMS-TStauStau_mStau-"
JOBS="jobs"

for MNLSP in {100..425..100}; do
    python ${SCRIPT} ${MODEL}${MNLSP} --in-dir /hadoop/cms/store/user/${USER}/mcProduction/LHE/${MODEL}${MNLSP} --slha ${JOBS}/${MODEL}${MNLSP}/${MODEL}${MNLSP}.slha --qcut-range ${QMIN} ${QMAX} --proxy ${vomsdir}
done
