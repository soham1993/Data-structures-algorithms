# -*- coding: utf-8 -*-
"""
Created on Fri May  8 23:59:56 2020

@author: Soham Dutta
"""
"""
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
 *
 * Solution
 * Take minimum size of two array. Possible number of partitions are from 0 to m in m size array.
 * Try every cut in binary search way. When you cut first array at i then you cut second array at (m + n + 1)/2 - i
 * Now try to find the i where a[i-1] <= b[j] and b[j-1] <= a[i]. So this i is partition around which lies the median.
 *
 * Time complexity is O(log(min(x,y))
 * Space complexity is O(1)"""
import math
def mediansortedarray(nums1,nums2):
    m=len(nums1)
    n=len(nums2)
    
    if(m>n):
        nums1,nums2,m,n=nums2,nums1,n,m
    l,h=0,m
    
    while(l<h):
        partx=(l+h)/2
        party=(m+n+1)/2-partx
        
        if (partx == 0):
            maxleftx=-math.inf
        else:
            maxleftx=nums1[partx-1]
            
        if (partx == m ):
            minrightx=math.inf
        else:
            minright=nums2[partx]
            
        if (party == 0):
            maxlefty=-math.inf
        else:
            maxlefty=nums1[party-1]
            
        if (party == m ):
            minrighty=math.inf
        else:
            minrighty=nums2[party]
            
            
        if((maxleftx<=minrighty) and (minrightx >=maxlefty):
            if((x+y)%2 == 0):
                return((max(maxleftx,maxlefty)+max(minleftx,minlefty))/2)
            else:
                return (max(maxleftx,maxlefty))
            
        elif(maxleftx>minrighty):
            
        
    
    
    
        
    
        
        