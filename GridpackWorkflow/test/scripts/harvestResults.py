import os
import subprocess
import argparse

argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logDir', action='store', help="The script that should be run on condor")
args = argParser.parse_args()


files = os.listdir(args.logDir)

inputFiles = [ f for f in files if 'err' in f ]

totalEvents = 0
passedEvents = 0
negWeightEvents = 0

for inFile in inputFiles:
    print
    print "Looking for results in file %s"%inFile
    resultsLine = None
    line = ''
    with open(os.path.join(args.logDir,inFile),'r') as f:
        while True:
            if line.startswith('Process'): header = line.replace('\n','')
            line = f.readline()
            if line.startswith("Total"):
                resultsLine = line
                break
            if line == '': break
    if resultsLine:
        print header
        print resultsLine
        res = resultsLine.split()
        totalEvents += int(res[7])
        passedEvents += int(res[4])
        negWeightEvents += int(res[6])
    else:
        print "No result found..."

format_str = "{:40}{:10}"

print "### RESULTS ###"
print "Found %s files to scan."%len(inputFiles)
print format_str.format("Total events:",totalEvents)
print format_str.format("Passed events:",passedEvents)
print format_str.format("Events w/ neg weight:",negWeightEvents)
print format_str.format("Fraction passed:",round(float(passedEvents)/totalEvents,4))
print format_str.format("Out of which with neg weight:",round(float(negWeightEvents)/passedEvents,4))
