# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 00:00:30 2020

@author: Soham Dutta
"""

class Node(object):
    def __init__(self,info):
        self.info=info;
        self.next=None
        self.prev=None;

class LinkedList: 

    def __init__(self): 
        self.head = None
        
    def insertbeg(self,data):
        self.temp=Node(data)
        if(self.head is None):
            self.head=self.temp
            return
        self.temp.next=self.head
        self.head.prev=self.temp
        self.head=self.temp
    def insertend(self,data):
        self.temp=Node(data)
        if (self.head is None):
            self.head=self.temp
            return
        self.p=self.head
        while(self.p.next is not None):
            self.p=self.p.next
        self.p.next=self.temp
        self.temp.prev=self.p
            
    def insert_after_given_node(self,data,item):
        self.temp=Node(data)
        self.p=self.head
        while(self.p is not None):
            if(self.p.info==data):
                self.temp.prev=self.p
                self.temp.next=self.p.next
                if(self.p.next):
                    
                    self.p.next.prev=self.temp
                self.p.next=self.temp
                return
            self.p=self.p.next
    def deletion(self,data):
         
         if(self.head is None):
             print("list is empty")
             return
         """deletion in front of the nodes"""
        
         if (self.head.info == data):
             
             self.temp=self.head
             self.head=self.head.next
             self.head.prev=None
             return
         self.temp=self.head
         """deletion between the nodes"""
          
         while(self.temp.next is not None):
             if (self.temp.info==data):
                 self.temp.prev.next=self.temp.next
                 self.temp.next.prev=self.temp.prev
                 return
             self.temp=self.temp.next
         if (self.temp.info == data):
            self.temp.prev=None
            return
         print("Element not found")
    
    def reverse(self):
        self.p1=self.head
        self.p2=self.p1.next
        self.p1.next=None
        self.p1.prev=self.p2
        while self.p2 is not None:
            self.p2.prev=self.p2.next
            self.p2.next=self.p1
            self.p1=self.p2
            self.p2=self.p2.prev
        self.head=self.p1
        print("List reversed\n")
        
    def display(self):
        temp = self.head 
        while (temp): 
            print( temp.info) 
            temp = temp.next
            
            
llist=LinkedList()
llist.insertbeg(1)
llist.insertbeg(10)
llist.insertbeg(11)
llist.insertend(100)
llist.insertbeg(12)
llist.insertbeg(14)
llist.insertbeg(8)
llist.display()
llist.reverse()
llist.display()

llist.deletion(10)
llist.display()

                 
                     
         