#!/bin/sh
GRIDPACKDIR=/hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS
MODEL="SMS-TSlepSlep_mSlep-"

for MNLSP in {100..1000..25}; do
	MODELSTR=${MODEL}${MNLSP}	
	echo "Copying ${GRIDPACKDIR}/${MODELSTR}/${MODELSTR}_tarball.tar.xz to the following directory on EOS:"
	echo "/store/group/phys_generator/cvmfs/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/SMS-SlepSlep/v2/${MODELSTR}_tarball.tar.xz"
	xrdcp ${GRIDPACKDIR}/${MODELSTR}/${MODELSTR}_tarball.tar.xz root://eoscms.cern.ch///eos/cms/store/group/phys_generator/cvmfs/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/SMS-SlepSlep/v2/${MODELSTR}_tarball.tar.xz
done
