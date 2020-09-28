class Solution:
    def average(self, salary: List[int]) -> float:
        reversesortedsal = sorted(salary, reverse =True)
        reversesortedsal.pop()
        sortedsal = sorted(reversesortedsal)
        sortedsal.pop()
        average = sum(sortedsal) / len(sortedsal)
        return average
        
  