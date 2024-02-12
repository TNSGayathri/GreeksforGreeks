#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        mod=1000000007
        s=0
        c=1
        k=1
        while c<=n:
            t=1
            j=1
            while t<=c:
                j=j*k
                k+=1
                t+=1
            s+=j
            c+=1
        return s%mod
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends