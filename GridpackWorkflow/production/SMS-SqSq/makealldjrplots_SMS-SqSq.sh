#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/djr.py"
MODEL="SMS-SqSq_mSq-"

for MPROD in {300..500..100}; do
    python ${SCRIPT} ${MODEL}${MPROD} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL}${MPROD} --qcut-range 55 59
done

for MPROD in {600..1200..100}; do
    python ${SCRIPT} ${MODEL}${MPROD} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL}${MPROD} --qcut-range 65 69
done

for MPROD in {1300..1600..100}; do
    python ${SCRIPT} ${MODEL}${MPROD} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL}${MPROD} --qcut-range 68 72
done
