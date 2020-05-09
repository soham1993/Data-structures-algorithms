# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:32:15 2020

@author: Soham Dutta
"""
def threeSumClosest( nums, target):
        nums=sorted(nums) 
        n=len(nums)
        diff=abs(target-(nums[0]+nums[1]+nums[n-1]))
        curclose=nums[0]+nums[1]+nums[n-1]
        closest=diff
        
        for i in range(n-1):
            l=i+1
            r=n-1
            
            while(l<r):
                print("new loop")
                print(nums[i],nums[l],nums[r])
                currsum=nums[i]+nums[l]+nums[r]
                print(currsum)
                diff=abs(target-currsum)
                print(diff)
                
                if(currsum==target):
                    return currsum
                if(currsum>target):
                    r=r-1
                    if(diff<closest):
                        closest=diff
                        curclose=currsum
                    
                    
                    
                    
                if(currsum<target):
                    l=l+1
                    if(diff<closest):
                        closest=diff
                        curclose=currsum
                        
            print(closest)
                    
        return (curclose)
                    
                    
        #return cloecur
a=threeSumClosest( [0,0,0], 1)