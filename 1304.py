class Solution:
    def sumZero(self, n: int) -> List[int]:
        lis = []
        for i in range(1, n//2+1):
            lis.append(i)
            lis.append(-i)
        if n%2 != 0:
                lis.append(0)          
        return lis