#!/usr/bin/env python

### Script to define scan grid

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *

model = "Higgsino-N2C1"
process = "Higgsino-N2C1"

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
    mpoints.append([mN2,mC1,nevt])

## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1])
Npts, Ndiff = len(mpoints), len(mset)
if Npts==Ndiff: print "\nGrid contains "+str(Npts)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Npts-Ndiff)+" DUPLICATE POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

Ntot = makePlot([mpoints], 'events', model, process, mN1s[0], mN1s[-1], mN2s[0], mN2s[-1])

print '\nScan contains '+"{0:,.0f}".format(Ntot*1000)+" events"
print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))

print
