class Solution:
    def duplicates(self, arr, n): 
        
    	# code here
    	d={}
    	l=[]
    	for i in arr:
    	    if i not in d:
    	        d[i]=1
    	    else:
    	        d[i]+=1
    	for i in d:
    	    if(d[i]>1):
    	        l.append(i)
    	if(l==[]):
    	    m=[-1]
    	    return m
    	l.sort()
    	return l


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends