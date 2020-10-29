class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bincon = bin(n)[2:]
        counter = 0
        for i in range(len(bincon)-1):
            if bincon[i] != bincon[i+1]:
                counter += 1
        if len(bincon)-1 == counter:
            return True
        else:
            return False