class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        def gen(array_list):
            for i in range(n): 
                yield from (array_list[i], array_list[i+n])
        return list(gen(nums))