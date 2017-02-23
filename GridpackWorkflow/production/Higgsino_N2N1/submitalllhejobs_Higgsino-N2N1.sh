#!/bin/sh
SCRIPT="../../test/scripts/submitLHECondorJob.py"
PROC="Higgsino-N2N1"
PARTN2="_mN2-"
PARTN1="_mN1-"

for MN2 in 100 120 140 160 180 200 220 240; do
    for DM in 7.5 10 15 20 30 40; do
	MN1=`awk "BEGIN {printf \"%.2f\n\", (${MN2}-${DM})}"`	
	MC1=`awk "BEGIN {printf \"%.2f\n\", ((${MN1}+${MN2})/2)}"`
	MN2STR=${MN2/./p}
	MN1STR=${MN1/./p}
	MC1STR=${MC1/./p}
	MODEL=${PROC}${PARTN2}${MN2STR}${PARTN1}${MN1STR}
	python ${SCRIPT} ${MODEL} --in-file /hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/${MODEL}/${MODEL}_tarball.tar.xz --proxy ${vomsdir} --nevents 25000 --njobs 5
    done
done
