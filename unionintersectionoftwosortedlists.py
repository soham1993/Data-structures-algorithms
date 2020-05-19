# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:44:12 2020

@author: Soham Dutta
"""
import sys
class Node(object):
    def __init__(self,info):
        self.info=info;
        self.next=None;
        
class LinkedList: 

    def __init__(self): 
        self.head = None
        
        
    
    def insertend(self,data):
        self.temp=Node(data)
        if(self.head==None):
            self.head=self.temp
            self.tail=self.temp
        else:
            self.tail.next=self.temp
            self.tail=self.temp
        
    def display(self):
        if(self.head is None):
            return 
        temp=self.head
        while(temp):
            print(temp.info,end=" ")
            temp=temp.next
        print("\n")
def length(head):
    p=head
    l=0
    if(head is None):
        return 0
    while(p):
        l+=1
        p=p.next
    return l
        
def union(head1,head2):
    
    head3=None
    tail3=None
   
    l=length(head1)
    r=length(head2)
    
    
    
    
    if(l<r):
        head1,head2,l,r=head2,head1,r,l
    a=[]
    p=head2
    while p:
        a.append(p.info)
        p=p.next
   
    q=head1
    while q:
        if q.info in a:
            a.remove(q.info)
            temp=Node(q.info)
            
            if(head3==None):
                head3=temp
                tail3=temp
            else:
                tail3.next=temp
                tail3=temp
                
        else:
            temp=Node(q.info)
            if(head3==None):
                head3=temp
                tail3=temp
            else:
                tail3.next=temp
                tail3=temp
        q=q.next      
    if a:
        for i in a:
            temp=Node(i)
            tail3.next=temp
            tail3=temp
            
    return head3
            
            
def intersection(head1,head2):
     
     
     head4=None
     tail4=None
     l=length(head1)
     r=length(head2)
     if(l<r):
        head1,head2,l,r=head2,head1,r,l
     a=[]
     p=head2
     while p:
         a.append(p.info)
         p=p.next
    
     
     q=head1
     while q:
          
          if q.info in a:
               temp=Node(q.info)
              
              
               if(head4==None):
                    head4=temp
                    tail4=temp
               else:
                    tail4.next=temp
                    tail4=temp
          q=q.next 
     
    
     return head4
 
if __name__=='__main__':   
    n,m=input().split()
    nums1=[int(n) for n in input().split()]
    nums2=[int(m) for m in input().split()]
    llist1=LinkedList()
    llist2=LinkedList()
    llist3=LinkedList()
    llist4=LinkedList()
    
    
    for i in range(int(n)):
        llist1.insertend(nums1[i])
    for i in range(int(m)):
        llist2.insertend(nums2[i])
    llist3.head=union(llist1.head,llist2.head)
    llist3.display()
    
    
    llist4.head=intersection(llist1.head,llist2.head)
    llist4.display()


 
  
            
            
            
                
       

     
    
       
            
            
        
        
        
        
        
        
        
        
        
        
