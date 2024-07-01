#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
       pre=[]
       x=0
       for i in arr:
           x+=i
           pre.append(x)
    #   print(pre)
       d={}
       for i in range(len(pre)):
           if(pre[i]==s):
               return [1,i+1]
           elif pre[i]-s in d:
               l=d[pre[i]-s]+2
               return [l,i+1]
           d[pre[i]]=i
       return [-1]
                  




#{ 
 # Driver Code Starts.
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends