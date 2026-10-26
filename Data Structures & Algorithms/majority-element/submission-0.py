class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        res = maxcount = 0
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
            if maxcount < counts[i]:
                res = i
                maxcount = counts[i]
        return res