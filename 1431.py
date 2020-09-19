class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        for i in candies:
            max_c = i + extraCandies
        
            t= True
            for j in candies:
                if max_c < j:
                    t = False
            ans.append(t)
        return ans
                