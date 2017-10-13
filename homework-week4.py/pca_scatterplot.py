#!/usr/bin/env python


"""
Usage <pca_scatterplot.py> <plink.eigenvec>

"""


import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_pca = pd.read_csv( sys.argv[1], sep="\t" )

x = df_pca["PC1"]
y = df_pca["PC2"]


fig = plt.figure()
plt.scatter((x),(y), alpha = 0.3)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.savefig("pca" + ".png" )
plt.close()