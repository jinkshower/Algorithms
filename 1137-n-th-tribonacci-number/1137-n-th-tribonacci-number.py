class Solution:
    def tribonacci(self, n: int) -> int:
        # computed = [-1] * (n + 1)
        # def fibo(n, computed):
        #     if n == 0:
        #         return 0
        #     if n == 1:
        #         return 1
        #     if n == 2:
        #         return 1
        #     if computed[n] != -1:
        #         return computed[n]
        #     computed[n] = fibo(n - 1, computed) + fibo(n -2, computed) + fibo(n -3, computed)
        #     return computed[n]
        
        # return fibo(n, computed)
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]
        