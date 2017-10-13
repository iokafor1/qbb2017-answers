#!/usr/bin/env python

"""
Plots Allele frequency
usage <homework-week3.py> <filtered.vcf> 
"""

import sys
import itertools
import matplotlib.pyplot as plt


vcf_file =  open(sys.argv[1])

allele_frequency = []


plt.figure()
for i in vcf_file:
    if i.startswith('#'):
        pass
    else:
        i = i.split('\t')[7]   
        i = i.lstrip("AF=")
        if "," in i:
            i = i.split(",")[0]
        allele_frequency.append(float(i))

 #        a = c.split(',')
 #        for l in a:

            
plt.hist(allele_frequency)
plt.savefig("Allele_frequency" + ".png")
plt.close()