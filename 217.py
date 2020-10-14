class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = collections.Counter(nums)
        k = list(a.keys())
        v = list(a.values())
        for i in range(len(v)):
            if v[i]>=2:
                return True