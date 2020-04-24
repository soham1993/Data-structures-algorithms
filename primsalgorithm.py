# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 00:10:32 2020

@author: Soham Dutta
"""

from collections import defaultdict
import heapq

class Graph:
    
    def __init__(self,V):
        self.V=V
        self.edges = defaultdict(list)
        self.distances = {}
        self.key={}
    
    def add_node(self, value):
        inf=float('inf')
       # self.nodes.add(value)
        self.distances[(value,value)]=inf
        self.key[(value)]=value
    
    def addEdge(self, from_node, to_node, distance):#adding edges
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance
    
    def priMST(self,startvertex):
        q=[]
        visited=[False]*self.V
        self.distances[(startvertex,startvertex)]=0
        heapq.heappush(q,startvertex)
        visited[startvertex]=True
        while q:
            actualvertex=heapq.heappop(q)
            for i in self.edges[actualvertex]:
                if (visited[i] is False):
                    distance=self.distances[(actualvertex,i)]
                    if(distance <self.distances[(i,i)]):
                        self.distances[i,i]=distance
                        self.key[(i)]=actualvertex
                        visited[i]=True
                        heapq.heappush(q,i)
        print("Shortest Paths from source vertex")
         
        for i in range(1,self.V):
                print(self.key[(i)],"\t",i,"\t",self.distances[(i,i)])
                
graph = Graph(5)
for i in range(5):
    graph.add_node(i)
graph.addEdge(0, 1, 2) 
graph.addEdge(0, 3, 6) 
graph.addEdge(1, 2, 3) 
graph.addEdge(1, 4, 5) 
graph.addEdge(1, 3, 8) 
graph.addEdge(3, 4, 9) 
graph.addEdge(2, 4, 7) 

graph.priMST(0) 
                
                
            
            
        
                