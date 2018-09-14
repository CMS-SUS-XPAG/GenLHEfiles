#!/usr/bin/env python
import os
import shutil
import subprocess

eos_dir='/eos/cms/store/group/phys_generator/cvmfs/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/Higgsino-N2N1/v2'
new_dir='/eos/cms/store/group/phys_generator/cvmfs/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/Higgsino-N2N1/v3'

cmd='eos find -f %s | grep -v noiter' % eos_dir
ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result = ps.communicate()
gridpacks = result[0].rstrip('\n').split('\n')

print gridpacks

prefix='root://eoscms.cern.ch/'


#count=-1
for gp in gridpacks:
    #count+=1
    #if count > 16: continue
    os.system('xrdcp -f %s/%s %s/%s' % (prefix,gp,prefix,eos_dir+'/old/'))
    print '-------- %s ----------'%gp
    os.system('eos cp %s .' % gp)
    gpname = gp.split('/')[-1]
    os.system('unxz %s' % gpname)
    tarname = gpname.replace('.xz','')
    os.system('tar -xvf %s' % tarname)
    os.system('cp runcmsgrid_LO.sh runcmsgrid.sh')
    os.system('chmod a+x runcmsgrid.sh')
    xz_opt="--lzma2=preset=9,dict=512MiB"
    os.system('XZ_OPT=%s' % xz_opt)
    os.system('tar -cJpsf %s mgbasedir process runcmsgrid.sh gridpack_generation*.log' % gpname)
    os.system('xrdcp -f %s %s/%s/' % (gpname,prefix,new_dir))
    #os.system('rm -r mgbasedir process runcmsgrid.sh gridpack_generation*.log')
    os.system('rm -r %s* mgbasedir process runcmsgrid.sh gridpack_generation*.log' % tarname)

