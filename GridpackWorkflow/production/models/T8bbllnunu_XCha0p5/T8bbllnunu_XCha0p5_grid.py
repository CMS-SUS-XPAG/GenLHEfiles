#!/usr/bin/env python

### Script to define scan grid

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *
import pprint

model = "T8bbllnunu_XCha0p5"
process = "StopStop"

# Number of events: min(goalLumi*xsec, maxEvents) (always in thousands)
goalLumi = 400
minLumi = 20 
minEvents, maxEvents = 50, 100
bandStep = 50
minDM, midDM, maxDM = 100, 200, 200

# Parameters that define the grid in the bulk and diagonal
class gridBlock:
  def __init__(self, xmin, xmax, xstep, ystep, dstep):
    self.xmin = xmin
    self.xmax = xmax
    self.xstep = xstep
    self.ystep = ystep
    self.dstep = dstep
    
scanBlocks = []
scanBlocks.append(gridBlock(200, 400, 50, 50,50))
scanBlocks.append(gridBlock(400,  1501, 50, 50, 25))
ymin, ymed, ymax = 0, 150, 650
hlines_below_grid = [25]
hline_xmin = 400


# Number of events for mass point, in thousands
def events(mass):
  xs = xsec(mass,process)
  nev = min(goalLumi*xs, maxEvents*1000)
  # if nev < xs*minLumi: nev = xs*minLumi
  nev = max(nev/1000, minEvents)
  return math.ceil(nev) # Rounds up

# -------------------------------
#    Constructing grid

cols = []
Nevents = []
xmin, xmax = 9999, 0
for block in scanBlocks:
  Nbulk, Ndiag = 0, 0
  for mx in range(block.xmin, block.xmax, min(bandStep, block.dstep)):
    xmin = min(xmin, block.xmin)
    xmax = max(xmax, block.xmax)
    col = []
    my = 0
    begBand = min(max(ymed, mx-maxDM), mx-minDM)
    begDiag = min(max(ymed, mx-midDM), mx-minDM)
    # Adding bulk points
    if (mx-block.xmin)%block.xstep == 0 :
      yrange = []
      if (mx>=hline_xmin): yrange.extend(hlines_below_grid)
      yrange.extend(range(ymin, begBand, block.ystep))
      for my in yrange:
        if my > ymax or my>mx-minDM: continue
        nev = events(mx)
        col.append([mx,my, nev])
        Nbulk += nev
    # Adding diagonal points in inside band
    if (mx-block.xmin)%bandStep == 0 :
      for my in range(begBand, mx-midDM, bandStep):
        if my > ymax: continue
        nev = events(mx)
        col.append([mx,my, nev])
        Ndiag += nev
    # Adding diagonal points in band closest to outer diagonal
    for my in range(begDiag, mx-minDM+1, block.dstep):
      if my > ymax: continue
      nev = events(mx)
      col.append([mx,my, nev])
      Ndiag += nev
    if(my !=  mx-minDM and mx-minDM <= ymax):
      my = mx-minDM
      nev = events(mx)
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


Ntot = Ntot/1e3
print '\nScan contains '+"{0:,.0f}".format(Ntot*1e6)+" events\n"
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
