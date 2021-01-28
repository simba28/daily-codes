class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # recursive solution
        if n==0: return 1.0
        if n==1: return x
        if n<0:
            return self.myPow(1/x,-n)
        res = self.myPow(x*x,n//2)
        if n%2==1:
            res *= x
            
        # iterative solution
#         if n==0: return 1.0
#         if n==1: return x
#         if n<0:
#             x = 1/x
#             n = -n
            
#         res = 1
#         while n>0:
#             if n%2==1:
#                 res *= x
#             x *= x
#             n = n//2

        return res

print(Solution().myPow(2,5))