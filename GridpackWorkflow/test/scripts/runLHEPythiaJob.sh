#### !/usr/local/bin/bash

### Script to generate LHE events and shower them using Pythia
### Intended for use with Condor at UCSD

### Authors:
### Ana Ovcharova
### Dustin Anderson

PROCESS=$1
NEVENTS=$2
FRAGMENT=$3
OUTDIR=$4
RANDOM_SEED=$5

CMSSW_REL="CMSSW_7_1_21_patch2"

echo "Process:"
echo $PROCESS

WORKDIR=$(pwd)
echo "Working directory: "
echo $WORKDIR

echo "Output directory set to: "
echo $OUTDIR

source /cvmfs/cms.cern.ch/cmsset_default.sh  
export SCRAM_ARCH=slc6_amd64_gcc481
echo $SCRAM_ARCH
echo $HOSTNAME
echo "Setting up a CMSSW release..."
eval `scramv1 project CMSSW ${CMSSW_REL}`
cd ${CMSSW_REL}/src
eval `scramv1 runtime -sh`

echo "Prepare fragment..."
mkdir -p Configuration/GenProduction/python
cp ${WORKDIR}/${FRAGMENT} Configuration/GenProduction/python/genfragment.py

eval "scramv1 build clean"
eval "scramv1 build"

echo "-----------> Let's begin...EVENT GENERATION"

echo "Unpacking gridpack tarball..."
tar -xaf $WORKDIR/${PROCESS}_tarball.tar.xz                                                    

echo "Running event generation..."
./runcmsgrid.sh $NEVENTS $RANDOM_SEED $(getconf _NPROCESSORS_ONLN)

echo "Generation finished. Copy output..."
LHEFILE='LHE_'${PROCESS}'_'${RANDOM_SEED}'.lhe'
#lcg-cp -v -b -D srmv2 --vo cms file:cmsgrid_final.lhe srm://bsrm-3.t2.ucsd.edu:8443/srm/v2/server?SFN=${OUTDIR}/$LHEFILE
gfal-copy -p -f -t 4200 cmsgrid_final.lhe gsiftp://gftp.t2.ucsd.edu/${OUTDIR}/${LHEFILE} --checksum ADLER32

echo "Fragment:"
cat Configuration/GenProduction/python/genfragment.py

#             SHOWER
#--------------------------------
GENFILE='GEN_'${PROCESS}'_'${FRAGMENT/.py/}'_'${RANDOM_SEED}'.root'

echo "--------------> Let's begin... SHOWER"
cmsDriver.py \
  Configuration/GenProduction/python/genfragment.py \
  --mc \
  --eventcontent RAWSIM \
  --datatier GEN-SIM \
  --conditions auto:run2_mc \
  --step GEN \
  --filein file:cmsgrid_final.lhe \
  --fileout file:${GENFILE} \
  -n -1

echo "Hadronization finished. Copy output..."
#lcg-cp -v -b -D srmv2 --vo cms file:`pwd`/${GENFILE} srm://bsrm-3.t2.ucsd.edu:8443/srm/v2/server?SFN=${OUTDIR}/${GENFILE}
gfal-copy -p -f -t 4200 ${GENFILE} gsiftp://gftp.t2.ucsd.edu/${OUTDIR}/${GENFILE} --checksum ADLER32

echo "ls in cmssw src dir"
ls

#cleanup
cd $WORKDIR
echo "ls in workdir"
ls
rm -rf ${CMSSW_REL}

echo "Bye."
