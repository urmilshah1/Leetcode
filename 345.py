class Solution:
    def reverseVowels(self, s: str) -> str:
        p1, p2 = 0, len(s) - 1
        lis = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        k = list(s)
        while p1 < p2:
            if k[p1] not in lis:
                p1 += 1
            elif k[p2] not in lis:
                p2 -= 1
            else:
                k[p1], k[p2] = k[p2], k[p1]
                p1 +=1 
                p2 -=1
        return "".join(k)     
        
        
            