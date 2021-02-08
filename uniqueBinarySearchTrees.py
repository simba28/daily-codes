# link => https://leetcode.com/problems/unique-binary-search-trees/


class Solution:
    # dynamic programming
    def numTrees(self, n: int) -> int:

        res = [0] * (n+1)
        res[0] = 1

        for i in range(1, n+1):

            for j in range(i):

                res[i] += res[j]*res[i-j-1]

        return res[n]
