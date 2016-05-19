#!/usr/bin/env python

### Utilities for constructing and plotting scan grids 

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
import numpy as np
import matplotlib.pyplot as plt

# Fit to gluino cross-section in fb
def xsec(mass, proc):
  if proc=="GlGl":
    return 4.563e+17*math.pow(mass, -4.761*math.exp(5.848e-05*mass))
  else:
    sys.exit("grid_utils::xsec - Unknown process name %s" % proc)
  
def matchParams(mass, proc):
  if proc=="GlGl":
    if mass>599 and  mass<799: return 118., 0.235
    elif mass<999: return 128., 0.235
    elif mass<1199: return 140., 0.235
    elif mass<1399: return 143., 0.245
    elif mass<1499: return 147., 0.255
    elif mass<1799: return 150., 0.267
    elif mass<2099: return 156., 0.290
    elif mass<2301: return 160., 0.315
    else: sys.exit("grid_utils::matchParams - Mass out of range %i" % mass)
  else: sys.exit("grid_utils::matchParams - Unknown process name %s" % proc)
    
def getAveEff(mpoints, proc):
  sum_wgt = 0.
  sum_evt = 0.
  for point in mpoints:
    qcut, tru_eff = matchParams(point[0], proc)
    sum_wgt += point[2]*tru_eff
    sum_evt += point[2]
  return sum_wgt/sum_evt
  
def makePlot(mpoints, type, model, proc, xmin, xmax, ymin, ymax, ifb):
  plt.figure(figsize=(17,10))
  plt.xlabel('$m(\widetilde{g})$ [GeV]', fontsize=18)
  plt.ylabel('$m(\chi^0_1)$ [GeV]', fontsize=18)
  Ntot = 0
  for col in mpoints:
    for mpoint in col:
      nev = mpoint[2]
      Ntot += nev
      if type == 'events': val = nev
      if type == 'factor': val = nev/xsec(mpoint[0], proc)/ifb*1000
      if type == 'lumi': val = nev/xsec(mpoint[0], proc)*1000
      plt.text(mpoint[0],mpoint[1], "{0:.0f}".format(val), 
               verticalalignment='center', horizontalalignment='center', fontsize=8)
  plt.axis([xmin-100, xmax+100, -50, ymax+100])
  plt.xticks(np.arange(xmin, xmax, 200))
  plt.yticks(np.arange(ymin, ymax+100, 200))
  plt.grid(True)
  if type == 'events': title = 'Thousands of '+model+' events to generate'
  if type == 'factor': title = 'Times more '+model+' MC events than expected in data for '+str(ifb)+' fb$^{-1}$'
  if type == 'lumi': title = 'Equivalent '+model+' MC luminosity in fb$^{-1}$'
  tot_s = ' ('+"{0:.1f}".format(Ntot/1000)+' million events in the scan)'
  plt.title(title+tot_s, fontweight='bold')
  pname = model+'_'+type+'.pdf'
  plt.savefig(pname, bbox_inches='tight')
  print ' open '+pname
  return Ntot
