#!/bin/bash

#First you need to set couple of settings:

# Number of cores to use while running
ncores=$1

CURRDIR=`pwd`
export PRODHOME=${CMSSW_BASE}/prod
# the folder where the generators will be installed
GEN_FOLDER=${PRODHOME}/Generators

MG=MG5_aMC_v2.2.1.tar.gz
MGSOURCE=https://cms-project-generators.web.cern.ch/cms-project-generators/$MG

SYSCALC=SysCalc_V1.1.0.tar.gz
SYSCALCSOURCE=https://cms-project-generators.web.cern.ch/cms-project-generators/$SYSCALC

MGBASEDIRORIG=${GEN_FOLDER}/MG5_aMC_v2_2_1
SCBASEDIRORIG=${GEN_FOLDER}/SysCalc

# create the install folder in case it doesn't exist yet
mkdir -p ${GEN_FOLDER}
cd ${GEN_FOLDER}

# Copy, Unzip and Delete the MadGraph tarball
wget --no-check-certificate ${MGSOURCE}
tar xzf ${MG}
rm ${MG}

# Apply any necessary patches on top of official release
mkdir -p ${GEN_FOLDER}/patches
cd ${GEN_FOLDER}/patches
wget https://raw.githubusercontent.com/cms-sw/genproductions/591ba2978dbd164b3482352980398cf5b422969c/bin/MadGraph5_aMCatNLO/patches/mgfixes.patch
wget https://raw.githubusercontent.com/cms-sw/genproductions/591ba2978dbd164b3482352980398cf5b422969c/bin/MadGraph5_aMCatNLO/patches/models.patch
cd ${GEN_FOLDER}
patch -l -p0 -i ${GEN_FOLDER}/patches/mgfixes.patch
patch -l -p0 -i ${GEN_FOLDER}/patches/models.patch

cd ${MGBASEDIRORIG}

# Setup LHAPDF

LHAPDFCONFIG=`echo "$LHAPDF_DATA_PATH/../../bin/lhapdf-config"`

# if lhapdf6 external is available then above points to lhapdf5 and needs to be overridden
LHAPDF6TOOLFILE=$CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/available/lhapdf6.xml
if [ -e $LHAPDF6TOOLFILE ]; then
  LHAPDFCONFIG=`cat $LHAPDF6TOOLFILE | grep "<environment name=\"LHAPDF6_BASE\"" | cut -d \" -f 4`/bin/lhapdf-config
fi

# make sure env variable for pdfsets points to the right place
export LHAPDF_DATA_PATH=`$LHAPDFCONFIG --datadir`

LHAPDFINCLUDES=`$LHAPDFCONFIG --incdir`
LHAPDFLIBS=`$LHAPDFCONFIG --libdir`
BOOSTINCLUDES=`scram tool tag boost INCLUDE`

# Set MG configuration

echo "set auto_update 0" > mgconfigscript
echo "set automatic_html_opening False" >> mgconfigscript
echo "set output_dependencies internal" >> mgconfigscript
echo "set lhapdf $LHAPDFCONFIG" >> mgconfigscript

# If number of cores is not specified, put it to 1
if [ -n ${ncores} ]; then
    ncores=1
fi

if [ ${ncores} -eq 1 ]; then
    echo "set run_mode 0" >> mgconfigscript
else
    echo "set run_mode 2" >> mgconfigscript
    echo "set nb_core" ${ncores} >> mgconfigscript
fi

echo "save options" >> mgconfigscript

./bin/mg5_aMC mgconfigscript

# get syscalc and compile
cd ${GEN_FOLDER}
wget --no-check-certificate ${SYSCALCSOURCE}
tar xzf ${SYSCALC}
rm ${SYSCALC}

cd ${SCBASEDIRORIG}
sed -i "s#INCLUDES =  -I../include#INCLUDES =  -I../include -I${LHAPDFINCLUDES} -I${BOOSTINCLUDES}#g" src/Makefile
sed -i "s#LIBS = -lLHAPDF#LIBS = ${LHAPDFLIBS}/libLHAPDF.a #g" src/Makefile
make

cd ${CURRDIR}