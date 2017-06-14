#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../../test/scripts/djr.py"
MODEL="SMS-N2N3_mN1-"

for MNLSP in {100..400..25}; do
    python ${SCRIPT} ${MODEL}${MNLSP}_mN2-25 /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL}${MNLSP} --qcut-range ${QMIN} ${QMAX}
done
