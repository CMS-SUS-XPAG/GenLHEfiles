#!/sbin/python

import sys
import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



TAG = bcolors.FAIL + "[DO_HEADERS]"


def fileExists(destiny, file):

  nameNoGz = file[0:file.find(".gz")]
  namexz = nameNoGz + ".xz"

  outputA = subprocess.Popen("/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select ls " + destiny + "/" + namexz, stdout=subprocess.PIPE, shell=True)
  outputB = outputA.communicate()[0]
  output = outputB.split("\n")
  if (output[0] != ''):
     return True
  return False


def expand(f, source, ListOfFiles, efficiency):

  l = f.split()
  mass1 = l[0]
  mass2 = l[1]
  number = int(l[2])

  
  files = []
  InfoForSending = []
  counter = 0
  for l in ListOfFiles:
    posmass1 = l.find("stop" + mass1 + "_")
    posmass2 = l.find("LSP" + mass2 + "_")
    if(posmass1 != -1 and posmass2 != -1):
      if(counter < (number/100000.0)/efficiency):
        files.append(l)
        InfoForSending.append(mass1 + " " + mass2 + " 100000 " + l) 
        counter = counter + 1

  return InfoForSending 


if __name__ == "__main__":

  mass_scan = sys.argv[1]
  template = sys.argv[2]
  model = sys.argv[3]
  efficiency = float(sys.argv[4])
  source = sys.argv[5]
  destiny = sys.argv[6]
  path = sys.argv[7]
  f_scan = open(mass_scan)
  lines = f_scan.readlines()
  f_scan.close()

  outputA = subprocess.Popen("/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select ls " + source, stdout=subprocess.PIPE, shell=True)
  outputB = outputA.communicate()[0]
  ListOfFiles = outputB.split("\n")
  
  print TAG + bcolors.OKBLUE + " Doing mass_scan in: " + bcolors.HEADER + mass_scan + bcolors.ENDC
  print TAG + bcolors.OKBLUE + " Name of the model: " + bcolors.HEADER + model + bcolors.ENDC
  print TAG + bcolors.OKBLUE + " Source: " + bcolors.HEADER + source + bcolors.ENDC
  print TAG + bcolors.OKBLUE + " Destiny: " + bcolors.HEADER + destiny + bcolors.ENDC
  
  list = []
  for f in lines:
    list = list + expand(f, source, ListOfFiles, efficiency)

  for l in list:
    text = l.split()
    mass1 = text[0]
    mass2 = text[1]
    number = text[2]
    theFile = text[3]
    if not fileExists(destiny, theFile):
      #print "bsub -o /dev/null -e /dev/null -q 8nh python2.7 " + path + "/process_file.py " + path + "/" + template + " " + mass1 + " " + mass2 + " " + number + " " + model + " " + source + " " + theFile + " " + destiny
      subprocess.call(["bsub -o /dev/null -e /dev/null -q 8nh python2.7 " + path + "/process_file.py " + path + "/" + template + " " + mass1 + " " + mass2 + " " + number + " " + model + " " + source + " " + theFile + " " + destiny], shell=True)
      subprocess.call(['sleep 0.001'], shell=True)

    


