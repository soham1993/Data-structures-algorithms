# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:44:02 2020

@author: Soham Dutta
"""

from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        #self.V=V
        self.edges=defaultdict(list)
        self.distances={}
        self.nodes = set()
        
    def add_node(self, value):
        inf=float('inf')
        self.nodes.add(value)
        self.distances[(value,value)]=inf
        
        
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance
        
    def dijsktra(self,startvertex):
        q=[] 
        self.distances[(startvertex,startvertex)]=0
        
        heapq.heappush(q,startvertex)
        while q:
            actualvertex=heapq.heappop(q)
            
            for i in self.edges[actualvertex]:
                distance=self.distances[(actualvertex,i)]
                newdistance=distance+self.distances[(actualvertex,actualvertex)]
                
                if (newdistance< self.distances[(i,i)]):
                    
                    self.distances[(i,i)]=newdistance
                    heapq.heappush(q,i)
                    
        print("Shortest Paths from source vertex")
        print("vertex\t distance")
        for i in self.nodes:
           print(i,"\t",self.distances[(i,i)])
           
g=Graph()

for i in range(9):
    g.add_node(i)

g.add_edge(0, 1, 4); 
g.add_edge(0, 7, 8); 
g.add_edge(1, 2, 8); 
g.add_edge(1, 7, 11); 
g.add_edge(2, 3, 7); 
g.add_edge(2, 8, 2); 
g.add_edge(2, 5, 4); 
g.add_edge(3, 4, 9); 
g.add_edge(3, 5, 14); 
g.add_edge(4, 5, 10); 
g.add_edge(5, 6, 2); 
g.add_edge(6, 7, 1); 
g.add_edge(6, 8, 6); 
g.add_edge(7, 8, 7); 

g.dijsktra(0)
