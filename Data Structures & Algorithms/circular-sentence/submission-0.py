class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split(" ")

        for i in range(len(s)):
            last_char = s[i][-1]

            next_first_char = s[(i+1) % len(s)][0]

            if last_char != next_first_char:
                return False
        
        return True
        
