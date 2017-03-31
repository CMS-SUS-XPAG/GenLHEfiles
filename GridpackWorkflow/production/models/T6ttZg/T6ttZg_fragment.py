import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

import math
import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

baseSLHATable="""
BLOCK MASS
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
   1000006     %MST%   # ~t_1
   2000006     1.00000000E+05   # ~t_2
   1000011     1.00000000E+05   # ~e_L
   2000011     1.00000000E+05   # ~e_R
   1000012     1.00000000E+05   # ~nu_eL
   1000013     1.00000000E+05   # ~mu_L
   2000013     1.00000000E+05   # ~mu_R
   1000014     1.00000000E+05   # ~nu_muL
   1000015     1.00000000E+05   # ~tau_1
   2000015     1.00000000E+05   # ~tau_2
   1000016     1.00000000E+05   # ~nu_tauL
   1000021     1.00000000E+05   # ~g
   1000022     1.00000000E+00
   1000023     %MCHI%
   1000024     1.00000000E+05
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
DECAY   1000006     1.00000000E+00   # stop1 decays
    0.00000000E+00    3    1000022      5     24  # dummy allowed decay, in order to turn on off-shell decays
    1.00000000E+00    2    1000023      6
DECAY   1000011     0.00000000E+00
DECAY   1000012     0.00000000E+00
DECAY   1000013     0.00000000E+00
DECAY   1000014     0.00000000E+00
DECAY   1000015     0.00000000E+00
DECAY   1000016     0.00000000E+00
DECAY   1000021     0.00000000E+00
DECAY   1000023     1.00000000E-01
     0.0000000    3     1000022        -1      1
     0.50000000E+00    2         23    1000022
     0.50000000E+00    2         22    1000022
DECAY   1000024     0.00000000E+00
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


model = "T6ttZg"
# weighted average of matching efficiencies for the full scan
# must equal the number entered in McM generator params
mcm_eff = 0.244
process = "StopStop"


# Fit to gluino-gluino cross-section in fb
def xsec(mass):
    if mass < 300: return 319925471928717.38*math.pow(mass, -4.10396285974583*math.exp(mass*0.0001317804474363))
    else: return 6953884830281245*math.pow(mass, -4.7171617288678069*math.exp(mass*6.1752771466190749e-05))

def matchParams(mass):
    if mass>99 and mass<199: return 62., 0.498
    elif mass<299: return 62., 0.361
    elif mass<399: return 62., 0.302
    elif mass<499: return 64., 0.275
    elif mass<599: return 64., 0.254
    elif mass<1299: return 68., 0.237
    elif mass<1801: return 70., 0.243
    else: return 70., 0.243


#### copy from grid.py
class gridBlock:
  def __init__(self, xmin, xmax, xstep, ystep, diagStep, minEvents):
    self.xmin = xmin
    self.xmax = xmax
    self.xstep = xstep
    self.ystep = ystep
    self.diagStep = diagStep
    self.minEvents = minEvents
    
model = "T6ttZg"
process = "StopStop"

# Number of events: min(goalLumi*xsec, maxEvents) (always in thousands)
goalLumi = 3200
minLumi = 1
maxEvents = 50
maxDM = 200

scanBlocks = []
scanBlocks.append(gridBlock(300, 1501, 100, 100, 50, 50))

minDM = 100
ymin, ymed, ymax = 100, 150, 1400
hlines_below_grid = [10,25,50,75]
hline_xmin = 800


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
    #if block.diagStep<100:
    #  my = mx-100
    #  nev = events(mx)
    #  col.append([mx,my, nev])
    #  Ndiag += nev
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
    mst, mchi = point[0], point[1]
    qcut, tru_eff = matchParams(mst)
    wgt = point[2]*(mcm_eff/tru_eff)
    
    slhatable = baseSLHATable.replace('%MST%','%e' % mst)
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
            '24:mMin = 0.1', # allows W offshelness to go down to 0.1 GeV (very low LSP points in the scan)
            '23:mMin = 0.1', # allows Z offshelness to go down to 0.1 GeV (very low LSP points in the scan)
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
            GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/SMS-StopStop/SMS-StopStop_mStop-%i_tarball.tar.xz' % mst),
            ConfigDescription = cms.string('%s_%i_%i' % (model, mst, mchi)),
            SLHATableForPythia8 = cms.string('%s' % slhatable),
            PythiaParameters = basePythiaParameters,
        ),
    )
