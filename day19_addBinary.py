class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # Normal approach by adding each bit
        
#         if len(a)>len(b):
#             x = a
#             y = b
#         else:
#             x = b
#             y = a
        
#         res = ''
        
#         temp = 0
#         i = -1
#         for _ in range(len(x),len(x)-len(y),-1):
#             no = int(x[i])+int(y[i])+temp
#             if no==3:
#                 res = '1'+res
#                 temp = 1
#             elif no==2:
#                 res = '0'+res
#                 temp = 1
#             elif no==1:
#                 res = '1'+res
#                 temp = 0
#             else:
#                 res = '0'+res
#                 temp = 0
#             i -= 1
        
#         i = -len(y)-1
#         for _ in range(len(x)-len(y),0,-1):
#             no = int(x[i])+temp
#             if no==2:
#                 res = '0'+res
#                 temp = 1
#             elif no==1:
#                 res = '1'+res
#                 temp = 0
#             else:
#                 res = '0'+res
#                 temp = 0
#             i -= 1
                
#         if temp==1:
#             res = '1'+res

        # by using python inbuilt functions
    
        x = int(a,2)
        y = int(b,2)
        res = x+y
        res = bin(res)[2:]
        
        return res
        
# print(Solution().addBinary('10000','1111111'))