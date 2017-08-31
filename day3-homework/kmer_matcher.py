#!/usr/bin/env python

"""
Match kmer from FASTA file
"""

import sys
import fasta


target = open(sys.argv[1])
query = open(sys.argv[2])
k = int(sys.argv[3])

count = 0

#create dictionary

kmer_dict = {}

for ident, sequence in fasta.FASTAReader( target ): #for identifier and sequence from fasta reader file "target"
    sequence = sequence.upper() #define sequence 
    for i in range( 0, len(sequence) - k +1): #for each line from start to length of sequence
        kmer = sequence[i:i+k] #kmer is defined as sequence length to of next kmer
        if kmer not in kmer_dict: #if kmer is not dictionary add it
            kmer_dict[kmer] = [i]
        else:
            kmer_dict[kmer].append(i) #if kmer is in dictionary append position
ident, sequence in fasta.FASTAReader( query ).next() #for identifier and sequence from fasta reader file "query"
sequence = sequence.upper() #define sequence 
for i in range( 0, len(sequence) - k +1): #for each line from start to length of sequence
    kmer = sequence[i:i+k]
    if count >= 1000:
        break
    else:
        if kmer in kmer_dict:
            print  kmer_dict[kmer],"\t",i,"\t",kmer 
            count += 1
            
    
            
            
    

