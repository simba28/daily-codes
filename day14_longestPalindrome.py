class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
                
        count = 0
        found_odd = False
        
        for i in d:
            
            if d[i]%2 == 0:
                count += d[i]
            else:
                found_odd = True
                count += d[i]-1
        
        if found_odd : count += 1
            
        return count
                
print(Solution().longestPalindrome("sudhanshu"))