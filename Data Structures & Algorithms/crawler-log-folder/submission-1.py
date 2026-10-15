class Solution:
    def minOperations(self, logs: List[str]) -> int:
       c = 0
       for i in logs:
        if i == "../":
            c-=1
        elif i == "./":
            continue
        else:
            c+=1
        if c<0:
            c=0
       return c
        