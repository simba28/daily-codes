# link => https://leetcode.com/problems/shortest-path-in-binary-matrix/


class Solution:
    def shortestPathBinaryMatrix(self, grid):

        if grid[0][0] != 0:
            return -1
        m = len(grid)
        n = len(grid[0])

        queue = [(0, 0, 1)]
        grid[0][0] = 1

        dir_ = ((0, 1), (1, 0), (0, -1), (-1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1))
        while queue:

            size = len(queue)
            while size > 0:
                pt = queue.pop(0)

                if pt[0] == m-1 and pt[1] == n-1:
                    return pt[2]

                for d in dir_:
                    r = pt[0] + d[0]
                    c = pt[1] + d[1]

                    if (r >= 0 and c >= 0 and r < m and c < n and grid[r][c] == 0):
                        queue.append((r, c, pt[2]+1))
                        grid[r][c] = 1

                size -= 1

        return -1


print(Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 0, 0], [1, 1, 0]]))
