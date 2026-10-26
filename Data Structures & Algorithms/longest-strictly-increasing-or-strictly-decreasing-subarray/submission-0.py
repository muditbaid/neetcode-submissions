class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # max_len tracks the highest streak we've seen overall
        max_len = 1
        
        # inc and dec track the lengths of the current streaks
        inc = 1
        dec = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
                dec = 1    # Reset decreasing streak
            elif nums[i] < nums[i-1]:
                dec += 1
                inc = 1    # Reset increasing streak
            else:
                # If numbers are equal, both streaks reset
                inc = 1
                dec = 1
                
            # Update the global maximum after every step
            max_len = max(max_len, inc, dec)
            
        return max_len