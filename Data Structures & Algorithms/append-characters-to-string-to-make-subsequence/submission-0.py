class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                i += 1  # Successfully matched a character in t
            j += 1      # Always move forward in s
            
        # The number of characters left in t that weren't matched
        return len(t) - i  

