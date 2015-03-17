#!/bin/bash

KEEPTAR=$1
JOBDIR=batch
OUTDIR=root://cmseos.fnal.gov//store/user/pedrok/SUSY2015/T1bbbb/genstep
THISDIR=${CMSSW_VERSION}/prod/GenLHEfiles/Run2Mechanism/genstep

# grid proxy check
voms-proxy-info --all > /dev/null
if [ $? -ne 0 ]; then
  voms-proxy-init -voms cms --valid 168:00
fi

# tarball of CMSSW area
if [ -z "$KEEPTAR" ]; then
  mkdir -p ${JOBDIR}
  tar --exclude=${THISDIR}/${JOBDIR} --exclude=${THISDIR}/logs --exclude=${THISDIR}/../lhe* --exclude=${THISDIR}/../scripts --exclude=${THISDIR}/../logs --exclude=${CMSSW_VERSION}/tmp -zcf ${JOBDIR}/${CMSSW_VERSION}.tar.gz -C ${CMSSW_BASE}/.. ${CMSSW_VERSION}
fi

for QCUT in 30 40 50 60
  do
    for FNAME in T1bbbb__1000021_800.0__n100000_p0_decayed_1000022_550 T1bbbb__1000021_800.0__n100000_p0_decayed_1000022_750 T1bbbb__1000021_1000.0__n100000_p0_decayed_1000022_700 T1bbbb__1000021_1000.0__n100000_p0_decayed_1000022_950
      do
        ./FStempsplit.sh ${JOBDIR} ${OUTDIR} ${FNAME} ${QCUT}
      done
  done
