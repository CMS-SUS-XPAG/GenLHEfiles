Central repository for generation of SUSY SMS events 
Startin from undecayed (gluino-gluino or stop-stop production) LHE files from MadGraph
to specific SMS decay chains 

Supported models are
T1tttt, T1bbbb, T1ttbb, T1tbbb, T1tttb, T1ttcc, T1t1t,
T2tt, T2tb, T2tb,
T5tttt, T5gg, T5wg
TChiwg, TChiNg

# Recipe for Fall17 branch to create Fall17 signal requests

Please be careful to insert your username and proxy id accordingly.

### make a dedicated directory for signal production

```
mkdir SUSYsignalProduction
cd SUSYsignalProduction
```

### Get the genproductions with the ucsd patch

```
git clone https://github.com/cms-sw/genproductions.git
cd genproductions
git remote add forUCSD https://github.com/danbarto/genproductions.git
git fetch forUCSD
git cherry-pick 541d4bc0c5a5f29105ca941cc7f7f98ae7a75c39
cd ..
```

### Get this repository
```
git clone https://github.com/danbarto/GenLHEfiles.git
cd GenLHEfiles
git fetch origin
git checkout -b Fall17
```

## Example for gridpack production and request

### get your proxy:
```
voms-proxy-init -voms cms -valid 100:00 -out /tmp/x509up_uYOURUSER; export X509_USER_PROXY=/tmp/x509up_uYOURUSER
```
### Produce a gridpack, e.g. (please check your path and specify proxy if needed!)
```
cd GridpackWorkflow/production/SMS-StopStop/
source writeallcards_SMS-StopStop.sh
python ../../test/scripts/submitGridpackCondorJob.py SMS-StopStop_mStop-650 --cards-dir jobs/SMS-StopStop_mStop-650 --genproductions-dir /home/users/YOURUSER/SUSYsignalProduction/genproductions/
```
If you submit from node 10 of UCSD you can check the status of the gridpack production with the command
```
condor_tail JOBID
```
At the moment, the gridpack will be transferred to the directory from which the job was submitted.
I'll update that so that the gridpack gets transfered to hadoop asap.

### I made an example request for fullsim with the new tune which seems to work:
https://cms-pdmv.cern.ch/mcm/requests?dataset_name=SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8&page=0&shown=127
