class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        s=0
        for i in nums:
            if i==1:
                c+=1
            else:
                s=max(s,c)
                c=0
        return max(s,c)