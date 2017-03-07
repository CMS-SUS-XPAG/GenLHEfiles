#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/submitPythiaCondorJob.py"
PROC="Higgsino_Full"
PARTMU="_MU-"
PARTM1="_M1-"
JOBS="jobs"
genprodir="/home/users/lshchuts/CMSSW_7_1_25_patch1/src/Configuration/GenProduction"
vomsdir="/tmp/x509up_u31605"

for MU in 100 120 140 160 180 200 220 240; do
    for M1 in 300 400 500 600 800 1000 1200; do
        MUSTR=${MU/./p}
        M1STR=${M1/./p}
        MODEL=${PROC}${PARTMU}${MUSTR}${PARTM1}${M1STR}
        python ${SCRIPT} ${MODEL} --in-dir /hadoop/cms/store/user/${USER}/mcProduction/LHE/${MODEL} --slha /home/users/lshchuts/GenLHEfiles/GridpackWorkflow/production/Higgsino_Full/slha/susyhit_slha_${MUSTR}_${M1STR}.out --qcut-range 76 76 --proxy ${vomsdir} --nJetMax 2
    done
done
