# link => https://leetcode.com/problems/count-submatrices-with-all-ones/submissions/


class Solution:
    def numSubmat(self, mat) -> int:

        m = len(mat)
        n = len(mat[0])

        arr = [[0] * n for _ in range(m)]

        for i in range(m):
            c = 0
            for j in range(n):
                if mat[i][j] == 1:
                    c += 1
                else:
                    c = 0

                arr[i][j] = c

        ans = 0
        for i in range(m):
            for j in range(n):
                x = float('inf')
                for k in range(i, m):
                    x = min(x, arr[k][j])
                    ans += x

        return ans


print(Solution().numSubmat([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))
