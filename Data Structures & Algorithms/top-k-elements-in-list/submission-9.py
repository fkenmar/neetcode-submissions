class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
        sorted_counter = dict(sorted(counter.items(), key=lambda item:item[1], reverse=True))
        return list(sorted_counter)[0:k:]