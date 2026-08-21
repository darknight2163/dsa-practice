class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        result = 0

        for i, price in enumerate(prices):
            minPrice = min(minPrice, price)
            result = max(result, price - minPrice)

        return result