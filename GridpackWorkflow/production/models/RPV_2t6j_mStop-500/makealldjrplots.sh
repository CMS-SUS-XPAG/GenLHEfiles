#!/bin/sh
QMIN=56
QMAX=70
SCRIPT="../../../test/scripts/djr.py"
MODEL="RPV_2t6j_mStop-500"
NJETMAX=2

python ${SCRIPT} ${MODEL} /hadoop/cms/store/user/${USER}/mcProduction/RAWSIM/${MODEL} --qcut-range ${QMIN} ${QMAX} --nJetMax ${NJETMAX}
