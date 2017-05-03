#!/bin/sh
GRIDPACKDIR=/hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS
MODEL='Higgsino-C1N1'
PARTN1='_mN1-'
PARTC1='_mC1-'

for MC1 in 80 100 120 140 160 180 200 220 240; do
    for DM in 3 7.5 10 15 20 30 40; do
	MN1=`awk "BEGIN {printf \"%.2f\n\", (${MC1}-${DM})}"`	
	MN1STR=${MN1/./p}
	MC1STR=${MC1/./p}
	MODELSTR=${MODEL}${PARTC1}${MC1STR}${PARTN1}${MN1STR}	
	echo "Copying ${GRIDPACKDIR}/${MODELSTR}/${MODELSTR}_tarball.tar.xz to the following directory on EOS:"
	echo "/store/group/phys_generator/cvmfs/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/${MODEL}/${MODELSTR}_tarball.tar.xz"
	xrdcp ${GRIDPACKDIR}/${MODELSTR}/${MODELSTR}_tarball.tar.xz root://eoscms.cern.ch///eos/cms/store/group/phys_generator/cvmfs/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/${MODEL}/${MODELSTR}_tarball.tar.xz
    done
done
