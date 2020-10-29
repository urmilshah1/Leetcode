class Solution:
    def maxPower(self, s: str) -> int:
        power = 1 
        maxi = power 
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                power += 1
                if power > maxi:
                    maxi = power
            else:
                power = 1
        return maxi
    
