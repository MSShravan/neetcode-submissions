class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        sizes = []
        for s in strs:
            sizes.append(str(len(s)))
        res = ",".join(sizes) + ",#"
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0

        while s[i] != "#":
            count = ''
            while s[i] != ",":
                count += s[i]
                i+=1
            sizes.append(int(count))
            i+=1
        i+=1

        for sz in sizes:
            res.append(s[i: i+sz])
            i+=sz

        return res