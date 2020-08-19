# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:44:04 2020

@author: Soham Dutta
"""

def absolutediff(N,K):
    
    store=set()
    
    def nums(numl,i):
        print(numl)
        
        if i<0 or i>9:
            return 
       
       
                
                
                
        
        numl.append(str(i))
        
        if len(numl)==N:
            
            s="".join(numl)
           
            if int(s) not in store:
                store.add(int(s))
                #numl.pop()
            return
        
       
        nums(numl[:],i+K)
        nums(numl[:],i-K)
                
            
       
        return
            
                 
                
    for i in range(1,10):
       
        nums([],i)
        
    final=[]
    for i in store:
        final.append(i)
        
    return final


print(absolutediff(2,2))
    
                
                
            
            
                
                
                
        
                