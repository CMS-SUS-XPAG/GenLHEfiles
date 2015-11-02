#/usr/bin/python

import sys

f = open(sys.argv[1])
efficiency = float(sys.argv[2])

total = 0
for l in f.readlines():
   k = l.split()
   total = total + float(k[2])


print total, "%.2f" % (total/efficiency)
