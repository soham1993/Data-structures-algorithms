# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:29:15 2020

@author: Soham Dutta
"""

from collections import defaultdict
class connectedcomponents:
    
    def __init__(self,V):
        self.V=V
        self.graph=defaultdict(list)
 
      
    def addEdge(self,u,v): # function to add edge to the graph  
        self.graph[u].append(v)
     
    def reverse(self): #function to find the transpose of the graph  
        g=connectedcomponents()
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g

    def DFS(self,i,visited): # A function used by DFS 
        
        visited[i]=True
        print(i),
        
        for j in self.graph[i]:
            if visited[j] is False:
                self.DFS(j,visited)
               
    def fillorder(self,i,visited,stack):#Filling the stack in order of their time stamp 
        visited[i]=True
        for j in self.graph[i]:
            if (visited[j] is False):
                self.fillorder(j,visited,stack)
                
        stack.append(i)
       
    def SCC(self):#This is the main function of finding strongly connected componenets 
        stack=[]
        
        visited=[False]*self.V
        
        for i in range(self.V):
            if visited[i] is False:
                self.fillorder(i,visited,stack)
     
      
            
                
        gr=self.reverse()   #calling the reverse function     
        visited=[False]*self.V
          
        while (stack):
            s=stack.pop()
            if visited[s] is False:
                gr.DFS(s,visited)
                print(" ")
                
                
            
# Create a graph given in the above diagram 
g = connectedcomponents(5) 
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 1) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 
  
   
print ("Following are strongly connected components " +
                           "in given graph") 
g.SCC()             
        
        
                