#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/djr.py"
MODEL="SMS-StopStop-3J_mStop-"

for MPROD in {200,225,325}; do
    python ${SCRIPT} ${MODEL}${MPROD} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL}${MPROD} --qcut-range ${QMIN} ${QMAX}
done
