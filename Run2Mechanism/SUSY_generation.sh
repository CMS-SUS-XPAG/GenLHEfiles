#!/bin/bash

CARDSDIR=$1
OUTDIR=$2
PROCNAME=$3
CUSTOMCARD=$4
ISCONDOR=$5

# check to make sure process or custom directory doesn't already exist
if [ -d ${PROCNAME} ]; then
  rm -rf ${PROCNAME}
fi
if [ -d ${CUSTOMCARD} ]; then
  rm -rf ${CUSTOMCARD}
fi

# Run the code-generation step to create the process directory
${MGBASEDIR}/bin/mg5_aMC ${CARDSDIR}/${PROCNAME}_proc_card.dat

# move generic process directory to specific custom directory for this job
mv ${PROCNAME} ${CUSTOMCARD}
cd ${CUSTOMCARD}

# Locating the run card

if [ ! -e ${CARDSDIR}/${PROCNAME}_run_card.dat ]; then
  echo ${CARDSDIR}/${PROCNAME}_run_card.dat " does not exist!"
  #exit 1;
else
  cp ${CARDSDIR}/${PROCNAME}_run_card.dat ./Cards/run_card.dat
fi

if [ ! -e ${CARDSDIR}/${PROCNAME}_param_card.dat ]; then
  echo ${CARDSDIR}/${PROCNAME}_param_card.dat " does not exist!"
  #exit 1;
else
  cp ${CARDSDIR}/${PROCNAME}_param_card.dat ./Cards/param_card.dat
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

  # Generate events

  echo "done" > makegrid.dat
  echo "./Cards/param_card.dat" >> makegrid.dat
  # Specific customization for this job (nevents, seed, mass values)
  if [ -e ${CARDSDIR}/${CUSTOMCARD}_customizecards.dat ]; then
    cat ${CARDSDIR}/${CUSTOMCARD}_customizecards.dat >> makegrid.dat
    echo "" >> makegrid.dat
  fi
  echo "done" >> makegrid.dat

  cat makegrid.dat | ./bin/generate_events pilotrun

  if [ -n "$ISCONDOR" ]; then
    echo "xrdcp output for condor"
    xrdcp -f Events/pilotrun/unweighted_events.lhe.gz ${OUTDIR}/${CUSTOMCARD}_unweighted_events.lhe.gz
  else
    echo "mv output for lxbatch"
    mkdir -p ${OUTDIR}
    mv Events/pilotrun/unweighted_events.lhe.gz ${OUTDIR}/${CUSTOMCARD}_unweighted_events.lhe.gz
  fi
  
  echo "End of job"
  
  exit 0

fi
