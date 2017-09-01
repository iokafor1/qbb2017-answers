#!/usr/bin/env python

"""


"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA


df = pd.read_csv( sys.argv[1], sep= "\t")

# print df
soi_plus = df['strand'] == "+"
soi_minus = df['strand'] == "-"

fpkms_plus = []
fpkms_minus = []

for row in df[soi_plus].itertuples():
    ch = row[2]
    p = (int(row[4]) - int(500))
    if p <= 0:
        p = 0 
    p2 = (int(row[4]) + int(500))
    name = row[6]
    
    print "%s\t%d\t%d\t%s" % (ch,p,p2,name)
    
for row in df[soi_minus].itertuples():
    ch = row[2]
    p = (int(row[4]) - int(500))
    if p <= 0:
        p = 0
    p2 = (int(row[4]) + int(500))
    name = row[6]
    print "%s\t%d\t%d\t%s" % (ch,p,p2,name)
    
    
