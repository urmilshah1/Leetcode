class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + 2*i)
        res = reduce(ixor, nums)
        return res
    
### I have taken a list and appended the values according to the requirements and using the xor operator, returned the res value.