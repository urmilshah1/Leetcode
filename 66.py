class Solution:
    def plusOne(self, digits: List[int]):
        n = len(digits)
        for i in range(n):
            j = n -1 -i
            if digits[j] == 9:
                digits[j] = 0    
            else: 
                digits[j] += 1
                return digits
        return [1] + digits
        
