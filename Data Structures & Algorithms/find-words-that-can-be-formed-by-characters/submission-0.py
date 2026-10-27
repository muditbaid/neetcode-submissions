class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = 0
        
        charc = Counter(chars)
        for i in words:
            flag = 1
            count = Counter(i)
            for x in set(i):
                if charc[x] < count[x]:
                    flag = 0
            if flag == 1:
                c += len(i)
            
        return c

            
            