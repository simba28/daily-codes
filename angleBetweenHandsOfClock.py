class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        mi = minutes * 6 
        
        hr = (hour * 30) + ((minutes/60)*30)
        
        return  min(abs(hr-mi), 360-abs(hr-mi))
        

# print(Solution().angleClock(1,60))