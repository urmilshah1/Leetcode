class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        [target.insert(index[i], nums[i]) for i in range(0, len(nums))]
        return target
    
    
    
    #Create a target array, using list comprehension, insert the array in the specific position. 