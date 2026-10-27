class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        out = [0] * len(queries)
        vowels = set("aeiou")
        presum = [0] * (len(words) + 1)
        prev = 0

        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                prev += 1
            presum[i + 1] = prev

        for i, q in enumerate(queries):
            l, r = q
            out[i] = presum[r + 1] - presum[l]
        
        return out


