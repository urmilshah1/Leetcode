class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        for i in S:
            if(i in J):
                counter += 1
            else:
                continue
        return counter
    
    #simply search for jewels in stones. If found, increment the counter by 1 else continue
    