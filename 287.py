class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = collections.Counter(nums)
        v = list(a.values()) 
        k = list(a.keys()) 
        z = (k[v.index(max(v))])
        return z