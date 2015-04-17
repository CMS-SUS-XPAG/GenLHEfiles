#!/bin/bash

KEEPTAR=$1
JOBDIR=batch
OUTDIR=root://cmseos.fnal.gov//store/user/pedrok/SUSY2015/T1bbbb/genstep
THISDIR=${CMSSW_VERSION}/prod/GenLHEfiles/Run2Mechanism/genstep

./FScheck.sh "$KEEPTAR" "$JOBDIR"

for QCUT in 30 40 50 60
  do
    for FNAME in T1bbbb__1000021_800.0__n100000_p0_decayed_1000022_550 T1bbbb__1000021_800.0__n100000_p0_decayed_1000022_750 T1bbbb__1000021_1000.0__n100000_p0_decayed_1000022_700 T1bbbb__1000021_1000.0__n100000_p0_decayed_1000022_950
      do
        ./FStempsplit.sh ${JOBDIR} ${OUTDIR} ${FNAME} ${QCUT}
      done
  done
