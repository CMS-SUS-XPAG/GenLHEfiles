# We need to add the model tag and the clustering information to each event
# We also insert a minimal header
import glob, os

def returnModelTag(fname, model):
    # this will work for filenames of the form
    # <model>_<mother>_<mothermass>_<LSP>_<LSPmass>_<other stuff, can include '_">
    # if your filename does not follow this convention, you will need to modify this function
    basename = fname.split("/")[-1].split(".")[0]
    parts = basename.split("_")
    tag = "# model %s_%s_%s" % (model, parts[2], parts[4])
    return tag

def returnOriginalLHEfilename(fname):
    # example of decayed filename: T1bbbb_gluino_1000_LSP_900_decayed_1.lhe
    # example of original undecayed filename: T1bbbb_gluino_1000_LSP_900_undecayed_1.lhe
    basename = fname.split("/")[-1]
    orig = basename.replace("decayed","undecayed")
    return orig

def add_info_to_LHE(outputdir,undecayed,decayed,modeltag,header):
    # function to add hashtags to the events
    # based on script from Alexis

    # Get the clustering info from the original undecayed file
    cluster_info = []
    f=open(undecayed,"r")
    lines=f.readlines()
    prev_line=-1
    for line in lines:
        if "</event>" in str(line):
            if prev_line != -1:
                cluster_info.append(lines[prev_line])
            else:
                print "</event> found in first line, something is wrong!"
        prev_line = prev_line+1
    f.close()

    # Put the clustering info in the decayed file
    b=0
    destination = open(outputdir+"/"+decayed.split("/")[-1].replace(".lhe","_final.lhe"),"w")
    source = open(decayed,"r")
    for line in source:
        # ignore the lines that pythia8 added
        if "pdf" in line: 
            continue 
        # if at init, put the header
        if "<init>" in line: 
            destination.write(header)
        # if at end of event, put the clustering info
        if "</event>" in str(line):
            destination.write(cluster_info[b])
            destination.write(modeltag.strip()+"\n")
            b=b+1
        destination.write(line)
    source.close()
    destination.close()
                                                                          
if __name__ == "__main__":
    
    # Name of the model, needed for the model tag that will be inserted into each event
    model = "T2qq"
    
    # Pick up the header file to use
    # Note that this is only needed if the files will go through official production
    headerfile = open("header_"+model)
    header = headerfile.read()

    # decayed files we want to process
    files_to_process = glob.glob("Decayed/"+model+"/*.lhe")

    # where to put the postprocessed files
    outputdir = "Decayed_postprocessed/"+model
    if not os.path.isdir(outputdir):
        os.makedirs(outputdir)
    
    # Process each file
    for f in files_to_process: 
        # construct model tag 
        # it will pick up the model name and find the mass information from the filename
        # please check the code for returnModelTag if it suits your filename convention
        tag = returnModelTag(f,model)
        print tag
        
        # specify original LHE file
        # This needs to be the unzipped original file from Madgraph, before doing the decay
        # It does not matter whether it already has the full SLHA information in it
        orig_lhe = "Undecayed_processed/" + returnOriginalLHEfilename(f)
        print orig_lhe

        # add the header and comment lines to the LHE file
        add_info_to_LHE(outputdir,orig_lhe,f,tag,header)
