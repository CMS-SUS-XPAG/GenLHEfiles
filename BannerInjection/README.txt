##################################################################################################################
##################################################################################################################
##################################################################################################################
####################################       Banner injection for SMS models       #################################
##################################################################################################################
##################################################################################################################
##################################################################################################################


1.- Introduction
================

Simplified Models (SMS) in the SUSY PAG are generated using *LHE templates* that only contain the SUSY particles
produced in the hard interaction. These templates are generated using Madgraph Leading Order with up to 2 extra
partons. The decays of these particles are done centrally in a different step and using Pythia8. The LHE events of
a given SMS scan should contain an SLHA header indicating the characteristic decay table. The process of taking the
LHE templates and adding the right SLHA header is called *Banner Injection*.

As an example consider the two different gluino scans T1tttt and T1bbbb. In order to produce these two scans
we need to use the gluino LHE events, and file by file, inject the right SLHA banner with the information about
how the gluino is going to decay (tops or bottoms). Once this is done we copy the files into the eos SUSY area.
This process can be divided in the following sub-processes:

* Getting the number of mass points and number of events associated with a given scan

* Dividing the scan in blocks with the same qcut and reasonable number of events

* Running banner injection script

* Some cautions when running the banner injection script


2.- Getting the number of mass points and number of events associated with a given scan
=======================================================================================

The number of mass points and the number of events per point has been coded already in a ROOT macro called:
SUSY_SMS_Models.C. This macro takes into account the cross sections of the corresponding process (gluino
production, stop production, etc) and calculates the mass points and total number of events for all the 
approved scans. In order to use it, just load the file compiled in ROOT .L SUS_SMS_Models.C+ and type go().
If you are working with a particular scan it is maybe a good idea to comment out the other scans in the 
go() method. The output you will get when running go is a list containing for every pair of masses the
following information:

"MASS1" "MASS2" "Needed Number of Events after Matching"

You will need this information in the next steps. Take into account that the "couts" for some of the SMS
models have not yet been included in SUSY_SMS_Models.C. If a model it's not printing anything, just go
to the code and add the proper couts following the examples.


3.- Dividing the scan in blocks with the same qcut and reasonable number of events
==================================================================================

The list you will get in step 2 contains the full scan, however we cannot process the whole scan in just one single
dataset for two reasons:

* The qcuts depend on the masses of the produced particles

* We have a limit of 50 Million LHE events before matching per dataset

This means that you have to split the list you got in a set of lists (about 10 more or less usually) each of them
with the same qcut. Consider the example of T1tttt where the total list would go from gluino masses of 600 to 2000. 
We should put that list in different text files according to the mass ranges, qcuts and number of events:

T1tttt_600to700.txt
T1tttt_700to800.txt
...
...
T1tttt_1800to2000.txt
 
If you want to add up the number of events you have in a given text file use:

python countNumberOfEvents.py T1tttt_600to700.txt [efficiency]

Efficiency means the matching efficiency for that LHE template and qcut. For gluinos and stops is about 0.25. This 
script will give you back the total number of LHE events of that file after matching, and the total LHE events
before matching. The latter has to be always smaller than 50 Million. 

The next step is to create a directory in the SUSY eos area associated to this scan and to the different blocks or
datasets that this scan will contain. As an example, in lxplus:

eos mkdir /eos/cms/store/group/phys_susy/LHE/13TeV/T1tttt/
eos mkdir /eos/cms/store/group/phys_susy/LHE/13TeV/T1tttt/T1tttt_600to700/
eos mkdir /eos/cms/store/group/phys_susy/LHE/13TeV/T1tttt/T1tttt_700to800/
...
...
eos mkdir /eos/cms/store/group/phys_susy/LHE/13TeV/T1tttt/T1tttt_1800to2000/


4.- Running banner injection script
====================================

The number of *LHE templates* files is huge. Getting them from eos, changing the banner and copy them back to the SUSY eos
area associated to the given scan cannot be done sequeantilly in a single computer. The script call "send_jobs.py" takes
care of this and will submit as many jobs to lxbatch as LHE files we have. In this way, it is possible to complete a single
scan in about half a day (depending strongly on the lxbatch queues). 

The syntax of send_jobs.py is the following:

python send_jobs.py mass_scan.txt banner.txt model_name efficiency source destiny currentPath 

* mass_scan.txt is the list of mass pairs and events produced in step 3

* banner.txt is the banner that we want to inject. **Always use the template included in github**. In this banner there are
placeholders called MASS1 and MASS2 to inject the right masses for every point. These placeholders have to be changed 
depending on the kind of scan we have (if it is a scan with gluinos going to neutralinos MASS1 and MASS2 should appear in the
SLHA mass line corresponding to gluinos and neutralinos). The decay table has to be adapted accordingly. It is important
to notice that pythia8 does not handel out of the box off-shell decays. If your scan includes off-shell decays just contact
the experts.

* model_name is the name of the model that will go in the final LHE event (T1tttt, T2tt, T5qqqqVV, etc, etc)

* efficiency is the matching efficiency, needed to know how many template LHE files should be processed

* source is the directory that contains the LHE templates
/eos/cms/store/group/phys_susy/LHE/13TeV/gluino_gluino_v2
/eos/cms/store/group/phys_susy/LHE/13TeV/stop_stop_v2
/eos/cms/store/group/phys_susy/LHE/13TeV/sbottom_sbottom_v2
/eos/cms/store/group/phys_susy/LHE/13TeV/sq_sq_v2


* destiny is the destiny directory (created in step 3)

* currentPath is just the current directory $PWD

The script will calculate how many LHE files are needed and will send jobs to lxbatch running the secondary script process_file.py
that takes care of really doing the banner injection.


5.- Some cautions when running the banner injection script

There are a couple of critical things when running send_jobs.py. 

* Indicating the syntax of the file name of the LHE templates. The script needs to extrac the masses contained in the LHE
template files. In order to do this the script uses the file name. If the file name is called:

gluino_gluino_500_LSP_100_run134314321.lhe.xz

the script will take the 500 and 100 doing parsing on "gluino" and "LSP". However the names of the templates can vary so
it is important to make sure by hand that send_jobs.py is able to extract the mass out of the file name. This ofently simply
requires to change the search for "gluino" into a search for "stop" for example if we would be moving to a stop template.

* The second caution is about not sending many jobs at the same time. For each dataset or block, send_jobs.py can generate
close to 300 jobs depending on the total number of events. If all of them try to access eos at the same time, there might
be problems and many of them might fail. For that reason is a good idea to send each dataset separately. It is also worth
noticing that send_jobs.py checks if a file already exists at destination and does not send it again. Indeed send_jobs.py
sends an error message (to be ignored) when the file does not exist at destination. The script can be used many times
in a row until no missing files are detected. 



