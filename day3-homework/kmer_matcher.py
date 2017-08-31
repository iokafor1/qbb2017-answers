#!/usr/bin/env python

"""
Match kmer from FASTA file
"""

import sys
import fasta


target = open(sys.argv[1])
query = open(sys.argv[2])
k = int(sys.argv[3])


#create dictionary

kmer_dict = {}

for ident, sequence in fasta.FASTAReader( target ): #for identifier and sequence from fasta reader file "target"
    sequence = sequence.upper() #define sequence 
    for i in range( 0, len(sequence) - k +1): #for each line from start to length of sequence
        kmer = sequence[i:i+k] #kmer is defined as sequence length to of next kmer
        if kmer not in kmer_dict: #if kmer is not dictionary add it
            kmer_dict[kmer] = [(ident,i)] # key kmer and value position and name "tuple"
        else:
            kmer_dict[kmer].append((ident,i)) #if kmer is in dictionary append position and ident
ident, sequence_q = fasta.FASTAReader( query ).next() #for identifier and sequence from fasta reader file "query"
sequence_q = sequence.upper() #define sequence 
for j in range( 0, len(sequence_q) - k +1): #for each line from start to length of sequence
    kmer_q = sequence_q[j:j+k]
    if kmer_q in kmer_dict:
        result = kmer_dict[kmer_q]
        for item in result:
            print item[0],"\t",item[1],"\t",j,"\t", kmer_q

  
            
    
            
            
    

