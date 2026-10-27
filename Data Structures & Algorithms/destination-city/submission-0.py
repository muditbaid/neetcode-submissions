class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest = set()
        citties = set()
        for i in paths:
            citties.add(i[0])
            dest.add(i[1])
        
        return (dest - citties).pop()
        
