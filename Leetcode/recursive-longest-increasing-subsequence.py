class Solution(object):
    def lengthOfLIS(self, nums):
        dp = {}
        def solution(i):
            if i == len(nums) - 1:
                return 1
            mx = 1

            if i in dp:
                return dp[i]

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    sol = 1 + solution(j)
                    mx = max(mx, sol)
            
            dp[i] = mx
            return mx

        mx = 0
        for i in range(len(nums)):
            mx = max(mx, solution(i))
        return mx