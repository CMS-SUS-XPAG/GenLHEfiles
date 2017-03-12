#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/djr.py"
MODEL="SMS-TStauStau_mStau-"

for MNLSP in {100..1000..100}; do
    python ${SCRIPT} ${MODEL}${MNLSP} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL}${MNLSP} --qcut-range ${QMIN} ${QMAX}
done
