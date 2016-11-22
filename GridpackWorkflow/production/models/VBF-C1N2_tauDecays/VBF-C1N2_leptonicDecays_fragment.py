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
   1000023     %MN2%            # ~chi_20
   1000025     1.00000000E+05   # ~chi_30
   1000035     1.00000000E+05   # ~chi_40
   1000024     %MN2%            # ~chi_1+
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
DECAY   1000021     0.00000000E+00   # gluino decays
DECAY   1000022     0.00000000E+00   # neutralino1 decays
DECAY   1000025     0.00000000E+00   # neutralino3 decays
DECAY   1000035     0.00000000E+00   # neutralino4 decays
DECAY   1000037     0.00000000E+00   # chargino2+ decays
"""

large_dm = """
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
"""

small_dm = """
DECAY   1000023     0.10000000E+00   # neutralino2 decays
    0.00000000E+00    3    1000022    11   -11
    1.00000000E+00    2    1000022    23
DECAY   1000024     0.10000000E+00   # chargino1+ decays
    1.00000000E+00    2    1000022    211
DECAY   1000011     0.00000000E+00   # selectron_L decays
DECAY   2000011     0.00000000E+00   # selectron_R decays
DECAY   1000012     0.00000000E+00   # snu_elL decays
DECAY   1000013     0.00000000E+00   # smuon_L decays
DECAY   2000013     0.00000000E+00   # smuon_R decays
DECAY   1000014     0.00000000E+00   # snu_muL decays
DECAY   1000015     0.00000000E+00   # stau_1 decays
DECAY   2000015     0.00000000E+00   # stau_2 decays
DECAY   1000016     0.00000000E+00   # snu_tauL decays
"""

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    RandomizedParameters = cms.VPSet(),
)

model = 'VBF-C1N2_leptonic'

dmlist = [1,2]
dmlist.extend(range(5,51,5))

mpoints = []
for ix in range(100, 501, 50):
  for idm in dmlist:
    mpoints.append([ix, ix-idm])


for point in mpoints:
    mn2, mlsp = point[0], point[1]
     
    m_slep =mlsp + 0.5*(mn2-mlsp)
    if mlsp==0: mlsp = 1
    slhatable = baseSLHATable.replace('%MN2%','%e' % mn2)
    slhatable = slhatable.replace('%MLSP%','%e' % mlsp)
    slhatable = slhatable.replace('%MSTAU%','%e' % m_slep)

    if (mn2-mlsp)<=2:
      slhatable += small_dm
    else:
      slhatable += large_dm
        
    # base hadronizer, no jet matching
    basePythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        MassParameters = cms.vstring(
            '23:mMin = 0.1',
        ), 
       parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                   'MassParameters'
        )
    )

    generator.RandomizedParameters.append(
        cms.PSet(
            ConfigWeight = cms.double(1.), # evenly distributed
            GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/VBF-C1N2/v1/VBF-C1N2_mChi-%i_tarball.tar.xz' % mn2),
            ConfigDescription = cms.string('%s_%i_%i' % (model, mn2, mlsp)),
            SLHATableForPythia8 = cms.string('%s' % slhatable),
            PythiaParameters = basePythiaParameters,
        ),
    )
