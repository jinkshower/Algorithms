class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 10 15 20 25 30 35
        # 0  0  10 15
        n = len(cost) #3
        dp = [1000] * (n + 1)

        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])
        
        return dp[n]

