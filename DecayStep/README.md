# A guide to decaying LHE files

You want to study a certain process, but there is no sample available? 
No need to despair, using this guide you will be able to make your own decayed LHE events, starting from existing "undecayed" LHE files.
If there are no undecayed files available for the hard process you want to start from, e.g. gluino pair production, you will first have to generate those yourself as well. Instructions on how to do that can be found elsewhere. 

The procedure to perform the decay is slightly different depending on whether you want to use Pythia6 or Pythia8 for the decay. 
As the default parton shower and hadronization for the 13TeV Monte Carlo will be done using Pythia8, I will for now focus on that approach. 

## Decaying LHE files using Pythia8 standalone

I have found that it is easiest to perform the decay using a standalone version of pythia8. 
In principle it should be possible to do it using CMSSW, but I have not figured out a way to do it yet. Once I do, I will update these instructions. 

There are several steps involved. Some can be omitted if the files are not intended to go through official production. 

1. Prepare the undecayed files to make them ready for the decay step
2. Do the actual decay
3. Postprocess the decayed file 

I will now go through each of these steps in detail below. I suggest you read through all the steps first, before starting your journey to decay your files. 

### Preparation of the undecayed files

The undecayed files you want to use will most likely not have the exact SLHA you want specified in their header.
The masses of all the particles will not be what you want, and the decay will probably not be specified at all. 
So, it is up to you to add this information. 
The exact way in which you do this does not matter so much. As long as the final result is an LHE file that has the full SLHA information in the header. 

You can for example just open the undecayed file in a text editor, and change the masses by hand. You can also add the DECAY blocks you want. 
MASS and DECAY blocks look like this: 
```
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
...
   1000006     1.00000000E+05   # ~t_1
   2000006     1.10000000E+05   # ~t_2
   1000021     1000             # ~g
   1000022     100              # ~chi_10 
...
```
```
DECAY  1000021  1.0 
   1.0  3  1000022 5 -5     # ~g -> ~chi_10 b bbar 
DECAY  1000022  0.0
```

If you will be decaying a lot of files, you probably want to automate this with a small script. 
I put an example script in this repository, called `process_undecayed_lhe.py`. Depending on your particular setup, you will probably have to make quite a few changes. There are many comments in the script, so it should be rather straight-forward to adapt to your needs. 

### Decaying the file

The first step will of course be setting up a standalone version of Pythia8. You can download the latest version from the pythia webpage: 

http://home.thep.lu.se/~torbjorn/Pythia.html 

Currently the latest version is 8.186. In principle you should just follow the instructions in the "Installation" section of that webpage. 
For convenience, this is what I did to get set up on lxplus. There is no need to setup a CMSSW environment beforehand. 

```
wget http://home.thep.lu.se/~torbjorn/pythia8/pythia8186.tgz
tar xzvf pythia8186.tgz
cd pythia8186
make
```

At this point you should have a working version of Pythia8. Now you can go into the `examples` folder and verify that you can compile and run one of the examples there. 

```
cd examples
make main01
./main01.exe
```

If that worked without problems, you are ready to get started and decay your own files. 
To make that very easy, I have prepared a few files. 
You can find them in the directory PythiaScripts. They should be copied into the examples folder of your Pythia8 setup. 
Please note that the LHE files you want to decay need to have the full SLHA information in the header.

I will now give some details on each of the files, and will then show you how to run the decay step. 

1. **main20.cc**
  * This is the Pythia8 program that will do the decay
  * It takes as argument a config file (see below) and the name for the output file
2. **template.cmnd**
  * This is the template of the config file that will be passed to the pythia executable
  * It specifies which file to use as input file, how many events to process, and turns off the parton shower and hadronization
3. **runDecay.py**
  * This is the scripts that calls pythia to do the decay
  * It has two options:
    1. `-d` :  the location of the directory that contains all the undecayed lhe files that need to be decayed. If the files in that directory have the string `undecayed` as part of the name, that will be changed to `decayed`. Otherwise the name of the output file will be kept the same as that of the inputfile. 
    2. `-n` : the number of events to process
  * Several directories will be made, for the config files, the log files and the resulting decayed files

Now that you know a bit about what each file does, you can simply start running by doing
```
python runDecay.py -d <input_dir> -n <nevents>
```
All `.lhe` files in the `input_dir` will be decayed and put in the `results` directory. 
Now you are ready to postprocess those decayed files to the required level (see next section).


### Postprocess the decayed file

Postprocessing of the decayed files is needed when you have used LHE files that include the production of extra partons at the matrix element level, or if you want to have the files processed in official production. 

Releases before CMSSW7X cannot handle LHE files with different headers in one request.
So for the usual scan approach, in which we combine multiple mass points in one dataset, we need to make sure that **all headers are the same**. 
To do that we remove the original header and put in place a new version, in which all differences have been removed. 
For LHE files that were produced using MadGraph and then possibly decayed using Pythia, the following things need to be removed or set to a dummy value: 
* `MGGenerationInfo` block. This can be removed completely
* Masses of the sparticles, you can put them to a dummy value

Another complication when processing multiple mass points together, is that you loose track of which event belongs to which mass point. To remedy that we add an additional comment line to each event, containing the model and the mass point information. This can then be retreived from the LHEEventProduct. 

If you produced events up to X extra partons, Madgraph will have added a line to the output LHE file containing clustering information that is needed by the parton shower program, in this case pythia, to do the proper jet matching. 
When running the decay step, this line is removed and in case of pythia8, replaced by another line (the exact meaning of that line is unclear). 
Until the new Madgraph-Pythia8 matching interface is fully setup and validated, I would recommend to stick to the old way of doing things (as for pythia6), and replace the new line with the old line from the undecayed file. While doing this you need to take care to copy things between the same events. 

I have provided a small script that will do all of these things, `process_decayed_lhe.py`.
As before, you will probably have to make some changes to this file, but there are plenty of comments to help you along. 

In case you want to do a private production on file without jet matching, you can skip this step and go straight ahead to FastSim or FullSim. 
