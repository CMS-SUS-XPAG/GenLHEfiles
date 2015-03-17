# SUSY Signal production in Run2

## Table of contents

* [Introduction](#introduction)
* [Getting started](#getting-started)
* [Step 1: Produce undecayed LHE files](#step-1-produce-undecayed-lhe-files)
   * [General procedure](#general-procedure)
   * [SUSY_generation.sh](#susy_generationsh)
   * [run_scan.py](#run_scanpy)
   * [Examples](#examples)
   * [Features to be added in the future](#features-to-be-added-in-the-future)
* [Step 2: Process undecayed LHE files](#step-2-process-undecayed-lhe-files)
   * [Constructing the config file](#constructing-the-config-file)
   * [Examples](#examples-1)
* [Step 3: Validation](#step-3-validation)
* [Step 4a: Injection into official production](#step-4a-injection-into-official-production)
* [Step 4b: Private production](#step-4b-private-production)
   * [Prepare a CMSSW area](#prepare-a-cmssw-area)
   * [GEN only](#gen-only)
   * [FASTSIM](#fastsim)
   * [FullSim](#fullsim)
   * [Phys14 setup](#phys14-setup)
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

For Run2 we have developed a simpler, and faster, method. We (i.e. the SUSY group) still need to
provide the undecayed LHE files, but the analysis groups will no longer have to do 
the decay themselves. This will be done as part of the central production from now
onwards. The only thing that will need to be done is to modify the header so that it
includes the mass spectrum and decay chain of your choice. In order to retrieve the
mass point information a model tag also needs to be added to the event. 

In this document we will provide a step-by-step guide to do all the needed steps to 
prepare your request for the official production. The steps that are done in the 
official production (once available)  will also be detailed so that you can easily produce a few mass
points privately if necessary. 


## Getting started

To use some the scripts available here, you need access to the CMSSW software. For most
people this means that you will be running on either lxplus, cmslpc, or on your local T2. 
**These scripts have only been tested on lxplus so far.** You might need to make changes 
here and there to get it to run on the local T2 (e.g. for batch submission). 

Most of the python scripts should be run using python 2.7. The easiest way to set 
this up on lxplus, is to do `cmsenv` in a recent CMSSW area.
You should also clone this git repository to get access to the necessary scripts.
The instructions below include all of these steps, as well as the steps
to install MadGraph and the associated programs.

```
cmsrel CMSSW_7_1_12
cd CMSSW_7_1_12
cmsenv
mkdir prod
cd prod
git clone git@github.com:kpedro88/GenLHEfiles.git
cd GenLHEfiles/Run2Mechanism
scripts/installGenerators.sh
source scripts/setupGenEnv.(c)sh
```

The code from this repository is put in $CMSSW_BASE/prod instead of $CMSSW_BASE/src
to make it easier to checkout and build CMSSW packages in $CMSSW_BASE/src if desired.

Note: if you want to run MadGraph on multiple cores, you need to specify the number of cores
when running the install script, like this:
```
scripts/installGenerators.sh 5
```

As a general user, you will not need to contribute to the repository. You will only need to
use the scripts provided here. Therefore, cloning the repository, which should work 
with one of the above commands, is all you need to know about git.
If you are unfamiliar with git(hub), and want to find more information on the use of 
git and github, you can have a look at the CMSSW github 
[FAQ](http://cms-sw.github.io/faq.html), the [github help pages](https://help.github.com/) 
or the [git book](http://git-scm.com/book/en/v2). 


## Step 1: Produce undecayed LHE files

The first thing you need to decide is what process you want to investigate, in 
particular what sparticles will be produced in the hard collision. Typically these are
gluinos, top squarks, bottom squarks, et cetera. 

Once you know what process you want, you should have a look at the SUSY group area on 
EOS (/store/group/phys_susy)
to check whether LHE files for that process have already been produced. If you
are happy with what is already available, then you can immediately proceed to Step 2. 
If your desired process is not there, or you want to look at different masses, then 
you will need to produce the undecayed LHE files yourself by following the 
instructions in this section. 

The relevant scripts for this step are available in this repository, and are called: 

 -  [scripts/SUSY_generation.sh](./scripts/SUSY_generation.sh)
 -  [run_scan.py](./run_scan.py)

I will explain the general procedure and the details on these two scripts in the 
following subsections. There is also an example provided that should run on lxbatch
without problems.  

#### General procedure

We will be using the [run_scan.py](./run_scan.py) script to make (and submit) several job scripts 
according to the mass scan we wish to perform. Each of the job scripts will set up a 
proper environment and will call the [SUSY_generation.sh](./SUSY_generation.sh) script to do the actual 
Madgraph running. They will also create a customization card on the fly that will be 
used to change the number of events, the seed and the mass(es). 
This means that you only need to provide one parameter card for the full scan. 

#### SUSY_generation.sh

**Prerequisites**: This script will attempt to set up a CMSSW area. You will thus need
access to the CMS software. You also need access to the LHAPDF6 libraries. 
On lxplus this script will work out of the box. This is not guaranteed on your local
cluster. 

For now **only production in LO mode is supported**.

The way to call the script in a standalone way, i.e. not through the `run_scan.py`, is: 
```
./SUSY_generation.sh cards lhe name custom
```

`cards` and `lhe` are the directories for the input cards and the output lhe files, respectively.

`name` is the most important parameter. It specifies the MadGraph cards that should be 
used. The [SUSY_generation.sh](./SUSY_generation.sh) script expects that there is a `cards` folder in the 
current working directory. In this folder it will look for cards with the following
 names:

- `name_proc_card.dat`
- `name_run_card.dat`
- `name_param_card.dat`
- `custom_customizecards.dat`

where `name` corresponds to the first argument of the script. The customization card is
optional, and can be omitted if the full process you want to generate is specified in 
the other cards. If you omit the customization card, give `custom` the same value as `name`.
If you use the example cards from the `cards` folder (see the [Examples](#examples)
section below), and you wish to run [SUSY_generation.sh](./SUSY_generation.sh) by itself, you will have to 
add a `gluino_customizecards.dat`. This card should set the gluino mass to a reasonable 
value, as the value that is in the `gluino_param_card.dat` is too high to be accessible
at the LHC. You can also change other things, such as the number of events, or seed.
```
# Contents of an example gluino_customizecards.dat
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

The included run_card has reasonable values for most processes. If you are not sure
whether you need to change some parameters, please contact the SUSY MC contacts and the
MC/Trigger/XPAG conveners. 

To summarize, if your cards are named `mytest_proc_card.dat`, `mytest_run_card.dat` and 
`mytest_param_card.dat`, then you should execute:
```
./SUSY_generation.sh cards lhe mytest mytest
```

#### run_scan.py

**Prerequisites**: the script will only work if you have access to python 2.7 and numpy. 
An easy way to achieve this is to set up a **CMSSW7X** area, as mentioned in 
[Getting Started](#getting-started). 

This is the script that will take care of the job submission. 
There are a number of options related to the actual submission, and a number related to
the masses of the particle(s) you want to scan. 
There are three different ways to pass the information on the masses to scan (`--mass`,
`--massrange`, or `--massdict`). 
If you are producing undecayed files and only need to change the mass of one particle (e.g. 
the gluino), you can use all three options. 
If you, on the otherhand, need to change the mass of multiple particles (e.g. for 
chargino-neutralino production), then you can only use the `--massdict` option.

The full list of options: 

- `-h, --help`: Display the help message. This includes all these options.
- `--name`: Process name (default='gluino'). Cards should be appropriately named, 
            e.g. gluino_run_card.dat 
- `--pdg`: PDG id of the particle whose mass you want to loop over (default=1000021). 
           For most cases this will be the particle that is pair-produced. This should 
	   thus be consistent with the process definition in the proc_card. This option
           is not relevant if you are using the --massdict option.
- `--mass`: White space separated list of masses to produce events for (default=1000) 
- `--massrange`: Mass range to produce events for. Format: MIN MAX STEP (no default). 
                 The value in MAX is not included in the range.
- `--massdict`: Name of a python file that contains the mass and pdg information. 
                The information should be stored in a list called `masses`. Each element
                of the list will be converted into a job, and should be in the form of a 
                dictionary {"pdgid1":mass1, "pdgid2":mass2, ...}
- `-n, --nevents`: Number of events to produce per run (default=10000)
- `-nruns`: Number of runs, useful if you want to produce a lot of events (default=1). 
            All jobs will be replicated nruns times. 
- `-ncores`: Number of cores to use for event generation (default=1)
- `-protocol`: Submission protocol: bsub or qsub or condor (default='bsub')
- `-q, --queue`: Queue to submit to (default='1nd')
- `--nosubmit`: Flag to turn of submission, job scripts are still created. Can be useful
  		if you want to run locally. 
-  `-o, --output`: Output directory for LHE file (default='lhe')

Each time you execute the script, a log file will be created. This log file includes the 
full setup which was used. The name of the log file includes the current time in order 
to make it easier to track things.

The [run_scan.py](./run_scan.py) script will create several directories in the working directory. 

- `scripts`: To hold the job scripts that will be submitted to the batch queue. This 
             directory is NOT cleaned by default by the script. 
- `logs`: To hold the error and log files that are returned by the batch system. This 
         directory is NOT cleaned by default by the script.
- `lhe`: To hold the output lhe files that are produced by the [SUSY_generation.sh](./SUSY_generation.sh) script

By default the script will submit to the 1nd queue. Depending on how many events you want
to run per job, you might need to change this. It is probably fine up to about 100k events
for up to two extra partons, but this has not been explicitely tested. 

It is also possible to speed up the event generation by running on more than 1 core. This 
can be used for running on lxbatch and for running locally (e.g. on lxplus). This option 
is not supported for batch systems that use `qsub` for submission. It is possible in principle
when using condor, but this is not supported by the script yet.


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
above, there are three arguments that you can use for this. The first two are the easiest
to use, and will be sufficient for most purposes:
```
# Specify one mass point, for example 1400 GeV
python run_scan.py --mass 1400

# Specify a list of mass points
# Note that you do not need to provide integers
python run_scan.py --mass 600 750 1200 1450.5

# Construct a mass range with fixed step
python run_scan.py --massrange 1000 1500 100
```
Using the third option requires an intermediate step, the creation of the python file
that hold the mass and pdgid information. 
You can put all the code you need to create the required mass list inside this python 
file. The only restriction is that the final list should be called `masses`. 
In the case of gluino production we could store the following lines in a file called
`my_mass_info.py`: 
```python
# create the list with mass,pdg information
masses = [{"1000021":mass} for mass in range(1000,1500,100)]
```
You would then call the main script as follows: 
```
python run_scan.py --massdict my_mass_info.py
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

In case you want to produce chargino neutralino2 production with a mass difference of 0.1 GeV, you would follow the above
with the difference that you need to use the `--massdict` option. The corresponding 
python file could look like: 
```python
masses = [{"1000023":mass, "1000024":(mass+0.1)} for mass in range(100,500,25)]
```

To run with Condor on cmslpc, it is necessary to specify the output directory using an xrootd path:
```
root://cmseos.fnal.gov//store/path/to/file
```
For more about xrootd, click [here](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookXrootdService).

#### Features to be added in the future

- submission with condor (volunteer with condor experience needed)
- support for running in NLO mode. This will require extensive validation.



## Step 2: Process undecayed LHE files

This step assumes that you have access to a set of undecayed LHE files, and that you
have decided what decay chain you are interested in. This means that you need to know
the branching fractions and the masses of all particles in the decay chain. This 
information will be put in the header of the undecayed LHE files. A script is provided
in this repository to do exactly that.  
In order to easily retrieve which event belongs to which mass point, the script will
also add a comment line, containing the model string, in each event block.
It is important to note that this comment line needs to come immediately after the 
particle info, and before the reweighting tags, as shown here: 
```
<event>
 5   1  0.3062500E-02  0.9857737E+03  0.7816531E-02  0.9324287E-01
       21   -1    0    0  502  501  0.00000000000E+00  0.00000000000E+00  0.14584166042E+04  0.14584166042E+04  0.00000000000E+00 0.  1.
       21   -1    0    0  505  502  0.00000000000E+00  0.00000000000E+00 -0.77210579382E+03  0.77210579382E+03  0.00000000000E+00 0.  1.
  1000021    1    1    2  503  504 -0.55821310427E+03  0.77519697385E+02  0.52543654093E+02  0.97998571870E+03  0.80000000000E+03 0. -1.
  1000021    1    1    2  504  501  0.57314551739E+03 -0.10793617560E+03  0.67419761292E+03  0.11977847984E+04  0.80000000000E+03 0. -1.
       21    1    1    2  505  503 -0.14932413122E+02  0.30416478217E+02 -0.40430456653E+02  0.52751880857E+02  0.00000000000E+00 0.  1.
# model T1tttt_800.0_100
<scales pt_clust_1="13000.00000" pt_clust_2="13000.00000" pt_clust_3="33.88420"></scales>
< other tags for event reweighting > 
</event>
```


There are actually two relevant scripts for this step. The first one, [update_header.py](./update_header.py) 
is the one you will need to execute. 
You can print the help message with the following:
```
python update_header.py --help
```
As you can see from the output, the script takes a config file as input. The structure
of this config file is explained below. There are also two optional flags:
`--pdg` which specifies the PDG ID of the mother particle (used to find the mass value in the undecayed lhe filename),
and `--stableLSP` which should be used if the input LHE files do not contain a line like
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

The config file that is needed as input to the [update_header.py](./update_header.py) script, will be read
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
in the correct format. This script is called [create_update_header_config.py](./create_update_header_config.py). 
There are no command line options for this script. You will have to open up a text 
editor and fill out the appropriate entries in the `options` dictionary at the bottom
of the file. The table below contains all the options that will be used by the 
[update_header.py](./update_header.py) script. Any other option will be ignored. 

| Option       | Info
| :----------- | :-----------------------------
| `name`       | This corresponds to the name you passed to the [run_scan.py](./run_scan.py) script. It corresponds to the beginning of the name of the input LHE files. The assumed naming convention for the undecayed files is: ```<name><mother mass><other stuff>undecayed.lhe(.gz)```. The processed files will have the names ``` <model><mother mass><other stuff>decayed<mass info>```. The mass info will include the pdg id and mass of all particles for which you made a change in the slha.  
| `nevents`    | Number of events you want to process for each input file. Put any negative value to process all events.
| `inputdir`   | Location of the LHE files you want to process.
| `outputdir`  | Location where you want the processed LHE files to be stored. This directory will be created if it does not exist yet. 
| `model`      | New name to replace the original `name` that is part of the LHE filename (gluino in the default example from Part 1). The output files will thus start with "model". If you pass the empty string as option, the name will become 'custom' or equal to `decay` if that option was set.
| `mass`       | The name of the python file that contains the `mass_dict` dictionary. More info on this below. In short it specifies how to set the masses of the sparticles appearing in the decay chain. 
| `slha`       | Full path of the SLHA file you want to use. Leave this option blank if you are happy with the SLHA file present in the undecayed LHE file and you only want to add decay branching ratios for particles that have no branching ratios specified. 
| `decay`      | Name of one of the predefined options for the decay chain. Currently you can choose from T1tttt, T1bbbb, T1qqqq, T2qq, T2bb, T2tt, T2tt_3BD and T2cc. If none of these suit you, you can leave this option blank and use either the `slha` or `decaystring` options. 
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
The important thing to note here is that we are using a multiline option, as the decay block 
will have to multiline as well. For the ConfigParser to accurately parse this, the second and
 following lines need to start by non-zero whitespace. That is why in the above command I 
have added some whitespace after each `\n`. 
When reading this config option, the ConfigParser will strip all this whitespace. 
This is a problem for these decay blocks, as the lines that contain the branching fractions 
need to be indented. In order to solve this problem, you need to add quotes. This is why in 
the above command you can see these escaped quotes. 

The last thing that needs to be explained before coming to the examples is the aforementioned 
mass dictionary. This dictionary will encapsulate the grid of parameter points you want
to generate.  
The keys of the dictionary are the masses of the mother particles, i.e. the
particles that were produced with Madgraph. 
It is assumed that the undecayed files have names like what is used in step 1 of these instructions. 
Two formats are allowed:

 -  `<name>__<pdg id_mother mass(es)>__<other stuff>_undecayed.lhe(.gz)`. 

The notation used for the second part of this (i.e. mother mass in most cases) should be used as 
keys in the mass dictionary.
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
The file [create_update_header_config.py](./create_update_header_config.py) contains 
several functions to create this
mass dictionary for you. Most of the standard scenarios for simplified model scans
are included. For example, for the case where you only need to update the mass of the LSP,
and generate LSP masses from 0 till the mass of the mother particle (with a certain step 
size), you can use the function `makeMassDict_standard_SMS` found in 
[makeMassDict.py](./makeMassDict.py) and automatically imported in 
[create_update_header_config.py](./create_update_header_config.py).
Each provided function comes with some comments, so I encourage you to have a look at them
to decide whether they are useful for your case. 

#### Examples

Let's continue with the gluino example from the first step and assume that we have
produced a set of undecayed LHE files, and stored them in a folder called `lhe`
```
> ls lhe/
gluino_1000.0_0_undecayed.lhe.gz
gluino_1200.0_0_undecayed.lhe.gz
gluino_1400.0_0_undecayed.lhe.gz
gluino_800.0_0_undecayed.lhe.gz
```

For this example we want to generate the T1bbbb SMS topology, where the gluinos decay
to b+bbar+LSP. Apart from the gluino mass, the only free mass parameter is the LSP mass. 
Let's consider that we want to end up with events for all LSP masses up to the gluino 
mass, in steps of 200 GeV. The required mass dictionary to achieve this can be easily
generated using the `makeMassDict_standard_SMS()` function in the 
[update_create_header_config.py](./update_create_header_config.py) script. 
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
mass_dict = {'1400.0': [{'1000022': 1},
                        {'1000022': 200}, 
                        {'1000022': 400}, 
                        {'1000022': 600}, 
                        {'1000022': 800}, 
                        {'1000022': 1000}, 
                        {'1000022': 1200}], 
             '1200.0': [{'1000022': 1}, 
                        {'1000022': 200}, 
                        {'1000022': 400}, 
                        {'1000022': 600}, 
                        {'1000022': 800}, 
                        {'1000022': 1000}], 
             '1000.0': [{'1000022': 1}, 
                        {'1000022': 200}, 
                        {'1000022': 400}, 
                        {'1000022': 600}, 
                        {'1000022': 800}], 
             '800.0': [{'1000022': 1},
                       {'1000022': 200}, 
                       {'1000022': 400}, 
                       {'1000022': 600}]}
```

To create the config file, you should update the `options` dictionary at the end of the 
[create_update_header_config.py](./create_update_header_config.py) script, give a name for the config file, and then 
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
           "decay": "T1bbbb",
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

The last step is then to pass your newly created config file to the [update_header.py](./update_header.py) 
script to actually create the processed LHE files.
```
python update_header.py myconfig.cfg
```
Now you have a set of LHE files that are in principle ready to be put through the 
official production. 

When using LPC Condor, the undecayed lhe.gz files will be stored on EOS. It is best to move the files from EOS to scratch space
before adding the decay information, to avoid overuse of the fuse mount for the file system. The script
(processUndecayed.sh)[./processUndecayed.sh] shows an example of how to do this.

## Step 3: Validation

You should make sure that your processed LHE files are valid. The easiest thing to 
do is to simply look at the LHE file and check whether the needed masses were updated, 
whether the DECAY block was properly injected, and whether each event contains the
correct comment line with the model tag. 

It is also a good idea to follow the instructions for the [private production](#step-4b:-private-production),
in particular those for the GEN step, to check that your LHE files will not cause
any issues during the further processing steps. 


## Step 4a: Injection into official production

Once you have processed the undecayed LHE files, and verified that things look ok, you
are ready to submit your request to the official production. To do this you should 
contact the SUSY MC Generator contacts, and coordinate with them to get your files
uploaded to EOS. All LHE files that are used as input in an official request need to 
be stored under /store/lhe, but only the Generator Contacts have write permissions. 
You will need to tell the MC Contacts exactly how many events are in your request. 

The Generator Contacts will then inject the request in the McM database 
(https://cms-pdmv.cern.ch/mcm/), and will report on it during the weekly Monte Carlo
Coordination Meeting. This is where the priority of the request will be discussed. 
If for some reason you need the samples very urgently, you should also contact the
SUSY conveners and relevant subgroup conveners. 

The last input that should be provided to the gencontacts, is the qcut values that 
should be used with your request. This value needs to be put in the Generator Fragment, 
such that Pythia8 will know how to properly match the matrix element and the parton 
shower. Please note that this is only needed if you have produced several multiplicities
of additional partons in the Madgraph step. The default for the SUSY group is to produce
up to 2 additional partons, so most requests will need to have a corresponding qcut. 

The qcut depends on the hard process, and on the mass of the produced particles. If 
someone already determined the qcut for the hard process (e.g. gluino pair production), 
and mass range you are interested in, you can simply reuse that value. 
An up-to-date list of qcut values can be found on this twiki page: 
https://twiki.cern.ch/twiki/bin/viewauth/CMS/SUSYMCProduction13TeV#QCUT_recommendations
If the qcut has not been determined yet, you should do it yourself by following the 
instructions in the section [Determining the QCUT](#determining-the-qcut). 


## Step 4b: Private production

You can of course also produce a few samples privately, rather than go through the full
production chain. In this case there is no need to upload files to EOS. You do need an
appropriate qcut value however. Once you have this number, you can update the generator
fragment and start the private production. Depending on the scope of the study you wish
to perform, you will need to run different steps. For all options you will need the 
appropriate genfragment. These can usually be found on the genproductions github page. 
Currently, a good fragment to use with the files produced using this setup is not yet
available there. In the mean time you can use the fragment I provide on my public area on
afs:

/afs/cern.ch/user/n/nstrobbe/public/genfragment.py

In this fragment you should update the value of `JetMatching:qCut`, and perhaps the 
value of `JetMatching:nJetMax`. The `nJetMax` should be set to the largest number of 
extra partons that are present in the lhe file. The SUSY default for this is `2`.  

#### Prepare a CMSSW area

Before you can start, you need to set up a CMSSW area. Which release(s) to use will depend
on whether or not you want to produce events up to FastSim or DIGI-RECO. The campaigns
for reconstruction in Run2 are not ready yet. The GEN-SIM campaign is already available
and is currenlty using `CMSSW_7_1_12`. 

To run the GEN step, you need to place the genfragment in a specific directory, and 
you should not forget to compile. 

Instructions: 
```
cmsrel CMSSW_7_1_12
cd CMSSW_7_1_12/src
cmsenv
mkdir -p Configuration/GenProduction/python
mv genfragment_cff.py Configuration/GenProduction/python
scram b
```

#### GEN only

If you only want to do a generator level study, or if you want to determine a proper 
qcut to be used with your samples, you only need to run the GEN step, which is quite
fast. 

In the official production this is done in two steps. In the first step the LHE file 
is converted into EDM format, and then in the second step the decay, parton shower and
 hadronization is performed. If you want to process multiple files in one go, you can 
pass a comma-separated list of files to the `--filein` argument. 
```
cmsDriver.py step0 --mc --eventcontent LHE --datatier GEN --conditions MCRUN2_71_V1::All --step NONE  --filein file:mylhe.lhe --fileout file:step0.root -n -1

cmsDriver.py Configuration/GenProduction/python/genfragment_cff.py --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot NominalCollision2015 --step GEN --magField 38T_PostLS1  --filein file:step0.root --fileout file:GEN.root -n -1
```

When doing things locally, you can condense this into a single run: 
```
cmsDriver.py Configuration/GenProduction/python/genfragment_cff.py --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot NominalCollision2015 --step GEN --magField 38T_PostLS1  --filein file:mylhe.lhe --fileout file:GEN.root -n -1
```

#### FASTSIM

The official FastSim for Run2 is not yet available.


#### FullSim

The final DIGI-RECO for Run2 is not yet available. 

Instructions for the GEN-SIM step: 
```
cmsDriver.py Configuration/GenProduction/python/genfragment_cff.py --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot NominalCollision2015 --step GEN,SIM --magField 38T_PostLS1  --filein file:mylhe.lhe --fileout file:GEN.root -n -1
```

#### Phys14 setup

Given that the full DIGI-RECO setup for Run2 is not ready yet, we also provide
instructions on how to make samples according to the Phys14 setup. 

##### GEN-SIM

The CMSSW release to be used is: **CMSSW_6_2_11** or later CMSSW_6_2_X

The cmsDriver command: 

```
cmsDriver.py GenFragment --filein file:input.lhe --fileout file:GENSIM.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier GEN-SIM --conditions POSTLS162_V1::All --step GEN,SIM --magField 38T_PostLS1 --geometry Extended2015 -n -1
```

##### DIGI-RECO-MINIAOD

The CMSSW release to be used is: **CMSSW_7_2_0**

The cmsDriver commands that were used in the official production:
```
cmsDriver.py step1 --filein file:GENSIM.root --fileout file:step1.root --pileup_input "dbs:/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM" --mc --eventcontent RAWSIM --inputEventContent REGEN --pileup AVE_20_BX_25ns --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier GEN-SIM-RAW --conditions PHYS14_25_V1 --step GEN:fixGenInfo,DIGI,L1,DIGI2RAW,HLT:GRun --magField 38T_PostLS1 -n -1 

cmsDriver.py step2 --filein file:step1.root --fileout file:step2.root --mc --eventcontent AODSIM,DQM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier AODSIM,DQMIO --conditions PHYS14_25_V1 --step RAW2DIGI,L1Reco,RECO,EI,DQM:DQMOfflinePOGMC --magField 38T_PostLS1 -n -1

cmsDriver.py step3 --filein file:step2.root --fileout file:out.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions PHYS14_25_V1 --step PAT -n -1
```
For private production the DQM info is probably not needed, so it should be safe to drop this step. 

If you want to run with 40 pileup, you should use the following command for the step1:
```
cmsDriver.py step1 --filein file:GENSIM.root --fileout file:step1.root --pileup_input "dbs:/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM" --mc --eventcontent RAWSIM --inputEventContent REGEN --pileup AVE_40_BX_25ns --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier GEN-SIM-RAW --conditions PHYS14_25_V1 --step GEN:fixGenInfo,DIGI,L1,DIGI2RAW,HLT:GRun --magField 38T_PostLS1 -n -1
```


## Determining the QCUT

To determine a good qcut for a given process, you need to scan different values and pick
the one that gives you smooth differential jet rate (DJR) plots. 

To obtain these plots we provide a script: [plotdjr.C](./plotdjr.C)
The input to this script is an EDM file containing the output of the GEN step. See the 
instructions for the "GEN only" step in the "Private production" section on how to 
produce a GEN file. 

You will also need to use the FWLite setup. So you will first have to do a `cmsenv` in a CMSSW area, 
and have a `rootlogon.C` file that sources the FWLite libraries. This file should contain
something along the following (taken from one of the workbook pages):

```C
{
  // Set up FW Lite for automatic loading of CMS libraries
  // and data formats.   As you may have other user-defined setup
  // in your rootlogon.C, the CMS setup is executed only if the CMS
  // environment is set up.
  //
  TString cmsswbase = getenv("CMSSW_BASE");
  if (cmsswbase.Length() > 0) {
    //
    // The CMSSW environment is defined (this is true even for FW Lite)
    // so set up the rest.
    //
    cout << "Loading FW Lite setup." << endl;
    gSystem->Load("libFWCoreFWLite.so");
    AutoLibraryLoader::enable();
    gSystem->Load("libDataFormatsFWLite.so");
    gSystem->Load("libDataFormatsPatCandidates.so");
   }
}
```


To create the DJR plots corresponding to a given GEN file, simply do the following: 

```
root -l
.L plotdjr.C
plotdjr("path/to/your/GENfile.root","outputbase")
```

This will give you three plots, called `outputbase_djr0.pdf`, `outputbase_djr1.pdf` and `outputbase_djr2.pdf`. 
For events produced up to two extra partons, only the first two of those plots are relevant. The third plot
should be smooth by construction. 
You will need to run over about 10-50k (depending on the matching efficiency) events to get a DJR plot that has 
low enough statistical fluctuations to be able to make a decision on the qcut value to use. 

