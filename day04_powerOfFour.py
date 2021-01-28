class Solution:
    def isPowerOfFour(self, num: int) -> bool :
        # for power of 4, in its bit representation, there can
        # only be a single 1 and that too in only odd positions.

        if num<=0:
            return False

        binary = bin(num)[2:][::-1]

        if binary.count('1') == 1 :
            if binary.index('1')%2 == 0:
                return True

        return False

print(Solution().isPowerOfFour(64))