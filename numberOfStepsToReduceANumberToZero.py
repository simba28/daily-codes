# link => https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/


class Solution:
    def __init__(self):
        self.res = 0

    def numberOfSteps(self, num: int) -> int:

        if num == 0:
            return self.res

        self.res += 1
        if num % 2 == 0:
            return self.numberOfSteps(num//2)
        else:
            return self.numberOfSteps(num-1)


print(Solution().numberOfSteps(14))
