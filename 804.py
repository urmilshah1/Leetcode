class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        solution = set()
        lst = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        for i in words:
            transformation = ""
            for j in i:
                transformation += lst[j]
            solution.add(transformation)
        return len(solution)
    
    