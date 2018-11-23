#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="SMS-StopStop_mStop-"
JOBS="jobs"
genprodir="/home/users/dspitzba/SUSYsignalProduction/genproductions/"

#for MPROD in {167..817..25} {183..833..25} {825..925..50} {1250..1400..50}; do  
#for MPROD in {175,250,275,350,650,850,1200}; do
for MPROD in {150..2400..25}; do
    python ${SCRIPT} ${MODEL}${MPROD} --cards-dir ${JOBS}/${MODEL}${MPROD} --genproductions-dir ${genprodir}
done
