# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/T1tbs_fragment.py --fileout file:T1tbs_1.root --eventcontent AODSIM --conditions 80X_mcRun2_asymptotic_v12 --customise_commands process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(50) \n process.source.firstRun = cms.untracked.uint32(1) \n process.generator.initialSeed = cms.untracked.uint32(1) --step LHE,GEN --python_filename jobcfg.py --no_exec -n 4
import FWCore.ParameterSet.Config as cms

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(4)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/T1tbs_fragment.py nevts:4'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string('file:T1tbs_1.root'),
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_v12', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
        JetMatchingParameters = cms.vstring('JetMatching:setMad = off', 
            'JetMatching:scheme = 1', 
            'JetMatching:merge = on', 
            'JetMatching:jetAlgorithm = 2', 
            'JetMatching:etaJetMax = 5.', 
            'JetMatching:coneRadius = 1.', 
            'JetMatching:slowJetPower = 1', 
            'JetMatching:qCut = 1.180000e+02', 
            'JetMatching:nQmatch = 5', 
            'JetMatching:nJetMax = 2', 
            'JetMatching:doShowerKt = off', 
            '25:m0 = 125.0'),
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings', 
            'JetMatchingParameters'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on')
    ),
    SLHATableForPythia8 = cms.string('\nBLOCK MASS  # Mass Spectrum\n# PDG code           mass       particle\n        25     1.00000000E+03\n        35     1.00000000E+03\n        36     1.00000000E+03\n        37     1.00000000E+03\n        6      1.72500000E+02\n   1000001     100000.0          # ~d_L\n   2000001     1.00000000E+05   # ~d_R\n   1000002     100000.0          # ~u_L\n   2000002     1.00000000E+05   # ~u_R\n   1000003     100000.0          # ~s_L\n   2000003     1.00000000E+05   # ~s_R\n   1000004     100000.0         # ~c_L\n   2000004     1.00000000E+05   # ~c_R\n   1000005     1.00000000E+05   # ~b_1\n   2000005     1.10000000E+05   # ~b_2\n   1000006     1.10000000E+05   # ~t_1\n   2000006     1.10000000E+05   # ~t_2\n   1000011     1.00000000E+04   # ~e_L\n   2000011     1.00000000E+04   # ~e_R\n   1000012     1.00000000E+04   # ~nu_eL\n   1000013     1.00000000E+04   # ~mu_L\n   2000013     1.00000000E+04   # ~mu_R\n   1000014     1.00000000E+04   # ~nu_muL\n   1000015     1.00000000E+04   # ~tau_1\n   2000015     1.00000000E+04   # ~tau_2\n   1000016     1.00000000E+04   # ~nu_tauL\n   1000021     7.500000e+02              # ~g\n   1000022     1.00000000E+05   # ~chi_10\n   1000023     1.00000000E+04   # ~chi_20\n   1000025     1.00000000E+04   # ~chi_30\n   1000035     1.00000000E+04   # ~chi_40\n   1000024     1.00000000E+05   # ~chi_1+\n   1000037     1.00000000E+04   # ~chi_2+\n# DECAY TABLE\n#         PDG            Width\nDECAY         6     1.134E+00        # top decays\nDECAY   1000006     0.00000000E+00   # stop2 decays\nDECAY   2000006     0.00000000E+00   # stop2 decays\nDECAY   1000005     0.00000000E+00   # sbottom1 decays\nDECAY   2000005     0.00000000E+00   # sbottom2 decays\n#         PDG            Width\nDECAY   1000011     0.00000000E+00   # selectron_L decays\nDECAY   2000011     0.00000000E+00   # selectron_R decays\nDECAY   1000013     0.00000000E+00   # smuon_L decays\nDECAY   2000013     0.00000000E+00   # smuon_R decays\nDECAY   1000015     0.00000000E+00   # stau_1 decays\nDECAY   2000015     0.00000000E+00   # stau_2 decays\n#         PDG            Width\nDECAY   1000012     0.00000000E+00   # snu_elL decays\nDECAY   1000014     0.00000000E+00   # snu_muL decays\nDECAY   1000016     0.00000000E+00   # snu_tauL decays\nDECAY   1000021     1.0000000E+00   # gluino decays\n#          BR         NDA      ID1       ID2\n     1.00000000E+00    3       6         5     3     # ~g -> t b s\nDECAY   1000024     0.0000000E+00   # chargino1 decays\nDECAY   1000022     0.00000000E+00   # neutralino1 decays\n'),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/SMS-GlGl/SMS-GlGl_mGl-750_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(4),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)


# Path and EndPath definitions
process.lhe_step = cms.Path(process.externalLHEProducer)
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.endjob_step,process.AODSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	if path in ['lhe_step']: continue
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 


# Customisation from command line
process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(50) 
process.source.firstRun = cms.untracked.uint32(1) 
process.generator.initialSeed = cms.untracked.uint32(1)

# Customisation from command line
process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(50) 
process.source.firstRun = cms.untracked.uint32(1) 
process.generator.initialSeed = cms.untracked.uint32(1)