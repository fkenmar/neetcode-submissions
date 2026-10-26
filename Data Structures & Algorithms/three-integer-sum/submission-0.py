class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-1,0,1,2,-1,-4]
        num = sorted(nums)
        #[-4,-1,-1,0,1,2]
        
        # [i,L,..,R]
        n = len(nums)
        left = 1
        right = n - 1

        # output
        res = []

        #[i,..,LR]
        for i in range(n-2):

            left = i+1
            right = n - 1

            while left < right:
                # evaluate
                if num[i] + num[left] + num[right] == 0:
                    #if i + L + R = 0
                    seq = [num[i],num[left],num[right]]
                    if seq not in res:
                        res.append(seq)
                    left+=1
                    right-=1
                
                elif num[i] + num[left] + num[right] > 0:
                    #if i + left + right > 0 find smaller nums so <- R
                    right-=1
                elif num[i] + num[left] + num[right] < 0:
                    #if i + left + right < 0 find bigger nums so L ->
                    left+=1
        return res


            

        