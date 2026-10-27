class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mc = Counter(magazine)
        rc = Counter(ransomNote)

        for i in ransomNote:
            if mc[i] < rc[i]:
                return False
        return True
