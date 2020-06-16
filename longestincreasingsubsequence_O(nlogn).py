# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:32:20 2020

@author: Soham Dutta
"""
import bisect
def LIS(arr):
    maxE,l=[arr[0]],1
    for i in range(1,len(arr)):
        if arr[i]<maxE[0]:
            maxE[0]=arr[i]
            
        elif arr[i]>maxE[l-1]:
            maxE.append(arr[i])
            l+=1
        else:
            maxE[bisect.bisect_left(maxE,arr[i])]=arr[i]
    return l


print(LIS([0,8,4,12,2,10,6,14,1,9,5,13]))
            
            
        