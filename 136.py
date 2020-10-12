class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = collections.Counter(nums)
        v = list(a.values()) 
        k = list(a.keys()) 
        z = (k[v.index(min(v))])
        return z