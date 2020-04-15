# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:53:52 2020

@author: Soham Dutta
"""
"""expression evaluation using binary tree"""
class node:
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None

def insert(arr,root,i,n):
    if (i<n):
        
            root=node(arr[i])
       
            root.left = insert(arr,root.left,2*i+1,n)
            root.right = insert(arr,root.right,2*i+2,n)
    return root
def eval(root):
    if root.info <='9' and root.info >='1':
        return root.info
    else:
        a=eval(root.left)
        b=eval(root.right)
        if(root.info =='+'):
            return(int(a)+int(b))
        if(root.info =='-'):
             return(int(a)-int(b))
        if(root.info =='*'):
             return(int(a)*int(b))
        if(root.info =='/'):
            return(int(int(a)/int(b)))
        
    
def display(root):
    if (root is None):
        return
    display(root.left)
    print(root.info)
    display(root.right)
root=None    
arr=['*','+','*','2','3','6','7']
n=len(arr)
root=insert(arr,root,0,n)
display(root)
val=eval(root)
print("The value is:")
print(val)