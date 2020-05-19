# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:39:55 2020

@author: Soham Dutta
"""

class Node(object):
    def __init__(self,info):
        self.info=info;
        self.next=None;
        
class LinkedList: 

    def __init__(self): 
        self.top = None
        
    def push(self,x):
        temp=Node(x)
        if(self.top is None):
            self.top=temp
            return
        else:
            temp.next=self.top
            self.top=temp
            
    def display(self):
        if self.top is None:
            print("Stack empty")
        else:
            temp=self.top
            while(temp):
                print(temp.info)
                temp=temp.next
            print("\n")
            print("*****")
    def pop(self):
        if self.top is None:
            print("No items")
            return
        self.top=self.top.next
        
            
prev=None
Next=None
def reverse(top1):
    global prev,Next
    if(top1 is None):
        return
    curr=top1
    Next=curr.next
    curr.next=prev
    prev=curr
    top=prev
    curr=reverse(Next)
    return prev
    
    
            
            
            
llist=LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.push(6)
llist.push(7)
llist.display()
llist1=LinkedList()
llist1.top=reverse(llist.top)
llist1.display()
llist1.pop()
llist1.display()
            
            
            
        