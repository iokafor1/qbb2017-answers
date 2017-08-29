#!/usr/bin/env python 

import sys

fh = open (sys.argv[1])

#if the line has "DROME" select line
for line in fh:
    if "DROME" in line: 
        #split white space and delimeter columns with a space
        ls = line.split() 
        if len(ls) > 3:
            #print last two columns of list 
            print ls[2], ls[3]
                
