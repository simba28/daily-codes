# link => https://leetcode.com/problems/where-will-the-ball-fall/


class Solution:
    def findBall(self, grid):

        def helper(i, j):
            if i == m:
                dp[(i, j)] = j
                return dp[(i, j)]

            if grid[i][j] == 1 and j == n-1:
                dp[(i, j)] = -1
                return dp[(i, j)]
            if grid[i][j] == -1 and j == 0:
                dp[(i, j)] = -1
                return dp[(i, j)]
            if grid[i][j] == 1 and grid[i][j+1] == -1:
                dp[(i, j)] = -1
                return dp[(i, j)]
            if grid[i][j] == -1 and grid[i][j-1] == 1:
                dp[(i, j)] = -1
                return dp[(i, j)]

            if grid[i][j] == 1:
                dp[(i, j)] = helper(i+1, j+1)

            if grid[i][j] == -1:
                dp[(i, j)] = helper(i+1, j-1)

            return dp[(i, j)]

        m = len(grid)
        n = len(grid[0])
        dp = {}
        ans = [0]*n
        for i in range(n):
            ans[i] = helper(0, i)

        return ans


print(Solution().findBall([[1, 1, 1, 1, 1, 1], [-1, -1, -1, -
                                                1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]))
