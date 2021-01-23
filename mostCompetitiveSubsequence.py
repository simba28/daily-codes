#link => https://leetcode.com/problems/find-the-most-competitive-subsequence/
#concept used => monotone stack

class Solution:
    def mostCompetitive(self, nums, k: int) :
        
        if not nums or len(nums)==k: return nums
        
        stack = []
        rem = len(nums) - k
        
        for num in nums:
            
            while (stack and rem and num<stack[-1]):
                stack.pop()
                rem -= 1
                
            stack.append(num)
            
        while rem:
            stack.pop()
            rem -= 1
            
        return stack

print(Solution().mostCompetitive([2,4,3,3,5,4,9,6], 4))