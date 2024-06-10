#User function Template for python3
class Solution:

	def matchPairs(self, n, nuts, bolts):
		# code here
		order = ["!", "#", "$", "%", "&", "*", "?", "@", "^"]

        # Initialize dictionary to count occurrences
        d = {symbol: 0 for symbol in order}
    
        # Count occurrences in nuts
        for nut in nuts:
            d[nut] += 1
    
        # Initialize index for updating nuts and bolts
        j = 0
    
        # Update nuts and bolts based on order
        for symbol in order:
            if d[symbol] != 0:
                nuts[j] = symbol
                bolts[j] = symbol
                j += 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(n, nuts, bolts)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends