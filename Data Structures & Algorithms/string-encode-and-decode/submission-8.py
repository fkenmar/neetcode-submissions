class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded+= s
            encoded+= "\x1f"
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        resStr = ""
        for i in s:
            if not i:
                return [""]
            elif i == "\x1f":
                res.append(resStr)
                resStr = ""
            else:
                resStr += i
        return res






        



        


