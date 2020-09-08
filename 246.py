class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
        ans = ''
        for n in num:
            if n not in d:
                return False
            ans += d[n]
            print(ans)
        return ans[::-1] == num
    
    #Created a dictionary to map the Strobogrammatic Number together.
    #If the number is in the dict, add it to ans variable. Compare the ans value to the original num value to return True or False
    