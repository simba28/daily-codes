class Solution:
    def eraseOverlapIntervals(self, intervals):
        
        if len(intervals)<2: return 0
        intervals.sort()
        
        count, lastIncluded = 0,0
        for i in range(1,len(intervals)):
            if intervals[i][0]<intervals[lastIncluded][1]:
                count += 1
                if intervals[i][1]<intervals[lastIncluded][1]:
                    lastIncluded = i
            else:
                lastIncluded = i
                
        return count
    
# print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))