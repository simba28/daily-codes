class Solution:
    def findMin(self, nums):
        
        h = len(nums)-1
        l = 0
        
        while l<h:
            m = (l+h)//2
            
            if nums[m]==nums[h]:
                if nums[l]==nums[m]:
                    l = l+1
                else:
                    h = m
            elif nums[m]>nums[h]:
                l = m+1
            else:
                h = m
                
        return nums[l]
        

print(Solution().findMin([2,2,2,10,11]))