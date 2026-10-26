class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alphabet = [0] * 26
        for i in range(len(s)):
            idx = ord(s[i]) - 97
            alphabet[idx] += 1
            idx = ord(t[i]) - 97
            alphabet[idx] -= 1
        if all(x == 0 for x in alphabet):
            return True
        else:
            return False
        