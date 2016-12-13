#!/bin/sh
SCRIPT="../../test/scripts/submitPythiaCondorJob.py"
MODEL="SMS-StopStop-3J_mStop-"
JOBS="jobs"

for MPROD in {200,225,325}; do
    python ${SCRIPT} ${MODEL}${MPROD} --in-dir /hadoop/cms/store/user/${USER}/mcProduction/LHE/${MODEL}${MPROD} --slha ${JOBS}/${MODEL}${MPROD}/${MODEL}${MPROD}.slha --qcut-range 60 80 --proxy ${vomsdir}
done
