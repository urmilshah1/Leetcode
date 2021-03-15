class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum1 = 0 
        chars_counter = collections.Counter(chars)
        for word in words:
            word_counter = collections.Counter(word)
            for c in word_counter:
                if word_counter[c] > chars_counter[c]:
                    break
            else:
                sum1 += len(word)
        return sum1