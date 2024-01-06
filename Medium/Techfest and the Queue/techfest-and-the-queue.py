
from typing import List

import math
class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        # code here
        s=0
        l=[0]*(b+1)
        for i in range(2,b+1):
            if(l[i]==0):
                for j in range(i,b+1,i):
                    l[j]=i
        for i in range(a,b+1):
            while i>1:
                i=i//l[i]
                s+=1
            
        return s






#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=int(input())
        b=int(input())
        
        obj = Solution()
        res = obj.sumOfPowers(a,b)
        
        print(res)
        

# } Driver Code Ends