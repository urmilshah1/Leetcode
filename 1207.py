class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)              
        a = len(set(count.values()))
        b = len(list(count.values()))        
        return a == b
        
        
