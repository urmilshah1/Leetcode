class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            heaviestStone = stones.pop(stones.index(max(stones)))
            secondHeaviest = stones.pop(stones.index(max(stones)))
            if heaviestStone - secondHeaviest != 0:
                stones.append(heaviestStone - secondHeaviest)
        if stones:
            return stones[0]
        else:
            return 0
    
    
    
   