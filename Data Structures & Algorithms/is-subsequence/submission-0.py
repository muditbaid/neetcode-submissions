class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
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