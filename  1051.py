class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_list = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if (sorted_list[i] != heights[i]):
                count += 1
        return count