class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = list()
        for val in nums:
            if val in x:
                return True
            else:
                x.append(val)
        return False