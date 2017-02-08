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
  elif proc=="StopStop" or proc=="SbotSbot" or proc=="SqSq":
    if mass < 300: return 319925471928717.38*math.pow(mass, -4.10396285974583*math.exp(mass*0.0001317804474363))
    else: return 6953884830281245*math.pow(mass, -4.7171617288678069*math.exp(mass*6.1752771466190749e-05))
  elif proc=="C1N2" or proc=="C1C1" or proc=="N2N3" or proc=="StauStau" or proc=="ttH_HtoTT" or proc=="tHW_HToTT" or proc=="tHq_HToTT" or proc=="SqSqPlusGamma":
    return 1.
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
  elif proc=="StauStau":
    if mass < 199: return 76,0.608
    elif mass < 299: return 76,52.5e-2
    elif mass < 399: return 76,48.5e-2
    elif mass > 399 : return 76,45.7e-2
    else: sys.exit("grid_utils::matchParams - Mass out of range %i" % mass)
  elif proc=="SqSq" or proc=="StopStop" or proc=="SbotSbot":
    if mass>99 and mass<199: return 62., 0.498
    elif mass<299: return 62., 0.361
    elif mass<399: return 62., 0.302
    elif mass<499: return 64., 0.275
    elif mass<599: return 64., 0.254
    elif mass<1299: return 68., 0.237
    elif mass<1451: return 70., 0.243
    elif mass<1801: return 74., 0.246
    else: sys.exit("grid_utils::matchParams - Mass out of range %i" % mass)
  elif proc=="SqSqPlusGamma":
    if mass>99 and mass<299: return 62., 0.410 
    elif mass < 399: return 62., 0.413
    elif mass < 499: return 62., 0.414
    elif mass < 599: return 64., 0.416
    # the following are copied from SqSq
    elif mass<1299: return 68., 0.237
    elif mass<1451: return 70., 0.243
    elif mass<1801: return 74., 0.246
    else: sys.exit("grid_utils::matchParams - Mass out of range %i" % mass)
  elif proc=="C1N2":
    if mass < 124: return 76,0.64
    elif mass < 151: return 76, 0.6
    elif mass < 176: return 76, 0.57
    elif mass < 226: return 76, 0.54
    elif mass < 326: return 76, 0.51
    elif mass < 451: return 76, 0.48
    elif mass < 651: return 76, 0.45
    elif mass < 1176: return 76, 0.42
    else: return 76,0.4
  elif proc=='N2N3':
    if mass < 199: return 76,0.52
    elif mass<299: return 76,0.524
    elif mass<399: return 76,0.492
    elif mass<499: return 76,0.464
    elif mass<599: return 76,0.451
    elif mass<699: return 76,0.437
    elif mass<799: return 76,0.425
    elif mass<899: return 76,0.413
    elif mass<999: return 76,0.402
    elif mass<1099: return 76,0.40
    elif mass<1199: return 76,0.398
    elif mass<1299: return 76,0.394
    else: return 76,0.394
  elif proc=='C1C1':
    if mass < 125: return 76,0.63
    elif mass < 150: return 76,0.6
    elif mass < 225: return 76,0.57
    elif mass < 300: return 76,0.53
    elif mass < 400: return 76,0.5
    elif mass < 525: return 76,0.47
    elif mass < 725: return 76,0.44
    else: return 76,0.42
  elif proc=='ttH_HToTT':
    if mass < 450.: return 76,0.435
    elif mass < 550.: return 76,0.409
    elif mass < 650.: return 76,0.383
    elif mass < 750.: return 76,0.369
    elif mass < 850.: return 76,0.355
    else: return 76,0.348
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
  if("GlGl" in proc): plt.xlabel('$m(\widetilde{g})$ [GeV]', fontsize=18)
  if("StopStop" in proc): plt.xlabel('$m(\widetilde{t})$ [GeV]', fontsize=18)
  if("SbotSbot" in proc): plt.xlabel('$m(\widetilde{b})$ [GeV]', fontsize=18)
  if("SqSq" in proc): plt.xlabel('$m(\widetilde{q})$ [GeV]', fontsize=18)
  if("C1N2" in proc): plt.xlabel('$m(\chi^{\pm}_{1})$ [GeV]', fontsize=18)
  if("StauStau" in proc): plt.xlabel('$m(\widetilde{\\tau})$ [GeV]', fontsize=18)
  if("ttH" in proc or "tHW" in proc or "tHq" in proc): plt.xlabel('$m_{H}$ [GeV]', fontsize=18)

  plt.ylabel('$m(\chi^0_1)$ [GeV]', fontsize=18)
  if model == 'T6ttWW':  plt.ylabel('$m(\chi^\pm_1)$ [GeV]', fontsize=18)

  ranges = [0, 50,   150,    400,      999]
  colors = ['black', 'green', 'blue', 'purple', 'red']

  Ntot = 0
  for col in mpoints:
    for mpoint in col:
      nev = mpoint[2]
      Ntot += nev
      if type == 'events': val = nev
      if type == 'lumi': val = nev/xsec(mpoint[0], proc)*1000
      if type == 'lumix8': val = nev/xsec(mpoint[0], proc)*1000/8
      if type == 'lumi_br5': val = nev/xsec(mpoint[0], proc)*1000*5
      if type == 'lumi_br4': val = nev/xsec(mpoint[0], proc)*1000*4
      if type == 'lumi_br2': val = nev/xsec(mpoint[0], proc)*1000/0.446

      font_col = colors[-1]
      for icol in range(len(colors)-1):
        if val>ranges[icol] and val<=ranges[icol+1]: font_col = colors[icol]
      val_s = "{0:.0f}".format(val)
      if val>=1000: 
        val_s = "{0:.1f}".format(val/1000)
      plt.text(mpoint[0],mpoint[1], val_s, fontweight='bold', color=font_col, 
               verticalalignment='center', horizontalalignment='center', fontsize=9)

  xmin = min([min([pt[0] for pt in column]) for column in mpoints if len(column)>0]) 
  xmax = max([max([pt[0] for pt in column]) for column in mpoints if len(column)>0]) 
  ymin = min([min([pt[1] for pt in column]) for column in mpoints if len(column)>0]) 
  ymax = max([max([pt[1] for pt in column]) for column in mpoints if len(column)>0]) 
  xtickmin, xtickmax = xmin-(xmin%100), xmax+100-(xmax%100)
  ytickmin, ytickmax = ymin-(ymin%100), ymax+100-(ymax%100)
  xtickstep, ytickstep = 200, 200
  xbuffer, ybuffer = 100, 100
  dx, dy = xmax-xmin, ymax-ymin
  if dx<1200: 
    xtickstep = 100
    xbuffer = 50
  if dy<1200: 
    ytickstep = 100
    ybuffer = 50
  #print "xmax is "+str(xmax)+", xmin is "+str(xmin)+", tickstep is "+str(tickstep)
  plt.axis([xmin-xbuffer, xmax+xbuffer, ymin-ybuffer, ymax+ybuffer])
  plt.xticks(np.arange(xtickmin, xtickmax, xtickstep))
  plt.yticks(np.arange(ytickmin, ytickmax, ytickstep))
  plt.grid(True)

  # Printing legend
  for icol in range(len(colors)):
    if icol < len(colors)-1: label = str(ranges[icol]+1)+"-"+str(ranges[icol+1])
    else: label = str(ranges[icol]+1)+"+"
    if type == 'events': label = label+"k"
    else: label = label+" fb$^{-1}$"
    plt.text(xmin-xbuffer/1.5,ymax+ybuffer/1.5-icol*dy/22, label, fontweight='bold', color=colors[icol], 
             verticalalignment='top', horizontalalignment='left', fontsize=16)

  if type == 'events': title = 'Thousands of '+model+' events to generate'
  if 'lumi' in type: title = 'Equivalent '+model+' MC luminosity in fb$^{-1}$'
  tot_s = ' ('+"{0:.1f}".format(Ntot/1000)+' million events in the scan)'
  plt.title(title+tot_s, fontweight='bold')
  pname = model+'_'+type+'.pdf'
  plt.savefig(pname, bbox_inches='tight')
  print ' open '+pname
  return Ntot
