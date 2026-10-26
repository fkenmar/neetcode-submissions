class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alphabet = [0] * 26
        for letter in s:
            idx = ord(letter) - 97
            alphabet[idx] += 1
        for letter in t:
            idx = ord(letter) - 97
            alphabet[idx] -= 1
        return all(x == 0 for x in alphabet)
        