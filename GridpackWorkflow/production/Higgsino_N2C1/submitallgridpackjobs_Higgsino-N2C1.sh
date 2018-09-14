#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
PROC="Higgsino-N2C1_"
PARTN2="mN2-"
PARTC1="mC1-"
JOBS="jobs"
genprodir="/home/users/dspitzba/SUSYsignalProduction_Summer16/genproductionsSummer16/"

#for MN2 in 100 120 140 160 180 200 220 240; do
#    for DM in 1 3 5 50; do
for MN2 in 250; do
    for DM in 1 3 5 7.5 10 15 20 30 40 50; do
	MN1=`awk "BEGIN {printf \"%.2f\n\", (${MN2}-${DM})}"`	
	MC1=`awk "BEGIN {printf \"%.2f\n\", ((${MN1}+${MN2})/2)}"`
	MN2STR=${MN2/./p}
	MN1STR=${MN1/./p}
	MC1STR=${MC1/./p}
	MODEL=${PROC}${PARTN2}${MN2STR}_${PARTC1}${MC1STR}
	python ${SCRIPT} ${MODEL} --cards-dir ${JOBS}/${MODEL} --genproductions-dir ${genprodir}
    done
done
