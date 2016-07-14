#!/usr/bin/env python

### Script to define scan grid

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *
    
model = "T6bbllslepton"
process = "SbotSbot"

nevt = 50
diag = 50
xmin, xmax, xstep = 1000, 1300, 50
ymin, ymax, ystep = 150, 1300, 50 

# -------------------------------
#    Constructing grid

mpoints = []
for mx in range(xmin, xmax+1, xstep):
  ylist = []
  if mx > ymax + diag: 
    ylist.extend(range(ymin, ymax+1, ystep))
  else:
    ylist.extend(range(ymin, mx-diag+1, ystep))
  for my in ylist:
    mpoints.append([mx,my,nevt])


## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1])
Ntot, Ndiff = len(mpoints), len(mset)
if Ntot==Ndiff: print "\nGrid contains "+str(Ntot)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Ntot-Ndiff)+" DUPLICATE POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

makePlot([mpoints], 'events', model, process, xmin, xmax, ymin, ymax)
Ntot = makePlot([mpoints], 'lumi', model, process, xmin, xmax, ymin, ymax)

Ntot = Ntot/1e3
print '\nScan contains '+"{0:,.0f}".format(Ntot*1e6)+" events\n"
print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))
print

