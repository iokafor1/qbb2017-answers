#!/usr/bin/env python

import sys

#open alignment file
fh = open(sys.argv[1])

#Start count at 0 
count = 0 

#look at each line
for line in fh:
   #if it is a header ignore it and continue on
    if line.startswith("@"):
        continue
    #count up and add up   
    count += 1
#print the total
print count 

#close sam file
fh.close()