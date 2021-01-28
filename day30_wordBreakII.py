class Solution:
    def wordBreak(self, s, wordDict):
        self.wordDict = set(wordDict)
        self.memo = {}
        return self.wordBreakHelper(s)
        
        
    def wordBreakHelper(self, s):
        
        if s in self.memo:
            return self.memo[s]
        
        result = []
        
        if len(s) == 0:
            result.append("")
            return result
        
        for word in self.wordDict:
            if s.startswith(word):
                subStrings = self.wordBreakHelper(s[len(word):])
                
                for subString in subStrings:
                    tmp = ' ' if subString else ''
                    result.append(word+tmp+subString)
        
        self.memo[s] = result
        
        return result

# print(Solution().wordBreak("pineapplepenapple",["apple", "pen", "applepen", "pine", "pineapple"]))