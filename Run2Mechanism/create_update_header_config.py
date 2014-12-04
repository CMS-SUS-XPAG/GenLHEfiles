#####################################################################
##                                                                 ##
## File:        create_update_header_config.py                     ##
##                                                                 ##
## Description: Create the config file needed to run               ##
##              update_header.py                                   ##
##                                                                 ##
## This script does not have any command line options, you should  ##
## modify the main part of the script by hand. Instructions can be ##
## found in the main part or on the github page.                   ##
##                                                                 ##
## You also need to create a dictionary that contains the mass     ##
## information for the decay step. Some functions are provided     ##
## that will do this for you. Please read the comments above those ##
## functions for more details. If you want to do something more    ##
## complicated, you will need to create the dictionary yourself.   ##
##                                                                 ##
## Author:   Nadja Strobbe                                         ##
## Created:  2014-12-04                                            ##
## Updated:  ...                                                   ##
##                                                                 ##
#####################################################################

import ConfigParser

## ----------------------------------------------------------------
## Write a config file with name 'configname' according to the 
## options passed via 'options'
## ----------------------------------------------------------------
def makeConfig(options, configname):
    config = ConfigParser.SafeConfigParser()

    config.add_section('Global')
    config.set('Global', 'name', options["name"])
    config.set('Global', 'nevents', options["nevents"])
    config.set('Global', 'inputdir', options["inputdir"])
    config.set('Global', 'outputdir', options["outputdir"])
    config.set('Global', 'model', options["model"])

    config.add_section('SLHA')
    config.set('SLHA', 'slha', options["slha"])
    config.set('SLHA', 'mass', options["mass"])
    config.set('SLHA', 'decay', options["decay"])
    config.set('SLHA', 'decaystring', options["decaystring"])

    with open(configname, 'w') as configfile:
        config.write(configfile)


## ---------------------------------------------------------------------
## Create a mass dictionary for standard SMS scenarios:
## For each mass in the list of 'mother_masses', we want to decay to a 
## range of LSP masses starting from 0 and ending at the considered 
## mother_mass. The step size is controlled via 'LSP_step'. 
## The dictionary code will be written to a file with name 'fname'. 
## This file should have a ".py" extension as it will be imported in the
## update_header.py script. 
## ---------------------------------------------------------------------
def makeMassDict_standard_SMS(mother_masses, LSP_step, fname="mass_dict.py"):
    to_print = "mass_dict = { \"%%.1f\"%%(x) : ([ {'1000022': mass} for mass in range(0,x,%s) ]) for x in %s }" % (
        LSP_step, mother_masses)
    
    with open(fname, 'w') as mdict:
        mdict.write(to_print)

## ---------------------------------------------------------------------
## Create a mass dictionary for SMS scenarios with an additional 
## sparticle in the decay chain that will have a fixed mass.
## fixed_pdg and fixed_mass are the pdg id and mass for the sparticle 
## that will have a fixed mass in all lhe files.
## var_pdg, var_min, var_max and var_step are the pdg id and mass range
## information for the sparticle that will have a variable mass. If 
## var_max is larger than the considered mother_mass, it will be 
## replaced by mother_mass. 
## The dictionary code will be written to a file with name 'fname'. 
## This file should have a ".py" extension as it will be imported in the
## update_header.py script. 
## ---------------------------------------------------------------------
def makeMassDict_SMS_fixed(mother_masses, 
                           fixed_pdg, fixed_mass,
                           var_pdg, var_min, var_max, var_step, 
                           fname="mass_dict.py"):
    to_print = "mass_dict = { \"%%.1f\"%%(x) : ([ {%(var_pdg)s : mass, %(fixed_pdg)s : %(fixed_mass)s} for mass in range(%(var_min)s,min(%(var_max)s,int(x)),%(var_step)s) ]) for x in %(mother_masses)s }" % locals()

    with open(fname, 'w') as mdict:
        mdict.write(to_print)


## ---------------------------------------------------------------------
## Create a mass dictionary for SMS scenarios with an additional 
## sparticle in the decay chain that will have a fixed mass difference
## with respect to the varying sparticle.
## fixed_pdg and fixed_mass_diff are the pdg id and mass difference  for
## the sparticle that will have a fixed mass difference. The mass 
## difference can be positive or negative
## var_pdg, var_min, var_max and var_step are the pdg id and mass range
## information for the sparticle that will have a variable mass. If 
## var_max is larger than the considered mother_mass, it will be 
## replaced by mother_mass. 
## The dictionary code will be written to a file with name 'fname'. 
## This file should have a ".py" extension as it will be imported in the
## update_header.py script. 
## ---------------------------------------------------------------------
def makeMassDict_SMS_massdiff(mother_masses, 
                              fixed_pdg, fixed_mass_diff,
                              var_pdg, var_min, var_max, var_step, 
                              fname="mass_dict.py"):
    to_print = "mass_dict = { \"%%.1f\"%%(x) : ([ {%(var_pdg)s : mass, %(fixed_pdg)s : mass+%(fixed_mass_diff)s} for mass in range(%(var_min)s,min(%(var_max)s,int(x)),%(var_step)s) ]) for x in %(mother_masses)s }" % locals()

    with open(fname, 'w') as mdict:
        mdict.write(to_print)


## ---------------------------------------------------------------------
## Create a mass dictionary for SMS scenarios with an additional 
## sparticle in the decay chain that has a mass according to a certain
## fraction x of the initial and final sparticles: 
## mass = x * m_mother + (1 - x) * m_LSP
## fixed_pdg and fixed_x_value are the pdg id and x value for the 
## sparticle that will have it's mass assigned through the x value. 
## var_pdg, var_min, var_max and var_step are the pdg id and mass range
## information for the sparticle that will have a variable mass. If 
## var_max is larger than the considered mother_mass, it will be 
## replaced by mother_mass. 
## The dictionary code will be written to a file with name 'fname'. 
## This file should have a ".py" extension as it will be imported in the
## update_header.py script. 
## ---------------------------------------------------------------------
def makeMassDict_SMS_xvalue(mother_masses, 
                            fixed_pdg, fixed_x_value,
                            var_pdg, var_min, var_max, var_step, 
                            fname="mass_dict.py"):
    to_print = "mass_dict = { \"%%.1f\"%%(x) : ([ {%(var_pdg)s : mass, %(fixed_pdg)s : x*%(fixed_x_value)s+(1-%(fixed_x_value)s)*mass} for mass in range(%(var_min)s,min(%(var_max)s,int(x)),%(var_step)s) ]) for x in %(mother_masses)s }" % locals()

    with open(fname, 'w') as mdict:
        mdict.write(to_print)


## ---------------------------------------------------------------------
## Main program part
##
## This is the part that you as a user should modify to obtain the 
## configuration you want to produce. 
## ---------------------------------------------------------------------
if __name__ == "__main__": 
    
    # Create the mass dictionary.
    # This encodes how each undecayed lhe file should be decayed.
    # There are several predefined functions available that take care of
    # the most basic setups you might want to run.
    # If these do not suit you, you can create your own dictionary. You 
    # should create a separate python file that creates the dictionary 
    # and stores it in a variable called mass_dict. If the variable is 
    # not called mass_dict, the update_header.py script will not be able 
    # to import it. The name of this python file should correspond to 
    # the entry you put in the options dictionary for 'mass'. 

    mass_dict = makeMassDict_standard_SMS(range(800,1205,100),100)


    # Fill out the options dictionary with your configuration:
    # options = {"name": <name corresponding to the start of inputfiles>, 
    #           "nevents": <number of events to run over, -1 means all>,
    #           "inputdir": <location of the undecayed files>, 
    #           "outputdir": <location to store the processed files>, 
    #           "model": "<model string to be used in the output files
    #                      Needs to be specified if using the decaystring
    #                      option. When using the decay option, the value
    #                      for decay will be used by default>",
    #           "slha": <location of full slha file in case you want to
    #                    replace the full slha block>,
    #           "mass": <.py file that contains the mass_dict>, 
    #           "decay": <SMS model for the decay, if your choice is part
    #                     of the already provided ones>,
    #           "decaystring": <Full decay string to be inserted into the
    #                           undecayed files. Useful if your choice is
    #                           not supported by default.>
    #           }

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
