# link=> https://leetcode.com/problems/sort-characters-by-frequency/submissions/

import heapq


class Solution:

    # using heap
    def frequencySort(self, s: str) -> str:

        d = {}
        for ch in s:
            if ch in d:
                d[ch] = [d[ch][0]+1, ch]
            else:
                d[ch] = [1, ch]

        arr = []
        for lst in d.values():
            arr.append(lst)

        heapq.heapify(arr)

        res = ''
        while arr:
            val, ch = heapq.heappop(arr)
            res = res + (ch*val)

        return res[::-1]

    # by sorting
    # def frequencySort(self, s: str) -> str:

    #     d = {}
    #     for ch in s:
    #         if ch in d:
    #             d[ch] = [d[ch][0]+1, ch]
    #         else:
    #             d[ch] = [1, ch]

    #     res = ''
    #     for n, ch in sorted(d.values(), reverse=True):
    #         tmp = ch*n
    #         res = res+tmp

    #     return res
