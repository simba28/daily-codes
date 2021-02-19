# link => https://leetcode.com/problems/partition-array-for-maximum-sum/submissions/


class Solution:
    def maxSumAfterPartitioning(self, arr, k: int) -> int:

        n = len(arr)
        dp = [0] * (n+1)

        for i in range(1, n+1):

            curMax = 0
            for x in range(1, min(i, k)+1):

                curMax = max(curMax, arr[i-x])
                dp[i] = max(dp[i], dp[i-x] + curMax*x)

        return dp[n]


print(Solution().maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))
