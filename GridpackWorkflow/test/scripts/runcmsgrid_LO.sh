#!/bin/bash

nevt=${1}
echo "%MSG-MG5 number of events requested = $nevt"

rnum=${2}
echo "%MSG-MG5 random seed used for the run = $rnum"

ncpu=${3}
echo "%MSG-MG5 number of cpus = $ncpu"

LHEWORKDIR=`pwd`

use_gridpack_env=true
if [ -n "$4" ]
  then
  use_gridpack_env=$4
fi

if [ "$use_gridpack_env" = true ]
  then
    if [ -n "$5" ]
      then
        scram_arch_version=${5}
      else
        scram_arch_version=slc6_amd64_gcc481
    fi
    echo "%MSG-MG5 SCRAM_ARCH version = $scram_arch_version"

    if [ -n "$6" ]
      then
        cmssw_version=${6}
      else
        cmssw_version=CMSSW_7_1_25_patch3
    fi
    echo "%MSG-MG5 CMSSW version = $cmssw_version"
    export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
    source $VO_CMS_SW_DIR/cmsset_default.sh
    export SCRAM_ARCH=${scram_arch_version}
    scramv1 project CMSSW ${cmssw_version}
    cd ${cmssw_version}/src
    eval `scramv1 runtime -sh`
fi
cd $LHEWORKDIR

cd process

#make sure lhapdf points to local cmssw installation area
LHAPDFCONFIG=`echo "$LHAPDF_DATA_PATH/../../bin/lhapdf-config"`

#if lhapdf6 external is available then above points to lhapdf5 and needs to be overridden
LHAPDF6TOOLFILE=$CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/available/lhapdf6.xml
if [ -e $LHAPDF6TOOLFILE ]; then
  LHAPDFCONFIG=`cat $LHAPDF6TOOLFILE | grep "<environment name=\"LHAPDF6_BASE\"" | cut -d \" -f 4`/bin/lhapdf-config
fi

#make sure env variable for pdfsets points to the right place
export LHAPDF_DATA_PATH=`$LHAPDFCONFIG --datadir`

echo "lhapdf = $LHAPDFCONFIG" >> ./madevent/Cards/me5_configuration.txt
# echo "cluster_local_path = `${LHAPDFCONFIG} --datadir`" >> ./madevent/Cards/me5_configuration.txt

if [ "$ncpu" -gt "1" ]; then
  echo "run_mode = 2" >> ./madevent/Cards/me5_configuration.txt
  echo "nb_core = $ncpu" >> ./madevent/Cards/me5_configuration.txt
fi

#########################################
# FORCE IT TO PRODUCE EXACTLY THE REQUIRED NUMBER OF EVENTS
#########################################

# define max event per iteration as 5000 if n_evt<45000 or n_evt/9 otherwise
max_events_per_iteration=$(( $nevt > 5000*9 ? ($nevt / 9) + ($nevt % 9 > 0) : 5000 ))
# set starting variables
produced_lhe=0
run_counter=0
# if rnum allows, multiply by 10 to avoid multiple runs 
# with the same seed across the workflow
run_random_start=$(($rnum*10))
# otherwise don't change the seed and increase number of events as 10000 if n_evt<50000 or n_evt/9 otherwise
if [  $run_random_start -gt "89999990" ]; then
    run_random_start=$rnum
    max_events_per_iteration=$(( $nevt > 10000*9 ? ($nevt / 9) + ($nevt % 9 > 0) : 10000 ))
fi

while [ $produced_lhe -lt $nevt ]; do
  
  # set the incremental iteration seed
  run_random_seed=$(($run_random_start + $run_counter))
  # increase the iteration counter
  let run_counter=run_counter+1 
  
  # don't allow more than 90 iterations
  if [  $run_counter -gt "90" ]; then
      echo "asking for more than 90 iterations, this should never happen"
      break
  fi
  # compute remaining events
  remaining_event=$(($nevt - $produced_lhe))
  
  echo "Running MG5_aMC for the "$run_counter" time"
  # set number of events to max_events_per_iteration or residual ones if less than that
  submitting_event=$(( $remaining_event < $max_events_per_iteration ? $remaining_event : $max_events_per_iteration ))
  # run mg5_amc
  echo "produced_lhe " $produced_lhe "nevt " $nevt "submitting_event " $submitting_event " remaining_event " $remaining_event
  echo run.sh $submitting_event $run_random_seed
  ./run.sh $submitting_event $run_random_seed
  
  # compute number of events produced in the iteration
  produced_lhe=$(($produced_lhe+`zgrep \<event events.lhe.gz | wc -l`))
  
  # rename output file to avoid overwriting
  mv events.lhe.gz events_${run_counter}.lhe.gz
  echo "run "$run_counter" finished, total number of produced events: "$produced_lhe"/"$nevt
  
  echo ""
  
done

# merge multiple lhe files if needed
ls -lrt events*.lhe.gz
if [  $run_counter -gt "1" ]; then
    echo "Merging files and deleting unmerged ones"
    cp /cvmfs/cms.cern.ch/phys_generator/gridpacks/lhe_merger/merge.pl ./
    chmod 755 merge.pl
    # ./madevent/bin/internal/merge.pl events*.lhe.gz events.lhe.gz banner.txt
    ./merge.pl events*.lhe.gz events.lhe.gz banner.txt
    rm events_*.lhe.gz banner.txt;
else
    mv events_${run_counter}.lhe.gz events.lhe.gz
fi

#########################################
#########################################
#########################################

echo "run finished, produced number of events:"
zgrep \<event events.lhe.gz |wc -l

cd $LHEWORKDIR

mv process/events.lhe.gz events_presys.lhe.gz
gzip -d events_presys.lhe.gz

echo "
# Central scale factors
scalefact:
1 2 0.5
# choice of correlation scheme between muF and muR
# set here to reproduce aMC@NLO order
scalecorrelation:
0 3 6 1 4 7 2 5 8
# PDF sets and number of members (0 or none for all members)
PDF:
" > syscalc_card.dat

is5FlavorScheme=1

#run syscalc to populate pdf and scale variation weights
if [ $is5FlavorScheme -eq 1 ]; then
  # 5F PDF
  echo "
  NNPDF30_lo_as_0130.LHgrid
  NNPDF30_lo_as_0130_nf_4.LHgrid
  NNPDF30_lo_as_0118.LHgrid 1
  NNPDF23_lo_as_0130_qed.LHgrid
  NNPDF23_lo_as_0119_qed.LHgrid 1
  cteq6l1.LHgrid
  MMHT2014lo68cl.LHgrid
  MMHT2014lo_asmzsmallrange.LHgrid
  HERAPDF15LO_EIG.LHgrid
  NNPDF30_nlo_as_0118.LHgrid 1
  NNPDF23_nlo_as_0119.LHgrid 1
  CT10nlo.LHgrid
  MMHT2014nlo68cl.LHgrid 1
 " >> syscalc_card.dat

else
 # 4F PDF
  echo "
  " >> syscalc_card.dat
fi

LD_LIBRARY_PATH=`${LHAPDFCONFIG} --libdir`:${LD_LIBRARY_PATH} ./mgbasedir/SysCalc/sys_calc events_presys.lhe syscalc_card.dat cmsgrid_final.lhe

#reweight if necessary
if [ -e process/madevent/Cards/reweight_card.dat ]; then
    echo "reweighting events"
    mv cmsgrid_final.lhe process/madevent/Events/GridRun_${run_random_start}/unweighted_events.lhe
    cd process/madevent
    ./bin/madevent reweight -f GridRun_${run_random_start}
    cd ../..
    mv process/madevent/Events/GridRun_${run_random_start}/unweighted_events.lhe.gz cmsgrid_final.lhe.gz
    gzip -d  cmsgrid_final.lhe.gz
fi

if [ -f process/madspin_card.dat ] ;then
    mv cmsgrid_final.lhe process
    cd process
    gzip  cmsgrid_final.lhe
    echo "import cmsgrid_final.lhe.gz" > madspinrun.dat
    rnum2=$(($rnum+1000000))
    echo `echo "set seed $rnum2"` >> madspinrun.dat
    cat ./madspin_card.dat >> madspinrun.dat
    cat madspinrun.dat | $LHEWORKDIR/mgbasedir/MadSpin/madspin
    cd $LHEWORKDIR
    mv process/cmsgrid_final_decayed.lhe.gz cmsgrid_final.lhe.gz
    gzip -d  cmsgrid_final.lhe.gz
fi

ls -l
echo

exit 0
