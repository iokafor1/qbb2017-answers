#!/usr/bin/env python

"""

usage <lastz.tsv> 

"""

import sys
import fasta
import itertools
import matplotlib.pyplot as plt



data = open(sys.argv[1])

count = 0
plt.figure()
for i in data:
    if "zstart1" in i:
        continue
    else:
        fields = i.split("\t")
        plt.plot((count,count+int(fields[3])), (int(fields[0]), int(fields[1])))
 
        # print count
  #       print count+int(fields[3])
  #       print int(fields[0])
  #       print int(fields[1])
  #
#         plt.plot(([count,count+int(fields[3])], [int(fields[0]),int(fields[1])]))
        count += int(fields[3])
#
#
#
#
plt.title('Velvet Assembled Reads')
plt.xlabel('Contigs')
plt.ylabel('Position')
plt.ylim((0,120000))
plt.xlim((0,80000))
plt.savefig("Velvet_Assembled_Reads" + ".png")
plt.close()

