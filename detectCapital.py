class Solution:
    def detectCapitalUse(self, word):
        if len(word)<2:
            return True
        
        if ord(word[0])<=90:
            
            if ord(word[1])<=90:
                for i in word[2:]:
                    if ord(i)>90:
                        return False
            else:
                for i in word[2:]:
                    if ord(i)<=90:
                        return False
        else:
            for i in word[1:]:
                if ord(i)<=90:
                    return False
                
        return True
        
print(Solution().detectCapitalUse('SIimba'))