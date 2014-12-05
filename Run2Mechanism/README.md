# SUSY Signal production in Run2


## Introduction

During Run1 the mechanism to produce the SUSY signal scans was very time-consuming. 
Most of the scans were done in different steps. In the first step the sparticles
were produced in Madgraph, and not decayed. This allowed us to reuse these undecayed
LHE files for different final states. The decay was done during a second step, using
 Pythia6. This step was usually delegated to the groups requesting the sample. To 
get set up to do this decay took some time, as the available documentation was not 
always easy to follow depending on the system of your local T2. Once the LHE files 
were decayed, they needed to be post-processed. Only then could they be put through
the official production. 

For Run2 we have developed a simpler method. We (i.e. the SUSY group) still need to
provide the undecayed LHE files, but the analysis groups will no longer have to do 
the decay themselves. This will be done as part of the central production from now
onwards. The only thing that will need to be done is to modify the header so that it
includes the mass spectrum and decay chain of your choice. 

In this document we will provide a step-by-step guide to do all the needed steps to 
prepare your request for the official production. The steps that are done in the 
official production will also be detailed so that you can easily produce a few mass
points privately if necessary. 


## Step 1: Produce undecayed LHE files

The first thing you need to decide is what process you want to investigate, in 
particular what sparticles will be produced in the hard collision. Typically these are
gluinos, top squarks, bottom squarks, et cetera. 

Once you know what process you want, you should have a look at the SUSY group area on 
EOS to check whether LHE files for that process have already been produced. If you
are happy with what is already available, then you can immediately proceed to Step 2. 
If your desired process is not there, or you want to look at different masses, then 
you will need to produce the undecayed LHE files yourself by following the 
instructions in this section. 

The relevant scripts for this step are available in this repository, and are called: 

 -  `SUSY_generation.sh`
 -  `run_scan.py`

I will explain the general procedure and the details on these two scripts in the 
following subsections. There is also an example provided that should run on lxbatch
without problems.  

#### General procedure

We will be using the `run_scan.py` script to make (and submit) several job scripts 
according to the mass scan we wish to perform. Each of the job scripts will set up a 
proper environment and will call the `SUSY_generation.sh` script to do the actual 
MadGraph running. They will also create a customization card on the fly that will be 
used to change the number of events, the seed and the mass. 
This means that you only need to provide one parameter card for the full scan. 

#### SUSY_generation.sh

This script is an adaptation of the `gridpack_generation.sh` script that can be found 
on the CMS genproductions github area: 
https://github.com/cms-sw/genproductions/tree/master/bin/MadGraph5_aMCatNLO

It follows the same general structure, and thus inherits the basic setup that you will
need to adhere to. 
For now **only production in LO mode is supported**.

The way to call the script in a standalone way, i.e. not through the `run_scan.py`, is: 
```
./SUSY_generation.sh name ncores
```

`ncores` specifies the number of cores that will be used during the event generation. 
If you do not specify, the default is to use one core. 

`name` is the most important parameter. It specifies the MadGraph cards that should be 
used. The `SUSY_generation.sh` script expects that there is a `cards` folder in the 
current working directory. In this folder it will look for cards with the following
 names:

- `name_proc_card.dat`
- `name_run_card.dat`
- `name_param_card.dat`
- `name_customizecard.dat`

where `name` corresponds to the first argument of the script. The customization card is
optional, and can be omitted if the full process you want to generate is specified in 
the other cards. If you use the example cards from the `cards` folder (see the Examples
section below), and you wish to run `SUSY_generation.sh` by itself, you will have to 
add a `gluino_customizecard.dat`. This card should set the gluino mass to a reasonable 
value, as the value that is in the `gluino_param_card.dat` is too high to be accessible
at the LHC. You can also change other things, such as the number of events, or seed.
```
# Contents of an example gluino_customizecard.dat
set run_card nevents 50000 
set run_card iseed 12345 
set param_card mass 1000021 1200
```
Alternatively, you can change these values directly in the other cards. 

The proc_card defines the process you want to generate. The last line of this card 
specifies the directory name that MadGraph will use to store the diagrams. It is very
important that this name is the same as the `name` argument. If not, the script will
not work, and you will get no events. As we will be running on the batch, and there might
be many diagrams, it is a good idea to suppress the production of jpeg files. 
The last line should thus read as follows
```
output name -nojpeg
```

To summarize, if your cards are named `mytest_proc_card.dat`, `mytest_run_card.dat` and 
`mytest_param_card.dat`, and you want to run with 4 cores, then you should execute:
```
./SUSY_generation.sh mytest 4
```

#### run_scan.py

**Prerequisites**: the script will only work if you have access to python 2.7 and numpy. 
An easy way to achieve this is to set up a **CMSSW7X** area. 

This is the script that will take care of the job submission. 
There are a number of options related to the actual submission, and a number related to
the masses of the particle you want to scan. 
For this first version only the very basic setup is supported, namely pair-production of
sparticles, without subsequent decays. If you want to do something which requires 
changing the mass of more than one particle, you cannot do it in one go. You will have
to run several times with the appropriate param_card.

The list of options: 

- `-h, --help`: Display the help message. This includes all these options.
- `--name`: Process name (default='gluino'). Cards should be appropriately named, 
            e.g. gluino_run_card.dat 
- `--pdg`: PDG id of the particle whose mass you want to loop over (default=1000021). 
           For most cases this will be the particle that is pair-produced. This should 
	   thus be consistent with the process definition in the proc_card. 
- `--mass`: White space separated list of masses to produce events for (default=1000) 
- `--massrange`: Mass range to produce events for. Format: MIN MAX STEP (no default). 
                 The value in MAX is not included in the range.
- `-n, --nevents`: Number of events to produce per run (default=10000)
- `-nruns`: Number of runs, useful if you want to produce a lot of events (default=1) 
- `-ncores`: Number of cores to use for event generation (default=1)
- `-protocol`: Submission protocol: bsub or qsub (default='bsub')
- `-q, --queue`: Queue to submit to (default='1nd')
- `--nosubmit`: Flag to turn of submission, job scripts are still created. Can be useful
  		if you want to run locally.  

Each time you execute the script, a log file will be created. This log file includes the 
full setup which was used. The name of the log file includes the current time in order 
to make it easier to track things.

The `run_scan.py` script will create several directories in the working directory. 

- `scripts`: To hold the job scripts that will be submitted to the batch queue. This 
             directory is NOT cleaned by default by the script. 
- `log`: To hold the error and log files that are returned by the batch system. This 
         directory is NOT cleaned by default by the script.
- `lhe`: To hold the output lhe files that are produced by the `SUSY_generation.sh` script
- `patches`: This directory will contain two patches for the MG5_aMC@NLO distribution. 
             The first time you run the script these patches will be downloaded from
             https://github.com/cms-sw/genproductions/tree/master/bin/MadGraph5_aMCatNLO

By default the script will submit to the 1nd queue. Depending on how many events you want
to run per job, you might need to change this. It is probably fine up to about 100k events
for up to two extra partons, but this has not been explicitely tested. 

It is also possible to speed up the event generation by running on more than 1 core. This 
can be used for running on lxplus and for running locally. This option is not supported
for batch systems that use `qsub` for submission. 

The job script will clean up after itself, meaning that it will copy over the output file, 
and then delete everything it created. If you are running locally and want to keep absolutely
everything, then you have to comment out the line in the script that does this removal. 
This line can be found at the end of the `makejob(...)` function. 


#### Examples

I have provided some example MadGraph cards in the `cards` directory. 

- `gluino_proc_card.dat`: This process card specifies gluino pair production with 
                          0 or 1 extra partons. You can uncomment the appropriate line
                          in the card to also include 2 extra partons. For this example
                          I would not recommend this, however, as it will increase the
                          running time substantially.
                          I have also excluded (with the `$` operator) any diagrams 
			  containing any other sparticle. They will not contribute
                          anyways as they have been chosen to be decoupled. 
 			  Also note that the name for the output directory had to be 
			  consistent with the naming for the cards. In this case it is 
			  put to "gluino". 
- `gluino_param_card.dat`: This parameter card should be useable for most simplified
  			   models. It puts all masses to a very high scale. The relevant
 			   masses will be set during run time as previously explained.
- `gluino_run_card.dat`: Basic run card for LO production. It includes the weights for 
  			 various scale and PDF choices. MLM matching is turned on with
			 `xqcut = 30`. 

To run the very basic example on lxplus, you can simply do: 
```
python run_scan.py
```
This will generate 10k events of gluino pair-production with a gluino mass of 1 TeV. 
The job will be submitted in the 1nd queue, and will use one processor core. Note that
we did not have to specify `--name` here as the default is `gluino` and the cards in the
cards folder are named `gluino_..._card.dat`. 

Most likely, you will want to generate events for different masses as well. As mentioned 
above, there are two arguments that you can use for this: 
```
# Specify one mass point, for example 1400 GeV
python run_scan.py --mass 1400

# Specify a list of mass points
# Note that you do not need to provide integers
python run_scan.py --mass 600 750 1200 1450.5

# Construct a mass range with fixed step
python run_scan.py --massrange 1000 1500 100
```

If you want to generate events for stop quarks for example, instead of gluinos, this is 
what you need to do: 

- Create a new set of cards
    - the process card should now specify something like `p p > t1 t1~`
    - the run card can probably stay the same
    - the param card can probably stay the same
- Give the **cards a coherent name**, e.g. `stop_proc_card.dat`, `stop_run_card.dat`, 
  `stop_param_card.dat`
- Make sure that the last line in the proc_card is consistent with your naming choice, 
  e.g. `output stop -nojpeg`
- Execute the script and change the relevant parameters. 
  ```
  python run_scan.py --name stop --pdg 1000006 --massrange 500 800 25 -n 50000
  ```
- Wait for your LHE files to be delivered


#### Features to be added in the future

- submission with condor (volunteer with condor experience needed)
- setting masses for multiple particles (needed for neutralino/chargino production)
- support for running in NLO mode. This will require extensive validation.



## Step 2: Process undecayed LHE files

This step assumes that you have access to a set of undecayed LHE files, and that you
have decided what decay chain you are interested in. This means that you need to know
the branching fractions and the masses of all particles in the decay chain. This 
information will be put in the header of the undecayed LHE files. A script is provided
in this repository to do exactly that. You can run the following command to get some
information on how to use the script.  
```
python updateHeader.py --help
```

**TO DO: Provide the updateHeader.py script**

## Step 4a: Injection into official production

Once you have processed the undecayed LHE files, and verified that things look ok, you
are ready to submit your request to the official production. To do this you should 
contact the SUSY MC Generator contacts, and coordinate with them to get your files
uploaded to EOS. All LHE files that are used as input in an official request need to 
be stored under /store/lhe, but only the Generator Contacts have write permissions. 

The Generator Contacts will then inject the request in the McM database 
(https://cms-pdmv.cern.ch/mcm/), and will report on it during the weekly Monte Carlo
Coordination Meeting. This is where the priority of the request will be discussed. 

The last input that should be provided to the gencontacts, is the qcut values that 
should be used with your request. This value needs to be put in the Generator Fragment, 
such that Pythia8 will know how to properly match the matrix element and the parton 
shower. Please note that this is only needed if you have produced several multiplicities
of additional partons in the Madgraph step. The default for the SUSY group is to produce
up to 2 additional partons, so most requests will need to have a corresponding qcut. 

The qcut depends on the hard process, and on the mass of the produced particles. If 
someone already determined the qcut for the hard process (e.g. gluino pair production), 
and mass range you are interested in, you can simply reuse that value. 
An up-to-date list of qcut values can be found on this twiki page: **put twiki here**
If the qcut has not been determined yet, you should do it yourself by following the 
instructions in the section "Determining the QCUT". 


## Step 4b: Private production

You can of course also produce a few samples privately, rather than go through the full
production chain. In this case there is no need to upload files to EOS. You do need an
appropriate qcut value however. Once you have this number, you can update the generator
fragment and start the private production. Depending on the scope of the study you wish
to perform, you will need to run different steps. For all options you will need the 
appropriate genfragment. The one to be used for samples produced using the procedure 
explained here, can be found on the genproductions github page: 

**TO DO: add link to genfragment**

In this fragment you should update the value of `JetMatching:qCut`, and perhaps the 
value of `JetMatching:nJetMax`. The `nJetMax` should be set to the largest number of 
extra partons that are present in the lhe file. The SUSY default for this is `2`.  

#### GEN only

#### FASTSIM


#### FullSim



## Determining the QCUT

To determine a good qcut for a given process, you need to scan different values and pick
the one that gives you smooth differential jet rate (DJR) plots. 

To obtain these plots we provide a script: **Name of DJR plot**
The input to this script is an EDM file containing the output of the GEN step. See the 
instructions for the "GEN only" step in the "Private production" section. 