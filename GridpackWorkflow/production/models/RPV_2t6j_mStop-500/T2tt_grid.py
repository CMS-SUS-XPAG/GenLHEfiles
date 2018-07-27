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
    
model = "T2tt"
process = "StopStop"
batch = 1

# Number of events: min(goalLumi*xsec, maxEvents) (always in thousands)
goalLumi = 400
minLumi = 1e-40 # Skip minimum lumi
minEvents, maxEvents = 20, 1000
diagStep, bandStep = 25, 50
midDM, maxDM = 300, 700
addDiag = [183, 167] # DeltaM for additional diagonal lines to be added

scanBlocks = []
if (batch==1): scanBlocks.append(gridBlock(350,  425, 50, 50))
elif (batch==2): scanBlocks.append(gridBlock(400,  1201, 50, 50))
minDM = 85
ymin, ymed, ymax = 0, 0, 650 



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
  for mx in range(block.xmin, block.xmax, min(bandStep, diagStep)):
    if (batch==2 and mx==block.xmin): continue
    xmin = min(xmin, block.xmin)
    xmax = max(xmax, block.xmax)
    col = []
    my = 0
    begBand = min(max(ymed, mx-maxDM), mx-minDM)
    begDiag = min(max(ymed, mx-midDM), mx-minDM)
    # Adding bulk points
    if (mx-block.xmin)%block.xstep == 0 :
      for my in range(ymin, begBand, block.ystep):
        if my > ymax: continue
        # Adding extra diagonals to the bulk
        for dm in addDiag:
          if(len(cols)==0 and batch==1): continue # Don't add point before the beginning
          dm_before = mx-block.xstep -my
          dm_after = mx - my
          if(dm>dm_before and dm<dm_after):
            nev = events(my+dm)
            col.append([my+dm,my, nev])
            Nbulk += nev
        nev = events(mx)
        col.append([mx,my, nev])
        Nbulk += nev
    # Adding diagonal points in inside band
    if (mx-block.xmin)%bandStep == 0 :
      for my in range(begBand, mx-midDM, bandStep):
        if my > ymax: continue
        # Adding extra diagonals to the band
        for dm in addDiag:
          if(len(cols)==0 and batch==1): continue # Don't add point before the beginning
          dm_before = mx-bandStep -my
          dm_after = mx - my
          if(dm>dm_before and dm<dm_after):
            nev = events(my+dm)
            col.append([my+dm,my, nev])
            Ndiag += nev
        # Adding standard diagonal points
        nev = events(mx)
        col.append([mx,my, nev])
        Ndiag += nev
    # Adding diagonal points in band closest to outer diagonal
    for my in range(begDiag, mx-minDM+1, diagStep):
      if my > ymax: continue
      # Adding extra diagonals to the band
      for dm in addDiag:
        if(len(cols)==0 and batch==1): continue # Don't add point before the beginning
        dm_before = mx-diagStep -my
        dm_after = mx - my
        if(dm>dm_before and dm<dm_after):
          nev = events(my+dm)
          col.append([my+dm,my, nev])
          Ndiag += nev
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
