class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for idx, num in enumerate(nums):
            for idx2, num2 in enumerate(nums):
                if idx != idx2 and num == num2:
                    print(f"idx1: {idx}, num: {num}.. idx2: {idx2}, num2:{num2}")
                    return True
        
        return False
