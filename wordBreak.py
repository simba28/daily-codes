'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
'''

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        
        self.wordDict = set(wordDict)
        self.memo = {}
        return self.helper(s) or False
        
    def helper(self, s):
        
        if s in self.memo:
            return self.memo[s]
        
        if not s:
            return True
        
        for word in self.wordDict:
            
            if s.startswith(word):
                self.memo[s] = self.helper(s[len(word):])
                if self.memo[s]:
                    return True

print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
        