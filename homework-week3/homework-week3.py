#!/usr/bin/env python

"""
Plots Allele frequency
usage <homework-week3.py> <filtered.vcf> 
"""

import sys
import itertools
import matplotlib.pyplot as plt


freebayes =  open(sys.argv[1])

allele_frequency = []


plt.figure()
for i in freebayes:
    if i.startswith('#'):
        pass
    else:
        i = i.split('\t')[7]
        c = i.split(';')[3]
        c = c.lstrip("AF=")
        a = c.split(',')
        for l in a:
            allele_frequency.append(float(l))
            
plt.hist(allele_frequency)
plt.savefig("Allele_frequency" + ".png")
plt.close()

            
     



    
    