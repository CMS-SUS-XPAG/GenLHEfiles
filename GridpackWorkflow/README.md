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

### Gridpack Generation

Submit gridpack generation jobs to run on Condor using `test/scripts/submitGridpackCondorJob.py`. In the chargino-neutralino production example, submit all jobs at once with:
```
source submitallgridpackjobs_SMS-TChiSlepSnu.sh
```
This script just runs `submitGridpackCondorJob.py` for each value of the chargino mass.  You may need to supply additional arguments (`--genproductions-dir` and `--proxy`) to `submitGridpackCondorJob.py` to ensure that it runs correctly with your local setup. See the python script for more info.

Each gridpack job will store its output on Hadoop, by default in `/hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS`.  

### LHE Event Generation

Now generate about 25000 LHE events from each gridpack, for use in determining the q-cuts and matching efficiencies.  The script `test/scripts/submitLHECondorJob.py` calls Condor to generate LHE events from a single gridpack. To submit jobs for all gridpacks at once, use (for chargino-neutralino production):
```
source submitalllhejobs_SMS-TChiSlepSnu.sh
```
See `submitLHECondorJob.py` for available options. You should supply the location of your proxy using `--proxy`.

Each LHE job will store its output on Hadoop, by default in `/hadoop/cms/store/user/${USER}/mcProduction/LHE`.  

### Q-cut Determination

To determine the best choice for the q-cut parameter, each set of 25000 LHE events should be showered using Pythia with a variety of q-cuts.  Before doing this, you need an SLHA file for each signal mass point you will study.  Do this using a template, as we did above with the MadGraph cards. For the chargino-neutralino example, use:
```
source writeslha_SMS-TChiSlepSnu.sh
```
This will place an SLHA file in the `jobs` directory for each signal mass.  Your SLHA file should specify the masses of the SUSY particle(s) in your model, and they should match the values used in gridpack generation. The SLHA can also specify decay modes for the SUSY particle(s), but this is not needed because it does not play a role in the determination of the q-cut.  

The script `test/scripts/submitPythiaCondorJob.py` will shower a single mass point using a range of different q-cuts.  To run this script on all mass points, use (for chargino-neutralino production, with q-cut running from 80 to 86):
```
source submitallpythiajobs_SMS-TChiSlepSnu.sh 80 86
```
See `submitPythiaCondorJob.py` for available options. As usual, make sure you specify your proxy's location using `--proxy`.  

Note that the script will configure Pythia using the default fragment found in `test/scripts/runPythiaJob.sh`.  Please check this fragment to make sure that it is correct for your signal process.  

Each GEN-SIM job will store its output on Hadoop, by default in `/hadoop/cms/store/user/${USER}/mcProduction/RAWSIM`.  

After all jobs have finished, make differential jet rate plots for each q-cut:
```
source makealldjrplots_SMS-TChiSlepSnu.sh
```
This script calls `test/scripts/djr.py` for each signal mass point.  It will produce PDF files with the DJR plots for each q-cut value.  
