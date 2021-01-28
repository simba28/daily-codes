class Solution:
    def topKFrequent(self, nums, k):
        
        # first I solved using lists and by counting each element
#         nums.sort()
        
#         lst = []
        
#         if len(nums)==1 or len(nums)==k:
#             return nums
        
#         j = -1
#         for i in range(1,len(nums)):
            
#             if nums[i]!=nums[i-1]:
#                 count = i-1-j
#                 j = i-1
             
#                 if len(lst)<k:
#                     lst.append([count,nums[i-1]])
#                     lst.sort()
#                 elif count>lst[0][0]:
#                     lst.append([count,nums[i-1]])
#                     lst.pop(0)
#                     lst.sort()
                    
#         count = len(nums)-j-1
#         if len(lst)<k:
#             lst.append([count,nums[-1]])
#         elif count>lst[0][0]:
#             lst.append([count,nums[-1]])
#             lst.pop(0)
# 
#         res = [x[1] for x in lst]


        # and then got the idea of using dictionaries that is a heap

        d = {}
    
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
                
        lst = sorted(d.items(), reverse=True, key= lambda x: x[1])
        
        res = [lst[i][0] for i in range(k)]


        return res

print(Solution().topKFrequent([1,1,1,1,2,2,2,3,5,6,3],3))