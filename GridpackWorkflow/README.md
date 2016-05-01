# Gridpack-based SMS production workflow 

## Structure

Folder `production` - will contain the MadGraph cards (or the scripts that generate them), fragments specifying the Pythia SLHA tables + any corresponding scripts - details to be determined once we settle on workflow.

Folder `test` - used to keep track of and share scripts, fragments for central production test workflows. 

## Instructions

### Gridpack Generation

Prepare the MadGraph cards for the process of interest. For a scan over several SUSY particle masses, it is easiest to prepare a set of template cards (with a string such as `%MNLSP%` in place of the particle's mass) and then use a script to generate all sets of cards from the templates.  

Ex: the folder `production/cards/SMS-TChiSlepSnu/templatecards` contains template cards for chargino-neutralino production. Create cards for each chargino mass using the script provided:
```
cd GridpackWorkflow/production/cards/SMS-TChiSlepSnu
source writeallcards_SMS-TChiSlepSnu.sh
```

Submit gridpack generation jobs to run on Condor using `test/scripts/submitGridpackCondorJob.py`. In the chargino-neutralino production example, submit all jobs at once with:
```
source submitallgridpackjobs_SMS-TChiSlepSnu.sh
```
You may need to supply additional arguments (`--genproductions-dir` and `--proxy`) to `submitGridpackCondorJob.py` to ensure that it runs correctly with your local setup.  
