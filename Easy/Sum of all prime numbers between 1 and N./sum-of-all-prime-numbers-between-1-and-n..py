#User function Template for python3

class Solution:
	def prime_Sum(self, n):
		# Code here
		l=[1 for i in range(n+1)]
		m=[]
        for i in range(2,int(n**0.5)+1):
            if l[i]==1:
                for j in range(i*i,n+1,i):
                    l[j]=0
        for i in range(2,len(l)):
            if(l[i]==1):
                m.append(i)
        return sum(m)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n= int(input())
		ob = Solution()
		ans = ob.prime_Sum(n)
		print(ans)
# } Driver Code Ends