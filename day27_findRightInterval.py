import bisect
class Solution:
    def findRightInterval(self, intervals):
        
        if len(intervals)<=1:
            return [-1]
        
        l = len(intervals)
        ints = sorted([[x,y,i] for i,[x,y] in enumerate(intervals)])
        begs = [i for i,_,_ in ints]
        res = [-1]*l
        
        for _,y,i in ints:
            
            t = bisect.bisect_left(begs, y)
            if t<l:
                res[i] = ints[t][2]
                      
        return res
            
print(Solution().findRightInterval([ [3,4], [2,3], [1,2] ]))