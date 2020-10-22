class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        a = collections.Counter(A)
        k = list(a.keys())
        v = list(a.values())
        z = (k[v.index(max(v))])
        return z