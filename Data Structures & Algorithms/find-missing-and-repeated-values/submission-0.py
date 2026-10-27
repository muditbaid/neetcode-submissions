class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums = list(range(1, n*n + 1))
        res = [0,0]
        flat_list = [num for row in grid for num in row]

        counts = Counter(flat_list)

        for i in nums:
            if i not in counts:
                res[1] = i
            elif counts[i] > 1:
                res[0] = i

        return res

