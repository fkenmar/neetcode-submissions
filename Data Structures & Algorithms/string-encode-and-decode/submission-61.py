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
            # restarts getting each length and word until end
            length = 0
            word = ''
            while s[curr] != '#':
                # gets the number as int, stops at delimeter
                num = int(s[curr])
                length = length * 10 + num
                curr += 1
            
            # skips delimeter
            if s[curr] == '#':
                curr += 1

            while length != 0:
                # gets each char of word until length is exhausted
                word += s[curr]
                curr += 1
                length -= 1
                
            # append word we get the loop restarts
            decoded.append(word)

        # output [hello,word]
        # output [hello,hello]
        return decoded

                



