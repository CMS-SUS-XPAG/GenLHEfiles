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
##   --massdict        Python file with dictionary containing      ##
##                     mass information and pdg ids                ##
##   -n, --nevents     Number of events to produce per run         ##
##   -nruns            Number of runs                              ##
##   -ncores           Number of cores to use for event generation ##
##   -protocol         Submission protocol: bsub, qsub, condor     ##
##   -q, --queue       Queue to submit to                          ##
##   --nosubmit        Flag to turn off submission, job scripts    ##
##                     are still created                           ##
##   -o, --output      Output directory for LHE file               ##
##                                                                 ##
## Author:   Nadja Strobbe                                         ##
## Created:  2014-11-27                                            ##
## Updated:  2015-03-12  Add Condor option and reorganize          ##
##                       (Kevin Pedro)                             ##
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
                        choices = ["bsub", "qsub", "condor"],
                        default = "bsub",
                        help = "Submission protocol (default: %(default)s)"
                        )
    parser.add_argument("-o","--output",
                        default = "",
                        help = "Directory for output LHE file (optional for lxbatch, necessary for condor)"
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
    mass_group.add_argument("--massdict",
                            help = "Dictionary containing mass information and pdg ids"
                            )
    return parser

# -----------------------------------------------------------------
# Print out used options
# -----------------------------------------------------------------
def print_configuration(args_dict):
    # open a file with timestamp
    configfile = open("logs/run_scan_%s.log" % (datetime.now().strftime('%Y%m%d_%H%M%S')),'w')
    for k,v in args_dict.iteritems():
        configfile.write("%s = %s \n" %(k,v) )
    configfile.close()

# -----------------------------------------------------------------
# Create customize card
# -----------------------------------------------------------------

def makecustom(PROCNAME, NEV, NRUN, PDGID, MASS, SEED):
    # Open a script which will be submitted
    customname = PROCNAME+"__"
    for pdg,mass in izip(PDGID,MASS):
        customname = customname + str(pdg) + "_" + str(mass) + "__"
    customname = customname + "n" + str(NEV) + "_p" + str(NRUN)
    mycustom = open("cards/" + customname + "_customizecards.dat",'w')

    # Create the customization script from the template
    mycustom.write("set run_card nevents %s\n" % (NEV) )
    mycustom.write("set run_card iseed %s\n" % (SEED) )
    for pdg,mass in izip(PDGID, MASS):
        mycustom.write("set param_card mass %s %s\n" % (pdg, mass) )

    mycustom.close()

    return customname
    
# -----------------------------------------------------------------
# Create job script
# -----------------------------------------------------------------
def makejob(PROTOCOL, RUNDIR, CMSSWBASE, CMSSWVER, PROCNAME, OUTDIR, NEV, NRUN, PDGID, MASS, SEED):
    jobprefix = ""
    jobsuffix = ""
    
    # get template scripts
    if PROTOCOL == "condor":
        jobprefix = "jobExecCondor"
        jobsuffix = ".jdl"
    elif PROTOCOL == "bsub" or PROTOCOL == "qsub":
        jobprefix = "jobExecLXbatch"
        jobsuffix = ".sh"
    
    # generate customization card for this job
    customname = makecustom(PROCNAME, NEV, NRUN, PDGID, MASS, SEED)
    
    jobname = jobprefix+"_"+customname+jobsuffix
    # these initial commands are common to condor and lxbatch
    jobcmd = "cat "+jobprefix+jobsuffix+" | sed -e s/CUSTOMCARD/"+customname+"/ | sed -e s/CMSSWVER/"+CMSSWVER+"/ | sed -e s~OUTDIR~"+OUTDIR+"~ | sed -e s/PROCNAME/"+PROCNAME+"/"
    # lxbatch needs some extra directory info because it doesn't use the CMSSW tarball
    if PROTOCOL == "bsub" or PROTOCOL == "qsub":
        jobcmd = jobcmd+" | sed -e s~CMSDIR~"+CMSSWBASE+"~ | sed -e s~RUNDIR~"+RUNDIR+"~"
    # now write to job file in scripts dir
    jobcmd = jobcmd+" > scripts/"+jobname
    print jobcmd
    
    # execute command to create job file
    os.system(jobcmd)
    
    # make job executable
    if PROTOCOL == "bsub" or PROTOCOL == "qsub":
        os.chmod("scripts/"+jobname,0755)
    
    return jobname    

# -----------------------------------------------------------------
# Submit a job
# -----------------------------------------------------------------
def submitjob(QUEUE, JOBNAME, RUNDIR, PROTOCOL, NCORES):
    # location to store error and log files
    errorfile = RUNDIR + "/log/" + JOBNAME.split("/")[-1].replace(".sh",".err")
    logfile = RUNDIR + "/log/" + JOBNAME.split("/")[-1].replace(".sh",".log")
    # submit the job based on the specified protocol
    submitcommand = ""
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

    elif PROTOCOL == "qsub": 
        submitcommand = ["qsub",
                         "-q %s" % (QUEUE),
                         "-e %s" % (errorfile),
                         "-o %s" % (logfile),
                         JOBNAME] 
        print ' '.join(submitcommand)
        
    elif PROTOCOL == "condor":
        submitcommand = ["condor_submit", JOBNAME]
        print ' '.join(submitcommand)

    else: 
        print "Unsupported submission protocol."
        return
        
    subprocess.call(' '.join(submitcommand), shell=True) 


# -----------------------------------------------------------------

if __name__ == "__main__": 

    # Parse the command line arguments and print them for provenance
    parser = makeCLParser()
    args = parser.parse_args()

    # Make a folder to store the log files
    if not os.path.isdir("logs"):
        os.mkdir(RUNDIR+"/logs")

    print_configuration(vars(args))

    # get some info from the OS
    CMSSWVER = os.getenv("CMSSW_VERSION")
    CMSSWBASE = os.getenv("CMSSW_BASE")
    RUNDIR = os.getcwd()

    # Make a folder to store the output
    if not os.path.isdir("lhe"):
        os.mkdir(RUNDIR+"/lhe")

    # The SUSY_generation.sh script needs to be in the current directory
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

    # Check the output directory specification
    if not args.output:
        if args.protocol == "qsub" or args.protocol == "bsub":
            args.output = RUNDIR+"/lhe"
        elif args.protocol == "condor":
            # output directory must be specified for condor
            sys.exit("No output directory specified for condor submission: quitting")

    # todo: check condor output for xrootd?

    # Deal with number of cores for qsub or condor protocols
    ncores = args.ncores
    if args.protocol == "qsub" or args.protocol == "condor":
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
                jobnames.append(makejob(args.protocol,
                                        RUNDIR,
                                        CMSSWBASE,
                                        CMSSWVER,
                                        procname, 
                                        args.output, 
                                        args.nevents, 
                                        nrun, 
                                        [args.pdg], 
                                        [mass], 
                                        seed)
                                )
                seed = seed + 1
    elif args.massdict != None:
        # A mass dictionary was provided
        print  "Will create jobs according to", args.massdict
        masslist = __import__(args.massdict.replace(".py",""))
        for massdict in masslist.masses:
            pdgs = []
            masses = []
            infostring = []
            for k, v in massdict.iteritems():
                pdgs.append(k)
                masses.append(v)
                infostring.append("%s_%s"%(k,v))
            procname = args.name 
            for nrun in xrange(args.nruns):
                jobnames.append(makejob(args.protocol,
                                        RUNDIR,
                                        CMSSWBASE,
                                        CMSSWVER, 
                                        procname, 
                                        args.output, 
                                        args.nevents, 
                                        nrun, 
                                        pdgs, 
                                        masses, 
                                        seed)
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
                jobnames.append(makejob(args.protocol,
                                        RUNDIR,
                                        CMSSWBASE,
                                        CMSSWVER, 
                                        procname, 
                                        args.output, 
                                        args.nevents, 
                                        nrun, 
                                        [args.pdg], 
                                        [mass], 
                                        seed)
                                )
                seed = seed + 1

    print "Done creating job scripts."
    
    # check for grid proxy for condor (necessary to xrdcp output to eos), then:
    # (re)generate CMSSW tarball for condor, after makejob so customize cards are made
    # exclude scripts, logs, lhe directories that get filled up with job submission files
    # but include cards, which are necessary to run
    # change to directory above CMSSW_BASE and tar CMSSW_BASE to get desired directory structure
    if args.protocol == "condor":
        try:
            proxy = subprocess.check_output("voms-proxy-info --all",shell=True)
        except subprocess.CalledProcessError:
            sys.exit("Grid proxy is necessary for LPC Condor. Call:\nvoms-proxy-init -voms cms\nand try again.")
    
        # need relative directory for excludes because of directory change in tar command
        RELDIR = CMSSWVER + RUNDIR.split(CMSSWVER)[-1]
        os.system("tar --exclude="+RELDIR+"/logs --exclude="+RELDIR+"/scripts --exclude="+RELDIR+"/lhe* -zcf scripts/"+CMSSWVER+".tar.gz -C "+CMSSWBASE+"/.. "+CMSSWVER)
    
    # Now submit the jobs if desired
    if not args.nosubmit:
        os.chdir("scripts")
        for job in jobnames:
            submitjob(args.queue, job, RUNDIR, args.protocol, ncores)
        print "Submitted all jobs."
        os.chdir("..")
