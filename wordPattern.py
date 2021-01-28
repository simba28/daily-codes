'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter 
in pattern and a non-empty word in str.
'''

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        
        lst = str.split()
        d = {}
        
        if len(pattern)!=len(lst):return False
        
        for i,ch in enumerate(pattern):
            
            if ch not in d:
                if lst[i] not in d.values():
                    d[ch] = lst[i]
                else:
                    return False
            
            else:
                if not d[ch]==lst[i]:
                    return False
                
        return True

print(Solution().wordPattern("abba", "dog cat cat dog"))