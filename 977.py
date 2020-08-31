class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        output = []
        for i in A:
            k = i * i
            output.append(k)
            output.sort()
        return output
    
    # Square the number and sort the array. 