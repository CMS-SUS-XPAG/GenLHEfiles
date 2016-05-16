#!/bin/sh
SCRIPT="../../test/scripts/submitLHECondorJob.py"
MODEL="SMS-GlGl_mGl-"

for MGL in {800..2300..100}; do
    python ${SCRIPT} ${MODEL}${MGL} --in-file /hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/${MODEL}${MGL}/${MODEL}${MGL}_tarball.tar.xz  --proxy ${vomsdir} --nevents 100000
done


