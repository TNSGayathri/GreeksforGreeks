#User function Template for python3
import math
class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        # return the count
        c=0
        a=int(math.log2(n))+1;
        for i in range(1,a+1):
            x=2**i
            c+=(n//x)*(x//2)
            y=(n%x)+1
            if y>(x//2):
                c+=y-(x//2)
        return c
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends