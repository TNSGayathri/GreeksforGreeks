#User function Template for python3
def max_sum(a,n):
    #code here
    n = len(a)
    if n == 0:
        return 0
    S = sum(i * a[i] for i in range(n))
    sum_a = sum(a)
    max_sum = S
    for i in range(1, n):
        S = S + sum_a - n * a[n - i]
        max_sum = max(max_sum, S)
    
    return max_sum



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends