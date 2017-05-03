#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
PROC="Higgsino-C1N1_"
PARTN1="mN1-"
PARTC1="mC1-"
JOBS="jobs"
genprodir="/home/users/lshchuts/CMSSW_7_1_25_patch1/src/Configuration/GenProduction"
vomsdir="/tmp/x509up_u31605"

for MC1 in 80 100 120 140 160 180 200 220 240; do
    for DM in 3 7.5 10 15 20 30 40; do
	MN1=`awk "BEGIN {printf \"%.2f\n\", (${MC1}-${DM})}"`	
	MN1STR=${MN1/./p}
	MC1STR=${MC1/./p}
	MODEL=${PROC}${PARTC1}${MC1STR}_${PARTN1}${MN1STR}
	python ${SCRIPT} ${MODEL} --cards-dir ${JOBS}/${MODEL} --proxy ${vomsdir} --genproductions-dir ${genprodir}
    done
done
