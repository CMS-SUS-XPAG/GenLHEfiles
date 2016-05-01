#!/bin/sh
MODEL="SMS-TChiSlepSnu"
JOBS="jobs"
PART="_mChi-"

for MNLSP in {100..1300..25}; do
    sed "s/%MNLSP%/${MNLSP}/g" templatecards/${MODEL}.slha > ${JOBS}/${MODEL}${PART}${MNLSP}/${MODEL}${PART}${MNLSP}.slha
done
