#!/bin/sh
source setup.sh
SCRIPT="../../../test/scripts/submitGridpackCondorJob.py"
JOBS="jobs"
PROC="SMS-TStauStau"

for MNLSP in {100..600..100}; do
    for MLSP in {1,100,200,300}; do
        if (( ${MLSP} >= ${MNLSP} ));then
            continue
        fi
        MODEL=${PROC}"_mStau-"${MNLSP}"_mLSP-"${MLSP}
        python ${SCRIPT} ${MODEL} --cards-dir ${JOBS}/${MODEL} --genproductions-dir ${genprodir} --proxy ${vomsdir}
    done
done
