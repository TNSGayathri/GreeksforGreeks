#User function Template for python3

class Solution:
    def game_with_number (self, l,  n) : 
        #Complete the function
        for i in range(n-1):
            l[i]=l[i]|l[i+1]
        return l


#{ 
 # Driver Code Starts

#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.game_with_number(arr, n);
    print(*res)




# } Driver Code Ends