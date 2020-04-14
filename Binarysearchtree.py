# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:23:31 2020

@author: Soham Dutta
"""
class node:
    def __init__(self, info): 
        
        self.info=info
        self.right=None
        self.left=None


def insert(ptr,val):
    """inserting in the binary tree"""
    if(ptr is None):
        ptr=node(val)
    elif(val<=ptr.info):
        ptr.left=insert(ptr.left,val)
    elif(val>ptr.info):
        ptr.right=insert(ptr.right,val)
   
   
    return ptr
   
        
    
def search(ptr,key):
    if(ptr is None):
        print("Element not found")
        
         
    elif(key<ptr.info):
         search(ptr.left,key)
    elif(key>ptr.info):
         search(ptr.right,key)
    else:
        print("element found")
"""deletion of key"""
def delete(ptr,key) :
    if(ptr is None):
        print("key not found")
    elif(key<ptr.info):
        ptr.left=delete(ptr.left,key)
    elif(key>ptr.info):
        ptr.right=(ptr.right,key)
    else:
        if(ptr.right is not None and ptr.left is not None):
            succ=ptr.right
            while(succ.left):
                succ=succ.left
            ptr.info=succ.info
            ptr.right = delete(ptr.right, succ.info)
        elif(ptr.right is not None):
            ptr=ptr.right
        elif(ptr.left is not None):
            ptr=ptr.left
        else:
            ptr=None
    return ptr

def min (ptr)   :
    if(ptr is None):
        print("Tree is empty")
    elif (ptr.left is None):
          print("the minimum is:")
          print(ptr.info)
    else:
        min(ptr.left)
           
        
def max(ptr):
    if(ptr is None):
        print("Tree is empty")
    elif (ptr.left is None):
          print("the max is:")
          print(ptr.info)
    else:
        max(ptr.right)

def preorder(ptr):
    if(ptr==None):
        return
    print(ptr.info)
    preorder(ptr.left)
    preorder(ptr.right)
        
def inorder(ptr):
    if(ptr==None):
        return
    inorder(ptr.left)
    print(ptr.info)
    inorder(ptr.right)
    
def postorder(ptr):
    if(ptr==None):
        return
    postorder(ptr.left)
    postorder(ptr.right)
    print(ptr.info)
"""finding height of the tree"""           
def height(ptr):
    if ptr is None:
        return 0;
    
    lheight=height(ptr.left)
    rheight=height(ptr.right)
    if lheight>rheight:
        return 1+lheight
    else:
        return 1+rheight            
        




root=None
arr=[45,56,9,23,25,100,6,0,52,51]

for i in range(0,9):
    root=insert(root,arr[i])

    
min(root)
max(root)
search(root,25)   
