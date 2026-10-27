class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps = {}
        
        for i in range(len(s)):
            if s[i] in maps:
                if maps[s[i]] != t[i]:
                    return False
            else:
                maps[s[i]] = t[i]
        return True