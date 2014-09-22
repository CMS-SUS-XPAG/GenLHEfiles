# Run the decay for a list of files
import os, glob, sys
from optparse import OptionParser

def doDecay(cfgname, outfilename):
    basename = cfgname.split("/")[-1].split(".")[0]
    command = "./main20.exe %s %s > logs/%s.log" % (cfgname, outfilename, basename)
    print command
    os.system(command)

def makeCfg(cfgname, inputfilename, nevents):
    f = open(cfgname,'w')
    t = open("template.cmnd")
    tlines = t.readlines()
    for l in tlines:
        newline = l
        if "INFILE" in l:
            newline = l.replace("INFILE",inputfilename)
        if "NEVENTS" in l:
            newline = l.replace("NEVENTS",str(nevents))
        f.write(newline)
    f.close()
    t.close()

if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("-d", "--dir", dest="undecayed_dir", default="/afs/cern.ch/work/n/nstrobbe/LHE/13TeV/OUTPUT/Undecayed_processed",
                      help="location of undecayed LHE files")
    parser.add_option("-n", "--nevents", dest="nevents", default=100000,
                      help="number of events to decay")

    (options, args) = parser.parse_args()
    
    # select all the files you want to decay
    # These files need to have the proper SLHA block in the header 
    # It is also assumed that the string "undecayed" is part of the name
    files_to_run = glob.glob(options.undecayed_dir+"/*.lhe")

    # make some directories to keep things organized
    if not os.path.isdir("logs"):
        os.mkdir("logs")
    if not os.path.isdir("cfgs"):
        os.mkdir("cfgs")
    if not os.path.isdir("results"):
        os.mkdir("results")

    for f in files_to_run: 
        print "Will run decay for file", f
        basename = f.split("/")[-1].split(".")[0]

        print "\tMaking config file"
        cfgname = "cfgs/decay_"+basename+".cmnd"
        makeCfg(cfgname,f,options.nevents)

        print "\tDoing decay"
        doDecay(cfgname, "results/"+basename.replace("undecayed","decayed")+".lhe")
