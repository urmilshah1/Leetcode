class Solution:
    def findComplement(self, num: int) -> int:
        a = bin(num)[2:]
        inverse_s = a.replace('1', '2') 
        inverse_s = inverse_s.replace('0', '1') 
        inverse_s = inverse_s.replace('2', '0') 
        b = int(inverse_s, 2)
        return b