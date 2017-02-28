import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

import math


generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    RandomizedParameters = cms.VPSet(),
)

def matchParams(mass):
    if mass < 221.: return 76,0.513
    elif mass < 241.: return 76,0.474
    else: return 76,0.5 # it shouldn't be used anyway

# weighted average of matching efficiencies for the full scan
# must equal the number entered in McM generator params
mcm_eff = 0.508

model = "MSSM-higgsino"
process = "Higgsino_Full"

# Number of events for mass point, in thousands
nevt = 100

MUs = [100., 120., 140., 160., 180., 200., 220., 240. ]
M1s  = [300., 400., 500., 600., 800., 1000., 1200. ]
# -------------------------------
#    Constructing grid

mpoints = []
for MU in MUs:
  for M1 in M1s:
    mpoints.append([MU,M1,nevt])

for point in mpoints:

    mu, m1 = point[0], point[1]

    muStr = str(int(mu))
    m1Str = str(int(m1))

    qcut, tru_eff = matchParams(mu)
    wgt = point[2]*(mcm_eff/tru_eff)
   
    with open('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/slha/Higgsino_Full/susyhit_slha_%d_%d.out' % (mu, m1)) as f:
        slhaTable = f.read()

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
            'JetMatching:qCut = %.0f' % qcut, #this is the actual merging scale
            'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
            'JetMatching:nJetMax = 2', #number of partons in born matrix element for highest multiplicity
            'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching
            '6:m0 = 172.5',
            '24:mMin = 0.1',
            '23:mMin = 0.1',
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = off', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
            'ResonanceDecayFilter:eMuAsEquivalent = off', #on: treat electrons and muons as equivalent
            'ResonanceDecayFilter:eMuTauAsEquivalent = on', #on: treat electrons, muons , and taus as equivalent
            'ResonanceDecayFilter:allNuAsEquivalent = on', #on: treat all three neutrino flavours as equivalent
            #'ResonanceDecayFilter:mothers =', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
            'ResonanceDecayFilter:daughters = 11,11',
            'Check:abortIfVeto = on',
        ), 
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'JetMatchingParameters'
        )
    )
    generator.RandomizedParameters.append(
        cms.PSet(
            ConfigWeight = cms.double(wgt),
            GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/%s/%s_MU-%s_M1-%s_tarball.tar.xz' % (process,process,muStr,m1Str)),
            ConfigDescription = cms.string('%s_%s_%s' % (model, muStr,m1Str)),
            SLHATableForPythia8 = cms.string('%s' % slhatable),
            PythiaParameters = basePythiaParameters,
        ),
    )
