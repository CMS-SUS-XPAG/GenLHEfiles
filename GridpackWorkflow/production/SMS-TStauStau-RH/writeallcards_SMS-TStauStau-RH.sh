#!/bin/sh
JOBS="jobs"
TEMP="templatecards"
PROC="SMS-TStauStau-RH"

### Create cards and SLHAs for all mass points

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
        mkdir -p "${JOBS}/${MODEL}"
        cp ${TEMP}/${PROC}_run_card.dat "${JOBS}/${MODEL}/${MODEL}_run_card.dat"
        sed "s/%MNLSP%/${MNLSP}/g;s/%MLSP%/${MLSP}/g" ${TEMP}/${PROC}_proc_card.dat > "${JOBS}/${MODEL}/${MODEL}_proc_card.dat"
        sed "s/%MNLSP%/${MNLSP}/g;s/%MLSP%/${MLSP}/g" ${TEMP}/${PROC}_customizecards.dat > "${JOBS}/${MODEL}/${MODEL}_customizecards.dat"
        sed "s/%MNLSP%/${MNLSP}/g;s/%MLSP%/${MLSP}/g" ${TEMP}/${PROC}.slha > ${JOBS}/${MODEL}/${MODEL}.slha
    done
done

