class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # iterate through prices
        # index = selling price
        # remember before min price
        max_profit = 0
        min_price = float("inf")
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])

            if prices[i] > min_price:
                max_profit = max(max_profit, prices[i] - min_price)
        return max_profit
                