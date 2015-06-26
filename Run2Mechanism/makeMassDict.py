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
    to_print = "mass_dict = { \"%%.1f\"%%(x) : ([ {'1000022': mass if mass!=0 else 1} for mass in range(0,x,%s) ]) for x in %s } \n" % (
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
    to_print = "mass_dict = { \"%%.1f\"%%(x) : ([ {%(var_pdg)s : mass if mass!=0 else 1, %(fixed_pdg)s : %(fixed_mass)s} for mass in range(%(var_min)s,min(%(var_max)s,int(x)),%(var_step)s) ]) for x in %(mother_masses)s } \n" % locals()

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
    to_print = "mass_dict = { \"%%.1f\"%%(x) : ([ {%(var_pdg)s : mass if mass!=0 else 1, %(fixed_pdg)s : mass+%(fixed_mass_diff)s} for mass in range(%(var_min)s,min(%(var_max)s,int(x)),%(var_step)s) ]) for x in %(mother_masses)s } \n" % locals()

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
    to_print = "mass_dict = { \"%%.1f\"%%(x) : ([ {%(var_pdg)s : mass if mass!=0 else 1, %(fixed_pdg)s : x*%(fixed_x_value)s+(1-%(fixed_x_value)s)*mass} for mass in range(%(var_min)s,min(%(var_max)s,int(x)),%(var_step)s) ]) for x in %(mother_masses)s } \n" % locals()

    with open(fname, 'w') as mdict:
        mdict.write(to_print)
