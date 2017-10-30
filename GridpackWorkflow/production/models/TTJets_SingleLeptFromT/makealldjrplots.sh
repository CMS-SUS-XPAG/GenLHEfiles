#!/bin/sh
QMIN=60
QMAX=80
SCRIPT="../../../test/scripts/djr.py"
MODEL="TTJets_SingleLeptFromT"
NJETMAX=3

python ${SCRIPT} ${MODEL} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL} --qcut-range ${QMIN} ${QMAX} --nJetMax ${NJETMAX}
