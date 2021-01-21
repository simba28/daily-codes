class Solution:

    # time O(n^2) and space O(1)
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

    # Dynamic programming time O(n^2) and space O(n^2)
    def longestPalindromeDP(self, s1):
        
        if (not s1 or len(s1) < 1): return ''
        
        len_ = len(s1)
        longest = 0
        res = ''
        
        dp = [[False for i in range(len_)] for j in range(len_)]
        
        for g in range(len_):
            
            i = 0
            j = g
            while ( j < len_ ):
                
                if (g == 0):
                    dp[i][j] = True
                elif (g == 1 and s1[i] == s1[j]):
                    dp[i][j] = True
                else:
                    if ( s1[i]==s1[j] and dp[i+1][j-1] ):
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                        
                if dp[i][j]:
                    longest = g + 1
                    res = s1[i:j+1]
                    
                i += 1
                j += 1
                    
        return res
        

print(Solution().longestPalindromeDP('sudnanshu'))