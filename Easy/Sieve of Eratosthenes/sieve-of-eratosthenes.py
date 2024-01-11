#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, N):
    	#code here 
    	def seive(n):
    	    m=[]
    	    l=[1 for i in range(n+1)]
    	    for i in range(2,n+1):
    	        if(l[i]==1):
    	            m.append(i)
    	            for j in range(i*i,n+1,i):
    	                l[j]=0
    	    return m
    	return seive(N)
    	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends