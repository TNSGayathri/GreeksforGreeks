class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        s=sum(a)
        c=sum(b)
        if(s==c):
            return 1
        d=s-c
        if(d%2!=0):
            return -1
        d=d//2
        a=set(a)
        for i in b:
            x=i+d
            if x in a:
                return 1
        return -1


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends