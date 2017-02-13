#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../../test/scripts/djr.py"
MODEL="SMS-C1N2_mC1-"

for MNLSP in {300,400}; do
    python ${SCRIPT} ${MODEL}${MNLSP} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL}${MNLSP} --qcut-range ${QMIN} ${QMAX}
done
