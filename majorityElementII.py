'''
given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.
'''

'''
Boyer-Moore Voting Algorithm
'''

'''
link 
https://leetcode.com/problems/majority-element-ii/solution/
'''


class Solution:
    def majorityElement(self, nums):
        
        if not nums: return []
        
        count1, count2, cand1, cand2 = 0, 0, None, None
        
        for num in nums:
            
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 += 1
            elif count2 == 0:
                cand2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
           
        res = []
        for c in (cand1, cand2):
            if nums.count(c) > len(nums)//3: res.append(c)
                
        return res
    
print(Solution().majorityElement([1,1,1,3,3,2,2,2]))