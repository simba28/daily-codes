'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
'''

class Solution:
    def insert(self, intervals, newInterval):
        
        result = []
        i, n = 0, len(intervals)
        
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
            
        mI = newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            mI[0] = min(intervals[i][0], mI[0])
            mI[1] = max(intervals[i][1], mI[1])
            i += 1
            
        result.append(mI)
        
        while i < n :
            result.append(intervals[i])
            i += 1
            
        return result
    
print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))