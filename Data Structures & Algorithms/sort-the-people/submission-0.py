class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        maps = {}
        for h, n in zip(heights, names):
            maps[h] = n
        
        res = []
        for h in reversed(sorted(heights)):
            res.append(maps[h])

        return res
