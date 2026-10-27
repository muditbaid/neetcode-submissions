class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        
        counts = Counter(nums)
        for i in counts.values():
            if i % 2 != 0:
                return False
        
        return True
