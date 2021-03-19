# link => https://leetcode.com/problems/coin-change/


class Solution:
    # using Dynamic Programming
    def coinChangeDP(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX]*amount

        for currAmount in range(1, amount+1):
            min_ = MAX
            for coin in coins:
                if currAmount - coin >= 0:
                    min_ = min(min_, dp[currAmount - coin])

            dp[currAmount] = min_ + 1

        return [dp[amount], -1][dp[amount] == MAX]

    # using BFS
    def coinChangeBFS(self, coins, amount):

        if amount == 0:
            return 0

        value1 = [0]
        value2 = []
        netCoin = 0
        visited = [False]*(amount+1)
        visited[0] = True
        while value1:
            netCoin += 1
            for v in value1:
                for coin in coins:
                    newVal = v + coin
                    if newVal == amount:
                        return netCoin
                    elif newVal > amount:
                        continue
                    elif not visited[newVal]:
                        visited[newVal] = True
                        value2.append(newVal)
            value1, value2 = value2, []

        return -1


# print(Solution().coinChangeBFS([1, 2, 5], 11)
print(Solution().coinChangeDP([1, 2, 5], 11))
