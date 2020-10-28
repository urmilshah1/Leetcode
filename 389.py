class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = sorted(s)
        b = sorted(t)
        i = 0
        while i < len(s):
            if a[i] != b [i]:
                return b[i] 
            i += 1
        return b[i]