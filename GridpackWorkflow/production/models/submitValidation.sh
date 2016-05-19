#!/bin/sh

MODEL=$1
# this needs to be modified if model has more than one dataset, i.e. more than one fragment
FRAGMENT=${MODEL}/fragment.py
SCRIPT="../../test/scripts/submitFragmentValidation.py"

python ${SCRIPT} --dataset ${MODEL} --fragment ${FRAGMENT} --proxy ${vomsdir} --njobs 100 --nevents 1000

