#!/usr/bin/env python

### Script to define scan grid

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *

model = "TChiWH_HToGG"
process = "C1N2"

# Parameters that define the grid in the bulk and diagonal
class gridBlock:
  def __init__(self, xmin, xmax, xstep, ystep):
    self.xmin = xmin
    self.xmax = xmax
    self.xstep = xstep
    self.ystep = ystep
    
scanBlocks = []
scanBlocks.append(gridBlock(150, 701, 25, 25))

minDM = 126
maxDM = 176
ymin, ymax = 0, 300
nev = 100
  
# -------------------------------
#    Constructing grid

cols = []
Nevents = []
xmin, xmax = 9999, 0
for block in scanBlocks:
  Nbulk, Ndiag = 0, 0
  for mx in range(block.xmin, block.xmax, block.xstep):
    xmin = min(xmin, block.xmin)
    xmax = max(xmax, block.xmax)
    col = []
    my = 0
    # Adding bulk points
    if (mx-block.xmin)%block.xstep == 0:
      for my in range(ymin, mx-minDM, block.ystep):
        if my > ymax: continue
        col.append([mx,my, nev])
        Nbulk += nev
    if my !=  mx-minDM and mx-minDM <= ymax:
      my = mx-minDM
      col.append([mx,my, nev])
      Ndiag += nev
    cols.append(col)
  Nevents.append([Nbulk, Ndiag])

mpoints = []
for col in cols: mpoints.extend(col)
# add shifted point
mpoints.append([127,0,nev])
    
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
