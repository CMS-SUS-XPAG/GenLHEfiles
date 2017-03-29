import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *


generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    RandomizedParameters = cms.VPSet(),
)

# Parameters that define the grid in the bulk and diagonal
class gridBlock:
  def __init__(self, xmin, xmax, xstep, ymin, ymax, ystep, diagStep):
    self.xmin = xmin
    self.xmax = xmax
    self.xstep = xstep
    self.ymin  = ymin
    self.ymax  = ymax
    self.ystep = ystep
    self.diagStep = diagStep

def matchParams(mass):
    if mass < 99: return 80,0.63
    elif mass < 149: return 80,0.62
    elif mass < 199: return 80,0.56
    elif mass < 249 : return 80,0.53
    elif mass < 299 : return 80,0.51
    elif mass < 349 : return 80,0.49
    elif mass < 399 : return 80,0.47
    else: return 80,0.46

model = "TStauStau-MaxMixing"

# Number of events for mass point, in thousands
nevt = 50

scanBlocks = []

scanBlocks.append(gridBlock(90,100,10,0,11,10,0))
scanBlocks.append(gridBlock(100,300,25,0,50,10,0))
scanBlocks.append(gridBlock(100,300,25,50,150,25,0))
scanBlocks.append(gridBlock(100,300,25,150,201,50,0))
scanBlocks.append(gridBlock(300,401,50,0,50,10,0))
scanBlocks.append(gridBlock(300,401,50,50,150,25,0))
scanBlocks.append(gridBlock(300,401,50,150,201,50,0))

# -------------------------------
#    Constructing grid

mpoints = []

for block in scanBlocks:
  for mx in range(block.xmin, block.xmax, block.xstep):
    for my in range(block.ymin, block.ymax, block.ystep):
      if mx > my + block.diagStep:
        mpoints.append([mx,my,nevt])

for point in mpoints:
    mstau, mlsp = point[0], point[1]
    qcut, tru_eff = matchParams(mstau)
    wgt = point[2]/tru_eff
    
    if mlsp==0: mlsp = 1

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
            GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/SMS-StauStau/MaxMixing/SMS-TStauStau-MM_mStau-%i_mLSP-%i_tarball.tar.xz' % (mstau,mlsp)),
            ConfigDescription = cms.string('%s_%i_%i' % (model, mstau, mlsp)),
            PythiaParameters = basePythiaParameters,
        ),
    )
