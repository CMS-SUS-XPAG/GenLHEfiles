#!/bin/sh
QMIN=$1
QMAX=$2
SCRIPT="../../test/scripts/djr.py"
MODEL="SMS-GlGl_mGl-"

for MGL in {800..2300..100}; do
    python ${SCRIPT} ${MODEL}${MGL} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL}${MGL} --qcut-range ${QMIN} ${QMAX}
done
