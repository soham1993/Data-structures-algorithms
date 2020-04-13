# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:51:07 2020

@author: Soham Dutta
"""

import sys
class Queue:
    
    def __init__(self):
        self.queue=[None] * 100
        self.front=-1
        self.rear=-1
 
    def isFull(self):
        if (self.rear==100 and self.front==0) or self.front==self.rear+1:
            return True
        return False
    
    def isEmpty(self):
        if self.front==-1:
            return True
        return False
        
    def insert(self,data):
        if self.isFull():
            print("Queue overflow")
            return
        if self.front==-1:
            self.front=0
            #self.rear = 0
            #self.queue[self.rear] = data 
            
            
            
        if self.rear==100:
            self.rear=0
            self.queue[self.rear] = data 
            
        else:
            self.rear=self.rear+1
            self.queue[self.rear]=data
            
    def delete(self):
        if self.isEmpty():
            print("queue Underflow")
           
        item=self.queue[self.front]
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        elif self.front==100:
            self.front=0;
        else:
            self.front=self.front+1;
        return item
    
   
    def display(self):
        if self.isEmpty():
            print("queue Underflow")
           
        if(self.front<=self.rear):
               self.temp=self.front
               while(self.temp<=self.rear):
                   print(self.queue[self.temp])
                   self.temp=self.temp+1
        else:
                while self.temp<100:
                    print(self.queue[self.temp])
                    self.temp+=1
                self.temp=0
                while self.temp<=self.rear:
                    print(self.queue[self.temp])
                    self.temp+=1
               
           
       
                

q=Queue()
q.insert(10)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)
q.display()
q.delete()
q.display()
q.delete()
q.display()
q.delete()
q.display()
