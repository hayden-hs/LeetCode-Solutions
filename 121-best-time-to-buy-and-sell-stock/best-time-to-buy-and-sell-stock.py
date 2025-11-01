class Solution:
    def maxProfit(self, prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            #price[left] < price[right] which means we will get profit
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else: 
                #Price[left] > price[right] so we will move left to the right
                left = right
            right += 1
        return max_profit
        