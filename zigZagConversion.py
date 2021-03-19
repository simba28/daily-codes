# link => https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        lst = []

        idx = 0
        j = 0
        while j < len(s):

            tmp = ['']*numRows

            if idx == 0:
                for i in range(numRows):
                    if j >= len(s):
                        break

                    tmp[i] = s[j]
                    j += 1
                idx = numRows-2

            else:
                tmp[idx] = s[j]
                j += 1
                idx -= 1

            lst.append(tmp.copy())

        ans = []
        for i in range(numRows):
            for x in lst:
                if x[i] != '':
                    ans.append(x[i])

        return ''.join(ans)
