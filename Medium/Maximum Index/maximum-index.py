#User function Template for python3

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,a, n): 
        ##Your code here
        m=0
        for i in range(n):
            for j in range(n-1,i,-1):
                # print(a[i],a[j])
                if(a[i]<=a[j]):
                    # print(a[i],a[j])
                    m=max(m,j-i)
                    break
                # break
        return m
                    





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends