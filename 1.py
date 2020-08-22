class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sums = nums[i] + nums[j]
                if (sums == target):
                    return [i,j]
    
    
    #Run two loops one with index i and other with index i+1. if the sums = target then return the index.