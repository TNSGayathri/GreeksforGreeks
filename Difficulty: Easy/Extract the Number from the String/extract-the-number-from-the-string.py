class Solution:
    def ExtractNumber(self,sentence):
        #code here
        l=sentence.split(" ")
        m=[]
        for i in l:
            if i.isdigit() and "9" not in i:
                m.append(int(i))
        if(m==[]):
            return "-1"
        return str(max(m))

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends