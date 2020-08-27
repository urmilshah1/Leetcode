class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        N = len(s)
        string = [""] * N
        
        for x, y in enumerate(indices):
            string[y] = s[x]
        return "".join(string)
    
    #After getting the length of the string 's'. I created another string called 'string'. Using the enumerate function, I joined two string with the indices. 