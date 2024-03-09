#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        # code here
        while r>0:
            l=""
            for i in s:
                if i=="1":
                    l+="10"
                else:
                    l+="01"
                if (len(l)>n):
                    break
            s=l
            r-=1
        return s[n]





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends