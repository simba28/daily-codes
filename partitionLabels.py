'''
Problem Statement
A string S of lowercase English letters is given. We want to partition 
this string into as many parts as possible so that each letter appears 
in at most one part, and return a list of integers representing the size 
of these parts.
'''

class Solution:
    def partitionLabels(self, S):
        
        last = {}
        for i,ch in enumerate(S):
            last[ch] = i
          
        res = []
        start, end = 0, 0
        for i in range(len(S)):
            end = max(end, last[S[i]])
            if i==end:
                res.append(i-start+1)
                start = i+1
                
        return res

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))