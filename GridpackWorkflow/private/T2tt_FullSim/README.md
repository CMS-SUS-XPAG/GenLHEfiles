# FullSim private production

This README describes how to produce private SMS signal samples, from the begin to the end. 

## Gridapack
Scripts are under GridpackWorkflow/test/scripts.
* prepare the Madgraph cards. Examples can be found at: GridpackWorkflow/production/cards
* checkout the genproductions repository
```bash
git clone https://github.com/cms-sw/genproductions
```
* create a proxy (deafult localtion is $HOME/.proxy)
```bash
voms-proxy-init --voms cms --valid 168:00
```
* run the gridpack creation on condor
```bash
python submitGridpackCondorJob.py <proc> --cards <card_dir> --genproduction <gen_dir> --proxy <path_proxy>
```
You should get the gridpack at: /cms/store/user/${USER}/mcProduction/GRIDPACKS/<proc>/<proc>_tarball.tar.gz


## lhe+pLHE+GS+DR+AODSIM+MINIAODSIM
Scripts are under GridpackWorkflow/test/scripts.
* Modify the prodScript.sh specifications (see top of the file), in particular: 
PROCESS: should be the same as <proc> used in the gridpack step, as it is used to retrieve the tarball.
MODEL: name which is written in the LHE event product
TAG: used to tag the dataset. You may want to add, for instance the information of the LSP mass, something like "_mLSP-XXX"
STOP_DECAY: specify stop decay used in the slha (can be generalised for other processes)
 QCUT: self explaining
* Make sure the correct slha is written under the <slha> header below. For instance, you should put the correct mass for the LSP.
* Make sure you have a valid proxy (see Gridpack section before)
* Run the submitMiniAODCondorJob.py script:
```bash
python submitMiniAODCondorJob.py prodScript.sh --gridpack <path_gridpack> --nevents <n_events> --njobs <n_jobs> --out-dir <out_dir> --proxy <path_proxy>
```
You may want to specify also the "--out-dir-eos" option (logical file name) if you want to xrdcp the output MiniAOD to EOS. Make sure the directory already exists, as no explicit check is done (apparently this is not possible at UCSD...)
