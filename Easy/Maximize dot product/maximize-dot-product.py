#User function Template for python3
class Solution:
	def maxDotProduct(self, m, n, a, b):
	    dp = [[0 for i in range(m + 1)] 
        for j in range(n + 1)]
 
    # Traverse through all elements of B[]
        for i in range(1, n + 1, 1):
             
            # Consider all values of A[] with indexes 
            # greater than or equal to i and compute
            # dp[i][j]
            for j in range(i, m + 1, 1):
                 
                # Two cases arise
                # 1) Include A[j]
                # 2) Exclude A[j] (insert 0 in B[]) 
                dp[i][j] = max((dp[i - 1][j - 1] +
                                (a[j - 1] * b[i - 1])) , 
                                dp[i][j - 1])
     
        # return Maximum Dot Product
        return dp[n][m] 
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,m = input().split()
		n,m = int(n),int(m)
		a = [int(x) for x in input().split()]
		b = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxDotProduct(n,m,a,b)
		print(ans)
# } Driver Code Ends