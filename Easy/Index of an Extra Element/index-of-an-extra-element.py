class Solution:
    def findExtra(self,n,a,b):
        #add code here
        d={}
        for i in range(len(b)):
            if a[i]!=b[i]:
                return i
        return len(a)-1


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))

# } Driver Code Ends