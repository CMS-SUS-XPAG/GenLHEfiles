ifeq ($(strip $(LCG/PyCoral)),)
lcg_PyCoral := coral/LCG/PyCoral
LCG/PyCoral := lcg_PyCoral
PyCoral := lcg_PyCoral
lcg_PyCoral_BuildFile    := $(CORAL_BASE)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
lcg_PyCoral_EX_USE := $(foreach d, coral  LCG/RelationalAccess python,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
lcg_PyCoral_EX_LIB   := lcg_PyCoral
ALL_EXTERNAL_PRODS += lcg_PyCoral
lcg_PyCoral_CLASS := LIBRARY
LCG/PyCoral_relbigobj+=lcg_PyCoral
endif
ifeq ($(strip $(LCG/CoralCommon)),)
lcg_CoralCommon := coral/LCG/CoralCommon
LCG/CoralCommon := lcg_CoralCommon
CoralCommon := lcg_CoralCommon
lcg_CoralCommon_BuildFile    := $(CORAL_BASE)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
lcg_CoralCommon_EX_USE := $(foreach d, coral  LCG/RelationalAccess xerces-c,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
lcg_CoralCommon_EX_LIB   := lcg_CoralCommon
ALL_EXTERNAL_PRODS += lcg_CoralCommon
lcg_CoralCommon_CLASS := LIBRARY
LCG/CoralCommon_relbigobj+=lcg_CoralCommon
endif
ifeq ($(strip $(LCG/CoralBase)),)
lcg_CoralBase := coral/LCG/CoralBase
LCG/CoralBase := lcg_CoralBase
CoralBase := lcg_CoralBase
lcg_CoralBase_BuildFile    := $(CORAL_BASE)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
lcg_CoralBase_EX_USE := $(foreach d, coral  boost boost_filesystem,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
lcg_CoralBase_EX_LIB   := lcg_CoralBase
ALL_EXTERNAL_PRODS += lcg_CoralBase
lcg_CoralBase_CLASS := LIBRARY
LCG/CoralBase_relbigobj+=lcg_CoralBase
endif
ifeq ($(strip $(LCG/RelationalAccess)),)
lcg_RelationalAccess := coral/LCG/RelationalAccess
LCG/RelationalAccess := lcg_RelationalAccess
RelationalAccess := lcg_RelationalAccess
lcg_RelationalAccess_BuildFile    := $(CORAL_BASE)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
lcg_RelationalAccess_EX_USE := $(foreach d, coral  LCG/CoralBase LCG/CoralKernel,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
lcg_RelationalAccess_EX_LIB   := lcg_RelationalAccess
ALL_EXTERNAL_PRODS += lcg_RelationalAccess
lcg_RelationalAccess_CLASS := LIBRARY
LCG/RelationalAccess_relbigobj+=lcg_RelationalAccess
endif
ifeq ($(strip $(LCG/XMLAuthenticationService)),)
lcg_XMLAuthenticationService := coral/LCG/XMLAuthenticationService
LCG/XMLAuthenticationService := lcg_XMLAuthenticationService
XMLAuthenticationService := lcg_XMLAuthenticationService
lcg_XMLAuthenticationService_BuildFile    := $(CORAL_BASE)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
lcg_XMLAuthenticationService_EX_USE := $(foreach d, coral  LCG/CoralCommon xerces-c,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
lcg_XMLAuthenticationService_EX_LIB   := lcg_XMLAuthenticationService
ALL_EXTERNAL_PRODS += lcg_XMLAuthenticationService
lcg_XMLAuthenticationService_CLASS := LIBRARY
LCG/XMLAuthenticationService_relbigobj+=lcg_XMLAuthenticationService
endif
ifeq ($(strip $(LCG/OracleAccess)),)
lcg_OracleAccess := coral/LCG/OracleAccess
LCG/OracleAccess := lcg_OracleAccess
OracleAccess := lcg_OracleAccess
lcg_OracleAccess_BuildFile    := $(CORAL_BASE)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
lcg_OracleAccess_EX_USE := $(foreach d, coral  LCG/CoralCommon oracle,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
lcg_OracleAccess_EX_LIB   := lcg_OracleAccess
ALL_EXTERNAL_PRODS += lcg_OracleAccess
lcg_OracleAccess_CLASS := LIBRARY
LCG/OracleAccess_relbigobj+=lcg_OracleAccess
endif
ifeq ($(strip $(LCG/MonitoringService)),)
lcg_MonitoringService := coral/LCG/MonitoringService
LCG/MonitoringService := lcg_MonitoringService
MonitoringService := lcg_MonitoringService
lcg_MonitoringService_BuildFile    := $(CORAL_BASE)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
lcg_MonitoringService_EX_USE := $(foreach d, coral  LCG/CoralCommon,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
lcg_MonitoringService_EX_LIB   := lcg_MonitoringService
ALL_EXTERNAL_PRODS += lcg_MonitoringService
lcg_MonitoringService_CLASS := LIBRARY
LCG/MonitoringService_relbigobj+=lcg_MonitoringService
endif
ifeq ($(strip $(LCG/ConnectionService)),)
lcg_ConnectionService := coral/LCG/ConnectionService
LCG/ConnectionService := lcg_ConnectionService
ConnectionService := lcg_ConnectionService
lcg_ConnectionService_BuildFile    := $(CORAL_BASE)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
lcg_ConnectionService_EX_USE := $(foreach d, coral  libuuid LCG/CoralCommon LCG/RelationalAccess boost,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
lcg_ConnectionService_EX_LIB   := lcg_ConnectionService
ALL_EXTERNAL_PRODS += lcg_ConnectionService
lcg_ConnectionService_CLASS := LIBRARY
LCG/ConnectionService_relbigobj+=lcg_ConnectionService
endif
ifeq ($(strip $(LCG/FrontierAccess)),)
lcg_FrontierAccess := coral/LCG/FrontierAccess
LCG/FrontierAccess := lcg_FrontierAccess
FrontierAccess := lcg_FrontierAccess
lcg_FrontierAccess_BuildFile    := $(CORAL_BASE)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
lcg_FrontierAccess_EX_USE := $(foreach d, coral  frontier_client openssl LCG/CoralCommon,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
lcg_FrontierAccess_EX_LIB   := lcg_FrontierAccess
ALL_EXTERNAL_PRODS += lcg_FrontierAccess
lcg_FrontierAccess_CLASS := LIBRARY
LCG/FrontierAccess_relbigobj+=lcg_FrontierAccess
endif
ifeq ($(strip $(LCG/EnvironmentAuthenticationService)),)
lcg_EnvironmentAuthenticationService := coral/LCG/EnvironmentAuthenticationService
LCG/EnvironmentAuthenticationService := lcg_EnvironmentAuthenticationService
EnvironmentAuthenticationService := lcg_EnvironmentAuthenticationService
lcg_EnvironmentAuthenticationService_BuildFile    := $(CORAL_BASE)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
lcg_EnvironmentAuthenticationService_EX_USE := $(foreach d, coral  LCG/CoralCommon,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
lcg_EnvironmentAuthenticationService_EX_LIB   := lcg_EnvironmentAuthenticationService
ALL_EXTERNAL_PRODS += lcg_EnvironmentAuthenticationService
lcg_EnvironmentAuthenticationService_CLASS := LIBRARY
LCG/EnvironmentAuthenticationService_relbigobj+=lcg_EnvironmentAuthenticationService
endif
ifeq ($(strip $(LCG/CoralKernel)),)
lcg_CoralKernel := coral/LCG/CoralKernel
LCG/CoralKernel := lcg_CoralKernel
CoralKernel := lcg_CoralKernel
lcg_CoralKernel_BuildFile    := $(CORAL_BASE)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
lcg_CoralKernel_EX_USE := $(foreach d, coral  LCG/CoralBase,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
lcg_CoralKernel_EX_LIB   := lcg_CoralKernel
ALL_EXTERNAL_PRODS += lcg_CoralKernel
lcg_CoralKernel_CLASS := LIBRARY
LCG/CoralKernel_relbigobj+=lcg_CoralKernel
endif
ifeq ($(strip $(LCG/XMLLookupService)),)
lcg_XMLLookupService := coral/LCG/XMLLookupService
LCG/XMLLookupService := lcg_XMLLookupService
XMLLookupService := lcg_XMLLookupService
lcg_XMLLookupService_BuildFile    := $(CORAL_BASE)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
lcg_XMLLookupService_EX_USE := $(foreach d, coral  LCG/CoralCommon xerces-c,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
lcg_XMLLookupService_EX_LIB   := lcg_XMLLookupService
ALL_EXTERNAL_PRODS += lcg_XMLLookupService
lcg_XMLLookupService_CLASS := LIBRARY
LCG/XMLLookupService_relbigobj+=lcg_XMLLookupService
endif
ifeq ($(strip $(LCG/SQLiteAccess)),)
lcg_SQLiteAccess := coral/LCG/SQLiteAccess
LCG/SQLiteAccess := lcg_SQLiteAccess
SQLiteAccess := lcg_SQLiteAccess
lcg_SQLiteAccess_BuildFile    := $(CORAL_BASE)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
lcg_SQLiteAccess_EX_USE := $(foreach d, coral  LCG/CoralCommon sqlite,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
lcg_SQLiteAccess_EX_LIB   := lcg_SQLiteAccess
ALL_EXTERNAL_PRODS += lcg_SQLiteAccess
lcg_SQLiteAccess_CLASS := LIBRARY
LCG/SQLiteAccess_relbigobj+=lcg_SQLiteAccess
endif
ifeq ($(strip $(LCG/RelationalService)),)
lcg_RelationalService := coral/LCG/RelationalService
LCG/RelationalService := lcg_RelationalService
RelationalService := lcg_RelationalService
lcg_RelationalService_BuildFile    := $(CORAL_BASE)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
lcg_RelationalService_EX_USE := $(foreach d, coral  LCG/CoralCommon boost,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
lcg_RelationalService_EX_LIB   := lcg_RelationalService
ALL_EXTERNAL_PRODS += lcg_RelationalService
lcg_RelationalService_CLASS := LIBRARY
LCG/RelationalService_relbigobj+=lcg_RelationalService
endif
