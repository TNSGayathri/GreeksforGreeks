#User function Template for python3

class Solution:
    def Maximize(self, a): 
        # Complete the function
        mod=int((10**9)+7)
        a.sort()
        s=0
        for i in range(1,len(a)):
            s+=(a[i]*i)%mod
        return s%mod
      



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        # k = int(input())
        ob = Solution()
        print(ob.Maximize(A))

# } Driver Code Ends