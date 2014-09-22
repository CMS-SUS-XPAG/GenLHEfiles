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

I will now give some details on each of the files, and will then show you how to run the decay step. 

1. **main20.cc**
  * This is the Pythia8 program that will do the decay
  * It takes as argument a config file (see below) and the name for the output file
  * By default it will process 100k events. You can easily change
2. **template.cmnd**
  * This is the template of the config file that will be passed to the pythia executable
  * It specifies which file to use as input file, how many events to process, and turns on the parton shower and hadronization
3. **runDecay.py**
  * This is the scripts that calls pythia to do the decay
  * It has two options:
    1. `-d` :  the location of the directory that contains all the undecayed lhe files that need to be decayed. The files in that directory need to have undergone the prep step as explained before, and have the string `undecayed` as part of the name. 
    2. `-n` : the number of events to process
  * Several directories will be made, for the config files, the log files and the resulting decayed files

Now that you know a bit about what each file does, you can simply start running by doing
```
python runDecay.py -d <input_dir> -n <nevents>
```
All `.lhe` files in the `input_dir` will be decayed and put in the `results` directory. 
Now you are ready to postprocess those decayed files to the required level (see next section).


### Postprocess the decayed file