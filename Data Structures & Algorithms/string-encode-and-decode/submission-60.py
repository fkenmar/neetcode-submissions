class Solution:

    def encode(self, strs: List[str]) -> str:
        # input [hello,world]
        encoded = ''
        for s in strs:
            encoded += f'{len(s)}#{s}'
        # output 5#hello5#world
        # output 10#hellohello
        return encoded

    def decode(self, s: str) -> List[str]:
        # input 5#hello5#world
        # input 10#hellohello
        decoded = []
        curr = 0
        while curr < len(s):
            length = 0
            word = ''
            while s[curr] != '#':
                num = int(s[curr])
                length = length * 10 + num
                curr += 1
            
            if s[curr] == '#':
                curr += 1

            while length != 0:
                word += s[curr]
                curr += 1
                length -= 1
            decoded.append(word)
        return decoded

                



