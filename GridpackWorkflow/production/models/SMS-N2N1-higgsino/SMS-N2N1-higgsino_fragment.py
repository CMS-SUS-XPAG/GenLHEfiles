import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

import math

baseSLHATable="""
#
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
        35     1.00000000E+05
        36     1.00000000E+05
        37     1.00000000E+05
        6      1.72500000E+02
   1000001     1.00000000E+05    # ~d_L
   2000001     1.00000000E+05   # ~d_R
   1000002     1.00000000E+05    # ~u_L
   2000002     1.00000000E+05   # ~u_R
   1000003     1.00000000E+05    # ~s_L
   2000003     1.00000000E+05   # ~s_R
   1000004     1.00000000E+05    # ~c_L
   2000004     1.00000000E+05   # ~c_R
   1000005     1.00000000E+05   # ~b_1
   2000005     1.00000000E+05   # ~b_2
   1000006     1.00000000E+05   # ~t_1
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
   1000022     %MN1%            # ~chi_10
   1000023     %MN2%            # ~chi_20
   1000025     1.00000000E+05   # ~chi_30
   1000035     1.00000000E+05   # ~chi_40
   1000024     %MC1%            # ~chi_1+
   1000037     1.00000000E+05   # ~chi_2+
#
#
#
#         PDG            Width
DECAY         6     1.134E+00        # top decays
DECAY   2000006     0.00000000E+00   # stop2 decays
DECAY   1000005     0.00000000E+00   # sbottom1 decays
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
DECAY   1000006     0.00000000E+00   # stop1 decays
DECAY   1000021     0.00000000E+00   # gluino decays
DECAY   1000022     0.00000000E+00   # neutralino1 decays
DECAY   1000023     0.10000000E+00   # neutralino2 decays
    0.00000000E+00   3    1000022   11   -11  #dummy decay
    1.00000000E+00   2    1000022   23
"""

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

model = "SMS-N2N1-higgsino"
process = "Higgsino-N2N1"

# Number of events for mass point, in thousands
nevt = 100

mN2s = [100., 120., 140., 160., 180., 200., 220., 240. ]
dMs  = [7.5, 10., 15., 20., 30., 40.]
mN1s = []
mC1s = []
# -------------------------------
#    Constructing grid

mpoints = []
for mN2 in mN2s:
  for dM in dMs:    
    mN1 = mN2 - dM
    mN1s.append(mN1)
    mC1 = (mN2+mN1)/2.
    mC1s.append(mC1)
    mpoints.append([mN2,mN1,nevt])

for point in mpoints:

    mn2, mn1 = point[0], point[1]
    mc1 = (mn2+mn1)/2.

    mn2Str = str(int(mn2))
    mn1Str = "{0:.2f}".format(mn1).replace(".","p")
    mc1Str = "{0:.2f}".format(mc1).replace(".","p")

    qcut, tru_eff = matchParams(mn2)
    wgt = point[2]*(mcm_eff/tru_eff)
    
    slhatable = baseSLHATable.replace('%MN2%','%e' % mn2)
    slhatable = slhatable.replace('%MC1%','%e' % mc1)
    slhatable = slhatable.replace('%MN1%','%e' % mn1)

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
            '23:onMode = off',
            '23:onIfAny = 11 13 15',
            '23:mMin = 0.1',
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
            GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/%s/%s_mN2-%s_mN1-%s_tarball.tar.xz' % (process,process,mn2Str,mn1Str)),
            ConfigDescription = cms.string('%s_%s_%s' % (model, mn2Str,mn1Str)),
            SLHATableForPythia8 = cms.string('%s' % slhatable),
            PythiaParameters = basePythiaParameters,
        ),
    )
