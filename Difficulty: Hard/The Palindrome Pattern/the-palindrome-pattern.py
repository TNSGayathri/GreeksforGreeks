#User function Template for python3

class Solution:
    def pattern (self, arr):
        def fun(arr):
            for i in range(len(arr)):
                if(arr[i][::-1]==arr[i]):
                    return i
            return -1
        
        n=len(arr)
        r=fun(arr)
        a=[]
        for i in range(n):
            k = []
            for j in range(n):
                k.append(arr[j][i])
            a.append(k)

        c=fun(a)
        # print(a,arr)
        if(r!=-1):
            return str(r)+" R"
        if(c!=-1):
            return str(c)+" C"
        return "-1"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends