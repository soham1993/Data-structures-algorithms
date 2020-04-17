# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:09:15 2020

@author: Soham Dutta
"""
def heapsort(arr):
    size=len(arr)-1
    buildheap(arr,size)
    display(arr)
    
    while (size>=0):
        maxval=arr[0]
        arr[0]=arr[size]
        size-=1
        restoredown(arr,0,size)
        arr[size+1]=maxval
    return arr
def display(arr):
    for i in range(0,len(arr)):
        print(arr[i])
def buildheap(arr,size):
    n=int(size+1/2)-1
    for i in range(n,-1,-1):
        restoredown(arr,i,size)
def restoredown(arr,i,size):
    num=arr[i]
    left=2*i+1
    right=left+1
    while(right<=size):
        if (num>= arr[left] and num>= arr[right]):
            arr[i]=num
            return
        elif(arr[left]>arr[right]):
            arr[i]=arr[left]
            i=left
        else:
            arr[i]=arr[right]
            i=right
        
        left=2*i
        right=left+1
        
    if(left == size and num < arr[left] ):
                arr[i]=arr[left]
                i = left

    arr[i]=num
"""it extracts the max and deletes it"""    
def extractmax(arr):
    num=arr[0]
    print("the max is:")
    print(num)
    size=len(arr)-1
    arr[0]=arr[size]
    size-=1
    buildheap(arr,size)
    display(arr)

arr=[4,5,16,80,4,100,200]
a=heapsort(arr)
#extractmax(a)


for i in range(0,len(a)):
    print("The sorted list is :")
    print(a[i])