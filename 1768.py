class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        len1 = len(word1)
        len2 = len(word2)
        maxi = max(len1, len2)
        for i in range(0, maxi):
            if i < len1:
                res += word1[i]
            if i < len2:
                res += word2[i]
        return res
                       
       