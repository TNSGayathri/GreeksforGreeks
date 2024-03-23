#User function Template for python3

class Solution:
    def series(self, n):
        # Code here
        mod=1000000007
        t1=0
        t2=1
        l=[0,1]
        n=n-1
        while n>0:
            t3=(t1+t2)%mod
            l.append(t3)
            t1=t2
            t2=t3
            n-=1
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends