'''
Given an unsorted integer array, find the smallest missing positive integer.

req
time -> O(n)
space -> O(1)
'''

class Solution:
    def firstMissingPositive(self, nums) -> int:
        
        if not nums: return 1
        
        n = len(nums)
        containsOne = False
        
        for i in range(n):
            if nums[i]==1:
                containsOne = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
                
        if not containsOne: return 1
        
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -1 * nums[idx]
                
        for i in range(n):
            if nums[i] > 0:
                return i+1
            
        return n+1

print(Solution().firstMissingPositive([7,8,9,11,12,1]))
