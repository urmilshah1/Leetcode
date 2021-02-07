class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        mask = 1
        while (n> 0):
            if ((n & mask) != 0):
                counter += 1
            n = n>>1;
        return counter