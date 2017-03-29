#!/usr/bin/env python

### Script to define scan grid

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *

model = "TStauStau-RH"
process = "StauStau-RH"

# Parameters that define the grid in the bulk and diagonal
class gridBlock:
  def __init__(self, xmin, xmax, xstep, ymin, ymax, ystep, diagStep):
    self.xmin = xmin
    self.xmax = xmax
    self.xstep = xstep
    self.ymin  = ymin
    self.ymax  = ymax
    self.ystep = ystep
    self.diagStep = diagStep

# Number of events for mass point, in thousands
nevt = 50
xmin, xmax = 90, 400 
ymin, ymax = 0, 200

scanBlocks = []

scanBlocks.append(gridBlock(90,100,10,0,11,10,0))
scanBlocks.append(gridBlock(100,300,25,0,50,10,0))
scanBlocks.append(gridBlock(100,300,25,50,150,25,0))
scanBlocks.append(gridBlock(100,300,25,150,201,50,0))
scanBlocks.append(gridBlock(300,401,50,0,50,10,0))
scanBlocks.append(gridBlock(300,401,50,50,150,25,0))
scanBlocks.append(gridBlock(300,401,50,150,201,50,0))

# -------------------------------
#    Constructing grid

mpoints = []

for block in scanBlocks:
  for mx in range(block.xmin, block.xmax, block.xstep):
    for my in range(block.ymin, block.ymax, block.ystep):
      if mx > my + block.diagStep:
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
