#!/bin/sh

### Script to run gridpack generation via a condor job
### Intended for use with Condor at UCSD

### Author: Dustin Anderson

PROCESS=$1
OUTDIR=$2

echo "Process"
echo $PROCESS

WORKDIR=$(pwd)
echo "Working directory: "
echo $WORKDIR

echo "Output directory set to: "
echo $OUTDIR

#copy patches and cards into correct location
mkdir patches
cp ${WORKDIR}/ucsd.patch patches/
cp ${WORKDIR}/mgfixes.patch patches/
cp ${WORKDIR}/models.patch patches/
mkdir -p cards/${PROCESS}
cp ${WORKDIR}/${PROCESS}_run_card.dat cards/${PROCESS}
cp ${WORKDIR}/${PROCESS}_proc_card.dat cards/${PROCESS}
cp ${WORKDIR}/${PROCESS}_customizecards.dat cards/${PROCESS}
cp ${WORKDIR}/${PROCESS}_param_card.dat cards/${PROCESS}

#run script
echo "Running gridpack generation"
./gridpack_generation.sh ${PROCESS} cards/${PROCESS} 

#copy output
echo "Copy output"
lcg-cp -v -b -D srmv2 --vo cms file:${PROCESS}_tarball.tar.xz srm://bsrm-3.t2.ucsd.edu:8443/srm/v2/server?SFN=${OUTDIR}/${PROCESS}_tarball.tar.xz
lcg-cp -v -b -D srmv2 --vo cms file:${PROCESS}.log srm://bsrm-3.t2.ucsd.edu:8443/srm/v2/server?SFN=${OUTDIR}/${PROCESS}.log

echo "ls in production dir"
ls

#cleanup
cd $WORKDIR
echo "ls in workdir"
ls
rm -rf genproductions

echo "Bye."
