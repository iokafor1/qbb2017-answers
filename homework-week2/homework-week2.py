#!/usr/bin/env python

"""

usage <contigs.fa>

"""

import sys
import fasta
import numpy as np


contig = open(sys.argv[1])
contig_seq = []

for ident, sequence in fasta.FASTAReader( contig ):
    contig_seq.append(sequence)
    
contig_len = []
    
for i in range(len(contig_seq)):
    contig_len.append(len(contig_seq[i]))

contig_len.sort()
mean_contig_len = np.mean(contig_len)
    
print "Min = " + str(min(contig_len))
print "Max = " + str(max(contig_len))
print "Mean = " + str(mean_contig_len)



i = 0
k = 0
while k < (sum(contig_len) / 2):
    i += 1
    k += contig_len[i]

n50 = contig_len[i]

print "n50 = " + str(n50)    
    
    
    
    
    
    