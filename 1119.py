class Solution:
    def removeVowels(self, S: str) -> str:
        result = []
        str1 = ""
        for char in S:
            if(char =='a' or char =='e'or char =='i' or char =='o'or char =='u'):
                continue
            else:
                result.append(char)
                str1= ''.join(result)
        return str1
    
    
    #Iterate through the string, if vowel found, then continue otherwise append it to the list.
    #For the format they require, I just joined the string and removed "", essentially converting it from list to string. 