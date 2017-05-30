#!/usr/bin/env python

### Script to define scan grid
import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *

dmlist = [1,2]
dmlist.extend(range(5,51,5))

mpoints = []
for ix in range(100, 501, 50):
  for idm in dmlist:
    mpoints.append([ix, ix-idm, 100])
    print "["+str(ix)+","+str(ix-idm)+"]",
  print

## Test print out for repeated points

mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1]+mp[2]*13)
Ntot, Ndiff = len(mpoints), len(mset)
if Ntot==Ndiff: print "\nGrid contains "+str(Ntot)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Ntot-Ndiff)+" DUPLICATE POINTS!!\n\n"

# Plot grid

makePlot([mpoints], 'events', 'VBF-C1N2_WZ', 'VBF-C1N2', 50, 550, 40, 520)

print
