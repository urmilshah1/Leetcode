class Solution:
    def removeElement(self, nums: List[int], val: int):
        try:
             while True:
                nums.remove(val)
        except:
                return len(nums)