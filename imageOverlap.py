'''
Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?
'''

class Solution:
    def largestOverlap(self, A, B):
        
        return max(self.shiftCount(A,B), self.shiftCount(B,A))
        
    def shiftCount(self, A, B):
        
        n, count = len(A), 0
        
        for x in range(n):
            for y in range(n):
                tmp = 0
                for i in range(y,n):
                    for j in range(x,n):
                        if A[i][j]==1 and B[i-y][j-x]==1:
                            tmp += 1
                count = max(tmp, count)
                
        return count

print(Solution().largestOverlap([[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]))