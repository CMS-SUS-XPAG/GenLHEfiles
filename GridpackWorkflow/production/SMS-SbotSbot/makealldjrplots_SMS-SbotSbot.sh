#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/djr.py"
MODEL="SMS-SbotSbot_mSbot-"

for MPROD in {300..1300..100}; do
    python ${SCRIPT} ${MODEL}${MPROD} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL}${MPROD} --qcut-range ${QMIN} ${QMAX}
done
