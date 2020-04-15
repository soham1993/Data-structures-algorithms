# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 00:56:35 2020

@author: Soham Dutta
"""
"""this a function to complete the grid"""
def printg(arr):
    for i in range(0,3):
        for j in range(0,3):
            print(arr[i][j],end=" ")
        print()
       
        
"""this function finds whheter wheter any item is empty"""
def findoccur(arr,l):
    for i in range(0,3):
        for j in range(0,3):
            if arr[i][j]==0:
                l[0]=i
                l[1]=j
                return True
    return False
"""the function checks whether the item is legal to use in the row"""
def findrow(arr,row,num):
    for i in range(0,3):
        if arr[row][i]==num:
            return True
    return False

"""the function checks whether the item is legal to use in the row"""
def findcol(arr,col,num):
    
      for i in range(0,3):
          
          if arr[i][col]==num:
              return True
      return False

"""this function checks whether the number can be placed in a given location""" 
def check_location_eligible(arr,row,col,num):
    return not findrow(arr,row,num) and not findcol(arr,col,num)

"""solving the problem"""
def solve(arr):
    l=[0,0]
    if not findoccur(arr,l):
         return True
    row=l[0] 
    col=l[1]
    
    for num in range(1,4):
        if check_location_eligible(arr,row,col,num) is True:
            arr[row][col]=num
            
            if(solve(arr)):
                return True
            arr[row][col]=0
    """this triggers backtracking"""
    return False
"""Main function"""
grid=[[2,0,3],[1,0,0],[0,0,1]]
"""if success print the grid """
if(solve(grid)): 
        printg(grid) 
else: 
        print ("No solution exists")
  