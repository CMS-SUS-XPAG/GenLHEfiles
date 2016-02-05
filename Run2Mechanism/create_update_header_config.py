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
import makeMassDict as m

## ----------------------------------------------------------------
## Write a config file with name 'configname' according to the 
## options passed via 'options'
## ----------------------------------------------------------------
def makeConfig(options, configname):
    config = ConfigParser.SafeConfigParser()

    config.add_section('Global')
    config.set('Global', 'name', options["name"])
    config.set('Global', 'pdg', options["pdg"])
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
    # The dictionary should have the follow format: 
    # mass_dict = {"mother_mass_1": [{"pdgid":mass, "pdgid":mass},
    #                                {"pdgid":mass, "pdgid":mass},
    #                                {"pdgid":mass, "pdgid":mass}],
    #              "mother_mass_2": [{"pdgid":mass, "pdgid":mass},
    #                                {...},
    #                                ... ], 
    #              ....
    #             }
    # If you have two mother pgd ids (e.g. for chargino-neutralino 
    # production), you should put those as a comma-separated list in the
    # key of the dictionary, e.g.
    # mass_dict = {"mother_mass_A_1,mother_mass_B_1": [...], ...}
    # Or more explicitly 
    # mass_dict = {"400,380": [{"1000022":100},
    #                          {"1000022":200}],
    #              "500,480": [{"1000022":100},
    #                          {"1000022":200}],
    #             }

    m.makeMassDict_standard_SMS(range(800,1605,100),100)

    # Fill out the options dictionary with your configuration:
    # All options need to be provided as strings.
    # options = {"name": <name corresponding to the start of inputfiles>, 
    #           "pdg": <comma-separated list of mother ids. Will mostly 
    #                   just contain one entry, potentially two for 
    #                   chargino-neutralino production>,
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
    #                     of the already provided ones ("T1tttt","T1bbbb",
    #                     "T1qqqq","T2tt","T2tt_3BD","T2cc","T2bb","T2qq")>,
    #           "decaystring": <Full decay string to be inserted into the
    #                           undecayed files. Useful if your choice is
    #                           not supported by default.>
    #           }

    options = {"name": "gluino", 
               "pdg": "1000021",
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
    configname = "tutorial.cfg"

    # Actually create the config file to be used by update_header.py
    makeConfig(options, configname)
