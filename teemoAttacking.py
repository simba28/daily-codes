'''
In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe 
be in poisoned condition. Now, given the Teemo's attacking ascending time series 
towards Ashe and the poisoning time duration per Teemo's attacking, you need to output 
the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and 
makes Ashe be in poisoned condition immediately.
'''

class Solution:
    def findPoisonedDuration(self, timeSeries, duration: int) -> int:
        
        if not timeSeries: return 0
        
        total = 0
        next_ = timeSeries[0]+duration
        
        for i in range(1, len(timeSeries)):
            
            if timeSeries[i] >= next_:
                total += duration
            else:
                total += timeSeries[i] - timeSeries[i-1]
                
            next_ = timeSeries[i]+duration
            
        total += duration
        
        return total

print(Solution().findPoisonedDuration([1,2], 2))
            
        