class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        j = 0
        maxpft = 0
        for i in range(1, len(prices)):
            if(prices[i] - prices[j] < 0):
                j = i
            else:
                profit = prices[i] - prices[j]
            
            maxpft = max(profit, maxpft)
        return maxpft