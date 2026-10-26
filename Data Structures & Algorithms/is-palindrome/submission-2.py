class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(filter(str.isalnum,s)).lower()
        
        left = 0
        right = len(s)-1

        print(s)

        while left <= right:
            print(right)
            leftChar = s[left]
            rightChar = s[right]

            if leftChar != rightChar: return False
                
            left+=1
            right-=1
        return True

            
        

    
