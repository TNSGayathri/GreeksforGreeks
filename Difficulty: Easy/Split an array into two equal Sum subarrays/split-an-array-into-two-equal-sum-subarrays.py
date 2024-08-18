class Solution:
    def canSplit(self, arr):
        #code here
        ls=0
        rs=sum(arr)
        if(ls==rs):
            return True
        for i in arr:
            ls+=i
            rs-=i
            if(ls==rs):
                return True
        return False


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends