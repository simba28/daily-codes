#link => https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        z, r = divmod(k-n, 25)
        return ('z'*z if z==n else ('a'*(n-z-1))+(chr(ord('a')+r)) + ('z'*z))
        
#         res = ['a' for i in range(n)]
        
#         total = n
#         idx = n-1
#         while idx >= 0:
            
#             if k-total > 25:
#                 res[idx] = 'z'
#                 idx -= 1
#                 total += 25
            
#             else:
                
#                 res[idx] = chr(97+k-total)
#                 break
                
#         return ''.join(res)

print(Solution().getSmallestString(3, 68))