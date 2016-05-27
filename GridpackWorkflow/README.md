# Gridpack-based SMS production workflow 

## Structure

Folder `production` - will contain the MadGraph cards (or the scripts that generate them), fragments specifying the Pythia SLHA tables + any corresponding scripts - details to be determined once we settle on workflow.

Folder `test` - used to keep track of and share scripts, fragments for central production test workflows. 

## Instructions

These instructions show how to generate gridpacks and determine q-cuts, using chargino-neutralino production as an example signal process.  Copy the bash scripts and cards used here and adapt them for the signal process you are interested in.  

### Card Preparation

Prepare the MadGraph cards for the process of interest. For a scan over several SUSY particle masses, it is easiest to prepare a set of template cards (with a string such as `%MNLSP%` in place of the particle's mass) and then use a script to generate all sets of cards from the templates.  

The folder `production/cards/SMS-TChiSlepSnu/templatecards` contains template cards for chargino-neutralino production. Create cards for each chargino mass using the script provided:
```
cd production/cards/SMS-TChiSlepSnu
source writeallcards_SMS-TChiSlepSnu.sh
```
This script also creates an SLHA file for each particle mass, for use in running Pythia later. When generating events for your own signal process, edit the template SLHA file in the `templatecards` directory for the desired signal. Your SLHA file should specify the masses of the SUSY particle(s) in your model, and they should match the values in the Madgraph customization card. The SLHA can also specify decay modes for the SUSY particle(s), but this is not needed because it does not play a role in the determination of the q-cut.

### Gridpack Generation

Submit gridpack generation jobs to run on Condor. A single job can be submitted using `test/scripts/submitGridpackCondorJob.py`. In the chargino-neutralino production example, submit all jobs at once with:
```
source submitallgridpackjobs_SMS-TChiSlepSnu.sh
```
This script just runs `submitGridpackCondorJob.py` for each value of the chargino mass.  You may need to supply additional arguments (`--genproductions-dir` and `--proxy`) to `submitGridpackCondorJob.py` to ensure that it runs correctly with your local setup. See the python script for more info, and modify `submitallgridpackjobs_SMS-TChiSlepSnu.sh` with the needed changes.

Each gridpack job will store its output on Hadoop, by default in `/hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS`.  

### LHE Event Generation

Now generate about 25000 LHE events from each gridpack, for use in determining the q-cuts and matching efficiencies.  The script `test/scripts/submitLHECondorJob.py` calls Condor to generate LHE events from a single gridpack. To submit jobs for all gridpacks at once, use (for chargino-neutralino production):
```
source submitalllhejobs_SMS-TChiSlepSnu.sh
```
See `submitLHECondorJob.py` for available options, and make any needed changes in `submitalllhejobs_SMS-TChiSlepSnu.sh`. You should supply the location of your proxy using `--proxy`.

Each LHE job will store its output on Hadoop, by default in `/hadoop/cms/store/user/${USER}/mcProduction/LHE`.  

### Q-Cut Determination

To determine the best choice for the q-cut parameter, each set of 25000 LHE events should be showered using Pythia with a variety of q-cuts.  The script `test/scripts/submitPythiaCondorJob.py` will shower a single mass point using a range of different q-cuts.  To run this script on all mass points, use (for chargino-neutralino production, with q-cut running from 80 to 86):
```
source submitallpythiajobs_SMS-TChiSlepSnu.sh 80 86
```
See `submitPythiaCondorJob.py` for available options. As usual, make sure you specify your proxy's location using `--proxy`.  

Note that the script will configure Pythia using the default fragment found in `test/scripts/runPythiaJob.sh`.  Please check this fragment to make sure that it is correct for your signal process.  

Each GEN-SIM job will store its output on Hadoop, by default in `/hadoop/cms/store/user/${USER}/mcProduction/RAWSIM`.  

After all jobs have finished, make differential jet rate plots for each q-cut:
```
source makealldjrplots_SMS-TChiSlepSnu.sh 80 86
```
Note that this will only succeed if you have ROOT set up. This script calls `test/scripts/djr.py` for each signal mass point.  It will produce PDF files with the DJR plots for each q-cut value.  

### Fragment validation

Inside `GridpackWorkflow/production/models` create a directory with the model name. In it, place the fragment named `${MODEL}_fragment.py`. To check if the fragment is ok locally before submitting jobs to condor, from inside the directory for the particular model do, e.g.:
```
./../../../test/scripts/runFragmentValidation.sh 1 $MODEL $PWD 50 local
```
Here, 1 is the random seed and 50 is the number of events. If you have more than one fragment for the model (e.g. there are two datasets) and you want to test all of them. Create a separate fragment for each attaching a tag s.t. the name is `${MODEL}_${TAG}_fragment.py`. Then run:
```
./../../../test/scripts/runFragmentValidation.sh 1 $MODEL $PWD 50 local $TAG
```
Once the fragment is verified locally, go to the `models` directory and submit condor validation like:
```
./submitValidation.sh $MODEL $NJOBS $NEVETNS $TAG
```
If no tag, just omit the last argument. The output will be sent to:`/hadoop/cms/store/$USER/mcProduction/AODSIM/${MODEL}/`.



