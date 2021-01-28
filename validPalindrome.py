class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<2:
            return True
        
        i = 0
        j = len(s)-1
        while i<j:
            while i<j and not s[i].isalnum():
                i += 1
            while j>i and not s[j].isalnum():
                j -= 1
            
            if i<j and s[i].lower()!=s[j].lower():
                return False
            
            i,j = i+1, j-1
        
        return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))