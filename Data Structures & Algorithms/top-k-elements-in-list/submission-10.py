class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for num in nums:
            seen[num]+=1
        val = sorted(seen.items(), key=lambda item:item[1], reverse=True)
        new = list(dict(val).keys())
        res = []
        for i in range(k):
            res.append(new[i])
        return res
            
            





        