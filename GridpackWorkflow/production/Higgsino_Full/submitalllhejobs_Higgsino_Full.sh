#!/bin/sh
SCRIPT="../../test/scripts/submitLHECondorJob.py"
PROC="Higgsino_Full"
PARTMU="_MU-"
PARTM1="_M1-"
genprodir="/home/users/lshchuts/CMSSW_7_1_25_patch1/src/Configuration/GenProduction"
vomsdir="/tmp/x509up_u31605"

for MU in 100 120 140 160 180 200 220 240; do
    for M1 in 300 400 500 600 800 1000 1200; do
        MUSTR=${MU/./p}
        M1STR=${M1/./p}
        MODEL=${PROC}${PARTMU}${MUSTR}${PARTM1}${M1STR}
        python ${SCRIPT} ${MODEL} --in-file /hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/${MODEL}/${MODEL}_tarball.tar.xz --proxy ${vomsdir} --nevents 25000 --njobs 5
    done
done

