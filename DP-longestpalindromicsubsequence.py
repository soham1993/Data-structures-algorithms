# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 12:53:18 2020

@author: Soham Dutta
"""

def longestPS(s):
    n = len(s) 
    dp = [[0 for x in range(n)] for x in range(n)] 
  
    for i in range(n): 
        dp[i][i] = 1
        
    for x in range(2, n+1): 
        for i in range(n-x+1): 
            j = i+x-1
            if s[i] == s[j] and x == 2: 
                dp[i][j] = 2
            elif s[i] == s[j]: 
                dp[i][j] = dp[i+1][j-1] + 2
            else: 
                dp[i][j] = max(dp[i][j-1], dp[i+1][j]); 
  
    return dp[0][n-1] 
if __name__=='__main__':
    s='AAIC'
    n=len(s)
    print(longestPS(s))
