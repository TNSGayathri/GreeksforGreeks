#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        # code here 
        start = max(1, q - n)
        end = min(n, q - 1)
        
        # Calculate the number of valid i values in the range
        count = max(0, end - start + 1)
        
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends