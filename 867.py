class Solution:
    def transpose(self, A: List[List[int]]):
        res = []
        for i in range(len(A[0])):
            temp = []
            for j in range(len(A)):
                temp.append(A[j][i])
            res.append(temp)
        return res