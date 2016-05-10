#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/submitPythiaCondorJob.py"
#MODEL="SMS-TChiSlepSnu_mChi-"
MODEL="SMS-N2N3_mN-"
JOBS="jobs"

for MNLSP in {100..1000..100}; do
    python ${SCRIPT} ${MODEL}${MNLSP} --in-dir /hadoop/cms/store/user/${USER}/mcProduction/LHE/${MODEL}${MNLSP} --slha ${JOBS}/${MODEL}${MNLSP}/${MODEL}${MNLSP}.slha --qcut-range ${QMIN} ${QMAX} --proxy ${vomsdir}
done
