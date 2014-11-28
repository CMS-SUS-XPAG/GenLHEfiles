#####################################################################
##                                                                 ##
## File:        run_scan.py                                        ##
##                                                                 ##
## Description: submission script for SUSY scans in Run2.          ##
##                                                                 ##
##   This script will produce a set of jobs that will be submitted ##
##   to a batch server, e.g. lxbatch.                              ##
##   For now only one particle mass can be changed per run. This   ##
##   means that only pair production of sparticles, without        ##
##   consequent decays, is currently supported.                    ##
##                                                                 ## 
## Supported options:                                              ## 
##   --name            Process name. Cards should be appropriately ##
##                     named, e.g. <name>_run_card.dat             ## 
##   --pdg             PDG id of particle to be produced           ## 
##   --mass            White space separated list of masses to     ## 
##                     produce events for                          ## 
##   --massrange       Mass range to produce events for            ## 
##                     Format: MIN MAX STEP                        ## 
##   -n, --nevents     Number of events to produce per run         ## 
##   -nruns            Number of runs                              ## 
##   -ncores           Number of cores to use for event generation ## 
##   -protocol         Submission protocol: bsub or qsub           ## 
##   -q, --queue       Queue to submit to                          ## 
##   --nosubmit        Flag to turn of submission, job scripts are ## 
##                     still created                               ## 
##                                                                 ##
## Author:   Nadja Strobbe                                         ##
## Created:  2014-11-27                                            ##
## Updated:  ...                                                   ##
##                                                                 ##
#####################################################################

import os, sys, subprocess
import argparse
import numpy as np
from datetime import datetime
from itertools import izip

# -----------------------------------------------------------------
# Command Line Parser
# -----------------------------------------------------------------
def makeCLParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name",
                        default = "gluino",
                        help = "Name for the process (default: %(default)s). Cards should be named <name>_run_card.dat, etc. "
                        )
    parser.add_argument("-n", "--nevents",
                        type = int,
                        default = 10000,
                        help = "Number of events per job (default: %(default)s)"
                        )
    parser.add_argument("--nruns",
                        type = int,
                        default = 1,
                        help = "Number of runs (default: %(default)s)"
                        )
    parser.add_argument("--ncores",
                        type = int,
                        default = 1,
                        help = "Number of cores to run with (default: %(default)s)"
                        )
    parser.add_argument("--protocol",
                        choices = ["bsub", "qsub"],
                        default = "bsub",
                        help = "Submission protocol (default: %(default)s)"
                        )
    parser.add_argument("-q", "--queue",
                        default = "1nd",
                        help = "Queue name (default: %(default)s)"
                        )
    parser.add_argument("--nosubmit",
                        action = 'store_true',
                        help = "Do not submit the jobs"
                        )
    parser.add_argument("--pdg",
                        type = int,
                        default = 1000021,
                        help = "PDG ID of particle to be produced (default: %(default)s)"
                        )
    mass_group = parser.add_mutually_exclusive_group()
    mass_group.add_argument("--mass",
                            type=float,
                            nargs = '*',
                            default = 1000,
                            help="Mass of particle to be produced. Can be a single value or a whitespace separated list (default: %(default)s)."
                            )
    mass_group.add_argument("--massrange",
                            type=float,
                            nargs = 3,
                            help="Define a range of masses to be produced. Format: min max step. Max is not included in the range.",
                            metavar = ('MIN', 'MAX', 'STEP')
                            )
    return parser

# -----------------------------------------------------------------
# Print out used options
# -----------------------------------------------------------------
def print_configuration(args_dict):
    # open a file with timestamp
    configfile = open("run_scan_%s.log" % (datetime.now().strftime('%Y%m%d_%H%M%S')),'w')
    for k,v in args_dict.iteritems():
        configfile.write("%s = %s \n" %(k,v) )
    configfile.close()

# -----------------------------------------------------------------
# Create job script
# -----------------------------------------------------------------
def makejob(HOMEDIR, PROCNAME, OUTPUT, NEV, NRUN, NCORES, PDGID, MASS, SEED):
    # Open a script which will be submitted
    jobname = HOMEDIR+"/scripts/"+PROCNAME+"__"
    for pdg,mass in izip(PDGID,MASS):
        jobname = jobname + str(pdg) + "_" + str(mass) + "__"
    jobname = jobname + str(NRUN)+".sh"
    #jobname = HOMEDIR+"/scripts/"+PROCNAME+"__"+str(PDGID)+"_"+str(MASS)+"__"+str(NRUN)+".sh"
    myjob = open(jobname,'w')
    myjob.write("#!/bin/bash \n")

    # Create a rundirectory
    myjob.write("mkdir run_SUSY; cd run_SUSY \n")

    # Copy over the needed files
    myjob.write("cp -r %s/patches . \n" % (HOMEDIR) )
    myjob.write("cp %s/SUSY_generation.sh . \n" % (HOMEDIR) )
    myjob.write("mkdir cards \n")
    myjob.write("cp %s/cards/%s_proc_card.dat cards/ \n" % (HOMEDIR, PROCNAME) )
    myjob.write("cp %s/cards/%s_run_card.dat cards/ \n" % (HOMEDIR, PROCNAME) )
    myjob.write("cp %s/cards/%s_param_card.dat cards/ \n" % (HOMEDIR, PROCNAME) )

    # Create the customization script from the template
    myjob.write("echo set run_card nevents %s > cards/%s_customizecards.dat \n" % (NEV, PROCNAME) )
    myjob.write("echo set run_card seed %s > cards/%s_customizecards.dat \n" % (SEED, PROCNAME) )
    for pdg,mass in izip(PDGID, MASS):
        myjob.write("echo set param_card mass %s %s >> cards/%s_customizecards.dat \n" % (pdg, mass, PROCNAME) )

    # Run the actual LHE generation
    myjob.write("./SUSY_generation.sh %s %s \n" % (PROCNAME, NCORES) )

    # Copy back the output
    myjob.write("cp %s/%s_unweighted_events.lhe.gz %s \n" % (PROCNAME, PROCNAME, OUTPUT) )

    # Clean up the area
    myjob.write("cd .. \n")
    myjob.write("rm -r run_SUSY \n")

    myjob.close()

    # make job executable
    os.chmod(jobname,0755)

    return jobname

# -----------------------------------------------------------------
# Submit a job
# -----------------------------------------------------------------
def submitjob(QUEUE, JOBNAME, HOMEDIR, PROTOCOL, NCORES):
    # location to store error and log files
    errorfile = HOMEDIR + "/log/" + JOBNAME.split("/")[-1].replace(".sh",".err")
    logfile = HOMEDIR + "/log/" + JOBNAME.split("/")[-1].replace(".sh",".log")
    # submit the job based on the specified protocol
    if PROTOCOL == "bsub":
        submitcommand = ["bsub",
                         "-q %s" % (QUEUE),
                         "-e %s" % (errorfile),
                         "-o %s" % (logfile)] 
        if NCORES > 1:
            submitcommand.extend(["-n %s" % (NCORES),
                                  "-R span[hosts=1]"])
        submitcommand.append(JOBNAME)
        print ' '.join(submitcommand)
        subprocess.call(' '.join(submitcommand) , shell=True)

    elif PROTOCOL == "qsub": 
        submitcommand = ["qsub",
                         "-q %s" % (QUEUE),
                         "-e %s" % (errorfile),
                         "-o %s" % (logfile),
                         JOBNAME] 
        print ' '.join(submitcommand)
        subprocess.call(' '.join(submitcommand), shell=True)

    else: 
        print "Unsupported submission protocol."


# -----------------------------------------------------------------

if __name__ == "__main__": 

    # Parse the command line arguments and print them for provenance
    parser = makeCLParser()
    args = parser.parse_args()
    print_configuration(vars(args))

    # Store the current working directory
    HOMEDIR = os.getcwd()

    # Make a folder to store the scripts
    if not os.path.isdir("scripts"):
        os.mkdir(HOMEDIR+"/scripts")

    # Make a folder to store the output
    if not os.path.isdir("lhe"):
        os.mkdir(HOMEDIR+"/lhe")

    # Make a folder to store the log files
    if not os.path.isdir("log"):
        os.mkdir(HOMEDIR+"/log")

    # The SUSY_generation.sh script needs to be in the working directory
    if not os.path.isfile("SUSY_generation.sh"): 
        sys.exit("SUSY_generation.sh is not in the current working directory!")

    # A cards directory with three cards must exist, otherwise the jobs will crash
    if not os.path.isdir("cards"): 
        sys.exit("There is no directory 'cards' in the current working directory!")
    else: 
        print "Checking if all three cards are there"
        if not os.path.isfile("cards/%s_run_card.dat" % (args.name)):
            sys.exit("There is no run card with name %s_run_card.dat" % (args.name))
        if not os.path.isfile("cards/%s_param_card.dat" % (args.name)):
            sys.exit("There is no param card with name %s_param_card.dat" % (args.name))
        if not os.path.isfile("cards/%s_proc_card.dat" % (args.name)):
            sys.exit("There is no proc card with name %s_proc_card.dat" % (args.name))
        print "    OK"

    # The patches directory must exist, otherwise the jobs will crash
    if not os.path.isdir("patches"): 
        os.mkdir(HOMEDIR+"/patches")
    if not (os.path.isfile("patches/mgfixes.patch") and os.path.isfile("patches/models.patch")):
        print "Will download missing patches"
        os.chdir("patches")
        c1 = "https://raw.githubusercontent.com/cms-sw/genproductions/master/bin/MadGraph5_aMCatNLO/patches/mgfixes.patch"
        subprocess.check_call(["wget",c1])
        c2 = "https://raw.githubusercontent.com/cms-sw/genproductions/master/bin/MadGraph5_aMCatNLO/patches/models.patch"
        subprocess.check_call(["wget",c2])
        os.chdir(HOMEDIR)
        print "    OK"

    # Deal with number of cores for qsub protocol
    ncores = args.ncores
    if args.protocol == "qsub":
        ncores = 1

    # Parse the mass-related arguments to create the jobs
    # Store jobnames for submission
    jobnames = []
    # Make sure to change the random seed between runs. 
    # Will just change it for every mass-run combo
    seed = 1
    if args.massrange != None:
        # A mass range was provided, create a job for each mass point in the range
        MIN, MAX, STEP = args.massrange
        print "Will create jobs for the mass range [%s,%s[ with step %s" % (MIN, MAX, STEP)
        for mass in np.arange(MIN, MAX, STEP):
            for nrun in xrange(args.nruns):
                procname = args.name 
                output = HOMEDIR + "/lhe/" + procname + str(mass) + "_" + str(nrun) + "_undecayed.lhe.gz"
                jobnames.append(makejob(HOMEDIR, 
                                        procname, 
                                        output, 
                                        args.nevents, 
                                        nrun, 
                                        ncores, 
                                        [args.pdg], 
                                        [mass], seed)
                                )
                seed = seed + 1
    else: 
        # List of masses was provided
        print "Will create jobs for masses", args.mass
        if type(args.mass) is int:
            args.mass = [args.mass]
        for mass in args.mass:
            for nrun in xrange(args.nruns):
                procname = args.name 
                output = HOMEDIR + "/lhe/" + procname + str(mass) + "_" + str(nrun) + "_undecayed.lhe.gz"
                jobnames.append(makejob(HOMEDIR, 
                                        procname, 
                                        output, 
                                        args.nevents, 
                                        nrun, 
                                        ncores, 
                                        [args.pdg], 
                                        [mass], 
                                        seed)
                                )
                seed = seed + 1

    print "Done creating job scripts."

    # Now submit the jobs if desired
    if not args.nosubmit:
        for job in jobnames:
            submitjob(args.queue, job, HOMEDIR, args.protocol, ncores)
        print "Submitted all jobs."
