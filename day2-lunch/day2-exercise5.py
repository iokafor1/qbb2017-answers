#!/usr/bin/env python 

import sys

#open alignment file
fh = open( sys.argv[1])

#start count and total at 0
total = 0.0
count = 0.0

#for each row skip if it has '@' header
for row in fh:
    if row.startswith( "@" ):
        continue
    #split rows into a series of strings    
    id = row.split('\t')
    #add the number in column 4 to total
    total = total + float(id[4])
    #increase count by 1
    count += 1

#print average    
print total / count    
    
    