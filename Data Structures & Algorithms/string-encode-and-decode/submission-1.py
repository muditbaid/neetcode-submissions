class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes = [str(len(s)) for s in strs]
        return ",".join(sizes) + "#" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        separator = s.index("#")
        size_part = s[:separator]
        data = s[separator + 1:]

        sizes = list(map(int, size_part.split(",")))

        decoded_strs = []
        start = 0

        for size in sizes:
            decoded_strs.append(data[start:start + size])
            start += size

        return decoded_strs 
        

