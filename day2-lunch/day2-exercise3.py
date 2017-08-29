#!/usr/bin/env python 


import sys

#open alignment file
fh = open( sys.argv[1] )

#start total at 0

total = 0

#look at each row

for row in fh:
    if row.startswith("@"):
        continue
    #if you see 1 score in string in row count up   
    if "NH:i:0:" in row: 
        total+=1
#print total    
print total
    
