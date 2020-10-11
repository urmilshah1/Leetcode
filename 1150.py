class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        count = 0 
        for i in range(len(nums)-1):
            if (nums[i] == nums[i+1] == target):
                count += 1
        if target not in nums:
            return False
        elif count >= len(nums)//2:
            return True
        else:
            return False
             