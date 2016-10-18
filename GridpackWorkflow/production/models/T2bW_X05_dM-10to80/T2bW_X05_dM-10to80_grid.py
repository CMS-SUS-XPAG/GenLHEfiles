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
    
model = "T2bW"
process = "StopStop"

# Number of events: min(goalLumi*xsec, maxEvents) (always in thousands)
goalLumi = 200
minLumi = 50 
minEvents, maxEvents = 20, 1000
xdiagStep, ydiagStep = 25, 10
minDM, maxDM = 10, 80

scanBlocks = []
scanBlocks.append(gridBlock(250,  801, 100, 100)) #Using only [x,y]diagStep
ymin, ymax = 0, 1100 


# Number of events for mass point, in thousands
def events(mass):
  xs = xsec(mass,process)
  nev = min(goalLumi*xs, maxEvents*1000)
  if nev < xs*minLumi: nev = xs*minLumi
  nev = max(nev/1000, minEvents)
  return math.ceil(nev) # Rounds up

# -------------------------------
#    Constructing grid

mpoints = []
Ndiag = 0
xmin, xmax = 9999, 0
for block in scanBlocks:
  for mx in range(block.xmin, block.xmax, xdiagStep):
    xmin = min(block.xmin, xmin)
    xmax = min(block.xmin, xmax)
    for my in range(mx-maxDM, mx-minDM+1, ydiagStep):
      if my > ymax: continue
      nev = events(mx)
      Ndiag += nev
      mpoints.append([mx,my, nev])

## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1])
Ntot, Ndiff = len(mpoints), len(mset)
nev_s = "{0:.1f}".format(Ndiag/1000)
if Ntot==Ndiff: print "\nGrid contains "+str(Ntot)+" mass points with "+nev_s+"M events. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Ntot-Ndiff)+" DUPLICATE MASS POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

makePlot([mpoints], 'events', model, process, xmin, xmax, ymin, ymax)
Ntot = makePlot([mpoints], 'lumi', model, process, xmin, xmax, ymin, ymax)
Ntot = makePlot([mpoints], 'lumi_br4', model, process, xmin, xmax, ymin, ymax)


print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))
print

