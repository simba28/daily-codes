# link => https://leetcode.com/problems/min-cost-climbing-stairs/


class Solution:

    def minCostClimbingStairs(self, cost) -> int:

        n = len(cost)
        self.dp = [0 for _ in range(n+1)]
        self.cost = cost

        return min(self.minCost(n-1), self.minCost(n-2))

    def minCost(self, n):

        if n < 0:
            return 0
        if n == 0 or n == 1:
            return self.cost[n]
        if self.dp[n] != 0:
            return self.dp[n]

        self.dp[n] = self.cost[n] + min(self.minCost(n-1), self.minCost(n-2))
        return self.dp[n]

    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1

        return min(f1, f2)
    '''
