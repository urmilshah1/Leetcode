class Solution:
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0
        for rows in grid:
            for value in rows:
                if value< 0:
                    counter += 1
        return counter