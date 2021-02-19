# link => https://leetcode.com/problems/stone-game-iii/
# youtube => https://www.youtube.com/watch?v=HsY3jFyaePU


class Solution:
    # Bottom Up
    def stoneGameIII(self, stoneValue) -> str:
        s = stoneValue
        n = len(stoneValue)
        dp = [0] * (n+1)
        i = n-1
        while i >= 0:

            ans = -float('inf')
            ans = max(ans, s[i]-dp[i+1])
            if i+1 < n:
                ans = max(ans, s[i]+s[i+1]-dp[i+2])
            if i+2 < n:
                ans = max(ans, s[i]+s[i+1]+s[i+2]-dp[i+3])
            dp[i] = ans
            i -= 1

        res = dp[0]
        return 'Alice' if res > 0 else ('Bob' if res < 0 else 'Tie')

    '''
    # Top Down
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        dp = {}
        
        def helper(i):
            
            if i >= n: return 0
            
            if (i) in dp:
                return dp[i]
            
            ans = -float('inf')
            tot = 0
            for j in (0,1,2):
                if i+j < n:
                    tot += stoneValue[i+j]
                ans = max(ans, tot-helper(i+j+1))
            dp[i] = ans
            return dp[i]
        
        n = len(stoneValue)
        res = helper(0)
        return 'Alice' if res > 0 else ('Bob' if res < 0 else 'Tie')

    '''


print(Solution().stoneGameIII([1, 2, 3, 7]))
