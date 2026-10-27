class Solution:
    def matching(self, pattern: str, s: str) -> bool:
        maps = {}
        if " " in pattern:
            pattern = pattern.split(" ")
        else:
            pattern = list(pattern)
        if " " in s:
            s = s.split(" ")
        else:
            s = list(s)

        for i in range(len(pattern)):
            if pattern[i] in maps and maps[pattern[i]] != s[i]:
                return False
            else:
                maps[pattern[i]] = s[i]
        
        return True



    def wordPattern(self, pattern: str, s: str) -> bool:
        return self.matching(pattern, s) and self.matching(s, pattern)

        