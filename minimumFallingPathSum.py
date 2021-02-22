# link => https://leetcode.com/problems/minimum-falling-path-sum/


class Solution:
    def minFallingPathSum(self, matrix) -> int:
        '''
        # from solution
        while len(matrix) >= 2:
            row = matrix.pop()
            for i in range(len(row)):
                matrix[-1][i] += min(row[max(0, i-1):min(len(row), i+2)])

        return min(matrix[0])
        '''

        # my code (dynamic programming)
        def helper(i, j):

            if i == n-1:
                return matrix[i][j]

            if (i, j) in dp:
                return dp[(i, j)]

            min_ = float('inf')
            for x in range(max(0, j-1), min(j+1+1, n)):
                min_ = min(min_, matrix[i][j]+helper(i+1, x))

            dp[(i, j)] = min_
            return dp[(i, j)]

        dp = {}
        n = len(matrix)
        min_ = float('inf')
        for i in range(n):
            min_ = min(min_, helper(0, i))
        return min_


print(Solution().minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
