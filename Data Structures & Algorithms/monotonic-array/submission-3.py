class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag = 1 if nums[1] >= nums[0] else 0
        for i in range(1,len(nums)):
            if nums[i] >= nums[i-1]:
                if flag == 1:
                    continue
                else:
                    return False
            
            elif nums[i] <= nums[i-1]:
                if flag == 0:
                    continue
                else:
                    return False
        return True
            

