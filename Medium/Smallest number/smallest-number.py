#User function Template for python3
class Solution:
    def smallestNumber (self, S, D):
        s=""
        if(S>D*9):
            return -1
        l=[9]*D;
        sm=sum(l)
        c=sm-S
        i=0
        while c>0:
            if(c>=8 and i==0):
                l[i]=l[i]-8
                c-=8
            elif(c>9):
                l[i]=l[i]-9
                c-=9
            else:
                l[i]=l[i]-c
                c-=c
            i+=1
        for i in l:
            s+=str(i)
        return s
            
            
            
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,D=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.smallestNumber(S,D))
# } Driver Code Ends