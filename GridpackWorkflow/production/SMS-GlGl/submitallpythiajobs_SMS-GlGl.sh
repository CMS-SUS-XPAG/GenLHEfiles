#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/submitPythiaCondorJob.py"
MODEL="SMS-GlGl_mGl-"
JOBS="jobs"

for MGL in {600..2300..100}; do
    python ${SCRIPT} ${MODEL}${MGL} --in-dir /hadoop/cms/store/user/${USER}/mcProduction/LHE/${MODEL}${MGL} --slha ${JOBS}/${MODEL}${MGL}/${MODEL}${MGL}.slha --slha ${JOBS}/${MODEL}${MGL}/${MODEL}${MGL}.slha --qcut-range ${MIN} ${MAX} --proxy ${vomsdir}
done
