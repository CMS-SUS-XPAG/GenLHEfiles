#!/bin/sh
JOBS="jobs"
TEMP="templatecards"
PROC="Higgsino_Full"
PARTMU="_MU-"
PARTM1="_M1-"

### Create cards and SLHAs for all mass points

for MU in 100 120 140 160 180 200 220 240; do
    for M1 in 300 400 500 600 800 1000 1200; do
        MUSTR=${MU/./p}
        M1STR=${M1/./p}
	MODEL=${PROC}${PARTMU}${MUSTR}${PARTM1}${M1STR}
	mkdir -p "${JOBS}/${MODEL}"
	cp ${TEMP}/${PROC}_run_card.dat "${JOBS}/${MODEL}/${MODEL}_run_card.dat"
	sed "s/%MU%/${MUSTR}/g;s/%M1%/${M1STR}/g" ${TEMP}/${PROC}_proc_card.dat > "${JOBS}/${MODEL}/${MODEL}_proc_card.dat"
	cp slha/susyhit_slha_${MUSTR}_${M1STR}.out "${JOBS}/${MODEL}/${MODEL}_param_card.dat"
#	cp slha/susyhit_slha_${MUSTR}_${M1STR}.out ${JOBS}/${MODEL}/${MODEL}.slha
    done
done
