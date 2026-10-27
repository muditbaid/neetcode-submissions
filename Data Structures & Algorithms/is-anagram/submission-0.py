class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for letter in s:
            if letter in t:
                t = t.replace(letter,"",1)
                s = s.replace(letter,"",1)
        if len(t)!=0:
            return False
        else:
            return True