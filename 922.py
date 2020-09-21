class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = []
        odd  = [] 
        for i in range(0, len(A)):
            if(A[i]%2==0):
                even.append(A[i])
            else:
                odd.append(A[i])
        output = list(zip(even , odd))
        output = [j for i in output for j in i]
        return output
    
    
    #add even numbers to even list, odd numbers to odd list. zip together and then add it to output list