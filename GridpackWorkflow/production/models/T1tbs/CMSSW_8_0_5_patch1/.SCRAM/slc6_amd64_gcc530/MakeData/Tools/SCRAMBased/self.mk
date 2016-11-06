ifeq ($(strip $(PhysicsToolsPatAlgos_plugins)),)
PhysicsToolsPatAlgos_plugins := self/src/PhysicsTools/PatAlgos/plugins
PhysicsToolsPatAlgos_plugins_LOC_USE := self cmssw PhysicsTools/PatAlgos FWCore/Framework FWCore/ParameterSet FWCore/MessageLogger FWCore/MessageService L1Trigger/GlobalTriggerAnalyzer HLTrigger/HLTcore DataFormats/PatCandidates DataFormats/BTauReco DataFormats/JetReco DataFormats/TrackReco DataFormats/Candidate DataFormats/HeavyIonEvent PhysicsTools/PatUtils CondFormats/JetMETObjects CommonTools/CandAlgos JetMETCorrections/Objects JetMETCorrections/JetCorrector TrackingTools/TransientTrack SimDataFormats/Track SimDataFormats/Vertex SimGeneral/HepPDTRecord RecoMET/METAlgorithms RecoEgamma/EgammaTools TrackingTools/IPTools root
PhysicsTools/PatAlgos_relbigobj+=PhysicsToolsPatAlgos_plugins
endif
ifeq ($(strip $(DQM/Integration)),)
src_DQM_Integration := self/DQM/Integration
DQM/Integration  := src_DQM_Integration
src_DQM_Integration_BuildFile    := $(RELEASETOP)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
src_DQM_Integration_EX_USE := $(foreach d, FWCore/Catalog RelationalAccess DataFormats/Provenance FWCore/Framework self cmssw CoralBase FWCore/ServiceRegistry FWCore/ParameterSet,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
ALL_EXTERNAL_PRODS += src_DQM_Integration
endif

ifeq ($(strip $(FastSimulation/TrackingRecHitProducer)),)
FastSimulationTrackingRecHitProducer := self/FastSimulation/TrackingRecHitProducer
FastSimulation/TrackingRecHitProducer := FastSimulationTrackingRecHitProducer
FastSimulationTrackingRecHitProducer_BuildFile    := $(RELEASETOP)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
FastSimulationTrackingRecHitProducer_EX_USE := $(foreach d, self cmssw DataFormats/Common DataFormats/DetId DataFormats/GeometrySurface DataFormats/GeometryVector DataFormats/SiPixelCluster DataFormats/SiPixelDetId DataFormats/SiStripCluster DataFormats/SiStripDetId DataFormats/TrackerRecHit2D DataFormats/TrackingRecHit FWCore/Framework FWCore/MessageLogger FWCore/ParameterSet FWCore/PluginManager FWCore/ServiceRegistry FWCore/Utilities FastSimDataFormats/External FastSimulation/Utilities Geometry/CommonDetUnit Geometry/CommonTopologies Geometry/Records Geometry/TrackerGeometryBuilder MagneticField/Engine MagneticField/Records RecoLocalTracker/ClusterParameterEstimator RecoLocalTracker/SiPixelRecHits RecoLocalTracker/Records SimDataFormats/CrossingFrame SimDataFormats/EncodedEventId SimDataFormats/TrackingHit boost clhep gsl,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
FastSimulationTrackingRecHitProducer_EX_LIB   := FastSimulationTrackingRecHitProducer
ALL_EXTERNAL_PRODS += FastSimulationTrackingRecHitProducer
FastSimulationTrackingRecHitProducer_CLASS := LIBRARY
FastSimulation/TrackingRecHitProducer_relbigobj+=FastSimulationTrackingRecHitProducer
endif
ifeq ($(strip $(FastSimulation/Event)),)
FastSimulationEvent := self/FastSimulation/Event
FastSimulation/Event := FastSimulationEvent
FastSimulationEvent_BuildFile    := $(RELEASETOP)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
FastSimulationEvent_EX_USE := $(foreach d, self cmssw DataFormats/HepMCCandidate DataFormats/Candidate DataFormats/Math DataFormats/Provenance FWCore/ParameterSet FastSimulation/BaseParticlePropagator FastSimulation/Particle FastSimulation/Utilities SimDataFormats/Track SimDataFormats/Vertex SimDataFormats/GeneratorProducts FastSimDataFormats/NuclearInteractions SimGeneral/HepPDTRecord hepmc,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
FastSimulationEvent_EX_LIB   := FastSimulationEvent
ALL_EXTERNAL_PRODS += FastSimulationEvent
FastSimulationEvent_CLASS := LIBRARY
FastSimulation/Event_relbigobj+=FastSimulationEvent
endif
ifeq ($(strip $(PhysicsTools/PatAlgos)),)
PhysicsToolsPatAlgos := self/PhysicsTools/PatAlgos
PhysicsTools/PatAlgos := PhysicsToolsPatAlgos
PhysicsToolsPatAlgos_BuildFile    := $(RELEASETOP)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
PhysicsToolsPatAlgos_EX_USE := $(foreach d, self cmssw DataFormats/Candidate DataFormats/Common DataFormats/EgammaCandidates DataFormats/EgammaReco DataFormats/JetReco DataFormats/Math DataFormats/METReco DataFormats/MuonReco DataFormats/PatCandidates DataFormats/TauReco DataFormats/TrackReco DataFormats/VertexReco FWCore/Framework FWCore/ParameterSet FWCore/ServiceRegistry FWCore/Utilities PhysicsTools/PatUtils PhysicsTools/Utilities PhysicsTools/IsolationAlgos Geometry/CaloTopology RecoEgamma/EgammaTools clhep,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
PhysicsToolsPatAlgos_EX_LIB   := PhysicsToolsPatAlgos
ALL_EXTERNAL_PRODS += PhysicsToolsPatAlgos
PhysicsToolsPatAlgos_CLASS := LIBRARY
PhysicsTools/PatAlgos_relbigobj+=PhysicsToolsPatAlgos
endif
ifeq ($(strip $(EventFilterHcalRawToDigiFiltersPlugins)),)
EventFilterHcalRawToDigiFiltersPlugins := self/src/EventFilter/HcalRawToDigi/plugins
EventFilterHcalRawToDigiFiltersPlugins_LOC_USE := self cmssw DataFormats/HcalDetId DataFormats/HcalDigi DataFormats/FEDRawData CondFormats/HcalObjects CalibFormats/HcalObjects FWCore/Framework FWCore/MessageLogger boost zlib EventFilter/HcalRawToDigi
EventFilter/HcalRawToDigi_relbigobj+=EventFilterHcalRawToDigiFiltersPlugins
endif
ifeq ($(strip $(EventFilterHcalRawToDigiPlugins)),)
EventFilterHcalRawToDigiPlugins := self/src/EventFilter/HcalRawToDigi/plugins
EventFilterHcalRawToDigiPlugins_LOC_USE := self cmssw DataFormats/HcalDetId DataFormats/HcalDigi DataFormats/FEDRawData CondFormats/HcalObjects CalibFormats/HcalObjects FWCore/Framework FWCore/MessageLogger boost zlib EventFilter/HcalRawToDigi
EventFilter/HcalRawToDigi_relbigobj+=EventFilterHcalRawToDigiPlugins
endif
ifeq ($(strip $(EventFilter/HcalRawToDigi)),)
EventFilterHcalRawToDigi := self/EventFilter/HcalRawToDigi
EventFilter/HcalRawToDigi := EventFilterHcalRawToDigi
EventFilterHcalRawToDigi_BuildFile    := $(RELEASETOP)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
EventFilterHcalRawToDigi_EX_USE := $(foreach d, self cmssw DataFormats/HcalDetId DataFormats/HcalDigi DataFormats/FEDRawData FWCore/MessageLogger CondFormats/HcalObjects FWCore/Utilities boost,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
EventFilterHcalRawToDigi_EX_LIB   := EventFilterHcalRawToDigi
ALL_EXTERNAL_PRODS += EventFilterHcalRawToDigi
EventFilterHcalRawToDigi_CLASS := LIBRARY
EventFilter/HcalRawToDigi_relbigobj+=EventFilterHcalRawToDigi
endif
ifeq ($(strip $(DQMOffline/Muon)),)
DQMOfflineMuon := self/DQMOffline/Muon
DQMOffline/Muon := DQMOfflineMuon
DQMOfflineMuon_BuildFile    := $(RELEASETOP)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
DQMOfflineMuon_EX_USE := $(foreach d, self cmssw Geometry/CSCGeometry FWCore/Framework DQMServices/Core DQMServices/Components FWCore/PluginManager DataFormats/MuonReco DataFormats/L1GlobalMuonTrigger DataFormats/FEDRawData RecoMuon/TrackingTools TrackingTools/TransientTrack DataFormats/CSCDigi DataFormats/CSCRecHit DataFormats/DTRecHit DataFormats/RPCDigi CondFormats/DTObjects CondFormats/CSCObjects CondFormats/DataRecord EventFilter/CSCRawToDigi CommonTools/TriggerUtils,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
ALL_EXTERNAL_PRODS += DQMOfflineMuon
DQMOfflineMuon_CLASS := LIBRARY
DQMOffline/Muon_relbigobj+=DQMOfflineMuon
endif
ifeq ($(strip $(FWCore/Version)),)
FWCoreVersion := self/FWCore/Version
FWCore/Version := FWCoreVersion
FWCoreVersion_BuildFile    := $(RELEASETOP)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
FWCoreVersion_EX_USE := $(foreach d, self cmssw ,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
FWCoreVersion_EX_LIB   := FWCoreVersion
ALL_EXTERNAL_PRODS += FWCoreVersion
FWCoreVersion_CLASS := LIBRARY
FWCore/Version_relbigobj+=FWCoreVersion
endif
ifeq ($(strip $(FastSimulationTrackingRecHitProducerAuto)),)
FastSimulationTrackingRecHitProducerAuto := self/src/FastSimulation/TrackingRecHitProducer/plugins
FastSimulationTrackingRecHitProducerAuto_LOC_USE := self cmssw DataFormats/Common DataFormats/DetId DataFormats/GeometrySurface DataFormats/GeometryVector DataFormats/SiPixelCluster DataFormats/SiPixelDetId DataFormats/SiStripCluster DataFormats/SiStripDetId DataFormats/TrackerRecHit2D DataFormats/TrackingRecHit FWCore/Framework FWCore/MessageLogger FWCore/ParameterSet FWCore/PluginManager FWCore/ServiceRegistry FWCore/Utilities FastSimDataFormats/External FastSimulation/Utilities Geometry/CommonDetUnit Geometry/CommonTopologies Geometry/Records Geometry/TrackerGeometryBuilder MagneticField/Engine MagneticField/Records RecoLocalTracker/ClusterParameterEstimator RecoLocalTracker/SiPixelRecHits RecoLocalTracker/Records SimDataFormats/CrossingFrame SimDataFormats/EncodedEventId SimDataFormats/TrackingHit FastSimulation/TrackingRecHitProducer boost clhep gsl
FastSimulation/TrackingRecHitProducer_relbigobj+=FastSimulationTrackingRecHitProducerAuto
endif
