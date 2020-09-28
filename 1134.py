class Solution:
    def isArmstrong(self, N: int) -> bool:
        lis = list(str(N))
        length = len(lis)
        sum1 = 0
        for i in lis:
            sum1 += int(i) **length
        if sum1 == N:
            return True
        else:
            return False
            
