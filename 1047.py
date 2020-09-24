class Solution:
    def removeDuplicates(self, S: str) -> str:
        def move(s):
            l = "abcdefghijklmnopqrstuvwxyz"
            for x in l:
                s = s.replace(x*2,"")
            return s
        
        while len(move(S)) != len(S):
            S = move(S)
        return S