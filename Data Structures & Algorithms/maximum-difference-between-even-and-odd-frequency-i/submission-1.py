class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        oddMax, evenMin = 0, len(s)

        for cnt in counts.values():
            if cnt & 1:
                oddMax = max(oddMax, cnt)
            else:
                evenMin = min(evenMin, cnt)
            
        return oddMax - evenMin
        
        
