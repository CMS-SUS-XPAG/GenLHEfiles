# SUSY Signal production in Run2

## Table of contents

* [Introduction](#introduction)
* [Step 1: Produce undecayed LHE files](#step-1-produce-undecayed-lhe-files)
   * [General procedure](#general-procedure)
   * [SUSY_generation.sh](#susy_generation.sh)
   * [run_scan.py](#run_scan.py)
   * [Examples](#examples)
   * [Features to be added in the future](#features-to-be-added-in-the-future)
* [Step 2: Process undecayed LHE files](#step-2-process-undecayed-lhe-files)
   * [Constructing the config file](#constructing-the-config-file)
   * [Examples](#examples-2)
* [Step 4a: Injection into official production](#step-4a-injection-into-official-production)
* [Step 3: Validation](#step-3-validation)
* [Step 4b: Private production](#step-4b-private-production)
   * [GEN only](#gen-only)
   * [FASTSIM](#fastsim)
   * [FullSim](#fullsim)
* [Determining the QCUT](#determining-the-qcut)



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
in this repository to do exactly that. 

There are actually two relevant scripts. The first one, `update_header.py` is the one
you will need to execute. 
You can print the help message with the following:
```
python update_header.py --help
```
As you can see from the output, the script takes a config file as input. The structure
of this config file is explained below. There is also one optional flag `--stableLSP`
which should be used if the input LHE files do not contain a line like
```
DECAY  1000022  0.0
```
in the slha block of the header, and you have chosen one of the predefined decay
scenarios (see info below). The help message contains the currently included decay
options.  

Once you have a valid config file, you can simply execute the script 
```
python update_header.py myconfig.cfg
```
and it will create a directory and put all the processed lhe files there. 
One thing to note is that the input lhe files do not need to be unzipped. The script
can handle the gzipped files that result from the first step. 
The output files will be unzipped however. 

#### Constructing the config file

The config file that is needed as input to the `update_header.py` script, will be read
by the standard python ConfigParser. It should have this structure: 
```
[Global]
name = gluino 
nevents = -1 
inputdir = lhe 
outputdir = lhe_processed 
model = 

[SLHA]
slha = 
mass = mass_dict.py 
decay = T1tttt 
decaystring = 
```

To make it easier for you, I have provided a script that will create the config file
in the correct format. This script is called `create_update_header_config.py`. 
There are no command line options for this script. You will have to open up a text 
editor and fill out the appropriate entries in the `options` dictionary at the bottom
of the file. The table below contains all the options that will be used by the 
`update_header.py` script. Any other option will be ignored. 

| Option       | Info
| :----------- | :-----------------------------
| `name`       | This corresponds to the name you passed to the `run_scan.py` script. It corresponds to the beginning of the name of the input LHE files. The assumed naming convention for the undecayed files is: ```<name><mother mass><other stuff>undecayed.lhe(.gz)```. The processed files will have the names ``` <model><mother mass><other stuff>decayed<mass info>```. The mass info will include the pdg id and mass of all particles for which you made a change in the slha.  
| `nevents`    | Number of events you want to process for each input file. Put any negative value to process all events.
| `inputdir`   | Location of the LHE files you want to process.
| `outputdir`  | Location where you want the processed LHE files to be stored. This directory will be created if it does not exist yet. 
| `model`      | New name to replace the original `name` that is part of the LHE filename (gluino in the default example from Part 1). The output files will thus start with "model". If you pass the empty string as option, the name will become 'custom' or equal to `decay` if that option was set.
| `mass`       | The name of the python file that contains the `mass_dict` dictionary. More info on this below. In short it specifies how to set the masses of the sparticles appearing in the decay chain. 
| `slha`       | Full path of the SLHA file you want to use. Leave this option blank if you are happy with the SLHA file present in the undecayed LHE file and you only want to add decay branching ratios for particles that have no branching ratios specified. 
| `decay`      | Name of one of the predefined options for the decay chain. Currently you can choose from T1tttt, T1bbbb, T1qqqq, T2qq, T2bb, T2tt, T2tt_3BD and T2cc. If none of these suit you, you can leave this option blank. 
| `decaystring`| If the decay you want is not provided in the predefined options, you can pass the full decay specification as a string. 

To avoid having to come back to this table all the time, there are comments in the file to remind you what each option means. 

An example of how to use the `decaystring` option would be 
```python
"decaystring" : "\"DECAY 1000021 1.0\"\n  \"   0.5  2  -6  1000006\"\n  \"   0.5  2  6  -1000006\"\n\"DECAY 1000006 0.5\"\n  \"  1.0  2  6  1000022\"\n"
```
This will put the following in the config file:
```
decaystring = "DECAY 1000021 1.0"
          "   0.5  2  -6  1000006"
          "   0.5  2  6  -1000006"
        "DECAY 1000006 0.5"
          "  1.0  2  6  1000022"
```
The important thing to note here is that we are using a multiline option, as the decay block will have to multiline as well. For the ConfigParser to accurately parse this, the second and following lines need to start by non-zero whitespace. That is why in the above command I have added some whitespace after each `\n`. The ConfigParser will then strip all this whitespace. This is a problem for these decay blocks, as the lines that contains the branching fractions need to be indented. In order to solve this problem, you need to add quotes. This is why in the above command you can see these escaped quotes. 


The last thing that needs to be explained before coming to the examples is the afore-mentioned 
mass dictionary. This dictionary will encapsulate the grid of parameter points you want
to generate.  
The keys of the dictionary are the masses of the mother particles, i.e. the
particles that were produced with MadGraph. It is assumed that the undecayed files have
a name like `<name><mother mass><other stuff>undecayed.lhe(.gz)`. The notation for the 
mother mass in this name should be used in the mass dictionary as well.  
The value corresponding to each key in the dictionary is a list of all the configurations
you wish to produce for that given mother mass (or key). 
Each configuration is encoded in a dictionary with the pdg id of the particles as keys, 
and the masses as values.  
In code form this becomes: 
```python
# Configuration dictionary for three different configurations
conf1 = {"1000006" : 500, 
         "1000022" : 300}
conf2 = {"1000006" : 600, 
         "1000022" : 200}
conf3 = {"1000006" : 1300, 
         "1000022" : 600}

# Required mass dictionary. 
# It is assumedthat the input files have mother masses of 
# "1200.0" and "1500.0"
mass_dict = {"1200.0" : [conf1, conf2],
             "1500.0" : [conf1, conf2, conf3]}
```
This mass dictionary should be stored in a python file (.py). **It is very important
that the dictionary is stored in a variable called `mass_dict`**, as in the example 
above. You can have code in the file that generates this mass dictionary. The main 
thing is to have a variable with the correct name. 
The file `create_update_header_config.py` contains several functions to create this
mass dictionary for you. Most of the standard scenarios for simplified model scans
are included. For example, for the case where you only need to update the mass of the LSP,
and generate LSP masses from 0 till the mass of the mother particle (with a certain step 
size), you can use the function `makeMassDict_standard_SMS`. 
Each provided function comes with some comments, so I encourage you to have a look at them
to decide whether they are useful for your case. 


#### Examples

Let's continue with the gluino example from the first step and assume that we have
produced a set of undecayed LHE files, and stored them in a folder called `lhe`
```
> ls lhe/
gluino1000.0_0_undecayed.lhe.gz
gluino1200.0_0_undecayed.lhe.gz
gluino1400.0_0_undecayed.lhe.gz
gluino800.0_0_undecayed.lhe.gz
```

For this example we want to generate the T1tttt SMS topology, where the gluinos decay
to t+tbar+LSP. Apart from the gluino mass, the only free mass parameter is the LSP mass. 
Let's consider that we want to end up with events for all LSP masses up to the gluino 
mass, in steps of 200 GeV. The required mass dictionary to achieve this can be easily
generated using the `makeMassDict_standard_SMS()` function in the `update_create_header_config.py`
script. 
```python
# Execute this to create a file called mass_dict.py containing the required mass dictionary
# makeMassDict_standard_SMS(mother_masses, LSP_step, fname="mass_dict.py")
makeMassDict_standard_SMS(range(800,1405,200),200)
```
The resulting python file will contain the following line: 
```python
mass_dict = { "%.1f"%(x) : ([ {'1000022': mass} for mass in range(0,x,200) ]) for x in [800, 1000, 1200, 1400] }
```
This constructs the full mass dictionary. If you find the above hard to parse, this is how 
this would look like if you write it out in full: 
```python
mass_dict = {'1400.0': [{'1000022': 0},
                        {'1000022': 200}, 
                        {'1000022': 400}, 
                        {'1000022': 600}, 
                        {'1000022': 800}, 
                        {'1000022': 1000}, 
                        {'1000022': 1200}], 
             '1200.0': [{'1000022': 0}, 
                        {'1000022': 200}, 
                        {'1000022': 400}, 
                        {'1000022': 600}, 
                        {'1000022': 800}, 
                        {'1000022': 1000}], 
             '1000.0': [{'1000022': 0}, 
                        {'1000022': 200}, 
                        {'1000022': 400}, 
                        {'1000022': 600}, 
                        {'1000022': 800}], 
             '800.0': [{'1000022': 0},
                       {'1000022': 200}, 
                       {'1000022': 400}, 
                       {'1000022': 600}]}
```

To create the config file, you should update the `options` dictionary at the end of the 
`create_update_header_config.py` script, give a name for the config file, and then 
actually create the config: 
```python
## To update in the create_update_header_config.py script: 
options = {"name": "gluino", 
           "nevents": "-1",
           "inputdir": "lhe", 
           "outputdir": "lhe_processed", 
           "model": "",
           "slha": "",
           "mass": "mass_dict.py", 
           "decay": "T1tttt",
           "decaystring": ""
           }

# Name for the config file
configname = "myconfig.cfg"

# Actually create the config file to be used by update_header.py
makeConfig(options, configname)
```
Then you should just execute the updated script.
```
python create_update_header_config.py
```

The last step is then to pass your newly created config file to the `update_header.py` 
script to actually create the processed LHE files.
```
python update_header.py myconfig.cfg
```
Now you have a set of LHE files that are in principle ready to be put through the 
official production. 

## Step 3: Validation

You should make sure that your processed LHE files are valid. The easiest thing to 
do is to simply look at the LHE file and check whether the needed masses were updated
and whether the DECAY block was properly injected. 

It is also a good idea to follow the instructions for the [private production](#step-4b:-private-production),
in particular those for the GEN step, to check that your LHE files will not cause
any issues during the further processing steps. 


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
