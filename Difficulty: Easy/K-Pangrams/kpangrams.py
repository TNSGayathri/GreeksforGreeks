#User function Template for python3
class Solution:
    def kPangram(self,string, k):
        c=0
        s=''
        for i in string:
            if i!=" ":
                c+=1
                s+=i
        # print(c)
        if c<26:
            return False
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        if len(d)==26:
            return True
        c=26-len(d)
        if c<=k:
            return True
        return False
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends