class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        
        # Loop through the string, stopping 2 characters before the end
        for i in range(len(num) - 2):
            # Check if 3 consecutive characters are identical
            if num[i] == num[i+1] == num[i+2]:
                # Update the maximum string found so far
                max_good = max(max_good, num[i:i+3])
                
        return max_good

