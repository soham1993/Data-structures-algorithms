# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:12:49 2020

@author: Soham Dutta
"""

class node: 

    def __init__(self, info): 
        self.info = info  
        self.left = None
        self.right = None 
        

def BtoDLL(root):
    if root.left:
        left=BtoDLL(root.left)
        while(left.right):
            left=left.right
        
        left.right=root
        root.left=left
        
    if root.right:
        right=BtoDLL(root.right)
        while(right.left):
            right=right.left
        right.left=root
        root.right=right
        
    return root

def BtodLL(root):
    if root==None:
        return root
    
    root=BtoDLL(root)
    
    while root.left:
        root=root.left
    return root
def printlist(root):
    if root==None:
        return 
    while(root):
        print(root.info,end=" ")
        root=root.right
    


if __name__=='__main__':
    root=None
    root=node(10)
    root.left=node(20)
    root.right=node(30)
    root.left.left=node(40)
    root.left.right=node(50)
    root.right.left=node(60)
    root.right.right=node(70)
    root=BtodLL(root)
    printlist(root)
        