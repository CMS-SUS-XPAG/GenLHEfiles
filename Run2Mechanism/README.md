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

The first thing you need to decide is what process you want to investigate, and what
are the sparticles that will be produced in the hard collision. Typically these are
gluinos, top squarks, bottom squarks, et cetera. 

Once you know what process you want, you should have a look at the SUSY group area on 
EOS to check whether LHE files for that process have already been produced. If you
are happy with what is already available, then you can immediately proceed to the 
next step. If your desired process is not there, or you want to look at different
masses, then you will need to produce the undecayed LHE files yourself by following
the instructions in this section. 

**TO DO: Add Madgraph instructions**


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
such that Pythia8 will now how to properly match the matrix element and the parton 
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