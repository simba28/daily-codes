#link => https://leetcode.com/problems/max-number-of-k-sum-pairs/
#concept used => two pointer method or hashing

from collections import defaultdict
class Solution:
    def maxOperations(self, nums, k: int) -> int:
        
        ans = 0
        seen = defaultdict(int)
        for b in nums:
            a = k - b
            if seen[a] > 0:
                ans += 1
                seen[a] -= 1
            else:
                seen[b] += 1
        return ans
                
        '''
        nums.sort()
        
        start = 0
        end = len(nums) - 1
        res = 0
        
        while start< end:
            
            sum_ = nums[start] + nums[end]
            
            if sum_ == k:
                res += 1
                start += 1
                end -= 1
                
            elif sum_ < k:
                start += 1
                
            else :
                end -= 1
                
        return res
        '''

print(Solution().maxOperations([1,3,3,3,4], 6))