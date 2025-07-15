class Solution:
    def rob(self, nums: List[int]) -> int:
        # 2 7 9 3
        # 2 1000 20000 3 1 30000
        # 2 1000 
        n = len(nums)
        dp = [-1] * n # max profit
        
        if n == 1:
            return nums[0]

        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, n):
            # rob i -> don't rob i - 1 rob i - 2
            # don't rob i -> rob i - 1 
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[n -1]