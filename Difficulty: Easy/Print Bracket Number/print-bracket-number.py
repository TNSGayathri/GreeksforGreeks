#User function Template for python3
class Solution:
	def bracketNumbers(self, str):
		# code here
		l=[]
		op=0
		close=[]
		for i in str:
		    if i=="(":
		        op+=1
		        close.append(op)
		        l.append(op)
		    elif i==")":
		        l.append(close[-1])
		        close.pop()
		return l
		        
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends