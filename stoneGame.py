# link => https://leetcode.com/problems/stone-game/submissions/


class Solution:
    def stoneGame(self, piles) -> bool:

        def helper(i, j):

            if i > j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = max(piles[i]-helper(i+1, j), piles[j]-helper(i, j-1))
            return dp[(i, j)]

        dp = {}
        return helper(0, len(piles)-1) > 0


print(Solution().stoneGame([5, 3, 4, 5]))
