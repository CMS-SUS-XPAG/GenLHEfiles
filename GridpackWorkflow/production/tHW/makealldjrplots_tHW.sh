#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/djr.py"
MODEL="tHW"

for MPROD in {350..550..20}; do  
    python ${SCRIPT} ${MODEL}_mH-${MPROD} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL}_mH-${MPROD} --qcut-range ${QMIN} ${QMAX}
done
