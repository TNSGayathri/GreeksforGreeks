
from typing import List

class Solution:

    def constructList(self, q: int, queries: List[List[int]]) -> List[int]:
        l = [0]
        current_xor = 0
        
        for query in queries:
            if query[0] == 0:
                l.append(query[1] ^ current_xor)
            else:
                current_xor ^= query[1]
        for i in range(len(l)):
            l[i] ^= current_xor
        
        l.sort()
        return l
            
        



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        q = int(input())

        queries = IntMatrix().Input(q, 2)

        obj = Solution()
        res = obj.constructList(q, queries)

        IntArray().Print(res)

# } Driver Code Ends