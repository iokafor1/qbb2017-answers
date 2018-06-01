#!/usr/bin/env python

"""<./wk13kraken.py> <*.Kraken>
"""

import sys
import pandas as pd

a = open(sys.argv[1])


kronadict = {}

for line in a:
    item = line.strip('\n').split('\t')
    if item[1] not in kronadict:
        kronadict[item[1]] = 1
    else:
        kronadict[item[1]] += 1
        
for a in kronadict:
    print str(kronadict[a]) + "\t" + "\t".join(a.split(";"))
    