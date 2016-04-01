#example gen fragment where a randomized parameter scan is performed over parameters
#in the SLHA table

#since the randomization occurs only at lumi section boundaries, test with command like
#cmsDriver.py randomizedParametersSLHA.py -s GEN --conditions auto:mc -n 1000 --eventcontent AODSIM --no_exec --customise_command "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)"

#or for full chain with fastsim
#cmsDriver.py randomizedParametersSLHAwmLHE.py -s GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2,DATAMIX,L1,L1Reco,RECO,HLT:@relval25ns --datamix PreMix --conditions auto:run2_mc --pileup_input dbs:/RelValFS_PREMIXUP15_PU25/CMSSW_8_0_0_pre2-PU25ns_76X_mcRun2_asymptotic_v12_FastSim-v1/GEN-SIM-DIGI-RAW --fast --era Run2_25ns --eventcontent AODSIM --datatier AODSIM --beamspot Realistic50ns13TeVCollision --customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput --no_exec --customise_command "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)"  -n 1000

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
   1000011     %MSLEP%          # ~e_L
   2000011     1.00000000E+05   # ~e_R
   1000012     %MSLEP%          # ~nu_eL
   1000013     %MSLEP%          # ~mu_L
   2000013     1.00000000E+05   # ~mu_R
   1000014     %MSLEP%          # ~nu_muL
   1000015     %MSLEP%          # ~tau_1
   2000015     1.00000000E+05   # ~tau_2
   1000016     %MSLEP%          # ~nu_tauL
   1000021     1.00000000E+05   # ~g
   1000022     %MN1%            # ~chi_10
   1000023     %MN2%            # ~chi_20
   1000025     1.00000000E+05   # ~chi_30
   1000035     1.00000000E+05   # ~chi_40
   1000024     %MC1%            # ~chi_1+
   1000037     1.00000000E+05   # ~chi_2+

# DECAY TABLE
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
    0.16666666E+00    2    1000011    -11
    0.16666666E+00    2    -1000011    11
    0.16666666E+00    2    1000013    -13
    0.16666666E+00    2    -1000013    13
    0.16666666E+00    2    1000015    -15
    0.16666666E+00    2    -1000015    15
DECAY   1000024     0.10000000E+00   # chargino1+ decays
    0.16666666E+00    2    -1000011    12
    0.16666666E+00    2    1000012    -11
    0.16666666E+00    2    -1000013    14
    0.16666666E+00    2    1000014    -13
    0.16666666E+00    2    -1000015    16
    0.16666666E+00    2    1000016    -15
DECAY   1000025     0.00000000E+00   # neutralino3 decays
DECAY   1000035     0.00000000E+00   # neutralino4 decays
DECAY   1000037     0.00000000E+00   # chargino2+ decays
"""

generator = cms.EDFilter("Pythia8GeneratorFilter",
  maxEventsToPrint = cms.untracked.int32(1),
  pythiaPylistVerbosity = cms.untracked.int32(1),
  filterEfficiency = cms.untracked.double(1.0),
  pythiaHepMCVerbosity = cms.untracked.bool(False),
  comEnergy = cms.double(13000.),
  RandomizedParameters = cms.VPSet(),
)

# define list of configurations
model = 'TChiSlepSnu-0p5'
# dict := mChi : mLSP step size
scan_dict = {300:50, 700:200, 800:200}

for m_c1 in scan_dict.keys():
  step = scan_dict[m_c1]
  nlsp = m_c1/step
  if (m_c1%step>0): nlsp +=1
  slhatable = baseSLHATable.replace('%MN2%','%e' %m_c1)
  slhatable = slhatable.replace('%MC1%','%e' %m_c1)

  for i in range(nlsp):
    m_lsp = 0. + i*step
    m_slep = m_lsp + 0.5*(m_c1-m_lsp)
    slhatable = baseSLHATable.replace('%MN1%','%e' % m_lsp)
    slhatable = slhatable.replace('%MSLEP%','%e' % m_slep)

    generator.RandomizedParameters.append(
      cms.PSet(
        ConfigWeight = cms.double(1.0),
        GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/SMS-TChiSlepSnu/SMS-TChiSlepSnu_mChi-%i_tarball.tar.xz' % m_c1),
        ConfigDescription = cms.string('%s_%i_%i' % (model, m_c1, m_lsp)),
        SLHATableForPythia8 = cms.string('%s' % slhatable),
        PythiaParameters = basePythiaParameters,
      ),
    )
