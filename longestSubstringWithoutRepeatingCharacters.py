#link => https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        tmp = 0
        idx = {}
        lastRpt = -1
        
        for i, ch in enumerate(s):
            
            if ch in idx:
                res = max(tmp, res)
                lastRpt = max(lastRpt, idx[ch])
                tmp = i - lastRpt
                idx[ch] = i
            
            else:
                idx[ch] = i
                tmp += 1
        
        return max(tmp, res)