class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        mini = min(A)
        res = list(map(int, str(mini)))
        S= 0
        for i in res:
            S += i 
        if S%2 !=0:
            return 0
        else:
            return 1