class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)):
            if(nums[i]==0):
                nums.append(nums[i])
                nums.remove(nums[i])
        
        # I checked if the element = 0 and added it to the end of the list, and deleted that specific number from the list.