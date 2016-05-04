#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/djr.py"
MODEL="SMS-TChiSlepSnu_mChi-"

for MNLSP in {100..1300..100}; do
    python ${SCRIPT} ${MODEL}${MNLSP} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL}${MNLSP} --qcut-range ${QMIN} ${QMAX}
done
