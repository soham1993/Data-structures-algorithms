# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 18:15:03 2020

@author: Soham Dutta
"""
class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]
        
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
        
    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in T
        """
        partial, ret, j = self.partial(P), [], 0
        
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = partial[j - 1]
            
        return ret

kmp = KMP()


p2 = "abc"
t2 = "abdabeabfabc"
kmp.partial(p2)
print(kmp.search(t2, p2))

p3 = "aab"
t3 = "aaabaacbaab"
kmp.partial(p3)
print(kmp.search(t3, p3))


