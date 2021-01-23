#link => https://leetcode.com/problems/determine-if-two-strings-are-close/

from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        return len(word1) == len(word2) \
            and set(word1) == set(word2) \
            and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
        
        '''
        if len(word1) != len(word2) or set(word1) != set(word2) : return False
        
        # w1 = sorted(word1)
        # w2 = sorted(word2)
        
        wd1 = {}
        wd2 = {}
        
        for ch in word1:
            wd1[ch] = wd1.get(ch, 0) + 1
        for ch in word2:
            wd2[ch] = wd2.get(ch, 0) + 1
            
        w1 = sorted(wd1.values())
        w2 = sorted(wd2.values())
        
        l1 = len(w1)
        l2 = len(w2)
        
        if l1 != l2: return False
        
        i = 0
        while i < l1:
            if w1[i] != w2[i]:
                return False
            i += 1
        
        return True
        
        '''
        
