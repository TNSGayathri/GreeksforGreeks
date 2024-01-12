#User function Template for python3

class Solution:
    def nCr(self, n, r):
        # code here
        def fact(n):
            p=1
            for i in range(2,n+1):
                p=(p*i)
            return p
        if(r>n):
            return 0
        else:
            a=fact(n)
            b=fact(r)
            c=fact(n-r)
            k=a//((b*c))
            return k%1000000007


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends