class Solution:
    def hIndex(self, citations):
        
        citations.sort(reverse = True)
        
        n = len(citations)
        i = 1
        while i<=n:
            
            if citations[i-1]<i:
                break
            i += 1
        return i-1

# print(Solution().hIndex([3,0,1,6,5])) 