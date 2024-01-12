
class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        t1=0
        t2=1
        if(n<=2):
            return n-1
        c=2
        while c<=n:
            t3=(t1+t2)%(1000000007)
            t1=t2
            t2=t3
            c+=1
        return t3%1000000007



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends