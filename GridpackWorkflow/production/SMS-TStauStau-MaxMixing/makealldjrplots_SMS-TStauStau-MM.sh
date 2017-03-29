#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/djr.py"
PROC="SMS-TStauStau-MM"

for MNLSP in {90..90..1} {100..400..50};do
    for MLSP in {1}; do
        #if (( ${MLSP} >= ${MNLSP} ));then
        #    continue
        #fi
        #if [[ ${MNLSP} -eq 90 ]] && [[ ${MLSP} -gt 10 ]];then
        #    continue
        #fi
        MODEL=${PROC}"_mStau-"${MNLSP}"_mLSP-"${MLSP}
        python ${SCRIPT} ${MODEL} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL} --qcut-range ${QMIN} ${QMAX}
    done
done
