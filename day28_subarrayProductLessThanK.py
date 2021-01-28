'''
our are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements 
in the subarray is less than k.
'''

class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        
        # if k <= 1: return 0
        prod = 1
        left = 0
        res = 0
        
        for right in range(len(nums)):
            
            prod *= nums[right]
            while prod >= k and left <= right:
                prod /= nums[left]
                left += 1
        
            res += right - left + 1
            
        return res
                
print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))