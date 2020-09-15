class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        p = 0
        for x in b:
            p = p * 10 + x
        return pow(a, p, 1337)