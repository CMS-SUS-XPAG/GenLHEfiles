SCRIPT="../../../test/scripts/submitLHEPythiaCondorJob.py"
MODEL="RPV_2t6j_mStop-500"
NJETMAX=2
QMIN=56
QMAX=70
FRAGMENT=fragment_LHEGS.py
PROXY=$X509_USER_PROXY

python $SCRIPT $MODEL --nevents 5000 --njobs 15 --fragment ${FRAGMENT} --qcut-range $QMIN $QMAX --qcut-step 2 --nJetMax $NJETMAX --proxy $PROXY --executable runLHEPythiaJob.sh
