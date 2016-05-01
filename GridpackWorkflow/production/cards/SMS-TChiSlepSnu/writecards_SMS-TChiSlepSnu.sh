#!/bin/sh

### Use the templates to create cards for a specific mass point

MNLSP=$1
SUBDIR="jobs"
TEMP="templatecards"
PROC="SMS-TChiSlepSnu"
PART="_mChi-"
MODEL=${PROC}${PART}${MNLSP}

mkdir -p "${SUBDIR}/${MODEL}"
cp ${TEMP}/${PROC}_run_card.dat "${SUBDIR}/${MODEL}/${MODEL}_run_card.dat"
sed "s/%MNLSP%/${MNLSP}/g" ${TEMP}/${PROC}_proc_card.dat > "${SUBDIR}/${MODEL}/${MODEL}_proc_card.dat"
sed "s/%MNLSP%/${MNLSP}/g" ${TEMP}/${PROC}_customizecards.dat > "${SUBDIR}/${MODEL}/${MODEL}_customizecards.dat"
