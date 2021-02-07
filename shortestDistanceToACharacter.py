# link => https://leetcode.com/problems/shortest-distance-to-a-character/


class Solution:

    # two pass approach
    def shortestToChar(self, s, c):

        prev = float('-inf')
        ans = []
        for i, ch in enumerate(s):
            if ch == c:
                prev = i
            ans.append(i-prev)

        prev = float('inf')
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev-i)

        return ans

    # using an array of indices where character is present
    # def shortestToChar(self, s: str, c: str):

    #     lst = [i for i in range(len(s)) if s[i] == c]

    #     res = []
    #     rpt = 0
    #     lpt = 0
    #     for idx, ch in enumerate(s):

    #         if rpt < len(lst)-1 and lst[rpt] < idx:
    #             lpt = rpt
    #             rpt += 1

    #         if ch == c:
    #             res.append(0)
    #         else:
    #             # lpt < idx < rpt
    #             if rpt < len(res):
    #                 rightDist = abs(lst[rpt] - idx)
    #             else:
    #                 rightDist = float('inf')
    #             leftDist = abs(idx - lst[lpt])
    #             res.append(min(leftDist, rightDist))

    #     return res
