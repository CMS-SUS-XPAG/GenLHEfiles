#!/bin/sh

MODEL=$1
NJOBS=$2
NEVENTS=$3
TAG=$4

# this needs to be modified if model has more than one dataset, i.e. more than one fragment
FRAGMENT=${PWD}/${MODEL}/${MODEL}_${TAG}_fragment.py
if [[ -z "${TAG}" ]]; then
   FRAGMENT=${PWD}/${MODEL}/${MODEL}_fragment.py
fi

if ! [[ -f ${FRAGMENT} ]]; then
    echo "Fragment file does not exist!"
    echo $FRAGMENT
    exit
fi

SCRIPT="${PWD}/../../test/scripts/submitFragmentValidation.py"

if [[ -z "${TAG}" ]]; then
    python ${SCRIPT} --model ${MODEL} --fragment ${FRAGMENT} --proxy "/tmp/x509up_u31582" --njobs ${NJOBS} --nevents ${NEVENTS}
else 
    python ${SCRIPT} --model ${MODEL} --fragment ${FRAGMENT} --tag ${TAG} --proxy "/tmp/x509up_u31582" --njobs ${NJOBS} --nevents ${NEVENTS}
fi
