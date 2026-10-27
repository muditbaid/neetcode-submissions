class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = []
        counts = Counter(arr)
        for i in range(len(arr)):
            if arr[i] == counts[arr[i]]:
                lucky.append(arr[i])
        if lucky:
            return max(lucky)
        else:
            return -1