#!/usr/bin/env python

"""

Usage <output_enrich.heat.npz> <ctcf_peaks.tsv>

"""

import numpy
import sys

# data=numpy.load('wk8enrich.heat.npz')
#
# print data.keys()

enrich = open(sys.argv[1])
ctcf = open(sys.argv[2])
data=numpy.load(enrich)
ctcf_pos = []
enrichment = data["0.enrichment"]
forward = data["0.forward"]
reverse = data["0.reverse"]
for i in ctcf:
    fields = i.split()
    if fields[1] == "Position":
        continue 
    else:
        ctcf_pos.append(float(fields[1]))


f_index=[]
r_index=[]

for i,frag in enumerate(forward):
    for j,pos in enumerate(ctcf_pos):
        if frag[0] <pos and frag[1]>pos:
            f_index.append(i)

for i,frag in enumerate(reverse):
    for j,pos in enumerate(ctcf_pos):
        if frag[0] <pos and frag[1]>pos:
            r_index.append(i)

ctcf_enrich=enrichment[f_index,:][:,r_index]

f_numpy = numpy.argmax(ctcf_enrich, axis = 0)
f_val = numpy.amax(ctcf_enrich, axis = 0)
r_numpy = numpy.argmax(ctcf_enrich, axis = 1)
r_val = numpy.amax(ctcf_enrich, axis = 1)

print 'Top rev primer interactions'
rev_i = 0
for fwd_i in f_numpy:
    print 'Rev region = %s, Fwd region = %s, enrichment = %s' % (reverse[rev_i], forward[fwd_i], f_val[rev_i])
    rev_i += 1
print '\nTop fwd primer interactions'
fwd_j = 0
for rev_j in r_numpy:
    print 'Fwd region = %s, Rev region = %s, enrichment = %s' % (forward[fwd_j], reverse[rev_j], r_val[fwd_j])
    fwd_j += 1



