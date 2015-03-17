########################################################################
## file: update_header.py                                             ##
##                                                                    ##
## description: Update the header of LHE files to include all needed  ##
##              SLHA information to do subsequent decays.             ##
##              This includes updating the MASS and DECAY blocks.     ##
##                                                                    ##
## Input is a configuration file that specifies all the actions that  ##
## will be taken. Please refer to create_update_header_config.py for  ##
## more information on how to construct a proper config file.         ##
##                                                                    ##
## There is a flag --stableLSP which should be used when you want a   ##
## stable LSP, and the original LHE file does not have this in the    ##
## header yet.                                                        ##
##                                                                    ##
## Author: Nadja Strobbe                                              ##
## Created: 2014-12-02                                                ##
## Updated: ...                                                       ##
##                                                                    ##
########################################################################

import sys, os, glob, re
import gzip
import argparse
import ConfigParser

## ---------------------------------------------------------------------
##  Process the lhe file with name 'infilename', and save it to a file
##  with name 'outfilename'. The masses to be replaced are specified in
##  'masses_to_replace'. This should be a dictionary of the form
##  {particle pdgId : mass}
##  The decay info should be the full decay block that needs to be 
##  inserted.
##  Please note that overriding branching fractions that are present in 
##  the original lhe, does not work yet.
## ---------------------------------------------------------------------
def process_lhe(infilename, outfilename, masses, decay_info, nevents, modeltag):
    if infilename.endswith(".lhe.gz"):
        infile = gzip.open(infilename)
    elif infilename.endswith(".lhe"):
        infile = open(infilename)
    else: 
        sys.exit("LHE files should have extension .lhe or .lhe.gz")
    outfile = open(outfilename,'w')

    lastblock = ""
    in_ev = False
    nev = 0
    for line in infile: 
        if "BLOCK" in line:
            lastblock = line
        newline = line
        if "MASS" in lastblock:
            for particle,mass in masses.iteritems():
                if particle in line:
                    newline = "      %s     %s       # \n" % (particle, mass)
        if "DECAY" in line and decay_info != "":
            # check the particles in decay_info
            # if they are there, do not keep the old info
            decay_part1 = line.split()[0] 
            decay_part2 = line.split()[1]
            if re.search("%s\s+%s"%(decay_part1, decay_part2),decay_info):
                continue
        if "</slha>" in line and decay_info != "":
            # add the DECAY before closing the tag
            # check whether decay_info ends in \n
            if decay_info.strip(" ")[-1:] == "\n":
                newline = decay_info
            else: 
                newline = decay_info+"\n"
            newline += line
        if in_ev and line.startswith("<"):
            newline = "%s\n%s" % (modeltag,line)
            in_ev = False
        outfile.write(newline)
        if "<event>" in line: 
            in_ev = True
        if "</event>" in line:
            nev += 1
        if nev == nevents:
            # We've reached the number of events we wanted
            # write out the end statement and stop
            outfile.write("</LesHouchesEvents>\n")
            break

    outfile.close()
    infile.close()

## ---------------------------------------------------------------------
##  Process the lhe file with name 'infilename', and save it to a file
##  with name 'outfilename'. 
##  The new slha block will be updated with with the mass information. 
##  Then the slha will be inserted into the lhe file.
## ---------------------------------------------------------------------
def process_lhe_with_slha(infilename, outfilename, slha, masses, nevents, modeltag):
    if infilename.endswith(".gz"):
        infile = gzip.open(infilename)
    elif infilename.endswith(".lhe"):
        infile = open(infilename)
    else: 
        sys.exit("File extension should be .lhe or .lhe.gz!")
    outfile = open(outfilename,'w')

    # create new slha in memory
    slha_new_list = []
    lastblock = ""
    for line in open(slha): 
        if "BLOCK" in line:
            lastblock = line
        newline = line
        if "MASS" in lastblock:
            for particle,mass in masses.iteritems():
                if particle in line:
                    newline = "      %s     %s       # \n" % (particle, mass)
        slha_new_list.append(newline)
    slha_new = "".join(slha_new_list)

    in_slha = False
    in_ev = False
    nev=0
    for line in infile: 
        newline = line
        if "</slha>" in line:
            # add the new slha info before closing the tag
            newline = "".join([slha_new,line])
            in_slha = False
        if in_slha:
            # Do not write the line
            continue
        if "<slha>" in line:
            in_slha = True
        if in_ev and line.startswith("<"):
            newline = "%s\n%s" % (modeltag,line)
            in_ev = False
        outfile.write(newline)
        if "<event>" in line: 
            in_ev = True
        if "</event>" in line:
            nev += 1
        if nev == nevents:
            # We've reached the number of events we wanted
            # write out the end statement and stop
            outfile.write("</LesHouchesEvents>\n")
            break

    outfile.close()
    infile.close()


## ---------------------------------------------------------------------
##  Dictionary containing a number of pre-defined decay scenarios
## ---------------------------------------------------------------------
def get_decay_dict():
    decay_dict = {
        "LSP_stable" : "DECAY  1000022  0.0\n",
        "T1tttt" : "DECAY  1000021  1.0 \n   1.0  3  1000022 6 -6     # ~g -> ~chi_10 t tbar \n",
        "T1bbbb" : "DECAY  1000021  1.0 \n   1.0  3  1000022 5 -5     # ~g -> ~chi_10 b bbar \n",
        "T1qqqq" : ("DECAY  1000021  1.0 \n   0.25  3  1000022 1 -1     # ~g -> ~chi_10 d dbar \n" + 
                    "   0.25  3  1000022 2 -2     # ~g -> ~chi_10 u ubar \n"+ 
                    "   0.25  3  1000022 3 -3     # ~g -> ~chi_10 s sbar \n"+ 
                    "   0.25  3  1000022 4 -4     # ~g -> ~chi_10 c cbar \n"),
        "T2tt"   : "DECAY  1000006  0.1 \n   1.0  2  1000022 6      # t1 -> ~chi_10 t \n",
        "T2tt_3BD" : "DECAY  1000006  0.1 \n   1.0  3  1000022  5  24      # t1 -> ~chi_10 b W+ \n",
        "T2cc"   : "DECAY  1000006  0.1 \n   1.0  2  1000022 4      # t1 -> ~chi_10 c \n",
        "T2bb"   : "DECAY  1000005  0.1 \n   1.0  2  1000022 5      # b1 -> ~chi_10 b \n",
        "T2qq"   : ("DECAY  1000001  0.1 \n   1.0  2  1000022 1      # ul -> ~chi_10 u \n" + 
                    "DECAY  1000002  0.1 \n   1.0  2  1000022 2      # dl -> ~chi_10 d \n" + 
                    "DECAY  1000003  0.1 \n   1.0  2  1000022 3      # sl -> ~chi_10 s \n" + 
                    "DECAY  1000004  0.1 \n   1.0  2  1000022 4      # cl -> ~chi_10 c \n" + 
                    "DECAY  2000001  0.1 \n   1.0  2  1000022 1      # ur -> ~chi_10 u \n" + 
                    "DECAY  2000002  0.1 \n   1.0  2  1000022 2      # dr -> ~chi_10 d \n" + 
                    "DECAY  2000003  0.1 \n   1.0  2  1000022 3      # sr -> ~chi_10 s \n" + 
                    "DECAY  2000004  0.1 \n   1.0  2  1000022 4      # cr -> ~chi_10 c \n") 
        }

    return decay_dict


## ---------------------------------------------------------------------
##  Create a parser for the command line arguments
## ---------------------------------------------------------------------
def makeCLParser():
    parser = argparse.ArgumentParser(
        description="Built-in decay options are: \n %s"%(get_decay_dict().keys())
        )
    parser.add_argument("cfg",
                        metavar = "configfile",
                        help = "Config file to be used. See create_update_header_config.py for more details."
                        )
    parser.add_argument("--pdg",
                        type = int,
                        default = 1000021,
                        help = "PDG ID of mother particle (default: %(default)s)"
                        )
    parser.add_argument("--stableLSP",
                        action="store_true",
                        help = "Flag to add 'DECAY 1000022 0' to the lhe files. Only needed if original file does not have this line yet, and only used if you have chosen one of the built-in decay options."
                        )
    return parser

## ---------------------------------------------------------------------
##  Check validity of the config file
##  Exit the script if config is not valid
## ---------------------------------------------------------------------
def checkConfig(config):
    # Both sections need to be present
    sections = ['Global', 'SLHA']
    for section in sections:
        if not config.has_section(section):
            sys.exit("Invalid config file, section '%s' is missing"%(section))

    # All options in the global section need to be present
    options1 = ['name', 'nevents', 'inputdir', 'outputdir', 'model']
    for option in options1: 
        if not config.has_option('Global', option):
            sys.exit("Invalid config file, option %s in section 'Global' is missing"%(option))

    # In the SLHA section we need the mass option and one of the three 
    # decay options
    if not config.has_option('SLHA', 'mass'):
        sys.exit("Invalid config file, option 'mass' in section 'SLHA' is missing")
    options2 = ['slha', 'decay', 'decaystring']
    decay_present = [config.has_option('SLHA',option) for option in options2]
    if not (True in decay_present):
        sys.exit("Invalid config file, you need to specify at least one decay option")


## ---------------------------------------------------------------------
##  Main function to execute
## ---------------------------------------------------------------------
if __name__ == "__main__":

    # Parse the command line
    parser = makeCLParser()
    args = parser.parse_args()

    # Parse the config file and check the validity
    config = ConfigParser.SafeConfigParser()
    config.read(args.cfg)
    checkConfig(config)

    # extract some info from the config
    name = config.get('Global','name')
    nevents = config.getint('Global','nevents')

    # Get the path to all files in the inputdir that match the 'name'
    # provided in the config. Files can be zipped (.lhe.gz).
    fnames_to_process = glob.glob(config.get('Global','inputdir')+"/"+
                                  name+"*.lhe*")

    # Make the output directory if it doesn't exist
    outputdir = config.get('Global', 'outputdir')
    if not os.path.isdir(outputdir):
        os.makedirs(outputdir)

    # Get the dictionary that includes the mass information
    if not os.path.isfile(config.get('SLHA','mass')):
        sys.exit("The specified mass dictionary file does not exist.")
    mass = __import__(config.get('SLHA','mass').replace(".py",""))
    mass_keys = mass.mass_dict.keys()

    # Get the model name
    model = config.get('Global','model').strip()

    # Check how the decay should be done, via decay option, decay
    # string or full slha as input
    # Update the model name if it is empty
    if config.has_option('SLHA','slha') and config.get('SLHA','slha').strip():
        if not os.path.isfile(config.get('SLHA','slha')):
            sys.exit("You specified a SLHA file that doesn't exist")
        decay = "slha"
        if not model:
            model = "custom"
    elif config.has_option('SLHA','decaystring') and config.get('SLHA','decaystring').strip():
        decay = config.get('SLHA','decaystring').replace("\"","")
        if not model:
            model = "custom"
    elif config.has_option('SLHA','decay') and config.get('SLHA','decay').strip():
        decay_dict = get_decay_dict()
        decay = decay_dict[config.get('SLHA','decay')]
        if args.stableLSP:
            decay += decay_dict["LSP_stable"]
        if not model:
            model = config.get('SLHA','decay')
    else:
        sys.exit("No decay information specified.")

    print "Will decay according to", decay


    # Loop over all input files and process them accordingly
    for f in fnames_to_process:
        # Get the mother mass from the filename
        # Assumes naming scheme as in run_scan.py
        base_f = os.path.basename(f)
        parts = base_f.split("_")
        for pnum, p in enumerate(parts):
            if p==str(args.pdg) and pnum < len(parts)-1:
                mother_mass = parts[pnum+1]
                found_mother_mass = True
                break
        if not found_mother_mass: 
            print "Unknown filename format, moving to the next file"
            continue

        # Look up what to do for that mass
        if not mother_mass in mass_keys:
            print "No mass info found corresponding to file", f, ", moving on..."
            continue
        else: 
            info = mass.mass_dict[mother_mass]
            # for each element in the info list, we need to create an output file
            for option in info:
                # construct output filename
                option_string = "__".join("%s_%s"%(key,val) for key,val in option.iteritems())
                out_f = base_f.replace("undecayed",
                                       "_".join(["decayed",option_string])
                                       ).replace(name,model).replace(".gz","")
                # construct the model tag to be inserted
                mass_string = "_".join("%s" % (val) for val in option.values())
                model_tag = "# model %s_%s_%s" % (model, mother_mass, mass_string)
                # Process the LHE file
                if decay != "slha":
                    process_lhe(f, 
                                os.path.join(outputdir,out_f), 
                                option, 
                                decay,
                                nevents,
                                model_tag)
                else:
                    process_lhe_with_slha(f, 
                                          os.path.join(outputdir,out_f),
                                          config.get('SLHA','slha'),
                                          option,
                                          nevents,
                                          model_tag)


