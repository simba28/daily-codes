class Solution:
    def maxProfit(self, prices):
        
        if len(prices) <= 1 : return 0
        A, B, C = 0, -prices[0], 0
        for i in range(1,len(prices)):
            tmp = A
            A = max(A,C)
            C = B + prices[i]
            B = max(B, tmp-prices[i])
            
        return max(A,C)

# print(Solution().maxProfit([1,2,3,0,2]))