class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stack = []
        for i in nums:
            if i in stack:
                return True
            else:
                stack.append(i)
        return False