class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prev = dict()
        
        for idx,val in enumerate(nums):
            diff = target-val
            if diff in prev:
                return [prev[diff],idx]
            prev[val]=idx


        return [left,right]

                




        