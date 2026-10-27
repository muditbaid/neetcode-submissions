class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        c = nums[0] % 2
        if len(nums) == 1:
            return True
        
        for i in nums[1:]:
            if i % 2 == c:
                return False
            else:
                c = i % 2
        return True