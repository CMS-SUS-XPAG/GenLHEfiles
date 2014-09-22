# Before running the decay step, we need to make sure the SLHA is properly included in the header of the LHE files

import sys

def process_lhe(infilename, outfilename, masses_to_replace, decay_info):
    infile = open(infilename)
    infile_lines = infile.readlines()

    outfile = open(outfilename,'w')
    lastblock = ""
    for l in infile_lines: 
        if "BLOCK" in l:
            lastblock = l
        newline = l
        if "MASS" in lastblock:
            for particle,mass,comment in masses_to_replace:
                if particle in l:
                    newline = "   %s     %s       #%s \n" % (particle, mass, comment)
        if "</slha>" in l:
            # add the DECAY before closing the tag
            # check whether decay_info ends in \n
            if decay_info.strip(" ")[-1:] == "\n":
                newline = decay_info
            else: 
                newline = decay_info+"\n"
            newline = newline + l
        outfile.write(newline)

    outfile.close()
    infile.close()

if __name__ == "__main__":

    # location of the undecayed, unprocessed files. 
    # The files should not be zipped. 
    inputdir = "Undecayed_processed/input/"

    # Which sparticle you want to decay. 
    # In my setup this is part of the name of the undecayed file; so it might not be necessary for you
    particle = "squark" # "stop", "gluino", "sbottom"
    
    # Name of the model you want to generate. This will go in the name of the output file
    model = "T2qq" # "T2tt", "T1tttt", ...

    # Make a list of all the undecayed files you want to process
    # This will need customizing depending on your needs
    # Here I want to decay a few files for a few mass points
    fnames_to_process = []
    basename = particle+"_MASS_xqcut30_NR.lhe" # template name of the undecayed file
    masses = [1200] # all masses you want to process
    nrs = [1] # in case you generated multiple files for the same mass and gave them a number
    for mass in masses:
        for nr in nrs:
            # build up the exact name of the undecayed file(s) you want to process
            name = basename.replace("MASS",str(mass)).replace("NR",str(nr))
            fnames_to_process.append(name)

    # You will also need to specify the masses for the sparticles in the decay chain
    # Depending on the length of the desired decay chain, you will need to add more lists here
    lsp_masses = [100] # all LSP masses needed for the decay

    # location of the output directory
    outputdir = "Undecayed_processed/"

    # Build up list with all the filenames for the output files
    fnames_output = []
    basename2 = "MODEL_"+particle+"_MASS_LSP_mass_xqcut30_NR.lhe"
    for i,mass in enumerate(masses):
        for nr in nrs:
            name = basename2.replace("MASS",str(mass)).replace("NR",str(nr))
            name = name.replace("MODEL",model)
            name = name.replace("mass",str(lsp_masses[i]))
            fnames_output.append(name)

    # Build a list containing for each files the masses that will have to be replaced
    list_masses_to_replace = []
    for i,mass in enumerate(masses):
        for nr in nrs:
            # append a list of tuples, one tuple for each mass to be replaced
            # the tuple should have three entries: the pdg id, the mass, and a comment about which particle it is (can be empty string)
            list_masses_to_replace.append([("1000022",lsp_masses[i]," ~chi_10")])

    # Examples for the DECAY block
    # Use these or build your own
    # Note that you always need to specify that the LSP should be stable
    LSP_stable = "DECAY  1000022  0.0\n"
    T1tttt_decay = "DECAY  1000021  1.0 \n   1.0  3  1000022 6 -6     # ~g -> ~chi_10 t tbar \n" + LSP_stable
    T1bbbb_decay = "DECAY  1000021  1.0 \n   1.0  3  1000022 5 -5     # ~g -> ~chi_10 b bbar \n" + LSP_stable
    T1qqqq_decay = "DECAY  1000021  1.0 \n   0.25  3  1000022 1 -1     # ~g -> ~chi_10 d dbar \n   0.25  3  1000022 2 -2     # ~g -> ~chi_10 u ubar \n   0.25  3  1000022 3 -3     # ~g -> ~chi_10 s sbar \n   0.25  3  1000022 4 -4     # ~g -> ~chi_10 c cbar \n" + LSP_stable
    T2tt_decay = "DECAY  1000006  0.1 \n   1.0  2  1000022 6      # t1 -> ~chi_10 t \n" + LSP_stable
    T2tt_decay_offshell = "DECAY  1000006  0.1 \n   1.0  3  1000022  5  24      # t1 -> ~chi_10 b W+ \n" + LSP_stable
    T2bb_decay = "DECAY  1000005  0.1 \n   1.0  2  1000022 5      # b1 -> ~chi_10 b \n" + LSP_stable
    T2qq_decay = "DECAY  1000001  0.1 \n   1.0  2  1000022 1      # ul -> ~chi_10 u \n" + \
        "DECAY  1000002  0.1 \n   1.0  2  1000022 2      # dl -> ~chi_10 d \n" + \
        "DECAY  1000003  0.1 \n   1.0  2  1000022 3      # sl -> ~chi_10 s \n" + \
        "DECAY  1000004  0.1 \n   1.0  2  1000022 4      # cl -> ~chi_10 c \n" + \
        "DECAY  2000001  0.1 \n   1.0  2  1000022 1      # ur -> ~chi_10 u \n" + \
        "DECAY  2000002  0.1 \n   1.0  2  1000022 2      # dr -> ~chi_10 d \n" + \
        "DECAY  2000003  0.1 \n   1.0  2  1000022 3      # sr -> ~chi_10 s \n" + \
        "DECAY  2000004  0.1 \n   1.0  2  1000022 4      # cr -> ~chi_10 c \n" + \
        LSP_stable

    # specify the decay you want to use for each file you want to process
    list_decay = []
    for i in range(len(fnames_output)):
        list_decay.append(T2qq_decay)

    # Do the actual processing
    # process_lhe(...) takes four inputs:
    #    1. full path to file to be processed
    #    2. full path to desired outputfile
    #    3. a list containing the info needed to replace the mass of a sparticle in the SLHA table
    #    4. a string containing the DECAY block
    for i in range(len(fnames_to_process)):
        print "Processing", fnames_to_process[i]
        process_lhe(inputdir+fnames_to_process[i], outputdir+fnames_output[i], list_masses_to_replace[i], list_decay[i])
