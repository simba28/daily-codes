class Solution:
    def findDuplicates(self, nums):
        
        # res = []
        # temp = set()
        # for num in nums:
        #     if num in temp:
        #         res.append(num)
        #     else:
        #         temp.add(num)
        # return res
        
        res = []
        nums.append(0)
        size = len(nums)
        for i in range(size):
            
            nums[nums[i]%size] += size
                
        for i in range(size):
            if int(nums[i]/size) > 1 :
                res.append(i)
                
        return res
        

print(Solution().findDuplicates([1,1,2,3,4,5,2,6,7]))