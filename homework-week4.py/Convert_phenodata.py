#!/usr/bin/env python

"""
Usage: Converts Phenotype text file to plink2 readable file


 <./Convert_phenodata.py> <tabBYxRM_PhenoData.txt>
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


pheno_1 = []
pheno_2 = []

phenotype = open(sys.argv[1], "r")
outfile = open(sys.argv[2], "w")

for line in phenotype:
    if line.startswith("\t"):
        outfile.write("\t" + line + "\n")
        continue
    if line.startswith("A"):
        pheno_1 = line.split()
        pheno_2 = pheno_1[0].replace("_", "\t") 
        remainder = "\t".join(pheno_1[1:])
        outfile.write(pheno_2 + "\t" + remainder + "\n")