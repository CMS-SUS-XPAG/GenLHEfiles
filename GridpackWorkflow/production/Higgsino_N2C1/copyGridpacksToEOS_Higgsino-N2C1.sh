#!/bin/sh
GRIDPACKDIR=/hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS
MODEL='Higgsino-N2C1'
PARTN2='_mN2-'
PARTC1='_mC1-'

#for MN2 in 100 120 140 160 180 200 220 240; do
for MN2 in 250; do
#    for DM in 1 3 5 50; do
    for DM in 1 3 5 7.5 10 15 20 30 40 50; do
	MN1=`awk "BEGIN {printf \"%.2f\n\", (${MN2}-${DM})}"`	
	MC1=`awk "BEGIN {printf \"%.2f\n\", ((${MN1}+${MN2})/2)}"`
	MN2STR=${MN2/./p}
	MN1STR=${MN1/./p}
	MC1STR=${MC1/./p}
	MODELSTR=${MODEL}${PARTN2}${MN2STR}${PARTC1}${MC1STR}	
	echo "Copying ${GRIDPACKDIR}/${MODELSTR}/${MODELSTR}_tarball.tar.xz to the following directory on EOS:"
	echo "/store/group/phys_generator/cvmfs/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/${MODEL}/${MODELSTR}_tarball.tar.xz"
	xrdcp ${GRIDPACKDIR}/${MODELSTR}/${MODELSTR}_tarball.tar.xz root://eoscms.cern.ch///eos/cms/store/group/phys_generator/cvmfs/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/${MODEL}/${MODELSTR}_tarball.tar.xz
    done
done
