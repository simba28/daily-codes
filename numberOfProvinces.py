# link => https://leetcode.com/problems/number-of-provinces/


class Solution:

    # dfs solution
    def findCircleNum(self, isConnected) -> int:

        n = len(isConnected)
        visited = set()

        def dfs(node):

            for idx, conn in enumerate(isConnected[node]):
                if conn == 1 and idx not in visited:
                    visited.add(idx)
                    dfs(idx)

        ans = 0
        for x in range(n):
            if x not in visited:
                ans += 1
                visited.add(x)
                dfs(x)

        return ans


print(Solution().findCircleNum([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
