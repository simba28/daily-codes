class Solution:
    def orangesRotting(self, grid):
        
        rotten = []
        r, c, fresh, t = len(grid), len(grid[0]), 0, 0
        
        for i in range(r):
            for j in range(c):
                
                if grid[i][j] == 2 :
                    rotten.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1
                    
        while rotten:
            
            num = len(rotten)
            
            for i in range(num):
                
                x,y = rotten.pop(0)
                
                if x>0 and grid[x-1][y]==1:
                    grid[x-1][y] = 2
                    rotten.append([x-1,y])
                    fresh -= 1
                if x<r-1 and grid[x+1][y]==1:
                    grid[x+1][y] = 2
                    rotten.append([x+1,y])
                    fresh -= 1
                if y>0 and grid[x][y-1]==1:
                    grid[x][y-1] = 2
                    rotten.append([x,y-1])
                    fresh -= 1
                if y<c-1 and grid[x][y+1]==1:
                    grid[x][y+1] = 2
                    rotten.append([x,y+1])
                    fresh -= 1
                    
            if rotten: t += 1
                
        return t if fresh==0 else -1
        
print(Solution().orangesRotting([[0,2,2]]))