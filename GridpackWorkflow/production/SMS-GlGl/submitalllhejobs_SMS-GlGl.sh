#!/bin/sh
SCRIPT="../../test/scripts/submitLHECondorJob.py"
MODEL="SMS-GlGl_mGl-"

source setup.sh

for MGL in {600..2300..100}; do
    python ${SCRIPT} ${MODEL}${MGL} --in-file /hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/${MODEL}${MGL}/${MODEL}${MGL}_tarball.tar.xz  --proxy ${vomsdir} --nevents 10000 --njobs 5
done


