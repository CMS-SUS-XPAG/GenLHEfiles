#!/bin/sh
SCRIPT="../../../test/scripts/submitGridpackCondorJob.py"
MODEL="SMS-TChiSlepSnu_mChi-"
JOBS="jobs"

for MNLSP in {100..1300..25}; do
    python ${SCRIPT} ${MODEL}${MNLSP} --cards-dir ${JOBS}/${MODEL}${MNLSP}
done
