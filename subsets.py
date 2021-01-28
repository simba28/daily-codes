class Solution:
    def subsets(self, nums):
        # from itertools import combinations
        nums.sort(reverse=True)
        res = []
        
#         for i in range(0,len(nums)+1):
#             comb = combinations(nums,i)
            
#             res.extend(list(comb))
                
#         return res
        
      # Using bits (for selection of the elements)
        for i in range(2**len(nums)):
            temp = list(bin(i)[2:])
            lst = []
            for i in range(-1,-len(temp)-1,-1):
                if temp[i]=='1':
                    lst.append(nums[i])
            
            res.append(lst)

        # iterative solution (by selecting elements one by one)
        # res = [[]]
        # for x in nums:
        #     n = len(res)
        #     for i in range(n):
        #         r = res[i] + [x]
        #         res.append(r)
            
        return res

test = Solution()
print(test.subsets([1,2,4]))