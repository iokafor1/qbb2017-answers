#!/usr/bin/env python   

import random

nums = range(0,100,10)

#what we are looking for
key = 10
##initialize the whle is to be searched
lo = 0 
hi = len(nums)

#main loop: keep going while there are options avaialable
while lo < hi:
    ## find the middle item
    mididx = (lo + hi) / 2
    mid = nums[mididx]
    print "checking in the range [%d,%d] mididx[%d] =[%d]" % (lo, hi, mididx, mid)
    ## compare the middle item to the list
    if (mid == key):
        print "Found %d==%d at index %d" % (key, mid, mididx)
        break
    #key is greater tha    
    elif (key > mid):
        lo = mididx + 1
    else:
        hi = mididx
    
        
    
    




    

