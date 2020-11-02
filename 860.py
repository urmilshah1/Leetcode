class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for c in bills:
            if c == 5:
                five += 1
            elif c == 10:
                five -= 1
                ten += 1
            elif c == 20 and ten != 0:
                ten -= 1
                five -= 1
            elif c == 20 and ten == 0:   
                five -= 3
            if five < 0:
                return False
        return True
    
    