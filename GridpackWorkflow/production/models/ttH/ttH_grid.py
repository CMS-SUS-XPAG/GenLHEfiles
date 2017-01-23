#!/usr/bin/env python

### Script to define scan grid

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *

model = "ttH"
process = "ttH"

# Number of events for mass point, in thousands
nevt = 100

xmin, xmax, xstep = 350, 550, 20
xmin_high, xmax_high, xstep_high = 600, 900, 50


# -------------------------------
#    Constructing grid

mpoints = []
for mx in range(xmin, xmax+1, xstep):
  my = mx
  mpoints.append([mx,my,nevt])

for mx in range(xmin_high, xmax_high+1, xstep_high):
  my = mx
  mpoints.append([mx,my,nevt])


## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1])
Npts, Ndiff = len(mpoints), len(mset)
if Npts==Ndiff: print "\nGrid contains "+str(Npts)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Npts-Ndiff)+" DUPLICATE POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

Ntot = makePlot([mpoints], 'events', model, process, xmin, xmax_high, xmin, xmax_high)

print '\nScan contains '+"{0:,.0f}".format(Ntot*1000)+" events"
print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))

print
