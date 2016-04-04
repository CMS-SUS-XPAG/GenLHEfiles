#example gen fragment where a randomized parameter scan is performed over parameters
#in the SLHA table

#since the randomization occurs only at lumi section boundaries, test with command like
#cmsDriver.py randomizedParametersSLHAwmLHE.py -s LHE,GEN --conditions auto:run2_mc -n 1000 --eventcontent LHE,RAWSIM --datatier LHE,GEN-SIM --no_exec --customise_command "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)"

#or for full chain with fastsim
#cmsDriver.py randomizedParametersSLHAwmLHE.py -s LHE,GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2,DATAMIX,L1,L1Reco,RECO,HLT:@relval25ns --datamix PreMix --conditions auto:run2_mc --pileup_input dbs:/RelValFS_PREMIXUP15_PU25/CMSSW_8_0_0_pre2-PU25ns_76X_mcRun2_asymptotic_v12_FastSim-v1/GEN-SIM-DIGI-RAW --fast --era Run2_25ns --eventcontent AODSIM,LHE --datatier AODSIM,LHE --beamspot Realistic50ns13TeVCollision --customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput --no_exec --customise_command "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)"  -n 1000


import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
    
basePythiaParameters = cms.PSet(
  pythia8CommonSettingsBlock,
  pythia8CUEP8M1SettingsBlock,
  JetMatchingParameters = cms.vstring(
    'JetMatching:setMad = off',
    'JetMatching:scheme = 1',
    'JetMatching:merge = on',
    'JetMatching:jetAlgorithm = 2',
    'JetMatching:etaJetMax = 5.',
    'JetMatching:coneRadius = 1.',
    'JetMatching:slowJetPower = 1',
    'JetMatching:qCut = 84', #this is the actual merging scale
    'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
    'JetMatching:nJetMax = 2', #number of partons in born matrix element for highest multiplicity
    'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching
  ), 
  parameterSets = cms.vstring('pythia8CommonSettings',
    'pythia8CUEP8M1Settings',
    'JetMatchingParameters'
  )
)

baseSLHATable="""
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
   1000001     1.00000000E+05   # ~d_L
   2000001     1.00000000E+05   # ~d_R
   1000002     1.00000000E+05   # ~u_L
   2000002     1.00000000E+05   # ~u_R
   1000003     1.00000000E+05   # ~s_L
   2000003     1.00000000E+05   # ~s_R
   1000004     1.00000000E+05   # ~c_L
   2000004     1.00000000E+05   # ~c_R
   1000005     1.00000000E+05   # ~b_1
   2000005     1.00000000E+05   # ~b_2
   1000006     1.00000000E+05   # ~t_1
   2000006     1.00000000E+05   # ~t_2
   1000011     %MSLEP%   # ~e_L
   2000011     1.00000000E+05   # ~e_R
   1000012     %MSLEP%   # ~nu_eL
   1000013     %MSLEP%   # ~mu_L
   2000013     1.00000000E+05   # ~mu_R
   1000014     %MSLEP%   # ~nu_muL
   1000015     %MSLEP%   # ~tau_1
   2000015     1.00000000E+05   # ~tau_2
   1000016     %MSLEP%   # ~nu_tauL
   1000021     1.00000000E+05   # ~g
   1000022     %MN1%           # ~chi_10
   1000023     %MN2%            # ~chi_20
   1000025     1.00000000E+05   # ~chi_30
   1000035     1.00000000E+05   # ~chi_40
   1000024     %MC1%            # ~chi_1+
   1000037     1.00000000E+05   # ~chi_2+
#         PDG            Width
DECAY   1000001     0.00000000E+00   # sdown_L decays
DECAY   2000001     0.00000000E+00   # sdown_R decays
DECAY   1000002     0.00000000E+00   # sup_L decays
DECAY   2000002     0.00000000E+00   # sup_R decays
DECAY   1000003     0.00000000E+00   # sstrange_L decays
DECAY   2000003     0.00000000E+00   # sstrange_R decays
DECAY   1000004     0.00000000E+00   # scharm_L decays
DECAY   2000004     0.00000000E+00   # scharm_R decays
DECAY   1000005     0.00000000E+00   # sbottom1 decays
DECAY   2000005     0.00000000E+00   # sbottom2 decays
DECAY   1000006     0.00000000E+00   # stop1 decays
DECAY   2000006     0.00000000E+00   # stop2 decays
#
DECAY   1000011     0.10000000E+00   # selectron_L decays
    1.00000000E+00    2    1000022    11
DECAY   2000011     0.00000000E+00   # selectron_R decays
DECAY   1000012     0.10000000E+00   # snu_elL decays
    1.00000000E+00    2    1000022    12
DECAY   1000013     0.10000000E+00   # smuon_L decays
    1.00000000E+00    2    1000022    13
DECAY   2000013     0.00000000E+00   # smuon_R decays
DECAY   1000014     0.10000000E+00   # snu_muL decays
    1.00000000E+00    2    1000022    14
DECAY   1000015     0.10000000E+00   # stau_1 decays
    1.00000000E+00    2    1000022    15
DECAY   2000015     0.00000000E+00   # stau_2 decays
DECAY   1000016     0.10000000E+00   # snu_tauL decays
    1.00000000E+00    2    1000022    16
DECAY   1000021     0.00000000E+00   # gluino decays
DECAY   1000022     0.00000000E+00   # neutralino1 decays
DECAY   1000023     0.10000000E+00   # neutralino2 decays
    %BRANCH_SL%    2    1000011    -11
    %BRANCH_SL%    2    -1000011    11
    %BRANCH_SL%    2    1000013    -13
    %BRANCH_SL%    2    -1000013    13
    %BRANCH_TL%    2    1000015    -15
    %BRANCH_TL%    2    -1000015    15
    %BRANCH_SN%    2    1000012     12
    %BRANCH_SN%    2    1000014     14
    %BRANCH_SN%    2    1000016     16
DECAY   1000024     0.10000000E+00   # chargino1+ decays
    %BRANCH_EM%    2    -1000011    12
    %BRANCH_EM%    2    1000012    -11
    %BRANCH_EM%    2    -1000013    14
    %BRANCH_EM%    2    1000014    -13
    %BRANCH_T%     2    -1000015    16
    %BRANCH_EM%    2    1000016    -15
DECAY   1000025     0.00000000E+00   # neutralino3 decays
DECAY   1000035     0.00000000E+00   # neutralino4 decays
DECAY   1000037     0.00000000E+00   # chargino2+ decays
"""

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/hadoop/cms/store/user/mliu/SUSYMC/SMS-TChiSlepSnu_mChi-700_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

generator = cms.EDFilter("Pythia8HadronizerFilter",
  maxEventsToPrint = cms.untracked.int32(1),
  pythiaPylistVerbosity = cms.untracked.int32(1),
  filterEfficiency = cms.untracked.double(1.0),
  pythiaHepMCVerbosity = cms.untracked.bool(False),
  comEnergy = cms.double(13000.),
  RandomizedParameters = cms.VPSet(),
)
### defining masses for scan

model_base = 'TChiSlepSnu'
m_n2 = 700
m_c1 = 700
baseSLHATable = baseSLHATable.replace('%MN2%','%e' %m_n2)
baseSLHATable = baseSLHATable.replace('%MC1%','%e' %m_c1)

#Flavor-democratic
#chi branching ratio
slep_branch = 0.08333333E+00
stau_branch = slep_branch
snu_branch = 0.16666666E+00
#ch1 branching ratio
ch_slep_em = 0.16666666E+00
ch_slep_tau = 0.16666666E+00
baseSLHATable_dem = baseSLHATable.replace('%BRANCH_SL%','%e'%slep_branch)
baseSLHATable_dem = baseSLHATable_dem.replace('%BRANCH_TL%','%e' %stau_branch)
baseSLHATable_dem = baseSLHATable_dem.replace('%BRANCH_SN%','%e' %snu_branch)
baseSLHATable_dem = baseSLHATable_dem.replace('%BRANCH_EM%','%e' %ch_slep_em)
baseSLHATable_dem = baseSLHATable_dem.replace('%BRANCH_T%','%e' %ch_slep_tau)

for i in range(17):
    for x  in [0.5,0.05,0.95]: #scan over different slepton masses (ekw scan 2,3,4)
        m_lsp = 0. + i*50 
        m_slep =m_lsp + x*(m_n2-m_lsp) # slepton mass
        slhatable = baseSLHATable_dem.replace('%MN1%','%e' % m_lsp)
        slhatable = slhatable.replace('%MSLEP%','%e' % m_slep)
        model = model_base+'Dem_' + str(x).replace('.','p')
        generator.RandomizedParameters.append(
             cms.PSet(
              ConfigWeight = cms.double(1.0),
              ConfigDescription = cms.string('%s_%i_%i' % (model, m_c1, m_lsp)),
              SLHATableForPythia8 = cms.string('%s' % slhatable),
              PythiaParameters = basePythiaParameters,
         ),
        )
####### tau-enriched ########
#chi branching ratio
slep_branch = 0.08333333E+00
stau_branch = slep_branch
snu_branch = 0.00000000
#ch1 branching ratio
ch_slep_em = 0.00000000
ch_slep_tau = 1.00000000
baseSLHATable_tauen = baseSLHATable.replace('%BRANCH_SL%','%e'%slep_branch)
baseSLHATable_tauen = baseSLHATable_tauen.replace('%BRANCH_TL%','%e' %stau_branch)
baseSLHATable_tauen = baseSLHATable_tauen.replace('%BRANCH_SN%','%e' %snu_branch)
baseSLHATable_tauen = baseSLHATable_tauen.replace('%BRANCH_EM%','%e' %ch_slep_em)
baseSLHATable_tauen = baseSLHATable_tauen.replace('%BRANCH_T%','%e' %ch_slep_tau)

for i in range(17):
    for x  in [0.5,0.05,0.95]: #scan over different slepton masses (ekw scan 2,3,4)
        m_lsp = 0. + i*50 
        m_slep =m_lsp + x*(m_n2-m_lsp) # slepton mass
        slhatable = baseSLHATable_tauen.replace('%MN1%','%e' % m_lsp)
        slhatable = slhatable.replace('%MSLEP%','%e' % m_slep)
        model = model_base+'TauEnriched_' + str(x).replace('.','p')
        generator.RandomizedParameters.append(
             cms.PSet(
              ConfigWeight = cms.double(1.0),
              ConfigDescription = cms.string('%s_%i_%i' % (model, m_c1, m_lsp)),
              SLHATableForPythia8 = cms.string('%s' % slhatable),
              PythiaParameters = basePythiaParameters,
         ),
        )
######## tau-dominated ########
#chi branching ratio
slep_branch = 0.00000000
stau_branch = 1.00000000
snu_branch = 0.00000000
#ch1 branching ratio
ch_slep_em = 0.00000000
ch_slep_tau = 1.00000000
baseSLHATable_tauden = baseSLHATable.replace('%BRANCH_SL%','%e'%slep_branch)
baseSLHATable_tauden = baseSLHATable_tauden.replace('%BRANCH_TL%','%e' %stau_branch)
baseSLHATable_tauden = baseSLHATable_tauden.replace('%BRANCH_SN%','%e' %snu_branch)
baseSLHATable_tauden = baseSLHATable_tauden.replace('%BRANCH_EM%','%e' %ch_slep_em)
baseSLHATable_tauden = baseSLHATable_tauden.replace('%BRANCH_T%','%e' %ch_slep_tau)

for i in range(17):
    for x  in [0.5]: #scan over different slepton masses (ekw scan 2,3,4)
        m_lsp = 0. + i*50 
        m_slep =m_lsp + x*(m_n2-m_lsp) # slepton mass
        slhatable = baseSLHATable_tauden.replace('%MN1%','%e' % m_lsp)
        slhatable = slhatable.replace('%MSLEP%','%e' % m_slep)
        model = model_base+'TauDom_' + str(x).replace('.','p')
        generator.RandomizedParameters.append(
             cms.PSet(
              ConfigWeight = cms.double(1.0),
              ConfigDescription = cms.string('%s_%i_%i' % (model, m_c1, m_lsp)),
              SLHATableForPythia8 = cms.string('%s' % slhatable),
              PythiaParameters = basePythiaParameters,
         ),
        )
#
