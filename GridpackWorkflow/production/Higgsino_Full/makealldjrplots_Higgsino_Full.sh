#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/djr.py"
MODEL="SMS-SqSq_mSq-"
PROC="Higgsino_Full"
PARTMU="_MU-"
PARTM1="_M1-"

for MU in 100 120 140 160 180 200 220 240; do
    for M1 in 300 400 500 600 800 1000 1200; do
        MUSTR=${MU/./p}
        M1STR=${M1/./p}
        MODEL=${PROC}${PARTMU}${MUSTR}${PARTM1}${M1STR}
        python ${SCRIPT} ${MODEL}${MPROD} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL}${MPROD} --qcut-range 76 76
    done
done
