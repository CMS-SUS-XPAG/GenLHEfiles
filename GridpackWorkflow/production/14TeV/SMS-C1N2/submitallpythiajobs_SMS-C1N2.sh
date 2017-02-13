#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../../test/scripts/submitPythiaCondorJob.py"
MODEL="SMS-C1N2_mC1-"
JOBS="jobs"
vomsdir="/tmp/x509up_u31606"

for MNLSP in {300,400} ; do
    python ${SCRIPT} ${MODEL}${MNLSP} --in-dir /hadoop/cms/store/user/${USER}/mcProduction/LHE/${MODEL}${MNLSP} --slha ${JOBS}/${MODEL}${MNLSP}/${MODEL}${MNLSP}.slha --qcut-range ${QMIN} ${QMAX} --proxy ${vomsdir}
done
