#!/usr/bin/env python

"""./manhattanscript1.py <plink.P10.assoc.linear (or another file)>
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

pvalue = []
pnums = []
pvas = []
good_x = []
good_y = []
bad_x = []
bad_y = []

phenofiles = open( sys.argv[1] )
count = 0
for line in phenofiles:
    if line.startswith(" ") or "NA" in line:
        continue
    else:
        cutoff = -np.log( 0.00005 )
        line = line.rstrip("\r\n").split()
        count += 1
        pvalue = -np.log( float(line[8]) )
        if pvalue > cutoff:
            good_x.append( count )
            good_y.append( pvalue )
        else: 
            bad_x.append( count )
            bad_y.append( pvalue )


plt.figure()
plt.scatter( good_x, good_y, color = 'red', alpha = 0.5 )
plt.scatter( bad_x, bad_y, color = 'blue', alpha = 0.5 )
plt.title("Manhattan Plot" + sys.argv[1])
plt.ylabel("-log(P-Value)")
plt.xlabel("SNP")
plt.savefig( "Manhanttan" + sys.argv[1] + ".png")
plt.close()