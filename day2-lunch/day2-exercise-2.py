#!/usr/bin/env python

import sys

#open alignment file
fh = open( sys.argv[1])

#start total 0

total = 0

#look at each row

for row in fh:
    if row.startswith("@"):
        continue
    #if you see 0 score in string in row count up    
    if "NM:i:0" in row: 
        total+=1
#print total    
print total
    
    