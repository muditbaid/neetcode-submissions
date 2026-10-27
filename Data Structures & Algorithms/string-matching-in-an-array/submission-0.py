class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substring = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] != "" and (words[i] != words[j]) and words[i] in words[j]:
                    substring.append(words[i])
        return substring
