
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(':')', '{':'}','[':']'}
        for char in s:
            if char in pairs:
                stack.append(pairs[char])
            else:
                if len(stack) == 0 or stack.pop() != char:
                    return False
        return len(stack) == 0
    
    
    #Implement a Stack, append values when they are found in the pair. if not then check the length and pop the variable.