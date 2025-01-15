class Solution:


    def climbStairs(self, n: int) -> int:
        dp = {}
        def solution(steps_left):
            if steps_left == 0:
                return 1
            if steps_left < 0:
                return 0
            elif steps_left in dp:
                return dp[steps_left]
            s = solution(steps_left - 1) + solution(steps_left -2)
            dp[steps_left] = s
            return s
        return solution(n)
