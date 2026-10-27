class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            encoded_string = ""
            return encoded_string
        sizes=[]
        encoded_string=""
        for s in strs:
            sizes.append(str(len(s)))
        
        encoded_string=",".join(sizes) + "#"
        encoded_string+="".join(strs)
        return encoded_string



    def decode(self, s: str) -> List[str]:
        sizes=[]
        decoded_strs=[]
        if s=="":
            return decoded_strs
        for i in s:
            if i=="#":
                start = s.index(i) + 1
                break
            if i==",":
                continue
            sizes.append(int(i))
        for i in sizes:
            decoded_strs.append(s[start:start+i])
            start += i
        return decoded_strs 
        

