#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="Higgsino-N2N1_"
PARTN2="mN2-"
PARTN1="mN1-"
JOBS="jobs"
genprodir="/home/users/dspitzba/SUSYsignalProduction/genproductions/"

for MN2 in 100; do
    for DM in 10; do
#for MN2 in 100 120 140 160 180 200 220 240 250; do
#    for DM in 1 3 5 7.5 10 15 20 30 40 50; do
	MN1=`awk "BEGIN {printf \"%.2f\n\", (${MN2}-${DM})}"`	
	MC1=`awk "BEGIN {printf \"%.2f\n\", ((${MN1}+${MN2})/2)}"`
	MN2STR=${MN2/./p}
	MN1STR=${MN1/./p}
	MC1STR=${MC1/./p}
	MODELSTR=${MODEL}${PARTN2}${MN2STR}_${PARTN1}${MN1STR}
	python ${SCRIPT} ${MODELSTR} --cards-dir ${JOBS}/${MODELSTR} --genproductions-dir ${genprodir}
    done
done
