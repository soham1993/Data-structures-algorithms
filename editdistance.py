# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:05:09 2020

@author: Soham Dutta
"""

def editdistance(s1,s2):
    m=len(s1)
    n=len(s2)
    dp=[[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(0,m+1):
        dp[0][i]=i
    for i in range(0,n+1):
        dp[i][0]=i
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    return dp[n][m]

print(editdistance("ABA","ABC"))