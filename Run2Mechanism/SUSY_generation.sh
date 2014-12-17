#!/bin/bash

###########################################################################################
# GENERAL INSTRUCTIONS:                                                                   #
# You should take care of having the following ingredients in order to have this recipe   #
# working: param card, run card and proc card (in a "cards" folder), MadGraph release,    #
# this script, all in the same folder!                                                    #
# Important: Unlike for SM production, the param card also needs to be provided to        #
# generate the appropriate SUSY spectrum                                                  #
###########################################################################################

###########################################################################################
#DISCLAIMER:                                                                              #
# This script has been tested in CMSSW_6_2_11 on slc6 and there is no guarantee it should #
# work in another release.                                                                #
# To try in another releases you should adapt it taking into account to put the correct   #
# parameters as the architechture, the release names and compatibility issues as decribed #
# in the comments in this script                                                          #
# Additionally, this script depends on the well behaviour of the lxplus machines, so if   #
# one job fails the full set of jobs will fail and then you have to try again             #
# Any issues should be addressed to: cms-madgraph-support-team_at_cernSPAMNOT.ch          #
###########################################################################################

###########################################################################################
# For runnning, the following command should be used                                      #
# bash create_gridpack_template.sh NAME_OF_PRODUCTION QUEUE_SELECTION                     #
# Or you can make this script as an executable and the launch it with                     #
# chmod +x create_gridpack_template.sh                                                    #
# ./create_gridpack_template.sh NAME_OF_PRODUCTION QUEUE_SELECTION                        #
# by NAME_OF_PRODUCTION you should use the names of run and proc card                     #
# for example if the cards are bb_100_250_proc_card_mg5.dat and bb_100_250_run_card.dat   #
# NAME_OF_PRODUCTION should be bb_100_250                                                 #
# for QUEUE_SELECTION is commonly used 1nd, but you can take another choice from bqueues  #
# If QUEUE_SELECTION is omitted, then run on local machine only (using multiple cores)    #
###########################################################################################

#set -o verbose

echo "Starting job on " `date` #Only to display the starting of production date
echo "Running on " `uname -a` #Only to display the machine where the job is running
echo "System release " `cat /etc/redhat-release` #And the system release

#First you need to set couple of settings:

# name of the run
name=${1}

# Number of cores to use while running
ncores=$2

#________________________________________
# to be set for user specific
# Release to be used to define the environment and the compiler needed

#For correct running you should place at least the run and proc card in a folder under the name "cards" in the same folder where you are going to run the script

export PRODHOME=`pwd`
# the folder where the script works, I guess
AFS_GEN_FOLDER=${PRODHOME}/${name}
# where to search for datacards, that have to follow a naming code: 
#   ${name}_proc_card_mg5.dat
#   ${name}_run_card.dat
CARDSDIR=${PRODHOME}/cards
# where to find the madgraph tarred distribution
MGDIR=${PRODHOME}/

MGBASEDIR=mgbasedir

MG=MG5_aMC_v2.2.1.tar.gz
MGSOURCE=https://cms-project-generators.web.cern.ch/cms-project-generators/$MG

SYSCALC=SysCalc_V1.1.0.tar.gz
SYSCALCSOURCE=https://cms-project-generators.web.cern.ch/cms-project-generators/$SYSCALC

MGBASEDIRORIG=MG5_aMC_v2_2_1


#######################################
# If the work area doesn't exist yet: #
#######################################
if [ ! -d ${AFS_GEN_FOLDER}/${name}_prod ];then
  #directory doesn't exist, create it and set up environment

  if [ ! -d ${AFS_GEN_FOLDER} ];then
    mkdir ${AFS_GEN_FOLDER}
  fi

  cd $AFS_GEN_FOLDER

#   export SCRAM_ARCH=slc6_amd64_gcc472 #Here one should select the correct architecture corresponding with the CMSSW release
#   export RELEASE=CMSSW_5_3_22

  export SCRAM_ARCH=slc6_amd64_gcc481
  export RELEASE=CMSSW_7_1_11

  ##############################
  # Create a workplace to work #
  ##############################
  scram project -n ${name}_prod CMSSW ${RELEASE} ; cd ${name}_prod ; mkdir -p work ; cd work
  WORKDIR=`pwd`
  eval `scram runtime -sh`


  ###############################################
  # Copy, Unzip and Delete the MadGraph tarball #
  ###############################################

  wget --no-check-certificate ${MGSOURCE}
  tar xzf ${MG}
  rm $MG

  ##########################################################
  # Apply any necessary patches on top of official release #
  ##########################################################

  patch -l -p0 -i $PRODHOME/patches/mgfixes.patch
  patch -l -p0 -i $PRODHOME/patches/models.patch

  cd $MGBASEDIRORIG

  ################
  # Setup LHAPDF #
  ################

  LHAPDFCONFIG=`echo "$LHAPDF_DATA_PATH/../../bin/lhapdf-config"`

  # if lhapdf6 external is available then above points to lhapdf5 and needs to be overridden
  LHAPDF6TOOLFILE=$CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/available/lhapdf6.xml
  if [ -e $LHAPDF6TOOLFILE ]; then
    LHAPDFCONFIG=`cat $LHAPDF6TOOLFILE | grep "<environment name=\"LHAPDF6_BASE\"" | cut -d \" -f 4`/bin/lhapdf-config
  fi

  # make sure env variable for pdfsets points to the right place
  export LHAPDF_DATA_PATH=`$LHAPDFCONFIG --datadir`

  LHAPDFINCLUDES=`$LHAPDFCONFIG --incdir`
  LHAPDFLIBS=`$LHAPDFCONFIG --libdir`
  BOOSTINCLUDES=`scram tool tag boost INCLUDE`


  ########################
  # Set MG configuration #
  ########################

  echo "set auto_update 0" > mgconfigscript
  echo "set automatic_html_opening False" >> mgconfigscript
  echo "set output_dependencies internal" >> mgconfigscript
  echo "set lhapdf $LHAPDFCONFIG" >> mgconfigscript

  # If number of cores is not specified, put it to 1
  if [ -n $ncores ]; then
      ncores=1
  fi

  if [ $ncores -eq 1 ]; then
      echo "set run_mode 0" >> mgconfigscript
  else
      echo "set run_mode 2" >> mgconfigscript
      echo "set nb_core" $ncores >> mgconfigscript
  fi

  echo "save options" >> mgconfigscript

  ./bin/mg5_aMC mgconfigscript

  # get syscalc and compile
  wget --no-check-certificate ${SYSCALCSOURCE}
  tar xzf ${SYSCALC}
  rm $SYSCALC

  cd SysCalc
  sed -i "s#INCLUDES =  -I../include#INCLUDES =  -I../include -I${LHAPDFINCLUDES} -I${BOOSTINCLUDES}#g" src/Makefile
  sed -i "s#LIBS = -lLHAPDF#LIBS = ${LHAPDFLIBS}/libLHAPDF.a #g" src/Makefile
  make

  cd $WORKDIR

  if [ "$name" == "interactive" ]; then
    exit 0
  fi

  echo `pwd`


  ##########################
  # Locating the proc card #
  ##########################

  if [ ! -e $CARDSDIR/${name}_proc_card.dat ]; then
          echo $CARDSDIR/${name}_proc_card.dat " does not exist!"
          #exit 1;
  else
          cp $CARDSDIR/${name}_proc_card.dat ${name}_proc_card.dat
  fi

  ################################################################
  # Run the code-generation step to create the process directory #
  ################################################################

  ./$MGBASEDIRORIG/bin/mg5_aMC ${name}_proc_card.dat
  
else  
  echo "Reusing existing directory assuming generated code already exists"
  echo "WARNING: If you changed the process card you need to clean the folder and run from scratch"
  
  cd $AFS_GEN_FOLDER
  
  WORKDIR=$AFS_GEN_FOLDER/${name}_prod/work/
  if [ ! -d ${WORKDIR} ]; then
    echo "Existing directory does not contain expected folder $WORKDIR"
    exit 1
  fi
  cd $WORKDIR

  eval `scram runtime -sh`

  ################
  # Setup LHAPDF #
  ################

  LHAPDFCONFIG=`echo "$LHAPDF_DATA_PATH/../../bin/lhapdf-config"`

  # if lhapdf6 external is available then above points to lhapdf5 and needs to be overridden
  LHAPDF6TOOLFILE=$CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/available/lhapdf6.xml
  if [ -e $LHAPDF6TOOLFILE ]; then
    LHAPDFCONFIG=`cat $LHAPDF6TOOLFILE | grep "<environment name=\"LHAPDF6_BASE\"" | cut -d \" -f 4`/bin/lhapdf-config
  fi

  # make sure env variable for pdfsets points to the right place
  export LHAPDF_DATA_PATH=`$LHAPDFCONFIG --datadir`  
  
  if [ "$name" == "interactive" ]; then
    exit 0
  fi

fi  

# We've got the process directory now, proceed to generate events. 
# First make sure there is no old stuff lying around

if [ -d processtmp ]; then
  rm -rf processtmp
fi

cp -r $name/ processtmp

cd processtmp

#########################
# Locating the run card #
#########################

if [ ! -e $CARDSDIR/${name}_run_card.dat ]; then
  echo $CARDSDIR/${name}_run_card.dat " does not exist!"
  #exit 1;
else
  cp $CARDSDIR/${name}_run_card.dat ./Cards/run_card.dat
fi      

if [ ! -e $CARDSDIR/${name}_param_card.dat ]; then
        echo $CARDSDIR/${name}_param_card.dat " does not exist!"
        #exit 1;
else
        cp $CARDSDIR/${name}_param_card.dat ./Cards/param_card.dat
fi

#automatically detect NLO mode or LO mode from output directory
isnlo=0
if [ -e ./MCatNLO ]; then
  isnlo=1
fi

if [ "$isnlo" -gt "0" ]; then
# Running in NLO mode  

  # This is not supported yet for susy processes!
  echo "NLO not supported for SUSY processes!!"
  exit 0

else
  #LO mode

  ###################
  # Generate events #
  ###################

  echo "done" > makegrid.dat
  echo "./Cards/param_card.dat" >> makegrid.dat
  #echo "set run_card nevents 10000" >> makegrid.dat 
  if [ -e $CARDSDIR/${name}_customizecards.dat ]; then
          cat $CARDSDIR/${name}_customizecards.dat >> makegrid.dat
          echo "" >> makegrid.dat
  fi
  echo "done" >> makegrid.dat

  cat makegrid.dat | ./bin/generate_events pilotrun

  mv Events/pilotrun/unweighted_events.lhe.gz ${PRODHOME}/${name}/${name}_unweighted_events.lhe.gz
  
  echo "End of job"
  
  exit 0

fi
