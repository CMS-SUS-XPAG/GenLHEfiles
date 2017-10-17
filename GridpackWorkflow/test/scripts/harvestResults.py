import os
import subprocess
import argparse
import math

argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logDir', action='store', help="The script that should be run on condor")
argParser.add_argument('--verbose', action="store_true", help="Show all the output")
args = argParser.parse_args()


files = os.listdir(args.logDir)

inputFiles = [ f for f in files if 'err' in f ]

totalEvents = 0
passedEvents = 0
negWeightEvents = 0

nResults = 0
avgTime = 0

for inFile in inputFiles:
    if args.verbose:
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
            if line.startswith(" - Avg event:"):
                timeline = line
                break
            if line == '': break
    if resultsLine:
        if args.verbose:
            print header
            print resultsLine
        res = resultsLine.split()
        totalEvents += int(res[7])
        passedEvents += int(res[4])
        negWeightEvents += int(res[6])
        avgTime += float(timeline.split()[3])
        nResults += 1
    else:
        if args.verbose:
            print "No result found..."

format_str = "{0:35}{1:>20}"

print totalEvents
print "### RESULTS ###"
print "Found %s files to scan."%len(inputFiles)
print format_str.format("Total events:",totalEvents)
print format_str.format("Passed events:",passedEvents)
print format_str.format("Events w/ neg weight:",negWeightEvents)
print format_str.format("Fraction passed:","%s +/- %s"%(round(float(passedEvents)/totalEvents,4), round(math.sqrt(float(passedEvents))/totalEvents,4)))
print format_str.format("Out of which with neg weight:",round(float(negWeightEvents)/passedEvents,4))
print format_str.format("Avg. Time:",round(float(avgTime)/nResults,1))
