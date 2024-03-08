#User function Template for python3
class Solution:
    def sameFreq(self, s):
        # code here
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        # print(d)
        l=list(d.values())
        k={}
        for i in l:
            if i not in k:
                k[i]=1
            else:
                k[i]+=1
        # print(k)
        m=max(list(k.values()))
        m=list(k.keys())[list(k.values()).index(m)]
        # print(m)
        c=0
        # print(l)
        c1=0
        for i in l:
            # print(i-m)
            if(i==1 and m==2):
                c+=1
            elif(i<m):
                return False
            elif i-m>=2:
                return False
            elif(i-m==1 and i>m):
                c+=1
        # print(c)
        if(c>1):
            return False
        return True
        
        
                
        # return 1
            
            




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends