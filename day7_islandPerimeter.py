class Solution:
    def islandPerimeter(self, grid):
          
        perimeter = 0 
        width = len(grid[0])
        height = len(grid)
        
        for i in range(height):
            for j in range(width):
                
                if grid[i][j]==1:
                    
                    # solution 1
                    '''
                    if (i==0 or grid[i-1][j]==0):
                        perimeter += 1
                    if (i==height-1 or grid[i+1][j]==0):
                        perimeter += 1
                    if (j==0 or grid[i][j-1]==0):
                        perimeter += 1
                    if (j==width-1 or grid[i][j+1]==0):
                        perimeter += 1
                        '''
                    
                    # solution 2 
                    
                    perimeter += 4
                    
                    if (i>0 and grid[i-1][j]==1):
                        perimeter -= 2
                    if (j>0 and grid[i][j-1]==1):
                        perimeter -= 2
                        
        return perimeter

test = Solution()
print(test.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))