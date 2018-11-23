#!/bin/sh
GRIDPACKDIR=/hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS
MODEL='SMS-StopStop_mStop-'
OUTMODEL='SMS-StopStop'
PART='_mStop-'

for MASS in {300..900..50} ; do
    echo "Copying ${GRIDPACKDIR}/${MODEL}${MASS}/${MODEL}${MASS}_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.gz to the following directory on EOS:"
    echo "/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/sus_sms/LO_PDF/SMS-StopStop/v1/${OUTMODEL}/${OUTMODEL}${PART}${MASS}_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz"
    xrdcp ${MODEL}${MASS}_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz root://eoscms.cern.ch///eos/cms/store/group/phys_generator/cvmfs/gridpacks/2017/13TeV/madgraph/V5_2.4.2/sus_sms/LO_PDF/${OUTMODEL}/v1/${OUTMODEL}${PART}${MASS}_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz
done
