#!/usr/bin/env python

### Utilities for constructing and plotting scan grids 

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
import numpy as np
import matplotlib.pyplot as plt

### Fits to gluino and squarks cross-sections in fb
### https://github.com/manuelfs/mc/blob/master/macros/fit_xsec.C
def xsec(mass, proc):
  if proc=="GlGl":
    return 4.563e+17*math.pow(mass, -4.761*math.exp(5.848e-05*mass))
  if proc=="StopStop" or proc=="SbotSbot" or proc=="SqSq":
    if mass < 300: return 319925471928717.38*math.pow(mass, -4.10396285974583*math.exp(mass*0.0001317804474363))
    else: return 6953884830281245*math.pow(mass, -4.7171617288678069*math.exp(mass*6.1752771466190749e-05))
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
  
def makePlot(mpoints, type, model, proc, xmin, xmax, ymin, ymax):
  plt.figure(figsize=(17,10))
  if("T1" in model or "T5" in model): plt.xlabel('$m(\widetilde{g})$ [GeV]', fontsize=18)
  if("T2tt"==model): plt.xlabel('$m(\widetilde{t})$ [GeV]', fontsize=18)
  if("T2qq" in model): plt.xlabel('$m(\widetilde{q})$ [GeV]', fontsize=18)
  if("T2bb"==model): plt.xlabel('$m(\widetilde{b})$ [GeV]', fontsize=18)

  plt.ylabel('$m(\chi^0_1)$ [GeV]', fontsize=18)
  Ntot = 0
  for col in mpoints:
    for mpoint in col:
      nev = mpoint[2]
      Ntot += nev
      if type == 'events': val = nev
      if type == 'lumi': val = nev/xsec(mpoint[0], proc)*1000
      if type == 'lumix8': val = nev/xsec(mpoint[0], proc)*1000/8
      if type == 'lumi_br5': val = nev/xsec(mpoint[0], proc)*1000*5
      if type == 'lumi_br2': val = nev/xsec(mpoint[0], proc)*1000*2
      if val<1000:
        plt.text(mpoint[0],mpoint[1], "{0:.0f}".format(val), 
                 verticalalignment='center', horizontalalignment='center', fontsize=8)
      else:
        plt.text(mpoint[0],mpoint[1], "{0:.1f}".format(val/1000), fontweight='bold', 
                 verticalalignment='center', horizontalalignment='center', fontsize=8, color='red')
  tickmin = xmin-(xmin%100)
  tickstep = 200
  xbuffer, ybuffer = 100, 100
  if xmax-xmin<1000: 
    tickstep = 100
    xbuffer = 50
  if ymax-ymin<1000: 
    ybuffer = 50
  plt.axis([xmin-xbuffer, xmax+xbuffer, ymin-ybuffer, ymax+ybuffer])
  plt.xticks(np.arange(tickmin, xmax, tickstep))
  plt.yticks(np.arange(ymin, ymax+100, tickstep))
  plt.grid(True)
  if type == 'events': title = 'Thousands of '+model+' events to generate'
  if 'lumi' in type: title = 'Equivalent '+model+' MC luminosity in fb$^{-1}$'
  tot_s = ' ('+"{0:.1f}".format(Ntot/1000)+' million events in the scan)'
  plt.title(title+tot_s, fontweight='bold')
  pname = model+'_'+type+'.pdf'
  plt.savefig(pname, bbox_inches='tight')
  print ' open '+pname
  return Ntot
