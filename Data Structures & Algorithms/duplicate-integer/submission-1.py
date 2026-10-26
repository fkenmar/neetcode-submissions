class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = {}
        for num in nums:
            if num in hs:
                return True
            else:
                hs[num] = 0
        return False
