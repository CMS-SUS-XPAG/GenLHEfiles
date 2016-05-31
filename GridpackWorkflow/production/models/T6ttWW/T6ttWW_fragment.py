import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

import math

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
   1000005     %MSBO%           # ~b_1
   2000005     1.10000000E+05   # ~b_2
   1000006     1.10000000E+05   # ~t_1
   2000006     1.10000000E+05   # ~t_2
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
   1000022     50               # ~chi_10
   1000023     1.00000000E+05   # ~chi_20
   1000025     1.00000000E+05   # ~chi_30
   1000035     1.00000000E+05   # ~chi_40
   1000024     %MC1%            # ~chi_1+
   1000037     1.00000000E+05   # ~chi_2+
#
#
#
#         PDG            Width
DECAY   1000006     0.00000000E+00   # stop2 decays
DECAY   2000006     0.00000000E+00   # stop2 decays
DECAY   2000005     0.00000000E+00   # sbottom2 decays
#
#         PDG            Width
DECAY   1000011     0.00000000E+00   # selectron_L decays
DECAY   2000011     0.00000000E+00   # selectron_R decays
DECAY   1000013     0.00000000E+00   # smuon_L decays
DECAY   2000013     0.00000000E+00   # smuon_R decays
DECAY   1000015     0.00000000E+00   # stau_1 decays
DECAY   2000015     0.00000000E+00   # stau_2 decays
#
#         PDG            Width
DECAY   1000012     0.00000000E+00   # snu_elL decays
DECAY   1000014     0.00000000E+00   # snu_muL decays
DECAY   1000016     0.00000000E+00   # snu_tauL decays


DECAY   1000005     1.00000000E+00   # sbottom1 decays
#          BR         NDA      ID1       ID2
     0.00000E+00    2     1000022         5  #dummy decay to enable off-shell tops
     1.00000E+00    2     -1000024        6

DECAY   1000021     0.00000000E+00   # gluino decays
DECAY   1000022     0.00000000E+00   # neutralino1 decays
DECAY   1000024     0.10000000E+00   # chargino1 decays
#          BR         NDA      ID1       ID2
     0.00000E+00    3     1000022         2     -1  #dummy decay to enable off-shell Ws
     1.00000E+00    2     1000022         24
"""

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    RandomizedParameters = cms.VPSet(),
)


model = "T6ttWW"
# weighted average of matching efficiencies for the full scan
# must equal the number entered in McM generator params
mcm_eff = 0.25

# Fit to sbottom-sbottom cross-section in fb
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
    else: return 70., 0.243

# Parameters that define the grid in the bulk and diagonal
class gridBlock:
  def __init__(self, xmin, xmax, xstep, ystep, diagStep):
    self.xmin = xmin
    self.xmax = xmax
    self.xstep = xstep
    self.ystep = ystep
    self.diagStep = diagStep
    
# Number of events: min(goalLumi*xsec, maxEvents) (always in thousands)
goalLumi = 3200
minLumi = 30
minEvents, maxEvents = 40, 100
minDM, midDM, maxDM = 25, 200, 300
bandStep = 50

scanBlocks = []
scanBlocks.append(gridBlock(300, 500, 50, 100, 25))
scanBlocks.append(gridBlock(500, 1201, 50, 100, 25))

ymin, ymed, ymax = 100, 250, 1200
hlines_below_grid = [75,125,150]
hline_xmin = 500


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
  for mx in range(block.xmin, block.xmax, min(bandStep, block.diagStep)):
    xmin = min(xmin, block.xmin)
    xmax = max(xmax, block.xmax)
    col = []
    my = 0
    begBand = min(max(ymed, mx-maxDM), mx-minDM)
    begDiag = min(max(ymed, mx-midDM), mx-minDM)
    # Adding bulk points
    if (mx-block.xmin)%block.xstep == 0 :
      # adding extra horizontal lines
      yrange = []
      if (mx>=hline_xmin): yrange.extend(hlines_below_grid)
      else: yrange.append(hlines_below_grid[0])
      yrange.extend(range(ymin, begBand, block.ystep))
      for my in yrange:      
        if my > ymax: continue
        nev = events(mx)
        col.append([mx,my, nev])
        Nbulk += nev
    # Adding diagonal points in inside band
    if (mx-block.xmin)%bandStep == 0 :
      for my in range(begBand, mx-midDM, bandStep):
        if my > ymax: continue
        nev = events(mx)
        col.append([mx,my, nev])
        Ndiag += nev
    # Adding diagonal points in band closest to outer diagonal
    for my in range(begDiag, mx-minDM+1, block.diagStep):
      if my > ymax: continue
      nev = events(mx)
      col.append([mx,my, nev])
      Ndiag += nev
    if(my !=  mx-minDM and mx-minDM <= ymax):
      my = mx-minDM
      nev = events(mx)
      col.append([mx,my, nev])
      Ndiag += nev
    cols.append(col)
  Nevents.append([Nbulk, Ndiag])

mpoints = []
for col in cols: mpoints.extend(col)

for point in mpoints:
    msbo, mnlsp = point[0], point[1]
    qcut, tru_eff = matchParams(msbo)
    wgt = point[2]*(mcm_eff/tru_eff)
    
    if mnlsp==0: mnlsp = 1
    slhatable = baseSLHATable.replace('%MSBO%','%e' % msbo)
    slhatable = slhatable.replace('%MC1%','%e' % mnlsp)

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
            GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/SMS-SbotSbot/SMS-SbotSbot_mSbot-%i_tarball.tar.xz' % msbo),
            ConfigDescription = cms.string('%s_%i_%i' % (model, msbo, mnlsp)),
            SLHATableForPythia8 = cms.string('%s' % slhatable),
            PythiaParameters = basePythiaParameters,
        ),
    )
