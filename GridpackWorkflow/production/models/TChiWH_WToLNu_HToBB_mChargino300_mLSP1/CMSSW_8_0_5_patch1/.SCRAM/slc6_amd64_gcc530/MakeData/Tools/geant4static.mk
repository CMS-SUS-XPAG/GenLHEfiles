ALL_TOOLS      += geant4static
geant4static_EX_LIB := geant4-static
geant4static_EX_USE := clhep xerces-c
geant4static_EX_FLAGS_CXXFLAGS  := -DG4MULTITHREADED -DG4USE_STD11 -ftls-model=global-dynamic -pthread

