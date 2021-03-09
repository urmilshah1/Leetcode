class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_c = 0
        for i in nums:
            if i == 1:
                count += 1 
            else:
                max_c  = max(count, max_c)
                count = 0
        return max(count, max_c)