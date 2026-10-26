class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        validStr = ''.join(filter(str.isalnum,s)).lower()

        
        return validStr == validStr[::-1]
