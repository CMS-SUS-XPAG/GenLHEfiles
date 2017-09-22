#!/bin/sh
JOBS="jobs"
TEMP="templatecards"
PROC="SMS-TStauStau"

### Create cards and SLHAs for all mass points

for MNLSP in {100..600..100}; do
    for MLSP in {1,100,200,300}; do
        if (( ${MLSP} >= ${MNLSP} ));then
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

