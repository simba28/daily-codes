#link => https://leetcode.com/problems/minimize-deviation-in-array/

#concept used => heap or priority queue

import heapq

class Solution:
    def minimumDeviation(self, nums) -> int:
        
        arr = []
        min_ = float('inf')
        
        for n in nums:
            
            if n%2 != 0:
                n *= 2
                
            heapq.heappush(arr, -n)
            min_ = min(min_, n)
            
        ans = float('inf')
        while True:
            cur = -heapq.heappop(arr)
            
            ans = min(ans, cur - min_)
            
            if cur % 2 != 0: break
                
            heapq.heappush(arr, -cur//2)
            min_ = min(min_, cur//2)
            
            
        return ans
print(Solution().minimumDeviation([1, 3, 4, 7, 5, 9]))