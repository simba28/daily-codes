'''
You are a professional robber planning to rob houses along a street. Each 
house has a certain amount of money stashed, the only constraint stopping 
you from robbing each of them is that adjacent houses have security system
connected and it will automatically contact the police if two adjacent houses 
were broken into on the same night.
'''

class Solution:
    def rob(self, nums):
        
        dp1, dp2 = 0, 0
        for num in nums:
            dp1, dp2 = dp2, max(dp1+num, dp2)
            
        return dp2

print(Solution().rob([2,7,9,3,1]))