#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/djr.py"
MODEL="Chi1Chi1_mChi-"

for MNLSP in {100..1500..50}; do
    python ${SCRIPT} ${MODEL}${MNLSP} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL}${MNLSP} --qcut-range ${QMIN} ${QMAX}
done
