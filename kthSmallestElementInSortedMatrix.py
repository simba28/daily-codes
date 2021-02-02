# link => https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

import heapq


class Solution:

    # using Binary Search
    def kthSmallest(self, matrix, k):

        n = len(matrix)
        min_ = matrix[0][0]
        max_ = matrix[-1][-1]

        def myCount(i):
            row = 0
            col = n-1
            count = 0
            while row < n and col >= 0:
                if matrix[row][col] <= i:
                    count += col+1
                    row += 1
                else:
                    col -= 1
            return count

        while min_ < max_:
            mid = (max_+min_)//2
            if myCount(mid) < k:
                min_ = mid+1
            else:
                max_ = mid

        return max_

    # # using heap O(k log n)
    # def kthSmallest(self, matrix, k):

    #     heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
    #     heapq.heapify(heap)

    #     n = len(matrix)
    #     res = 0
    #     for _ in range(k):

    #         res, i, j = heapq.heappop(heap)
    #         if j+1 < n:
    #             heapq.heappush(heap, (matrix[i][j+1], i, j+1))

    #     return res

    # # trivial solution with time complexity O(n^2 log k)
    # def kthSmallest(self, matrix, k: int) -> int:

    #     arr = []

    #     for lst in matrix:

    #         for val in lst:

    #             heapq.heappush(arr, -val)
    #             if len(arr) > k:
    #                 heapq.heappop(arr)

    #     return -heapq.heappop(arr)


print(Solution().kthSmallest([[1, 3, 4], [5, 8, 9], [14, 16, 17]], 6))
