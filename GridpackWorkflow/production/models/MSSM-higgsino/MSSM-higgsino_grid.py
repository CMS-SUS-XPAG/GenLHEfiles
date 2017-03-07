#!/usr/bin/env python

### Script to define scan grid

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *

model = "MSSM-higgsino"
process = "Higgsino_Full"

# Number of events for mass point, in thousands
nevt = 100

MUs = [100., 120., 140., 160., 180., 200., 220., 240. ]
M1s  = [300., 400., 500., 600., 800., 1000., 1200. ]
# -------------------------------
#    Constructing grid

mpoints = []
for MU in MUs:
  for M1 in M1s:    
    mpoints.append([MU,M1,nevt])

## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1])
Npts, Ndiff = len(mpoints), len(mset)
if Npts==Ndiff: print "\nGrid contains "+str(Npts)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Npts-Ndiff)+" DUPLICATE POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

Ntot = makePlot([mpoints], 'events', model, process, M1s[0], M1s[-1], MUs[0], MUs[-1])

print '\nScan contains '+"{0:,.0f}".format(Ntot*1000)+" events"
print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))

print
