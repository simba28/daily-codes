class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0 
        i = 1
        while True:
            if n-i>-1:
                ans += 1
                n -= i
                i += 1
            else:
                break
        return ans

# x = Solution()
# print(x.arrangeCoins(100))
        