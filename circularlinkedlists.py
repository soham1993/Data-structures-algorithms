# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 13:03:45 2020

@author: Soham Dutta
"""

class Node(object):
    def __init__(self,info):
        self.info=info;
        self.next=None;

class LinkedList: 

    def __init__(self): 
        self.head = None
    def inserbeg(self,data):
        self.temp=Node(data)
        if(self.head is None):
             self.head=self.temp
             self.head.next=self.head
             return
        self.p=self.head
        while(self.p.next is not self.head):
             self.p=self.p.next
        self.temp.next=self.head
        self.p.next=self.temp
        self.head=self.temp
    def insertend(self,data):
         self.temp=Node(data)
         if(self.head is None):
             self.head=self.temp
             self.head.next=self.head
             return
         self.p=self.head
         while(self.p.next is not self.head):
             self.p=self.p.next
         self.p.next=self.temp
         self.temp.next=self.head
    def insertafter(self,data,item):
        self.p=self.head
        while self.p.next is not self.head:
            if self.p.info==item:
                self.temp=node(data)
                self.temp.next=self.p.next
                self.p.next=self.temp
                return
            self.p=self.p.next
        if self.p.info==item:
            self.temp=node(data)
            self.p.next=self.temp
            self.temp.next=self.head
    def deletion (self,data):
        if (self.head is None):
            print("List is empty")
            return
        if self.head.next==self.head:
            if self.head.info==data:
                self.temp=self.head;
                self.head=None
                return
           
        self.p=self.head
        while(self.p.next is not self.head):
            if(self.p.next.info==data):
                self.temp=self.p.next
                self.p.next=self.temp.next
                return
            self.p=self.p.next
        if(self.head.info==data):
             self.temp=self.head
             self.p.next=self.head.next
             self.head=self.p.next
             return
        else:
            print("element not found")
         
                
                                   
    def display(self):
        print("new circular linked lists")
        self.p=self.head
        while(self.p.next is not self.head):
            print(self.p.info)
            self.p=self.p.next
        print(self.p.info)
        
       
llist=LinkedList()
llist.inserbeg(1)
llist.inserbeg(10)
llist.inserbeg(11)
llist.inserbeg(12)
llist.inserbeg(14)
llist.inserbeg(8)
llist.display()

llist.deletion(10)
llist.deletion(10)


llist.insertend(25)
llist.display()



             
        
            