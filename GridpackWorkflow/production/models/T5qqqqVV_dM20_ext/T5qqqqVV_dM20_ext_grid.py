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
  def __init__(self, xmin, xmax, xstep, ystep, maxDM, dstep, minEvents):
    self.xmin = xmin
    self.xmax = xmax
    self.xstep = xstep
    self.ystep = ystep
    self.maxDM = maxDM
    self.dstep = dstep
    self.minEvents = minEvents
    
model = "T5qqqqVV_dM20"
process = "GlGl"

## Efficiency of the 1 lepton filter
##  double pw = 2/3., pz = 1/3., pwl = 1/3., pzl = 1/10.
##  bf_1L = pw*pw*(1-pow(1-pwl,2)) + pz*pz*(1-pow(1-pzl,2)) + 2*pw*pz*(1-(1-pwl)*(1-pzl))
bf_1L = 0.446 

# Number of events: min(goalLumi*xsec, maxEvents) (always in thousands)
goalLumi, minLumi, maxEvents = 800*bf_1L, 20*bf_1L, 50

scanBlocks = []
scanBlocks.append(gridBlock(600,  800, 50, 50, 1000, 50, 20))
scanBlocks.append(gridBlock(800,  2001, 50, 50, 1000, 50, 20))
minDM = 25
ymin, ymed, ymax = 0, 200, 1500 


# Number of events for mass point, in thousands
def events(mass):
  xs = xsec(mass,process)
  nev = min(goalLumi*xs, maxEvents*1000)
  if nev < xs*minLumi: nev = xs*minLumi
  nev = max(nev/1000, minEvents)
  return math.ceil(nev) # Rounds up

# -------------------------------
#    Constructing grid

cols = []
Nevents = []
xmin, xmax = 9999, 0
for block in scanBlocks:
  Nbulk, Ndiag = 0, 0
  minEvents = block.minEvents
  for mx in range(block.xmin, block.xmax, block.dstep):
    xmin = min(xmin, block.xmin)
    xmax = max(xmax, block.xmax)
    col = []
    my = 0
    begDiag = max(ymed, mx-block.maxDM)
    # Adding bulk points
    if (mx-block.xmin)%block.xstep == 0 :
      for my in range(ymin, begDiag, block.ystep):
        if my > ymax: continue
        nev = events(mx)
        if mx > 1700 or my > 1200: #only add points not included in previous scan
            col.append([mx,my, nev])
            Nbulk += nev
    # Adding diagonal points
    for my in range(begDiag, mx-minDM+1, block.dstep):
      if my > ymax: continue
      nev = events(mx)
      if mx > 1700 or my > 1200: #only add points not included in previous scan
          col.append([mx,my, nev])
          Ndiag += nev
    if(my !=  mx-minDM and mx-minDM <= ymax):
      my = mx-minDM
      nev = events(mx)
      if mx > 1700 or my > 1200: #only add points not included in previous scan
          col.append([mx,my, nev])
          Ndiag += nev
    cols.append(col)
  Nevents.append([Nbulk, Ndiag])

mpoints = []
for col in cols: mpoints.extend(col)

## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1])
Ntot, Ndiff = len(mpoints), len(mset)
if Ntot==Ndiff: print "\nGrid contains "+str(Ntot)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Ntot-Ndiff)+" DUPLICATE POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

makePlot(cols, 'events', model, process, xmin, xmax, ymin, ymax)
Ntot = makePlot(cols, 'lumi', model, process, xmin, xmax, ymin, ymax)
Ntot = makePlot(cols, 'lumi_br2', model, process, xmin, xmax, ymin, ymax)
#makePlot(cols, 'factor')

Ntot = Ntot/1e3
print '\nScan contains '+"{0:.1f}".format(Ntot)+" million events\n"
print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))
print

for ind in range(len(scanBlocks)):
  Nbulk, Ndiag = Nevents[ind][0]/1e3, Nevents[ind][1]/1e3
  Nblock = Nbulk+Ndiag
  print "From "+'{:>4}'.format(scanBlocks[ind].xmin)+" to "+str(scanBlocks[ind].xmax)+": ",
  print "{0:>4.1f}".format(Nblock)+"M ("+"{0:>4.1f}".format(Nblock/Ntot*100)+" %) events, "+"{0:>4.1f}".format(Nbulk),
  print "M ("+"{0:>4.1f}".format(Nbulk/Ntot*100)+" %) in the bulk, "+"{0:>4.1f}".format(Ndiag)+"M (",
  print "{0:.1f}".format(Ndiag/Ntot*100)+" %) in the diagonal"

print
