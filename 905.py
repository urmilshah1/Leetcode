class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans = []
        ans2 = []
        for i in A:
            if(i%2 ==0):
                ans.append(i)
            else:
                ans2.append(i)
        ans = ans + ans2
        return ans