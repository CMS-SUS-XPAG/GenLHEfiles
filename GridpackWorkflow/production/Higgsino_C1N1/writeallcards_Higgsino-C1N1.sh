#!/bin/sh
JOBS="jobs"
TEMP="templatecards"
PROC="Higgsino-C1N1"
PARTN1="_mN1-"
PARTC1="_mC1-"

### Create cards and SLHAs for all mass points

for MC1 in 80 100 120 140 160 180 200 220 240; do
    for DM in 3 7.5 10 15 20 30 40; do
	MN1=`awk "BEGIN {printf \"%.2f\n\", (${MC1}-${DM})}"`	
	MN1STR=${MN1/./p}
	MC1STR=${MC1/./p}
	MODEL=${PROC}${PARTC1}${MC1STR}${PARTN1}${MN1STR}
	mkdir -p "${JOBS}/${MODEL}"
	cp ${TEMP}/${PROC}_run_card.dat "${JOBS}/${MODEL}/${MODEL}_run_card.dat"
	sed "s/%MN1%/${MN1STR}/g;s/%MC1%/${MC1STR}/g" ${TEMP}/${PROC}_proc_card.dat > "${JOBS}/${MODEL}/${MODEL}_proc_card.dat"
	sed "s/%MN1%/${MN1}/g;s/%MC1%/${MC1}/g" ${TEMP}/${PROC}_customizecards.dat > "${JOBS}/${MODEL}/${MODEL}_customizecards.dat"
	sed "s/%MN1%/${MN1}/g;s/%MC1%/${MC1}/g" ${TEMP}/${PROC}.slha > ${JOBS}/${MODEL}/${MODEL}.slha
    done
done
