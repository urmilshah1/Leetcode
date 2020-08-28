class Solution:
    def numIdenticalPairs(self, nums: List[int]):
        count = 0
        for i1 in range(len(nums)):
            for i2 in range(i1 + 1, len(nums)):
                if(nums[i1]==nums[i2]):
                    count += 1 
        return count
                
            
         
            
            