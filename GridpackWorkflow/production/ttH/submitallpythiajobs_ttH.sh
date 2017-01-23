#!/bin/sh
SCRIPT="../../test/scripts/submitPythiaCondorJob.py"
MODEL="ttH"
JOBS="jobs"
NJETMAX=1

for MPROD in {350..550..20} {600..900..50}; do
    python ${SCRIPT} ${MODEL}_mH-${MPROD} --in-dir /hadoop/cms/store/user/${USER}/mcProduction/LHE/${MODEL}_mH-${MPROD} --slha ${JOBS}/${MODEL}_mH-${MPROD}/${MODEL}_mH-${MPROD}.slha --qcut-range 60 90 --proxy ${vomsdir} --nJetMax 1
done
