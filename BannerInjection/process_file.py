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


def doFile(template, source, destiny, mass1, mass2, file, modelname, number):

  nameNoGz = file[0:file.find(".gz")]
  name_aux = "aux" + nameNoGz
  namexz = nameNoGz + ".xz"

  #subprocess.call("mkdir -p /tmp/pablom/", stdout=subprocess.PIPE, shell=True)
  #subprocess.call("/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select cp " + source + "/" + file + " /tmp/pablom/", stdout=subprocess.PIPE, shell=True)
  #subprocess.call(['gunzip ' + "/tmp/pablom/" + file], shell=True)
  #subprocess.call(['mv ' + "/tmp/pablom/" + nameNoGz + " " + "/tmp/pablom/" + name_aux], shell=True)
  subprocess.call("/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select cp " + source + "/" + file + " .", stdout=subprocess.PIPE, shell=True)
  subprocess.call(['gunzip ' + "./" + file], shell=True)
  subprocess.call(['mv ' + "./" + nameNoGz + " " + "./" + name_aux], shell=True)

  filew = open("./" + nameNoGz, "w")
  source = open("./" + name_aux)

  temp = open(template)

  mass1t = mass1
  mass2t = mass2

  if(int(mass1t) == 0):
    mass1t = "1"
  if(int(mass2t) == 0):
    mass2t = "1"

  for l in temp.readlines():
   
    if( l.find("MASS1") != -1 ):
      l = l.replace("MASS1", mass1t)
    if( l.find("MASS2") != -1 ):
      l = l.replace("MASS2", mass2t)

    filew.write(l)

  counter = 0
  writeLine = 0
  for l in source.readlines():
    if(writeLine == 1):
      if(l.find("<scales") != -1 and l.find("</scales>") != -1):
        filew.write("# model " + modelname + "_" + mass1 + "_" + mass2 +"\n")
      #if(l.find("</event>") != -1):
      #  counter = counter + 1
        #if(counter == number):
        #  filew.write("</event>" + "\n")
        #  filew.write("</LesHouchesEvents>" + "\n")
        #  break
      filew.write(l)
    if(l.find("## END BANNER##") != -1):
      writeLine = 1
  filew.close()

  subprocess.call(['rm ' + "./" + name_aux], shell=True)
  subprocess.call(['xz -z -1 ' + "./" + nameNoGz], shell=True)
  
  subprocess.call("/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select cp " + "./" + namexz + " " + destiny + "/", stdout=subprocess.PIPE, shell=True)
  subprocess.call("rm " + "./" + namexz, shell=True)


if __name__ == "__main__":

  template = sys.argv[1]
  mass1 = sys.argv[2] 
  mass2 = sys.argv[3] 
  number = int(sys.argv[4])
  modelname = sys.argv[5]
  source = sys.argv[6]
  file = sys.argv[7]
  destiny = sys.argv[8]
  doFile(template, source, destiny, mass1, mass2, file, modelname, number)


