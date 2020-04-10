# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:43:09 2020

@author: Soham Dutta
"""
"""Inserting a element at the front of a list """
class Node(object):
    def __init__(self,info):
        self.info=info;
        self.next=None;

class LinkedList: 

    def __init__(self): 
        self.head = None
    
    def inserbeg(self,data):
        self.temp=Node(data)
        if (self.head==None):
            self.head=self.temp
            return
        self.temp.next=self.head
        self.head=self.temp
    
    def insertend(self,data):
        self.temp=Node(data)
        if(self.head==None):
            self.head=self.temp
            return
        self.p=self.head
        while(self.p.next !=None):
            self.p=self.p.next
        self.p.next=self.temp
    
    def insertafter(self,data,item):
        self.temp=Node(data)
        self.p=self.head
        while(self.p != None):
            if(self.p.info == item):
                self.temp.next=self.p.next
                self.p.next=self.temp
                return
            self.p=self.p.next
        print("Item not found")
        
    def insertpos(self,data,pos):
        self.temp=Node(data)
        if (pos==1):
            self.temp.next=self.head
            self.head=self.temp
            return
        self.p=self.head
        while(pos>2 and self.p is not None):
            self.p=self.p.next
            pos=pos-1
        if (self.p is None):
            print("Length exceeded")
        else:
            temp.next=self.p.next
            self.p.next=self.temp
            
    def deletion (self,data):
        if (self.head is None):
            print("List is empty")
            return
        if(self.head.info==data):
            self.temp=self.head
            self.head=self.head.next
            return
        self.p=self.head
        
        while(self.p.next is not None):
            if (self.p.next.info==data):
                self.temp=self.p.next
                self.p.next=temp.next
                return
            self.p=self.p.next
        print("element not found")
    def display(self):
        if (self.head is None):
            print ("List is empty")
        self.p=self.head
        while(self.p is not None):
            print(self.p.info)
            self.p=self.p.next
    def count(self):
        c=0
        
        self.p=self.head
        while(self.p is not None):
            c=c+1
          
            self.p=self.p.next
        print(c)
        
    def reverse(self):
         
        self.prev=None
        self.curr=self.head
        while self.curr is not None:
            self.Next=self.curr.next
            self.curr.next=self.prev
            self.prev=self.curr
            self.curr=self.Next
        self.head=self.prev
        return
        

llist=LinkedList()
llist.inserbeg(1)
llist.inserbeg(10)
llist.inserbeg(11)
llist.inserbeg(12)
llist.inserbeg(14)
llist.inserbeg(8)
llist.display()
llist.reverse()
llist.display()
llist.count()