SCRIPT="../../../test/scripts/submitLHEPythiaCondorJob.py"
MODEL="TTJets_SingleLeptFromT"
NJETMAX=3
QMIN=60
QMAX=80
FRAGMENT=fragment_LHEGS.py
PROXY="/tmp/x509up_u31606"

python $SCRIPT $MODEL --nevents 5000 --njobs 5 --fragment ${FRAGMENT} --qcut-range $QMIN $QMAX --qcut-step 2 --nJetMax $NJETMAX --proxy $PROXY --executable runLHEPythiaJob.sh
