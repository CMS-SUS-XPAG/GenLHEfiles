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
    'JetMatching:qCut = 58', #this is the actual merging scale
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
BLOCK MODSEL  # Model selection
     1     0   # Low energy spectrum
#
BLOCK SMINPUTS  # Standard Model inputs
         1     1.27934000E+02   # alpha_em^-1(M_Z)^MSbar
         2     1.16639000E-05   # G_F [GeV^-2]
         3     1.17200000E-01   # alpha_S(M_Z)^MSbar
         4     9.11870000E+01   # M_Z pole mass
         5     4.25000000E+00   # mb(mb)^MSbar
         6     1.75000000E+02   # mt pole mass
         7     1.77700000E+00   # mtau pole mass
#
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
        25     1.00000000E+03
        35     1.00000000E+03
        36     1.00000000E+03
        37     1.00000000E+03
        6      1.72500000E+02
   1000001     100000.0          # ~d_L
   2000001     1.00000000E+05   # ~d_R
   1000002     100000.0          # ~u_L
   2000002     1.00000000E+05   # ~u_R
   1000003     100000.0          # ~s_L
   2000003     1.00000000E+05   # ~s_R
   1000004     100000.0          # ~c_L
   2000004     1.00000000E+05   # ~c_R
   1000005     1.00000000E+05   # ~b_1
   2000005     1.10000000E+05   # ~b_2
   1000006     1.10000000E+05   # ~t_1
   2000006     1.10000000E+05   # ~t_2
   1000011     %MSLEP%   # ~e_L
   2000011     1.00000000E+04   # ~e_R
   1000012     %MSLEP%   # ~nu_eL
   1000013     %MSLEP%   # ~mu_L
   2000013     1.00000000E+04   # ~mu_R
   1000014     %MSLEP%   # ~nu_muL
   1000015     %MSLEP%   # ~tau_1
   2000015     1.00000000E+04   # ~tau_2
   1000016     %MSLEP%   # ~nu_tauL
   1000021     1.00000000E+04   # ~g
   1000022     %MN1%           # ~chi_10
   1000023     %MN2%            # ~chi_20
   1000025     1.00000000E+04   # ~chi_30
   1000035     1.00000000E+04   # ~chi_40
   1000024     %MC1%            # ~chi_1+
   1000037     1.00000000E+04   # ~chi_2+
#         PDG            Width
DECAY         6     1.134E+00        # top decays
DECAY   2000006     0.00000000E+00   # stop2 decays
DECAY   1000005     0.00000000E+00   # sbottom1 decays
DECAY   2000005     0.00000000E+00   # sbottom2 decays
#
DECAY   1000011     0.10000000E+00   # selectron_L decays
#           BR         NDA      ID1       ID2       ID3
1.00000000E+00    2    1000022    11
DECAY   2000011     0.00000000E+00   # selectron_R decays
DECAY   1000012     0.10000000E+00   # snu_elL decays
#           BR         NDA      ID1       ID2       ID3
1.00000000E+00    2    1000022    12
DECAY   1000013     0.10000000E+00   # smuon_L decays
#           BR         NDA      ID1       ID2       ID3
1.00000000E+00    2    1000022    13
DECAY   2000013     0.00000000E+00   # smuon_R decays
DECAY   1000014     0.10000000E+00   # snu_muL decays
#           BR         NDA      ID1       ID2       ID3
1.00000000E+00    2    1000022    14
DECAY   1000015     0.10000000E+00   # stau_1 decays
#           BR         NDA      ID1       ID2       ID3
1.00000000E+00    2    1000022    15
DECAY   2000015     0.00000000E+00   # stau_2 decays
DECAY   1000016     0.10000000E+00   # snu_tauL decays
#           BR         NDA      ID1       ID2       ID3
1.00000000E+00    2    1000022    16
DECAY   1000021     0.00000000E+00   # gluino decays
DECAY   1000022     0.00000000E+00   # neutralino1 decays
DECAY   1000023     0.10000000E+00   # neutralino2 decays
#           BR         NDA      ID1       ID2       ID3
0.16666666E+00    2    1000011    -11
0.16666666E+00    2    -1000011    11
0.16666666E+00    2    1000013    -13
0.16666666E+00    2    -1000013    13
0.16666666E+00    2    1000015    -15
0.16666666E+00    2    -1000015    15
DECAY   1000024     0.10000000E+00   # chargino1+ decays
#           BR         NDA      ID1       ID2       ID3
0.16666666E+00    2    -1000011    12
0.16666666E+00    2    1000012    -11
0.16666666E+00    2    -1000013    14
0.16666666E+00    2    1000014    -13
0.16666666E+00    2    -1000015    16
0.16666666E+00    2    1000016    -15
DECAY   1000025     0.00000000E+00   # neutralino3 decays
DECAY   1000035     0.00000000E+00   # neutralino4 decays
DECAY   1000037     0.00000000E+00   # chargino2+ decays

BLOCK NMIX  # Neutralino Mixing Matrix
  1  1     0.00000000E+00   # N_11
  1  2     0.00000000E+00  # N_12
  1  3     0.70710678E+00  # N_13
  1  4     0.70710678E+00  # N_14
  2  1     0.00000000E+00  # N_21
  2  2     0.00000000E+00  # N_22
  2  3     0.70710678E+00  # N_23
  2  4    -0.70710678E+00  # N_24
  3  1     0.00000000E+00  # N_31
  3  2     0.00000000E+00  # N_32
  3  3     0.00000000E+00  # N_33
  3  4     0.00000000E+00  # N_34
  4  1     0.00000000E+00  # N_41
  4  2     0.00000000E+00  # N_42
  4  3     0.00000000E+00  # N_43
  4  4     0.00000000E+00  # N_44
#
BLOCK UMIX  # Chargino Mixing Matrix U
  1  1     0.00000000E+00   # U_11
  1  2     1.00000000E+00   # U_12
  2  1     0.00000000E+00   # U_21
  2  2     0.00000000E+00   # U_22
#
BLOCK VMIX  # Chargino Mixing Matrix V
  1  1     0.00000000E+00   # V_11
  1  2     1.00000000E+00   # V_12
  2  1     0.00000000E+00   # V_21
  2  2     0.00000000E+00   # V_22
#
BLOCK STOPMIX  # Stop Mixing Matrix
  1  1     0.00000000E+00   # cos(theta_t)
  1  2     0.00000000E+00   # sin(theta_t)
  2  1     0.00000000E+00   # -sin(theta_t)
  2  2     0.00000000E+00   # cos(theta_t)
#
BLOCK SBOTMIX  # Sbottom Mixing Matrix
  1  1     0.00000000E+00   # cos(theta_b)
  1  2     0.00000000E+00   # sin(theta_b)
  2  1     0.00000000E+00   # -sin(theta_b)
  2  2     0.00000000E+00   # cos(theta_b)
#
BLOCK STAUMIX  # Stau Mixing Matrix
  1  1     CT # cos(theta_tau)
  1  2     ST # sin(theta_tau)
  2  1    -ST # -sin(theta_tau)
  2  2     CT # cos(theta_tau)
#
BLOCK ALPHA  # Higgs mixing
           0.00000000E+00   # Mixing angle in the neutral Higgs boson sector
#
BLOCK HMIX Q=  1.00000000E+05  # DRbar Higgs Parameters
         1     1.00000000E+05   # mu(Q)               
         2     1.00000000E+05   # tanbeta(Q)          
         3     1.00000000E+05   # vev(Q)              
         4     1.00000000E+05   # MA^2(Q)             
#
BLOCK GAUGE Q=  1.00000000E+03  # The gauge couplings
     1     3.60000000E-01   # gprime(Q) DRbar
     2     6.46000000E-01   # g(Q) DRbar
     3     1.10000000E+00   # g3(Q) DRbar
#
BLOCK AU Q=  1.00000000E+03  # The trilinear couplings
  1  1    0.00000000E+00   # A_u(Q) DRbar
  2  2    0.00000000E+00   # A_c(Q) DRbar
  3  3    0.00000000E+00   # A_t(Q) DRbar
#
BLOCK AD Q=  1.00000000E+03  # The trilinear couplings
  1  1    0.00000000E+00   # A_d(Q) DRbar
  2  2    0.00000000E+00   # A_s(Q) DRbar
  3  3    0.00000000E+00   # A_b(Q) DRbar
#
BLOCK AE Q=  1.00000000E+03  # The trilinear couplings
  1  1    0.00000000E+00   # A_e(Q) DRbar
  2  2    0.00000000E+00   # A_mu(Q) DRbar
  3  3    0.00000000E+00   # A_tau(Q) DRbar
#
BLOCK Yu Q=  1.00000000E+03  # The Yukawa couplings
  1  1     0.00000000E+00   # y_u(Q) DRbar
  2  2     0.00000000E+00   # y_c(Q) DRbar
  3  3     8.74064983E-01   # y_t(Q) DRbar
#
BLOCK Yd Q=  1.00000000E+03  # The Yukawa couplings
  1  1     0.00000000E+00   # y_d(Q) DRbar
  2  2     0.00000000E+00   # y_s(Q) DRbar
  3  3     1.35994628E-01   # y_b(Q) DRbar
#
BLOCK Ye Q=  1.00000000E+03  # The Yukawa couplings
  1  1     0.00000000E+00   # y_e(Q) DRbar
  2  2     0.00000000E+00   # y_mu(Q) DRbar
  3  3     1.00415339E-01   # y_tau(Q) DRbar
#
BLOCK MSOFT Q=  1.00000000E+03  # The soft SUSY breaking masses at the scale Q
         1     1.00000000E+05   # M_1
         2     1.00000000E+05   # M_2
         3     1.00000000E+05   # M_3
        21     1.00000000E+05   # M^2_Hd
        22     1.00000000E+05   # M^2_Hu
        31     1.00000000E+05   # M_eL
        32     1.00000000E+05   # M_muL
        33     1.00000000E+05   # M_tauL
        34     1.00000000E+05   # M_eR
        35     1.00000000E+05   # M_muR
        36     1.00000000E+05   # M_tauR
        41     1.00000000E+05   # M_q1L
        42     1.00000000E+05   # M_q2L
        43     1.00000000E+05   # M_q3L
        44     1.00000000E+05   # M_uR
        45     1.00000000E+05   # M_cR
        46     1.00000000E+05   # M_tR
        47     1.00000000E+05   # M_dR
        48     1.00000000E+05   # M_sR
        49     1.00000000E+05   # M_bR
"""

generator = cms.EDFilter("Pythia8GeneratorFilter",
  maxEventsToPrint = cms.untracked.int32(1),
  pythiaPylistVerbosity = cms.untracked.int32(1),
  filterEfficiency = cms.untracked.double(1.0),
  pythiaHepMCVerbosity = cms.untracked.bool(False),
  comEnergy = cms.double(13000.),
  RandomizedParameters = cms.VPSet(),
)

### defining masses for scan

CharginoMasses = [300,700,800]

for m_c1 in CharginoMasses:

    slhatable = baseSLHATable.replace('%MN2%','%e' %m_c1)
    slhatable = slhatable.replace('%MC1%','%e' %m_c1)

    for i in range(18):
        m_lsp = 0. + i*50 #need to update this.
        m_slep = m_lsp+ 0.5*(m_c1-m_lsp) # hmmmmmm? what are these
        slhatable = slhatable.replace('%MN1%','%e' % m_lsp)
        slhatable = slhatable.replace('%MSLEP%','%e' % m_slep)
  
        generator.RandomizedParameters.append(
           cms.PSet(
           ConfigWeight = cms.double(1.0),
           GridpackPath =  cms.string('/hadoop/cms/store/user/mliu/SUSYMC/SMS-TChiSlepSnu_mChi-%i_tarball.tar.xz' % m_c1),
           ConfigDescription = cms.string('Chargino = %e MLSP = %e' % (m_c1,m_lsp)),
           SLHATableForPythia8 = cms.string('%s' % slhatable),
           PythiaParameters = basePythiaParameters,
    ),
  )
