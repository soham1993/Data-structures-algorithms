# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:49:23 2020

@author: Soham Dutta
"""
from collections import defaultdict
class topo:
    def __init__(self,V):
        self.V=V
        self.graph=defaultdict(list)
        
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
"""main function for topological sort"""        
    def topologicalsortutil(self,v,visited,stack):
        visited[v]=True
        
        for j in self.graph[v]:
            if visited[j]==False:
                self.topologicalsortutil(j,visited,stack)
                
        stack.insert(0,v)
        
        
    def top(self):
        
        visited=[False]*self.V
        stack=[]
        
        for i in range (self.V):
             if visited[i]==False:
                self.topologicalsortutil(i,visited,stack)
                
        print(stack)
            
                
g= topo(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
  
print ("Following is a Topological Sort of the given graph")
g.top()        
        
        