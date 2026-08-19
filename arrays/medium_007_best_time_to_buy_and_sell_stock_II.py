class Solution:
    """
    Idea: Add every positive day-to-day increase.
    If prices keep increasing, adding daily gains is equivalent to 
    buying at the start and selling at the end.
    """
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit 