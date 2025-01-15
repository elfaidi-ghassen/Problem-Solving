class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def solution(i, amount_so_far):
            if i in dp:
                return dp[i] + amount_so_far
            
            if i >= len(nums):
                return amount_so_far
            mx = 0
            for k in range(i + 2, len(nums) + 2):
                s = solution(k, amount_so_far + nums[i])
                if s > mx:
                    mx = s
            dp[i] = mx - amount_so_far
            print(dp)
            return mx
                
        mx = 0

        for i in range(len(nums)):
            mx = max(mx, solution(i, 0))
        return mx
