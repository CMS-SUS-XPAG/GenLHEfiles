#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="SMS-SbotSbot_mSbot-"
JOBS="jobs"
genprodir='/home/users/dspitzba/SUSYsignalProduction/genproductions/'

#for MPROD in {925..1225..50} {1350..1600..50}; do
for MPROD in {300..1250..25} {1300..2300..50}; do
    python ${SCRIPT} ${MODEL}${MPROD} --cards-dir ${JOBS}/${MODEL}${MPROD} --genproductions-dir ${genprodir}
done
