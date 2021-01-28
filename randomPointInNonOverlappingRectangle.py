import random
class Solution:

    def __init__(self, rects):
        self.numPts = 0
        self.rects = rects
        self.rectCumCount = []
        for rect in rects:
            self.numPts += (rect[2]-rect[0]+1)*(rect[3]-rect[1]+1)
            self.rectCumCount.append(self.numPts)
        

    def pick(self):
        ptIdx = random.randint(0,self.numPts-1)
        l,r = 0, len(self.rects)-1
        while l<r :
            mid = l + (r-l)//2
            if self.rectCumCount[mid] <= ptIdx : l = mid+1
            else : r = mid
                
        rect = self.rects[l]
        x_pts = rect[2]-rect[0]+1
        y_pts = rect[3]-rect[1]+1
        ptsInRect = x_pts*y_pts
        ptStart = self.rectCumCount[l]-ptsInRect
        offSet = ptIdx - ptStart
        return [rect[0] + offSet%x_pts, rect[1] + offSet//x_pts]
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()