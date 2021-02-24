# link => https://leetcode.com/problems/arithmetic-slices/


class Solution:
    # dynamic programming
    def numberOfArithmeticSlices(self, A):

        sum_ = 0
        dp = 0
        for i in range(2, len(A)):

            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp = 1 + dp
                sum_ += dp
            else:
                dp = 0

        return sum_

    '''
    # recursive approach
    def numberOfArithmeticSlices(self, A):

        self.sum = 0

        def slices(i):

            if i < 2:
                return 0

            ap = 0
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                ap = 1 + slices(i-1)
                self.sum += ap
            else:
                slices(i-1)

            return ap

        slices(len(A)-1)
        return self.sum
    '''


print(Solution().numberOfArithmeticSlices([7, 7, 7, 7, 7]))
