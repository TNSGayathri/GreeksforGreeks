#User function Template for python3

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        d1={}
        d2={}
        d3={}
        l=[]
        for i in A:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        for i in B:
            if i not in d2:
                d2[i]=1
            else:
                d2[i]+=1
        for i in C:
            if i not in d3:
                d3[i]=1
            else:
                d3[i]+=1
        for i in d1.keys():
            if i in d2.keys() and i in d3.keys():
                l.append(i)
        l.sort()
        return l
            
        
                
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends