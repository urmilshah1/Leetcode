class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maxi = -1
        a = collections.Counter(arr)
        v = list(a.values()) 
        k = list(a.keys()) 
        for k, v in a.items():
            if k == v and k > maxi:
                maxi = k
        return maxi
    