class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if Counter(s) > Counter(t):
            return False
        indexes = []
        for i in s:
            if i in t:
                indexes.append(t.rindex(i))
            else:
                return False
        if indexes == sorted(indexes):
            return True
        else:
            return False