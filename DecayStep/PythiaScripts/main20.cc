// main20.cc is a part of the PYTHIA event generator.
// Copyright (C) 2014 Torbjorn Sjostrand.
// PYTHIA is licenced under the GNU GPL version 2, see COPYING for details.
// Please respect the MCnet Guidelines, see GUIDELINES for details.

// This is a simple test program. It shows how PYTHIA 8 can write
// a Les Houches Event File based on its process-level events.

#include "Pythia8/Pythia.h"
using namespace Pythia8;
int main(int argc, char *argv[]) {
  // Needs two arguments: command cfg and name of outputfile
  if (argc != 3){
    std::cout << "Please provide the cfg file and output file names!" << std::endl;
    return 1;
  }
  std::string cfg = argv[1];
  std::string outfilename = argv[2]; 

  std::cout << "Using config " << cfg << std::endl;
  std::cout << "Will write decayed file to " << outfilename << std::endl;

  // Generator.
  Pythia pythia;

  // Read config file
  pythia.readFile( cfg, 0);

  // Create an LHAup object that can access relevant information in pythia.
  LHAupFromPYTHIA8 myLHA(&pythia.process, &pythia.info);

  // Open a file on which LHEF events should be stored, and write header.
  myLHA.openLHEF(outfilename);

  // LHC 8 TeV initialization.
  pythia.readString("Beams:eCM = 13000.");
  pythia.init();

  // Store initialization info in the LHAup object.
  myLHA.setInit();

  // Write out this initialization info on the file.
  myLHA.initLHEF();

  // Loop over events.
  int nEvent = pythia.mode("Main:numberOfEvents");
  for (int i = 0; i < nEvent; ++i) {

    // Generate an event.
    pythia.next();

    // Store event info in the LHAup object.
    myLHA.setEvent();

    // Write out this event info on the file.
    // With optional argument (verbose =) false the file is smaller.
    myLHA.eventLHEF();
  }

  // Statistics: full printout.
  pythia.stat();

  // Update the cross section info based on Monte Carlo integration during run.
  myLHA.updateSigma();

  // Write endtag. Overwrite initialization info with new cross sections.
  myLHA.closeLHEF(true);

  // Done.
  return 0;
}
