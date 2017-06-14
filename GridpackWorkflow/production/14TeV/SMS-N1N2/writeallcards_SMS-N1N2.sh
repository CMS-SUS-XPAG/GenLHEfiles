#!/bin/sh
JOBS="jobs"
TEMP="templatecards"
PROC="SMS-N1N2"

### Create cards and SLHAs for all mass points

for MNLSP in {100..400..25}; do
    for MLSP in {7.5,25,50}; do
        MODEL=${PROC}"_mN1-"${MLSP}"_mN2-"${MNLSP}
        mkdir -p "${JOBS}/${MODEL}"
        cp ${TEMP}/${PROC}_run_card.dat "${JOBS}/${MODEL}/${MODEL}_run_card.dat"
        sed "s/%MNLSP%/${MNLSP}/g;s/%MLSP%/${MLSP}/g" ${TEMP}/${PROC}_proc_card.dat > "${JOBS}/${MODEL}/${MODEL}_proc_card.dat"
        sed "s/%MNLSP%/${MNLSP}/g;s/%MLSP%/${MLSP}/g" ${TEMP}/${PROC}_customizecards.dat > "${JOBS}/${MODEL}/${MODEL}_customizecards.dat"
        sed "s/%MNLSP%/${MNLSP}/g;s/%MLSP%/${MLSP}/g" ${TEMP}/${PROC}.slha > ${JOBS}/${MODEL}/${MODEL}.slha
    done
done
