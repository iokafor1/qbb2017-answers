#!/usr/bin/env python

"""
Takes a directory of fastq files, turns them into sam files with bwa mem, converts them to bam, sorts, and indexes them using samtools

Usage:
./sam_bam_index_sort.py <fastq directory>
"""

import os
import sys

path =  os.path.abspath( sys.argv[1] )

files = os.listdir( path )

for each in files:
    prefix = each.split('.')[0]
    os.system( 'bwa mem -R "@RG\\tID:%s\\tSM:%s" sacCer3.fa Variance/%s.fastq > %s.sam' % (prefix, prefix, prefix, prefix) )
    os.system( 'samtools view -b -S %s.sam > %s.bam' % (prefix, prefix) )
    os.system( 'samtools sort -m 100000000 %s.bam -o %s_sorted.bam' % (prefix, prefix) )
    os.system( 'samtools index %s_sorted.bam' % (prefix) )
    
    
