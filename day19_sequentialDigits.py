'''
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
'''

from collections import deque
class Solution:
    def sequentialDigits(self, low: int, high: int) :
        
        self.low = low
        self.high = high
        l = len(str(low))
        h = len(str(high))
        
        self.res = []
        
        for le in range(l, h+1):
            start = 1
            end = 10-le
            if le==l:
                start = int(str(low)[0])
            if le==h:
                end = int(str(high)[0])
            
            for i in range(start, end+1):
                self.helper(str(i), le)
                
        return self.res
            
    
    def helper(self, dig, le):
        
        if dig[-1]=='0':return
        if len(dig)>le:return
        
        if len(dig)==le:
            if self.low <= int(dig) <= self.high:
                self.res.append(int(dig))
            else:
                return
            
        self.helper(dig+str(int(dig[-1])+1),le)

# class Solution:
#     def sequentialDigits(self, low, high):
#         out = []
#         queue = deque(range(1,10))
#         while queue:
#             elem = queue.popleft()
#             if low <= elem <= high:
#                 out.append(elem)
#             last = elem % 10
#             if last < 9: queue.append(elem*10 + last + 1)
#             if elem>high:break
                    
        # return out
        
# class Solution:
#     def sequentialDigits(self, low: int, high: int):
#         s='123456789'
#         ans=[]
#         for i in range(len(s)):
#             for j in range(i+1,len(s)):
#                 st=int(s[i:j+1])
#                 if(st>=low and st<=high):
#                     ans.append(st)
#         ans.sort()            
#         return ans
        
print(Solution().sequentialDigits(99,1000))
        