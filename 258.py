class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        
        next_num = 0
        while num > 0:
            next_num += num%10
            num = num//10
        
        return self.addDigits(next_num)