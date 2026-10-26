class Solution:
    encoded = ""
    def encode(self, strs: List[str]) -> str:
        for s in strs:
            self.encoded+= s
            self.encoded+= "\x1f"
        return self.encoded

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






        



        


