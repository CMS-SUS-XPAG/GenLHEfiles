#!/bin/sh
GRIDPACKDIR=/hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS
MODEL='ttH_mH-'
OUTMODEL='ttH'
PART='_mH-'

for MASS in {350..550..20} {600..900..50}; do  
    echo "Copying ${GRIDPACKDIR}/${MODEL}${MASS}/${MODEL}${MASS}_tarball.tar.xz to the following directory on EOS:"
    echo "/store/group/phys_generator/cvmfs/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/${OUTMODEL}/${OUTMODEL}${PART}${MASS}_tarball.tar.xz"
    xrdcp ${GRIDPACKDIR}/${MODEL}${MASS}/${MODEL}${MASS}_tarball.tar.xz root://eoscms.cern.ch///eos/cms/store/group/phys_generator/cvmfs/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/${OUTMODEL}/${OUTMODEL}${PART}${MASS}_tarball.tar.xz
done
