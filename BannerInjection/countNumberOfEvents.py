#/usr/bin/python

import sys

f = open(sys.argv[1])
efficiency = int(sys.argv[2])

total = 0
for l in f.readlines():
   k = l.split()
   total = total + int(k[2])


print total, total*efficiency
