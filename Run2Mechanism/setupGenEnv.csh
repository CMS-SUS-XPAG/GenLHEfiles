#!/bin/tcsh

set PRODHOME = ${CMSSW_BASE}/prod
# the folder where the generators will be installed
set GEN_FOLDER = ${PRODHOME}/Generators

setenv RUNBASEDIR ${PRODHOME}/GenLHEfiles/Run2Mechanism
setenv MGBASEDIR ${GEN_FOLDER}/MG5_aMC_v2_2_1
setenv SCBASEDIR ${GEN_FOLDER}/SysCalc

# Setup LHAPDF

set LHAPDFCONFIG = `echo "$LHAPDF_DATA_PATH/../../bin/lhapdf-config"`

# if lhapdf6 external is available then above points to lhapdf5 and needs to be overridden
set LHAPDF6TOOLFILE = $CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/available/lhapdf6.xml
if [ -e $LHAPDF6TOOLFILE ]; then
  set LHAPDFCONFIG = `cat $LHAPDF6TOOLFILE | grep "<environment name \"LHAPDF6_BASE\"" | cut -d \" -f 4`/bin/lhapdf-config
fi

# make sure env variable for pdfsets points to the right place
setenv LHAPDF_DATA_PATH `$LHAPDFCONFIG --datadir`
