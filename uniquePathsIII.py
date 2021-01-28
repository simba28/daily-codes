'''
On a 2-dimensional grid, there are 4 types of squares:

--> 1 represents the starting square.  There is exactly one starting square.
--> 2 represents the ending square.  There is exactly one ending square.
--> 0 represents empty squares we can walk over.
--> -1 represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending 
square, that walk over every non-obstacle square exactly once.
'''

class Solution:
    def uniquePathsIII(self, grid) -> int:
        
        m = len(grid)
        n = len(grid[0])
        zeroes = 0
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    zeroes += 1
                elif grid[i][j] == 1:
                    sx, sy = i, j
                    
        def dfs(i, j, zeroes):
            nonlocal res
            
            if ( i<0 or j<0 or i>=m or j>=n or grid[i][j]==-1):
                return
            
            if grid[i][j] == 2 and zeroes==-1:
                res += 1
                return
            
            tmp = grid[i][j]
            grid[i][j] = -1
            zeroes -= 1
            
            for x,y in [(0,1), (0,-1), (1,0), (-1,0)]:
                dfs(i+x,j+y,zeroes)
            
            grid[i][j] = tmp
            zeroes += 1
            
        dfs(sx, sy, zeroes)
        return res


print(Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))