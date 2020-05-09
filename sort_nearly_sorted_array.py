# -*- coding: utf-8 -*-
"""
Created on Sat May  9 19:55:40 2020

@author: Soham Dutta
"""
from heapq  import heappop, heappush, heapify 
def sortedarray(nums1,k):
    heap=nums1[:k+1] #pushing k elements in the heap
    heapify(heap)
    i=0
    for j in range(k+1,len(nums1)):
        nums1[i]=heappop(heap)
        heappush(heap,nums1[j])
        i+=1
    while heap:
        nums1[i]=heap
    