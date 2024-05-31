
class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        o="acegikmoqsuwy"
        e="bdfhjlnprtvxz"
        x=0
        y=0
        for i in d.keys():
            if (i in e and d[i]%2==0):
                x+=1
            elif(i in o and d[i]%2!=0):
                y+=1
        if((x+y)%2==0):
            return "EVEN"
        else:
            return "ODD"
                



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends