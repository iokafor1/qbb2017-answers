#!/usr/bin/env python

import sys

#open alignment file
fh = open( sys.argv[1])

#create empty list called chromosome
chromosome = []

#for each row skip if it has '@' header
for row in fh:
    if row.startswith( "@" ):
        continue
    #split each row into a series of strings    
    id = row.split('\t')
    #if columb has * skip
    if id[2] != "*":
        #append chromosome list with index 2 of list
        chromosome.append(id[2])
    else:
        pass
    
print chromosome[:10]


