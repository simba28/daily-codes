class Solution:
    def sortArrayByParity(self, A):
#         even = []
#         odd = []
#         for n in A:
#             if n%2 == 0:
#                 even.append(n)
#             else:
#                 odd.append(n)
                
#         return even+odd

        i, j = 0, len(A)-1
        while i<j:
            if A[i]%2 > A[j]%2:
                A[i], A[j] = A[j], A[i]
                
            if A[i]%2 == 0:
                i += 1
            if A[j]%2 == 1:
                j -= 1
                
        return A

print(Solution().sortArrayByParity([1,2,3,4,5,6,7,8]))
        