#!/bin/sh
QMIN=74
QMAX=94
SCRIPT="../../test/scripts/djr.py"
MODEL="SMS-StopStop_mStop-"

#for MPROD in {2000..2700..100}; do
for MPROD in 2800; do
    python ${SCRIPT} ${MODEL}${MPROD} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL}${MPROD} --qcut-range ${QMIN} ${QMAX}
done
