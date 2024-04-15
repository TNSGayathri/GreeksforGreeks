#User function Template for python3
class Solution:
    def countElements(self, a, b, n, query, q):
        # code here
        k=max(max(a),max(b))
        l=[0]*(k+1)
        m=[]
        for i in b:
            l[i]+=1
        # print(l)
        for i in range(1,len(l)):
            l[i]+=l[i-1]
        for i in query:
            m.append(l[a[i]])
        return m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends