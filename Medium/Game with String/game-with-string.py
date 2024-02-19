#User function Template for python3

class Solution:
    def minValue(self, s, k):
        # code here
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=list(d.values())
        while k!=0:
            m=max(l)
            i=l.index(m)
            m=m-1
            l[i]=m
            k-=1
        su=0
        for i in l:
            su+=(i*i)
        return su
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends