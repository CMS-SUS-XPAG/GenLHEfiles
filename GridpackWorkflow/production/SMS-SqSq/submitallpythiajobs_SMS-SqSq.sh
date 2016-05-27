#!/bin/sh
SCRIPT="../../test/scripts/submitPythiaCondorJob.py"
MODEL="SMS-SqSq_mSq-"
JOBS="jobs"

for MPROD in {300..1800..100}; do
    python ${SCRIPT} ${MODEL}${MPROD} --in-dir /hadoop/cms/store/user/${USER}/mcProduction/LHE/${MODEL}${MPROD} --slha ${JOBS}/${MODEL}${MPROD}/${MODEL}${MPROD}.slha --qcut-range 60 90 --proxy ${vomsdir}
done

