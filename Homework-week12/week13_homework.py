#!/usr/bin/env 


"""
Usage: <week13_homework.py> <.kraken>

"""


import sys

iko = sys.argv[1]

krona={}

for line in open iko:
    item = line.strip('\n').split('\t')
    if item [1] not in krona:
        krona[item[1]] = 1
    else:
        krona[item[1]] +=1
        
for iko in krona:
    print str(krona[iko]) + "\t" + "\t".join(iko.split(";"))
    
    
    