
PYTHIA8=$(shell cd $(CMSSW_BASE) && scramv1 tool tag pythia8 PYTHIA8_BASE)
LHAPDF=$(shell  cd $(CMSSW_BASE) && scramv1 tool tag lhapdf LHAPDF_BASE)

all: main20.exe

main20.exe: main20.cc
	@echo  "Will use PYTHIA8 from $(PYTHIA8)"
	@echo  "Will use LHAPDF from $(LHAPDF)"
	g++ -O2 -ansi -pedantic -W -Wall -Wshadow -I$(PYTHIA8)/include main20.cc -o main20.exe  -L$(PYTHIA8)/lib -L$(LHAPDF)/lib -lpythia8 -lLHAPDF -ldl
