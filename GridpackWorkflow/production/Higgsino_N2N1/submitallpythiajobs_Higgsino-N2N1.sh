#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/submitPythiaCondorJob.py"
PROC="Higgsino-N2N1"
PARTN2="_mN2-"
PARTN1="_mN1-"
JOBS="jobs"

for MN2 in 100 120 140 160 180 200 220 240; do
    for DM in 7.5 10 15 20 30 40; do
	MN1=`awk "BEGIN {printf \"%.2f\n\", (${MN2}-${DM})}"`	
	MC1=`awk "BEGIN {printf \"%.2f\n\", ((${MN1}+${MN2})/2)}"`
	MN2STR=${MN2/./p}
	MN1STR=${MN1/./p}
	MC1STR=${MC1/./p}
	MODEL=${PROC}${PARTN2}${MN2STR}${PARTN1}${MN1STR}
	python ${SCRIPT} ${MODEL} --in-dir /hadoop/cms/store/user/${USER}/mcProduction/LHE/${MODEL} --slha ${JOBS}/${MODEL}/${MODEL}.slha --qcut-range ${QMIN} ${QMAX} --proxy ${vomsdir}
    done
done
