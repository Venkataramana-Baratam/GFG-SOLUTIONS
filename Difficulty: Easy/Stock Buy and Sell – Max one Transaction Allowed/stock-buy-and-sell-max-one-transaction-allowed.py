class Solution:
    def maxProfit(self, prices):
        # code here
        
        
        max_profit = 0
        
        mini = prices[0]
        
        for ind,val in enumerate(prices):
            
            if mini>val:
                mini = val
            profit = val - mini
            if profit>max_profit:
                
                max_profit = profit
                
        return max_profit