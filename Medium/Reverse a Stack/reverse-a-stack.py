#User function Template for python3

from typing import List

class Solution:
    def reverse(self,St): 
        #code here
        s=len(St)-1
        for i in range(0,len(St)//2):
            St[i],St[s-i]=St[s-i],St[i]


#{ 
 # Driver Code Starts

#Initial Template for Python 3

 
for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
# } Driver Code Ends