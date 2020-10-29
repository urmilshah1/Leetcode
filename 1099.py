class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        S = -1 
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i] + A[j] < K:
                    S = max(S, A[i]+A[j])
        return S