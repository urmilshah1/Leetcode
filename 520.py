class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        variations = []
        variations.append(word.upper())
        variations.append(word.lower())
        variations.append(word.capitalize())
        if word in variations:
            return True
        else:
            return False
        
        
        ''' count= 0
        for char in word:
            if char.isupper():
                count += 1
        return len(word) == count
           This case passes most cases. It fails when the letter is a single alphabet "a" to "z".
           
           '''