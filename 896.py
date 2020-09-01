class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A == sorted(A):
            return True
        elif list(reversed(A)) == sorted(A):
            return True
        else:
            return False
            
            
        #If the list is sorted or reverse sorted, then return True. Otherwise return False