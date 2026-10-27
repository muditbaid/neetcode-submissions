class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = list(set(sorted(nums, reverse=True)))
        return abs(((nums[0]*nums[1]) - (nums[-1]*nums[-2])))

        