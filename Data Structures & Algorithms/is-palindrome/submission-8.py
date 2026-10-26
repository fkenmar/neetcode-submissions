class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = "".join(filter(str.isalnum, s)).lower()

        right = len(sentence)-1
        left = 0

        while left < right:
            if sentence[left] != sentence[right]:
                return False
            left+=1
            right -=1

        return True