class Solution(object):
    def lengthOfLIS(self, nums):
            dp = [0] * len(nums)
            dp[-1] = 1
            for i in range(len(nums) - 2, -1, -1):
                for j in range(i + 1, len(nums)):
                    if nums[j] > nums[i]:
                        dp[i] = max(dp[i], dp[j])
                dp[i] += 1
            return max(dp)