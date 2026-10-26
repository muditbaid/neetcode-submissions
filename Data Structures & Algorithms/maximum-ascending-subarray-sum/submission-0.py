class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        inc = [nums[0]]
        maxSum = nums[0]

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                inc.append(nums[i])
                maxSum = max(maxSum, sum(inc))
            else:
                inc = [nums[i]]  # Reset to a list, not an integer
                maxSum = max(maxSum, sum(inc)) # Don't overwrite the global max
                
        return maxSum