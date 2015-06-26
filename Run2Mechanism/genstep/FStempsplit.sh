#!/bin/bash

JOBDIR=$1
OUTDIR=$2
FNAME=$3
QCUT=$4

echo ""
echo ">> `/bin/date` Submitting condor job(s) : $1 $3 $4"

mkdir -p ${JOBDIR}

cat ./GEN_checkQcut_batch.py \
| sed -e s/FNAME/${FNAME}/ \
| sed -e s/THEQCUT/${QCUT}/ \
> ${JOBDIR}/GEN_${FNAME}_checkQcut${QCUT}.py

cat ./jobExecCondor.jdl \
| sed -e s/JOBNAME/GEN_${FNAME}_checkQcut${QCUT}/ \
| sed -e s/CMSSWVER/${CMSSW_VERSION}/ \
| sed -e s~OUTDIR~${OUTDIR}~ \
> ${JOBDIR}/jobExecCondor_GEN_${FNAME}_checkQcut${QCUT}.jdl

cd ${JOBDIR}
condor_submit jobExecCondor_GEN_${FNAME}_checkQcut${QCUT}.jdl
cd -