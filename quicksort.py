# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:46:12 2020

@author: Soham Dutta
"""

def partition(a,p,q):
    x=a[p]
    i=p
    for j in range(p,q+1):
        if a[j]<=x:
            i=i+1
            t=a[i]
            a[i]=a[j]
            a[j]=t
    t=a[i]
    a[i]=a[p]
    a[p]=t
    return i

def quicksort(a,p,r):
    if (p<r):
        q=partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)
        
arr = [10,80,30,90,40,50,70] 
n = len(arr) 
print ("Given array is") 
for i in range(n): 
    print ("%d" %arr[i])
 
mergesort(arr,0,n-1) 
print ("\n\nSorted array is") 
for i in range(n): 
    print ("%d" %arr[i])    
        
