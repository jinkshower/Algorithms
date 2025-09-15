class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        
        l = r = 0
        n = len(prices)

        while (r < n):
            max_p = max(max_p, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
            r += 1
        return max_p