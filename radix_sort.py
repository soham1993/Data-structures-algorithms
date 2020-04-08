# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:26:31 2020

@author: Soham Dutta
"""

def countsort(a,place):
    n=len(a)
    b=10*[0]
    output=n*[0]
    
    for i in range(0,n):
        index=a[i]//place
        b[index%10]=b[index%10]+1
    for j in range (1,10):
        b[j]=b[j]+b[j-1]
        
    k=n-1
    while(k>=0):
         index=a[k]//place
         output[b[index%10]-1]=a[k]
         b[index%10]=b[index%10]-1
         k=k-1
    for i in range(0,n):
        a[i]=output[i]
    print(a)
        
def radixsort(a):
    max_element=max(a)
    place=1
    while (max_element//place>0):
        countsort(a,place)
        place=place*10
        
data = [121, 432, 564, 23, 1, 45, 788]
radixsort(data)
print(data)
         
        
        
        