#!/bin/sh
SCRIPT="../../test/scripts/submitLHECondorJob.py"
MODEL="SMS-GlGl_mGl-"

#/hadoop/cms/store/user/dspitzba/mcProduction/sus_sms/2017/LO_PDF/SMS-GlGl

#source setup.sh

for MGL in {2000..2800..100}; do
    python ${SCRIPT} ${MODEL}${MGL} --in-file /hadoop/cms/store/user/${USER}/mcProduction/sus_sms/2017/LO_PDF/SMS-GlGl/${MODEL}${MGL}_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz  --nevents 10000 --njobs 5
done


