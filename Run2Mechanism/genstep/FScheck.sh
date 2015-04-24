#!/bin/bash

KEEPTAR=$1
JOBDIR=$2

# grid proxy existence & expiration check
PCHECK=`voms-proxy-info -timeleft`
if [[ ($? -ne 0) || ("$PCHECK" -eq 0) ]]; then
  voms-proxy-init -voms cms --valid 168:00
fi

# tarball of CMSSW area
if [ -z "$KEEPTAR" ]; then
  mkdir -p ${JOBDIR}
  tar --exclude-caches-all -zcf ${JOBDIR}/${CMSSW_VERSION}.tar.gz -C ${CMSSW_BASE}/.. ${CMSSW_VERSION}
fi

