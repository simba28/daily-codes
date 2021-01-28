class Solution:
    def prisonAfterNDays(self, cells, N):
        
        # pattern is repeating after every 14 days
        N = (N-1) % 14 + 1
        for _ in range(N):
            nxt = []
            nxt.append(0)
            for i in range(1,7):
                if cells[i-1]==cells[i+1]:
                    nxt.append(1)
                else:
                    nxt.append(0)
            nxt.append(0)
            cells = nxt.copy()
            
        return nxt

test = Solution()
print(test.prisonAfterNDays([1,0,0,1,0,0,1,0], 10000000))

