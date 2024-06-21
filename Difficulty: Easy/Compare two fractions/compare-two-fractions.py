#User function Template for python3


class Solution:
    def compareFrac (self, str):
        
        # code here
        l=str.split(", ")
        s1=l[0].split("/")
        s2=l[1].split("/")
        c=int(s1[0])/int(s1[1])
        d=int(s2[0])/int(s2[1])
        if(c>d):
            return s1[0]+"/"+s1[1]
        elif(c==d):
            return "equal"
        return s2[0]+"/"+s2[1]
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends