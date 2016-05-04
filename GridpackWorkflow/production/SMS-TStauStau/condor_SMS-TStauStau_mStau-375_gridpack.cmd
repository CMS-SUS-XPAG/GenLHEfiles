Universe = grid
Grid_Resource = condor cmssubmit-r1.t2.ucsd.edu glidein-collector.t2.ucsd.edu
x509userproxy=/tmp/x509up_u31584
+DESIRED_Sites="T2_US_UCSD"
Executable = /home/users/mliu/susy_mc/GenLHEfiles/GridpackWorkflow/test/scripts/runGridpackGeneration.sh
arguments =  SMS-TStauStau_mStau-375 /hadoop/cms/store/user/mliu/mcProduction/GRIDPACKS/SMS-TStauStau_mStau-375
Transfer_Executable = True
should_transfer_files = YES
transfer_input_files = /home/users/mliu/susy_mc/GenLHEfiles/GridpackWorkflow/test/scripts/gridpack_generation.sh,/home/users/mliu/genproductions//bin/MadGraph5_aMCatNLO/runcmsgrid_LO.sh,/home/users/mliu/genproductions//bin/MadGraph5_aMCatNLO/cleangridmore.sh,/home/users/mliu/susy_mc/GenLHEfiles/GridpackWorkflow/test/scripts/ucsd.patch,/home/users/mliu/genproductions//bin/MadGraph5_aMCatNLO/patches/mgfixes.patch,/home/users/mliu/genproductions//bin/MadGraph5_aMCatNLO/patches/models.patch,jobs/SMS-TStauStau_mStau-375/SMS-TStauStau_mStau-375_run_card.dat,jobs/SMS-TStauStau_mStau-375/SMS-TStauStau_mStau-375_proc_card.dat,jobs/SMS-TStauStau_mStau-375/SMS-TStauStau_mStau-375_customizecards.dat
Notification = Never
Log=gen_SMS-TStauStau_mStau-375_gridpack.log.$(Cluster).$(Process)
output=gen_SMS-TStauStau_mStau-375_gridpack.out.$(Cluster).$(Process)
error=gen_SMS-TStauStau_mStau-375_gridpack.err.$(Cluster).$(Process)
queue 1
