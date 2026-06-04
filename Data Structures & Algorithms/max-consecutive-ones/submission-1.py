class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        # Brute Force
        # n, res = len(nums), 0

        # for i in range(n):
        #     cnt = 0
        #     for j in range(i,n):
        #         if nums[j] == 0:
        #             break
        #         cnt += 1
        #     res = max(res, cnt)
        # return cnt
        
        # res, cnt = 0, 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         res = max(res, cnt)
        #         cnt = 0
        #     else:
        #         cnt +=1
        # return max(res,cnt)
        
        res, cnt = 0, 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                cnt = 0
            res = max(res, cnt)
        return res
