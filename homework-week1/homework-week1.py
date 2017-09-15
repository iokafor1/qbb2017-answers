#!/usr/bin/env python 

import sys
import fasta
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.regression.linear_model 

"""
Usage <alignment_prot.fa> <1000 homologs.fa>

"""


amino_acid = open(sys.argv[1])
nucleic_acid = open(sys.argv[2])


aa_list = []
na_list = []



for ident, sequence in fasta.FASTAReader(amino_acid):
    aa_list.append(sequence)
    
for ident, sequence in fasta.FASTAReader(nucleic_acid):
    na_list.append(sequence)
    
full_seq=[]
for j, peptide_seq in enumerate(aa_list):
    i = 0
    new_seq = ""
    nucleotide_seq = na_list[j] 
    for p in peptide_seq:
        if p == "-":
            new_seq += "---"
        else:
            new_seq += nucleotide_seq[i:i+3]
            i += 3
    full_seq.append(new_seq)




bases = ['T', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))



Dn = []
Ds = []
for k in range(0,len(full_seq[0]),3):
    n = 0
    s = 0
    r_codon = full_seq[0][k:k+3]
    for seq in full_seq:
        t_codon = seq[k:k+3]
        if t_codon == r_codon:
            pass
        elif t_codon == '---' or r_codon == '---':
           pass
        elif "W" in t_codon or "W" in r_codon:
            pass  
        elif "Y" in t_codon or "Y" in r_codon:
            pass    
        elif "R" in t_codon or "R" in r_codon:
            pass
        elif "N" in t_codon or "N" in r_codon:
            pass        
        elif "S" in t_codon or "S" in r_codon:
            pass
        elif "-" in t_codon or "-" in r_codon:
            pass
        elif "M" in t_codon or "M" in r_codon:
            pass    
        elif "K" in t_codon or "K" in r_codon:
            pass            
        elif codon_table[t_codon] == codon_table[r_codon]:
            s += 1
        elif codon_table[t_codon] != codon_table[r_codon]:
            n +=1
    Ds.append(s)
    Dn.append(n) 

ratio=[]    
for i in range(len(Ds)):
    if Ds[i] == 0 or Dn[i] == 0:
        pass
    else:
        r = float(Ds[i])/Dn[i]
        ratio.append(r)

    
x = range(len(ratio)) 
  
plt.figure()
plt.scatter(x,ratio)
plt.yscale('log')
plt.xlabel('Position')
plt.ylabel('ratio (Ds/Dn)')
plt.title('Selection')
plt.savefig('Selection.png')
plt.close()    
    
         
          


 