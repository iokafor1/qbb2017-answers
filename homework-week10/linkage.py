#!/usr/bin/env python



import numpy as np
import sys
import pandas as pd
from matplotlib import pyplot as plt
import scipy.cluster.hierarchy as hac 
from scipy.spatial.distance import pdist
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans

inFile = open(sys.argv[1],'r')
colHeaders = inFile.next().strip().split()[1:]
rowHeaders = []
dataMatrix = []

for line in inFile:
    data= line.strip().split('\t')
    rowHeaders.append(data[0])
    dataMatrix.append([float(x) for x in data[1:]])
    
dataMatrix = np.array(dataMatrix)


linkageMatrix = hac.linkage(dataMatrix, method = "average")

heatmapOrder = hac.leaves_list(linkageMatrix)

linkageMatrix_transposed = hac.linkage(dataMatrix.T, method = "average")

heatmapOrder_transposed = hac.leaves_list(linkageMatrix_transposed)


orderedDataMatrix = dataMatrix[heatmapOrder,:][:,heatmapOrder_transposed]

labels = np.array( ['CFU', 'poly', 'unk', 'int', 'mys', 'mid'])
labels_t = labels[ heatmapOrder_transposed ]
plt.figure()
plt.imshow(orderedDataMatrix, aspect='auto', interpolation= 'nearest')
plt.grid(False)
plt.xticks( [ x for x in range(6)], labels_t)
plt.title("Heatmap of Iris Characteristic")
plt.colorbar()
plt.savefig('heatmap.png')
plt.close


plt.figure()
hac.dendrogram(linkageMatrix_transposed, labels=labels)
plt.savefig( 'dendrogram.png' )
plt.close()

kmeans= KMeans( n_clusters=5, random_state=0 )
kmeans.fit( dataMatrix )
labels = kmeans.predict( dataMatrix )
dataMatrix_df = pd.merge( pd.DataFrame(dataMatrix, columns = ['CFU', 'poly', 'unk', 'int', 'mys', 'mid']),
pd.DataFrame( labels, columns=['cluster'] ), left_index=True, right_index=True )
k_clustered = dataMatrix_df.sort_values('cluster')[['CFU', 'poly', 'unk', 'int', 'mys', 'mid']].values

plt.figure()
plt.imshow(k_clustered, aspect='ratio', interpolation='nearest')
plt.grid(False)
plt.title("Heatmap of Iris chracteristics")
plt.colorbar()
plt.xticks()
plt.savefig("k_clustered.png")



