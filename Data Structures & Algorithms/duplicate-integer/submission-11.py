class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = list()
        for idx,val in enumerate(nums):
            if val in x:
                print(val)
                return True
                
            else:
                print(val)
                x.append(val)
        
        return False