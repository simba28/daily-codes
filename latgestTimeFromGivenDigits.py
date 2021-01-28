'''
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a 
time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.
'''

import itertools

class Solution:
    def largestTimeFromDigits(self, arr):
        arr.sort(reverse=True)
        
        for h, i, j, k in itertools.permutations(arr):
            if h*10+i < 24 and j*10+k < 60:
                return str(h)+str(i)+':'+str(j)+str(k)
        else:
            return ""

print(Solution().largestTimeFromDigits([0,0,1,0]))