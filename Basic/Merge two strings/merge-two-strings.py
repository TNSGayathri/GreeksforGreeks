#User function Template for python3
class Solution:
    def merge(self, S1, S2):
        # code here
        s=""
        for i in range(min(len(S1),len(S2))):
            s+=S1[i]
            s+=S2[i]
        i=i+1
        if(i==len(S1)):
            while i<len(S2):
                s+=S2[i]
                i+=1
        else:
            while i<len(S1):
                s+=S1[i]
                i+=1
        return s
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S1,S2 = map(str,input().strip().split())
        ob = Solution()
        print(ob.merge(S1, S2))
# } Driver Code Ends