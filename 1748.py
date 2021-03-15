class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        a = collections.Counter(nums)
        k = list(a.keys())
        v = list(a.values())
        z = 0
        for k, v in a.items():
            if v == 1:
                z += k
        return z