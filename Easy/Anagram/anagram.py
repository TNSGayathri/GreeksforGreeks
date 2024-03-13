#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        l=[]
        m=[]
        if(len(a)!=len(b)):
            return False
        for i in a:
            l.append(i)
        for i in b:
            m.append(i)
        l= ''.join(sorted(l))
        m = ''.join(sorted(m))
        for i in range(len(l)):
            # print(l[i],m[i])
            if l[i]!=m[i]:
                return False
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends