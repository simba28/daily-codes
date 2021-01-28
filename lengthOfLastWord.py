'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word (last word means the last appearing word if we loop from 
left to right) in the string.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        l, result = len(s), 0
        
        for i in range(l-1,-1,-1):
            if s[i]!=' ': result += 1
            else:
                if result>0:break
                    
        return result
        

print(Solution().lengthOfLastWord('hello world'))
