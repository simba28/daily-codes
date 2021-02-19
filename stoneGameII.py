# link => https://leetcode.com/problems/stone-game-ii/
# youtube => https://www.youtube.com/watch?v=6hu5G-abkdg


class Solution:
    def stoneGameII(self, piles) -> int:
        dp = {}
        def helper(i, m):

            if i >= n:
                return 0
            tot = 0
            ans = -float('inf')
            if (i, m) in dp:
                return dp[(i, m)]

            for j in range(0, 2*m):

                if (i+j < n):
                    tot += piles[i+j]
                ans = max(ans, tot-helper(i+j+1, max(m, j+1)))

            dp[(i, m)] = ans
            return dp[(i, m)]

        n = len(piles)
        sum_ = sum(piles)
        diff = helper(0, 1)
        # dp = {}
        return (sum_+diff)//2


print(Solution().stoneGameII([2, 7, 9, 4, 4]))
