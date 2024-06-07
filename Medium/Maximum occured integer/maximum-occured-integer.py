#User function Template for python3

class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,n, l, r, maxx):
        ##Your code here
        count = [0] * (maxx + 2)
        for i in range(n):
            count[l[i]] += 1
            count[r[i] + 1] -= 1
        max_occurrence = count[0]
        result = 0
        for i in range(1, maxx + 1):
            count[i] += count[i - 1]
            if count[i] > max_occurrence:
                max_occurrence = count[i]
                result = i
    
        return result
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

A = [0] * 1000000


def main():

    T = int(input())

    while (T > 0):

        global A
        A = [0] * 1000000

        n = int(input())

        l = [int(x) for x in input().strip().split()]
        r = [int(x) for x in input().strip().split()]

        maxx = max(r)
        ob = Solution()
        print(ob.maxOccured(n, l, r, maxx))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends