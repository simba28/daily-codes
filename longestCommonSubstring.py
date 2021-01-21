class Solution:
    def longestCommonSubstring(self, s1, s2):

        x = len(s1)
        y = len(s2)

        dp = [[0 for i in range(x+1)] for j in range(y+1)]

        lcs = 0
        res = ''
        lonPalin = ''

        for i in range(1, x+1):
            for j in range(1, y+1):

                if (s1[i-1] == s2[j-1]):
                    dp[j][i] = 1 + dp[j-1][i-1]
                    if dp[j][i] >= lcs:
                        lcs = dp[j][i]
                        res = s1[i-lcs:i]
                        if s1.index(res) == s1.index(res[::-1]):
                            lonPalin = res
                else:
                    dp[j][i] = 0

        return (res, lcs, lonPalin)


string = 'abacdfgdcaba'
print(Solution().longestCommonSubstring(string, string[::-1]))
