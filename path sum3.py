# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 00:38:25 2020

@author: Soham Dutta
"""

class Solution(object):
    def __init__(self):
        self.count=0
        
    def pathSum(self, root, target):
        d={}
        d[0]=1
        def Sum(root,s):
           
            if root is None:
                return 
            s+=root.val
            
            if s-target in d:
               
                self.count+=d[s-target]
                
            if s in d :
                d[s]+=1
            elif s not in d :
                d[s]=1
            
            Sum(root.left,s)
            Sum(root.right,s)
            d[s]-=1
        Sum(root,0)
        return self.count
            
            
           