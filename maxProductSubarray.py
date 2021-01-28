'''
Given an integer array nums, find the contiguous subarray within an array (containing at least 
one number) which has the largest product
'''

class Solution:
    def maxProduct(self, nums):
        
        maxOverall = nums[0]
        maxCurrent, minCurrent = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            
            if nums[i] == 0:
                maxCurrent = 0
                minCurrent = 0
                
            elif nums[i] > 0:
                if maxCurrent>0:
                    maxCurrent = maxCurrent*nums[i]
                else:
                    maxCurrent = nums[i]
                if minCurrent<0:
                    minCurrent = minCurrent*nums[i]
                else:
                    minCurrent = nums[i]
                
            else:
                tmp = maxCurrent
                # maxCurrent= max(nums[i], minCurrent*nums[i])
                # minCurrent= min(nums[i], minCurrent*nums[i], nums[i]*tmp)
                if minCurrent<0:
                    maxCurrent = minCurrent*nums[i]
                else:
                    maxCurrent = nums[i]
                    
                minCurrent= min(nums[i], minCurrent*nums[i], nums[i]*tmp)
                
            maxOverall = max(maxCurrent, maxOverall)
            
        return maxOverall
    
#         for i in range(1,len(nums)):
            
#             tmp = maxCurrent
#             maxCurrent = max(nums[i], nums[i]*maxCurrent, nums[i]*minCurrent)
#             minCurrent = min(nums[i], nums[i]*tmp, nums[i]*minCurrent)
#             maxOverall = max(maxCurrent, maxOverall)
            
#         return maxOverall

print(Solution().maxProduct([-4,-3,-2,-4]))
        