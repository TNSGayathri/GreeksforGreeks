#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        s=0
        l=len(str(n))
        t=n
        c=0
        while t>0:
            r=t%10
            c+=r**3
            t=t//10
        if(c==n):
            return "Yes"
        return "No"
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends