class Solution:
    def maxNumberOfBalloons(self, txt: str) -> int:
           return min(txt.count('b'), txt.count('a'), txt.count('l')//2, txt.count('o')//2, txt.count('n'))
        
        
