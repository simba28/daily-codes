# link => https://leetcode.com/problems/minimum-path-sum/


class Solution:
    def minPathSum(self, grid) -> int:
        # very good approach, dynamic programming
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if i == 0 or j == 0:
                    if i == 0 and j != 0:
                        grid[i][j] += grid[i][j-1]
                    if i != 0 and j == 0:
                        grid[i][j] += grid[i-1][j]
                    continue
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[i][j]
    '''
    # recursion using memoization
    def minPathSum(self, grid) -> int:
        
        def helper(i,j):
            
            if i==m-1 and j==n-1:
                dp[(i,j)] = grid[i][j]
                return dp[(i,j)]
                
            if (i,j) in dp:
                return dp[(i,j)]
            
            right, down = float('inf'), float('inf')
            if j<n-1:
                right = grid[i][j] + helper(i,j+1)
            if i<m-1:
                down = grid[i][j] + helper(i+1,j)
                
            dp[(i,j)] = min(right, down)
            return dp[(i,j)]
        
        m = len(grid)
        n = len(grid[0])
        dp = {}
        return helper(0,0)
        '''
