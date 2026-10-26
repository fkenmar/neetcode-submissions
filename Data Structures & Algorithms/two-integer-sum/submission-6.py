class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        output = []
        for idx, num in enumerate(nums):
            if (target - num) == num:
                output.append(idx)
            elif (target - num) in nums:
                print('b')
                return [idx,nums.index(target-num)] 
        return output
                




        