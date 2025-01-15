class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # V3
        n = len(cost)
        # dp = [0] * n
        first = cost[n - 1]
        second = cost[n - 2]
        for i in range(n - 3, -1, -1):
            temp = second
            second = cost[i] + min(first, second)
            first = temp
        return min