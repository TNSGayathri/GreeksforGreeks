#User function Template for python3
class Solution:
	def setBits(self, n):
		# code here
		c=0
		while n>0:
		    if n&1==1:
		        c+=1
		    n=n>>1
		return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.setBits(N)
		print(ans)




# } Driver Code Ends