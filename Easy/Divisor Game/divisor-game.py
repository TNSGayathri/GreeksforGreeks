#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def divisorGame(self, N):
        #Code here
        if(N%2==0):
            return True
        else:
            return False

#{ 
 # Driver Code Starts.


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        N = int(input())

        obj = Solution()
        ans = obj.divisorGame(N)

        if ans:
            print("True")
        else:
            print("False")

        t -= 1
# } Driver Code Ends