#!/bin/sh
source setup.sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/submitPythiaCondorJob.py"
PROC="SMS-TStauStau-MM"
JOBS="jobs"

for MNLSP in {90..90..1} {100..400..50};do
    for MLSP in {1}; do
        #if (( ${MLSP} >= ${MNLSP} ));then
        #    continue
        #fi
        #if [[ ${MNLSP} -eq 90 ]] && [[ ${MLSP} -gt 10 ]];then
        #    continue
        #fi
        MODEL=${PROC}"_mStau-"${MNLSP}"_mLSP-"${MLSP}
        python ${SCRIPT} ${MODEL} --in-dir /hadoop/cms/store/user/${USER}/mcProduction/LHE/${MODEL} --slha ${JOBS}/${MODEL}/${MODEL}.slha --qcut-range ${QMIN} ${QMAX} --proxy ${vomsdir}
    done
done
