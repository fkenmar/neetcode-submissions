class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        validNums = sorted(list(set(nums)))
        box = []
        seq = []
        print(validNums)
        for i in range(len(validNums)):
            prev = validNums[i-1]
            curr = validNums[i]
            if prev + 1 == curr:
                seq.append(curr)
            else:
                seq=[]
                box.append(seq)
                seq.append(curr)
        if nums == []: return 0
        return len(max(box,key=len))


        