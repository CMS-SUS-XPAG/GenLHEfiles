import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

import math

baseSLHATable="""
BLOCK MASS
   2000001     1.00000000E+05
   2000002     1.00000000E+05
   2000003     1.00000000E+05
   2000004     1.00000000E+05
   2000005     1.00000000E+05
   2000006     1.00000000E+05
   2000011     1.00000000E+05
   2000013     1.00000000E+05
   2000015     1.00000000E+05
   1000001     1.00000000E+05
   1000002     1.00000000E+05
   1000003     1.00000000E+05
   1000004     1.00000000E+05
   1000005     1.00000000E+05
   1000006     1.00000000E+05
   1000011     1.00000000E+05
   1000012     1.00000000E+05
   1000013     1.00000000E+05
   1000014     1.00000000E+05
   1000015     1.00000000E+05
   1000016     1.00000000E+05
   1000021     %MGLU%
   1000022     1.00000000E+00
   1000023     %MCHI%
   1000024     %MCHI%
   1000025     1.00000000E+05
   1000035     1.00000000E+05
   1000037     1.00000000E+05
#
DECAY   2000001     0.00000000E+00
DECAY   2000002     0.00000000E+00
DECAY   2000003     0.00000000E+00
DECAY   2000004     0.00000000E+00
DECAY   2000005     0.00000000E+00
DECAY   2000006     0.00000000E+00
DECAY   2000011     0.00000000E+00
DECAY   2000013     0.00000000E+00
DECAY   2000015     0.00000000E+00
DECAY   1000001     0.00000000E+00
DECAY   1000002     0.00000000E+00
DECAY   1000003     0.00000000E+00
DECAY   1000004     0.00000000E+00
DECAY   1000005     0.00000000E+00
DECAY   1000006     0.00000000E+00
DECAY   1000011     0.00000000E+00
DECAY   1000012     0.00000000E+00
DECAY   1000013     0.00000000E+00
DECAY   1000014     0.00000000E+00
DECAY   1000015     0.00000000E+00
DECAY   1000016     0.00000000E+00

DECAY   1000021     1.00000000E+00
     0.00000000E+00    3         -6          6    1000022
     1.00000000E-01    3         -1          1    1000023
     1.00000000E-01    3         -2          2    1000023
     1.00000000E-01    3         -3          3    1000023
     1.00000000E-01    3         -4          4    1000023
     1.00000000E-01    3         -5          5    1000023
     1.25000000E-01    3         -2          1    1000024
     1.25000000E-01    3          2         -1    -1000024
     1.25000000E-01    3         -4          3    1000024
     1.25000000E-01    3          4         -3    -1000024

DECAY   1000023     1.00000000E-01
     1.00000000E+00    2         22    1000022
DECAY   1000024     1.00000000E-01
     0.0000000    3     1000022        -1      2
     1.0000000    2     1000022        24

DECAY   1000022     0.00000000E+00
"""

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    RandomizedParameters = cms.VPSet(),
)


model = "T5Wg"
# weighted average of matching efficiencies for the full scan
# must equal the number entered in McM generator params
mcm_eff = 0.253


# Fit to gluino-gluino cross-section in fb
def xsec(mass):
    return 4.563e+17*math.pow(mass, -4.761*math.exp(5.848e-05*mass))

def matchParams(mass):
  if mass>599 and  mass<799: return 118., 0.235
  elif mass<999: return 128., 0.235
  elif mass<1199: return 140., 0.235
  elif mass<1399: return 143., 0.245
  elif mass<1499: return 147., 0.255
  elif mass<1799: return 150., 0.267
  elif mass<2099: return 156., 0.290
  elif mass<2301: return 160., 0.315
  else: sys.exit("grid_utils::matchParams - Mass out of range %i" % mass)



# Parameters that define the grid in the bulk and diagonal
class gridBlock:
  def __init__(self, xmin, xmax, xstep, ystep, diagStep, minEvents):
    self.xmin = xmin
    self.xmax = xmax
    self.xstep = xstep
    self.ystep = ystep
    self.diagStep = diagStep
    self.minEvents = minEvents


# Parameters to define the grid
goalLumi = 1600
minLumi = 80
maxEvents = 150
maxDM = 300

scanBlocks = []
scanBlocks.append(gridBlock(800, 1000, 100, 100, 100,40))
scanBlocks.append(gridBlock(1000, 2000, 50, 100, 50,40))
scanBlocks.append(gridBlock(2000, 2101, 50, 100, 50,20))
minDM = 10
ymin, ymed, ymax = 200, 700, 2100
hlines_below_grid = [10,25,50,100,150]
hline_xmin = 1000


# Number of events for mass point, in thousands
def events(mass):
  xs = xsec(mass)
  nev = min(goalLumi*xs, maxEvents*1000)
  if nev < xs*minLumi: nev = xs*minLumi
  nev = max(nev/1000, minEvents)
  return math.ceil(nev) # Rounds up


# -------------------------------
#    Constructing grid

cols = []
Nevents = []
xmin, xmax = 9999, 0
for block in scanBlocks:
  Nbulk, Ndiag = 0, 0
  minEvents = block.minEvents
  for mx in range(block.xmin, block.xmax, block.diagStep):
    xmin = min(xmin, block.xmin)
    xmax = max(xmax, block.xmax)
    col = []
    my = 0
    begDiag = max(ymed, mx-maxDM)
    # Adding bulk points
    if (mx-block.xmin)%block.xstep == 0:
      # adding extra horizontal lines
      yrange = []
      if (mx>=hline_xmin): yrange.extend(hlines_below_grid)
      else: yrange.append(hlines_below_grid[0])
      yrange.extend(range(ymin, begDiag, block.ystep))
      for my in yrange:
        if my > ymax: continue
        nev = events(mx)
        col.append([mx,my, nev])
        Nbulk += nev
    # Adding diagonal points
    for my in range(begDiag, mx-minDM+1, block.diagStep):
      if my > ymax: continue
      nev = events(mx)
      col.append([mx,my, nev])
      Ndiag += nev
    if block.diagStep<100:
      my = mx-25
      nev = events(mx)
      col.append([mx,my, nev])
      Ndiag += nev
    if my !=  mx-minDM and mx-minDM <= ymax:
      my = mx-minDM
      nev = events(mx)
      col.append([mx,my, nev])
      Ndiag += nev
    cols.append(col)
  Nevents.append([Nbulk, Ndiag])

mpoints = []
for col in cols: mpoints.extend(col)


for point in mpoints:
    mglu, mchi = point[0], point[1]
    qcut, tru_eff = matchParams(mglu)
    wgt = point[2]*(mcm_eff/tru_eff)
    
    if mchi==0: mchi = 1
    slhatable = baseSLHATable.replace('%MGLU%','%e' % mglu)
    slhatable = slhatable.replace('%MCHI%','%e' % mchi)

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
            '24:mMin = 7.', # allows W offshelness to go down to 7 GeV (very low LSP points in the scan)
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
            GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/SMS-GlGl/SMS-GlGl_mGl-%i_tarball.tar.xz' % mglu),
            ConfigDescription = cms.string('%s_%i_%i' % (model, mglu, mchi)),
            SLHATableForPythia8 = cms.string('%s' % slhatable),
            PythiaParameters = basePythiaParameters,
        ),
    )
