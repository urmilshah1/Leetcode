class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = 1
        result = []
        for num in range(1, len(nums) + 1):
            if num not in dic:
                result.append(num)
        return result