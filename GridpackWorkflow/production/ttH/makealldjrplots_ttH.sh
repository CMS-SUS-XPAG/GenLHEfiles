#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/djr.py"
MODEL="ttH"

for MPROD in {350..550..20} {600..900..50}; do  
    python ${SCRIPT} ${MODEL}_mH-${MPROD} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL}_mH-${MPROD} --qcut-range ${QMIN} ${QMAX}
done
