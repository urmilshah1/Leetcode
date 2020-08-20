class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []  #make an array 
        a = 0  #Intialize a to 0 
        for i in nums:
            a += i   #Increment a by the number at index i 
            sums.append(a) #add it to the list
        return sums #return the entire list