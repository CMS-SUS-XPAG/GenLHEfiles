#!/bin/sh
source setup.sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
JOBS="jobs"
PROC="SMS-TStauStau-LH"

for MNLSP in {90..90..1} {100..300..25} {350..400..50};do
    for MLSP in {0..50..10} {75..150..25} {200..200..1}; do
        if [[ ${MLSP} -eq 0 ]];then
            MLSP=1
        fi
        if (( ${MLSP} >= ${MNLSP} ));then
            continue
        fi
        if [[ ${MNLSP} -eq 90 ]] && [[ ${MLSP} -gt 10 ]];then
            continue
        fi
        MODEL=${PROC}"_mStau-"${MNLSP}"_mLSP-"${MLSP}
        python ${SCRIPT} ${MODEL} --cards-dir ${JOBS}/${MODEL} --genproductions-dir ${genprodir} --proxy ${vomsdir}
    done
done
