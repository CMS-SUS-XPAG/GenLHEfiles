#!/bin/sh

### Use the templates to create cards for a specific mass point

MNLSP=$1
SUBDIR="jobs"
PROC="SMS-TChiSlepSnu"
PART="_mChi-"
MODEL=${PROC}${PART}${MNLSP}

mkdir -p "${SUBDIR}/${MODEL}"
cp ${PROC}/${PROC}_run_card.dat "${SUBDIR}/${MODEL}/${MODEL}_run_card.dat"
sed "s/%MNLSP%/${MNLSP}/g" ${PROC}/${PROC}_proc_card.dat > "${SUBDIR}/${MODEL}/${MODEL}_proc_card.dat"
sed "s/%MNLSP%/${MNLSP}/g" ${PROC}/${PROC}_customizecards.dat > "${SUBDIR}/${MODEL}/${MODEL}_customizecards.dat"
