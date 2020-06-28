# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 20:09:30 2020

@author: Soham Dutta
"""

class Solution(object):
    def countPrimes(self, n):
        prime = [True for i in range(n+1)]
        p = 2
        while p*p<=n:
            if prime[p]:
                for i in range(p*p,n+1,p):
                    prime[i]=False
            p+=1
        res = []
        for p in range(2,n):
            if prime[p]:
                res.append(p)
        return len(res)
       