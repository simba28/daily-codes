# link => https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
# youtube => https://www.youtube.com/watch?v=pYs3qj42h3c

# important discusstin link => https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O(N)-Time-and-Space


class Solution:
    def mctFromLeafValues(self, arr) -> int:

        cache = {}

        def helper(st, end):

            if (st == end):
                cache[(st, end)] = (arr[st], 0)
                return cache[(st, end)]

            if (st, end) in cache:
                return cache[(st, end)]

            minSum = float('inf')
            maxLeaf = -float('inf')
            for i in range(st, end):
                left = helper(st, i)
                right = helper(i+1, end)
                maxLeaf = max(left[0], right[0])
                minSum = min(minSum, left[1]+right[1]+left[0]*right[0])

            cache[(st, end)] = (maxLeaf, minSum)
            return cache[(st, end)]

        res = helper(0, len(arr)-1)
        return res[1]
