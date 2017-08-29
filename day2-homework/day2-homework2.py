#!/usr/bin/env python

import sys

# Add three arguments either skip or "something else" 
mapping = open( sys.argv[1] ) 
c_tab = open( sys.argv[2] )
arg = sys.argv[3]
#start count at 0
count = 0

#create dictionary of mapping data
mapping_dict = {}
#for each row in mapping
for row in mapping:
    #strip
    line = row.rstrip("\r\n").split()
    #designate key and definition
    mapping_dict[line[1]] = line[0]
#for each line in c_tab count up until 100 is reached then stop    
for i in c_tab:
    if count >= 100:
        break
    #if not then print match with identifier     
    else:
        c_tab_strip = i.rstrip("\r\n").split()
        if c_tab_strip[8] in mapping_dict:
            print i.strip() ,"\t", mapping_dict[c_tab_strip[8]]
            count += 1
        else:
            if arg == "skip":
                pass
            else:
                print i.strip() ,"\t", "*"
        
           
    
    
    




