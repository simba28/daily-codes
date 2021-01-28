class Solution:
    def reverseBits(self, n):
        binary = bin(n)[2:]
        binary = ('0'*(32-len(binary)))+binary
        binary = binary[::-1]
        res = int(binary,2)
        return res

test = Solution()
print(test.reverseBits(4294967295))