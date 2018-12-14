#!/bin/sh
QMIN=150
QMAX=170
SCRIPT="../../test/scripts/djr.py"
MODEL="SMS-GlGl_mGl-"

#for MGL in {600..2800..25}; do
for MGL in {2500..2800..100}; do
    python ${SCRIPT} ${MODEL}${MGL} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL}${MGL} --qcut-range ${QMIN} ${QMAX}
done
