class Solution:
    def titleToNumber(self, s: str) -> int:
        
        res = 0
        
        for idx,char in enumerate(s[::-1]):
            
            res += (ord(char)-64) * (26**idx)
        
        return res

print(Solution().titleToNumber('ABCDEF'))