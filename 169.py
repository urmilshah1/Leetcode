class Solution:
    def majorityElement(self, nums: List[int]):
        nums.sort()
        return nums[len(nums)//2]      
  
  
  #Here used a simple sorting the list and after that I returned the number which was more than the length of the list. 