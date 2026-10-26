class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = len(set(nums)) < len(nums)
        return duplicates
        