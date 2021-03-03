# link => https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

import heapq


class Solution:
    # using max heap
    def kWeakestRows(self, mat, k):

        res = []

        for i, row in enumerate(mat):

            sum_ = sum(row)
            heapq.heappush(res, (-sum_, -i))
            if len(res) > k:
                heapq.heappop(res)

        ans = []
        while res:
            ans.insert(0, -heapq.heappop(res)[1])

        return ans

    '''
    def kWeakestRows(self, mat, k):

        # by sorting
        for i in range(len(mat)):
            mat[i].append(i)

        mat.sort(key=lambda x: sum(x[:-1]))

        return [mat[i][-1] for i in range(k)]
    '''


print(Solution().kWeakestRows([[1, 0, 0, 0],
                               [1, 1, 1, 1],
                               [1, 0, 0, 0],
                               [1, 0, 0, 0],
                               [1, 1, 0, 0],
                               [1, 1, 1, 0]], 3))
