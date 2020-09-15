class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k, l = 0 , 0
        while k < len(s) and l < len(t):
            if t[l] == s[k]:
                k = k+1
            l = l+1
        return k == len(s)