class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = set()

        for idx,val in enumerate(nums):
            diff = target - val
            if diff in seen:
                return[nums.index(diff),idx]
            seen.add(val)
        