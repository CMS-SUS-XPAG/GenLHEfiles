#!/usr/bin/env python

### Script to define scan grid

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *

model = "ResonantSmu"
process = ""

# Number of events for mass point, in thousands
def events(mx):
  if (mx<800): return 45
  else: return 25

diag = 100
xmin, xmax, xstep = 200, 3000, 100
ymin, ymax, ystep = 100, 2900, 100 

# -------------------------------
#    Constructing grid

mpoints = []
for mx in range(xmin, xmax+1, xstep):
  ylist = range(ymin, mx-diag+1, ystep)
  for my in ylist:
    mpoints.append([mx,my,events(mx)])

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
print
