#!/usr/bin/env python

### Script to define scan grid

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *

# Parameters that define the grid in the bulk and diagonal
class gridBlock:
  def __init__(self, xmin, xmax, xstep, ystep):
    self.xmin = xmin
    self.xmax = xmax
    self.xstep = xstep
    self.ystep = ystep
    
model = "TChiWZ_ZToLL"
process = "C1N2"

# Number of events: min(goalLumi*xsec, maxEvents) (always in thousands)
diagStep = 100
maxDM = 150
extras = range(10,141,10)
extras.extend([7,15])

scanBlocks = []
scanBlocks.append(gridBlock(100, 701, 25, 25))
minDM = 150
ymin, ymed, ymax = 0, 0, 300 


# Number of events for mass point, in thousands
def events(dm):
  if dm<=40: return 100
  else: return 50

# -------------------------------
#    Constructing grid

cols = []
xmin, xmax = 9999, 0
for block in scanBlocks:
  for mx in range(block.xmin, block.xmax, block.xstep):
    xmin = min(xmin, block.xmin)
    xmax = max(xmax, block.xmax)
    col = []
    my = 0
    begDiag = max(ymed, mx-maxDM)
    # Adding bulk points
    if (mx-block.xmin)%block.xstep == 0 :
      for my in range(ymin, begDiag, block.ystep):
        if my > ymax: continue
        nev = events(mx-my)
        col.append([mx,my, nev])
    if(my !=  mx-minDM and mx-minDM <= ymax) or (my ==  mx-minDM):
      if mx-minDM>=0:
        my = mx-minDM
        nev = events(mx-my)
        col.append([mx,my, nev])
      for ydm in extras:
        nev = events(ydm)
        if (mx-ydm <= ymax) and (mx-ydm>=0): col.append([mx,mx-ydm, nev])
    cols.append(col)

mpoints = []
for col in cols: mpoints.extend(col)

## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1]+mp[2]*13)
Ntot, Ndiff = len(mpoints), len(mset)
if Ntot==Ndiff: print "\nGrid contains "+str(Ntot)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Ntot-Ndiff)+" DUPLICATE POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

makePlot(cols, 'events', model, process, xmin, xmax, ymin, ymax)
Ntot = makePlot(cols, 'lumi', model, process, xmin, xmax, ymin, ymax)
#makePlot(cols, 'factor')

print '\nScan contains '+"{0:,.0f}".format(Ntot*1e3)+" events\n"
print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))
print

print
