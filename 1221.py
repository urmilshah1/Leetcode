class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = 0
        ans= 0
        for letter in s:
            if letter == 'R':
                counter -= 1
            else:
                counter += 1
                
            if counter == 0:
                ans += 1
                
        return ans
    