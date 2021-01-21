class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        self.s = s
        self.l = len(s)
        
        if ( not s or len(s) < 1): return ''
        
        start = 0
        end = 0
        
        for i in range(self.l):
            len1 = self.expandAroundCenter(i, i)
            len2 = self.expandAroundCenter(i, i+1)
            len_ = max(len1, len2)
            if ( len_ > end - start):
                start = i - ((len_-1) // 2)
                end = i + (len_//2)
                
        return self.s[start: end+1]
        
    def expandAroundCenter(self, left, right):
        
        if not self.s or left > right:
            return ''
        
        while ( left >= 0 and right < self.l and self.s[left]==self.s[right]):
            left -= 1
            right += 1
            
        return right - left - 1
        

print(Solution().longestPalindrome('sudnanshu'))