#!/bin/bash

PRODHOME=${CMSSW_BASE}/prod
# the folder where the generators will be installed
GEN_FOLDER=${PRODHOME}/Generators

export RUNBASEDIR=${PRODHOME}/GenLHEfiles/Run2Mechanism
export MGBASEDIR=${GEN_FOLDER}/MG5_aMC_v2_2_1
export SCBASEDIR=${GEN_FOLDER}/SysCalc

# Setup LHAPDF

LHAPDFCONFIG=`echo "$LHAPDF_DATA_PATH/../../bin/lhapdf-config"`

# if lhapdf6 external is available then above points to lhapdf5 and needs to be overridden
LHAPDF6TOOLFILE=$CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/available/lhapdf6.xml
if [ -e $LHAPDF6TOOLFILE ]; then
  LHAPDFCONFIG=`cat $LHAPDF6TOOLFILE | grep "<environment name=\"LHAPDF6_BASE\"" | cut -d \" -f 4`/bin/lhapdf-config
fi

# make sure env variable for pdfsets points to the right place
export LHAPDF_DATA_PATH=`$LHAPDFCONFIG --datadir`
