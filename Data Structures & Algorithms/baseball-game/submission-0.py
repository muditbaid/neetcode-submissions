class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        res = 0
        for op in operations:
            if op == "+":
                res += score[-1] + score[-2]
                score.append(score[-1] + score[-2])
            elif op == "D":
                res += (2*score[-1])
                score.append(2*score[-1])
            elif op == "C":
                res -= score.pop()
            else:
                res += int(op)
                score.append(int(op))
        return res