class Solution:
	def topK(self, nums, k):
		#Code here
		d = {}
		for i in nums:
		    if i not in d:
		        d[i] = 1
		    else:
		        d[i] += 1
		sorted_dict = sorted([[v, key] for (key, v) in d.items()],reverse = True)
		res = []
		for i in sorted_dict:
		    if k > 0:
		        res.append(i[1])
		    k -= 1
		return res


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
    	
# } Driver Code Ends