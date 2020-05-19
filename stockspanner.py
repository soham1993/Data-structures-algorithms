# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:27:06 2020

@author: Soham Dutta
"""

class StockSpanner(object):

    def __init__(self):
        self.s=[]
        self.c=0
        self.s1=[]
        

    def next(self, price):
        if not self.s:
            self.s.append(self.c)
            self.s1.append(price)
            return 1
        self.s1.append(price)
        self.c+=1
        while(self.s and self.s1[self.s[-1]]<=price):
            self.s.pop()
        if(not self.s):
            k=(self.c+1)
        else:    
            k=self.c-self.s[-1]
        self.s.append(self.c)
        return k