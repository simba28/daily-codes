class Solution:
    def singleNumber(self, nums):
        
        # time = O(n) and space = O(1)
        res = [0,0]
        xor = 0
        for i in nums:
            xor ^= i
            
        xor = xor & (-xor)
        
        for i in nums:
            if i&xor == 0:
                res[0] ^= i
            else:
                res[1] ^= i
                
        return res
        
        # time = O(n) and space = O(n)

#         d = {}
        
#         for i in nums:
#             if i in d:
#                 d.pop(i)
#             else:
#                 d[i]=1
                
#         res = [x for x in d]
#         return res
        
print(Solution().singleNumber([1,2,3,4,3,2,1,5]))
    