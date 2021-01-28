'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell 
one share of the stock), design an algorithm to find the maximum profit.
'''

class Solution:
    def maxProfit(self, prices) :
        
        profit = 0
        l = len(prices)
        
        if not prices: return 0
        
        min_ = prices[0]
        max_ = prices[0]
        
        i = 1
        while i<l:
            if prices[i]<min_:
                min_ = prices[i]
                
            else:
                max_ = prices[i]
                profit = max(profit, max_-min_)
            
            i += 1
            
        return profit
            
print(Solution().maxProfit([7,1,5,3,6,4]))