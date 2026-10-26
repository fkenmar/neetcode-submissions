class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 1:
            return [nums[0]]

        seen = defaultdict(list)

        for num in nums:
            seen[num].append(num)

        seen = sorted(seen.items(),key=lambda item: len(item[1]),reverse=True)

        output = []

        for num in range(k):
            output.append(seen[num][0])
        
        return output
            

        
        