import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring("/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/T2bH-Hgg/T2bH-Hgg-sbm250-sbw1-chi2m230-chi2w0p1-chi1m100_tarball.tar.xz"),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)
#Link to datacards:
#https://github.com/cms-sw/genproductions/tree/db02d1ef531bf4c0be99e078af5934ec46a7ada6/bin/MadGraph5_aMCatNLO/cards/production/13TeV/T2bH-Hgg/T2bH-Hgg-sbm250-sbw1-chi2m230-chi2w0p1-chi1m100

baseSLHA = """
#
BLOCK MASS # 
      6 1.730000e+02 #  mt
      25 1.25e02 #  mh01
      35 1.00e05 #  mh02
      36 1.00e05 #  ma0
      37 1.00e05 #  mh
      1000001 1.00e05 #  set of param :1*msd1, 1*msd2
      1000002 1.00e05 #  set of param :1*msu1, 1*msu2
      1000003 1.00e05 #  sl : msd1
      1000004 1.00e05 #  cl : msu1
      1000005 250   #  msd3
      1000006 1.00e05 #  msu3
      1000011 1.00e05 #  set of param :1*msl1, 1*msl2
      1000012 1.00e05 #  set of param :1*msn1, 1*msn2
      1000013 1.00e05 #  mul- : msl1
      1000014 1.00e05 #  svm : msn1
      1000015 1.00e05 #  msl3
      1000016 1.00e05 #  msn3
      1000021 1.00e05 #  mgo
      1000022 1  #  mneu1
      1000023 131 #  mneu2
      1000024 1.00e05 #  mch1
      1000025 1.00e05 #  mneu3
      1000035 1.00e05 #  mneu4
      1000037 1.00e05 #  mch2
      2000001 1.00e05 #  set of param :1*msd4, 1*msd5
      2000002 1.00e05 #  set of param :1*msu4, 1*msu5
      2000003 1.00e05 #  sr : msd4
      2000004 1.00e05 #  cr : msu4
      2000005 1.00e05 #  msd6
      2000006 1.00e05 #  msu6
      2000011 1.00e05 #  set of param :1*msl4, 1*msl5
      2000013 1.00e05 #  mur- : msl4
      2000015 1.00e05 #  msl6
## INFORMATION FOR DECAY
DECAY 1000001 5.312788e+00 #  wsd1
DECAY 1000002 5.477195e+00 #  wsu1
DECAY 1000003 5.312788e+00 #  wsd2
DECAY 1000004 5.477195e+00 #  wsu2
DECAY 1000005 1.000000e+00 #  wsd3
     1.00000000E+00    2     1000023       5
DECAY 1000006 2.021596e+00 #  wsu3
DECAY 1000011 2.136822e-01 #  wsl1
DECAY 1000012 1.498816e-01 #  wsn1
DECAY 1000013 2.136822e-01 #  wsl2
DECAY 1000014 1.498816e-01 #  wsn2
DECAY 1000015 1.483273e-01 #  wsl3
DECAY 1000016 1.475190e-01 #  wsn3
DECAY 1000021 5.506754e+00 #  wgo
DECAY 1000022 0.000000e+00 #  n1 : 0.0
DECAY 1000023 1.000000e-01 #  wneu2
     1.00000000E+00    2     1000022       25
DECAY 1000024 1.704145e-02 #  wch1
DECAY 1000025 1.915985e+00 #  wneu3
DECAY 1000035 2.585851e+00 #  wneu4
DECAY 1000037 2.486895e+00 #  wch2
DECAY 2000001 2.858123e-01 #  wsd4
DECAY 2000002 1.152973e+00 #  wsu4
DECAY 2000003 2.858123e-01 #  wsd5
DECAY 2000004 1.152973e+00 #  wsu5
DECAY 2000005 8.015663e-01 #  wsd6
DECAY 2000006 7.373133e+00 #  wsu6
DECAY 2000011 2.161216e-01 #  wsl4
DECAY 2000013 2.161216e-01 #  wsl5
DECAY 2000015 2.699061e-01 #  wsl6
"""

generator = cms.EDFilter("Pythia8HadronizerFilter",
  maxEventsToPrint = cms.untracked.int32(1),
  pythiaPylistVerbosity = cms.untracked.int32(1),
  filterEfficiency = cms.untracked.double(1.0),
  pythiaHepMCVerbosity = cms.untracked.bool(False),
  comEnergy = cms.double(13000.),
  PythiaParameters = cms.PSet(
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
      'JetMatching:qCut = 58', #this is the actual merging scale
      'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
      'JetMatching:nJetMax = 2', #number of partons in born matrix element for highest multiplicity
      'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching
      '25:m0 = 125.0',
      'ResonanceDecayFilter:filter = on',
      'ResonanceDecayFilter:mothers = 25',
      'ResonanceDecayFilter:daughters = 22,22',
    ), 
    parameterSets = cms.vstring('pythia8CommonSettings',
      'pythia8CUEP8M1Settings',
      'JetMatchingParameters'
    )
  ),
  SLHATableForPythia8 = cms.string(baseSLHA),
)
