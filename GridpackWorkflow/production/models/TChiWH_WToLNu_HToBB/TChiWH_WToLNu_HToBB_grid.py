#!/usr/bin/env python

### Script to define scan grid

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *

model = "TChiWH_WToLNu_HToBB"
process = "C1N2"

# Number of events for mass point, in thousands
nevt = 30

diag_low, diag_high = 125, 125
xmin, xmax, xstep = 125, 700, 25
ymin, ymax, ystep_low, ystep_high = 0, 300, 25, 25 

# -------------------------------
#    Constructing grid

mpoints = []
for mx in range(xmin, xmax+1, xstep):
  ylist = []
  if mx > (ymax + (diag_low - diag_high)): 
    ylist.extend(range(ymin, ymax+1, ystep_low))
  elif mx > ymax:
    ylist.extend(range(ymin, mx - diag_low, ystep_low))
    ylist.extend(range(mx - diag_low, ymax+1, ystep_high))
  else:
    ylist.extend(range(ymin, mx - diag_low, ystep_low))
    ylist.extend(range(mx - diag_low, mx-diag_high+1, ystep_high))
  for my in ylist:
    if mx<my +176:
       nevt=100
    else:nevt=30
    if mx>my+120:
       mpoints.append([mx,my,nevt])
    
## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1])
Npts, Ndiff = len(mpoints), len(mset)
if Npts==Ndiff: print "\nGrid contains "+str(Npts)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Npts-Ndiff)+" DUPLICATE POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

Ntot = makePlot([mpoints], 'events', model, process, xmin, xmax, ymin, ymax)

print '\nScan contains '+"{0:,.0f}".format(Ntot*1000)+" events"
print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))

print
