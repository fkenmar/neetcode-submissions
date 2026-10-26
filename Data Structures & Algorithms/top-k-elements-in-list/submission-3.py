class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = []
        print(counter.most_common()[0][0])
        for i in range(k):
            num = counter.most_common()[0][0]
            res.append(num)
            counter.pop(num)

        return res