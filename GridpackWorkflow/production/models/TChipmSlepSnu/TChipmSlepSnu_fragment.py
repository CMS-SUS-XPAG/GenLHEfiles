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
   1000005     1.00000000E+05   # ~b_1
   2000005     1.00000000E+05   # ~b_2
   1000006     1.00000000E+05   # ~t_1
   2000006     1.00000000E+05   # ~t_2
   1000011     %MSTAU%          # ~e_L
   2000011     1.00000000E+05   # ~e_R
   1000012     %MSTAU%          # ~nu_eL
   1000013     %MSTAU%          # ~mu_L
   2000013     1.00000000E+05   # ~mu_R
   1000014     %MSTAU%          # ~nu_muL
   1000015     %MSTAU%          # ~tau_1
   2000015     1.00000000E+05   # ~tau_2
   1000016     %MSTAU%          # ~nu_tauL
   1000021     1.00000000E+05   # ~g
   1000022     %MLSP%            # ~chi_10
   1000023     1.00000000E+05   # ~chi_20
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
DECAY   1000023     0.00000000E+00   # neutralino2 decays
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

# weighted average of matching efficiencies for the full scan
# must equal the number entered in McM generator params
mcm_eff = 0.460

def matchParams(mass):
    if mass < 125: return 76,0.63
    elif mass < 150: return 76,0.6
    elif mass < 225: return 76,0.57
    elif mass < 300: return 76,0.53
    elif mass < 400: return 76,0.5
    elif mass < 525: return 76,0.47
    elif mass < 725: return 76,0.44
    else: return 76,0.42

model = "TChipmSlepSnu"

# Number of events for mass point, in thousands
nevt = 10

diag = 50
xmin, xmax, xstep = 100, 800, 25
ymin, ymax, ystep = 0, 600, 25 

# -------------------------------
#    Constructing grid

mpoints = []
for mx in range(xmin, xmax+1, xstep):
  ylist = []
  if mx > ymax + diag: 
    ylist.extend(range(ymin, ymax+1, ystep))
  else:
    ylist.extend(range(ymin, mx-diag+1, ystep))
  for my in ylist:
    mpoints.append([mx,my,nevt])
    
for point in mpoints:
    mc1, mlsp = point[0], point[1]
    qcut, tru_eff = matchParams(mc1)
    wgt = point[2]*(mcm_eff/tru_eff)
    
    m_slep = mlsp + 0.5*(mc1-mlsp)
    if mlsp==0: mlsp = 1
    slhatable = baseSLHATable.replace('%MC1%','%e' % mc1)
    slhatable = slhatable.replace('%MLSP%','%e' % mlsp)
    slhatable = slhatable.replace('%MSTAU%','%e' % m_slep)

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
            GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/SMS-C1C1/SMS-C1C1_mC1-%i_tarball.tar.xz' % mc1),
            ConfigDescription = cms.string('%s_%i_%i' % (model, mc1, mlsp)),
            SLHATableForPythia8 = cms.string('%s' % slhatable),
            PythiaParameters = basePythiaParameters,
        ),
    )
