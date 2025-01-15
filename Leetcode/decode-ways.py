class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def solution(start, end):
            if start >= len(s):
                return 0

            segment = s[start : end + 1]
            if segment[0] == "0" or int(segment) < 1 or int(segment) > 26:
                return 0

            if end in dp:
                return dp[end]

            if end == len(s) - 1:
                return 1

            if start < end:
                dp[end] = solution(end + 1, end + 1) + solution(end + 1, end + 2)
                return dp[end]
            else:
                dp[end] = solution(start + 1, end + 1) + solution(start + 1, end + 2)
                return dp[end]

        return solution(0, 0) + solution(0, 1)