#link => https://leetcode.com/problems/sort-the-matrix-diagonally/
#concept => just normally traverse and sort the diagonals at the go

class Solution:
    def diagonalSort(self, mat) :
        
        m = len(mat)
        n = len(mat[0])
        
        i = m-1
        j = 0
        while i >= 0 and j < n :
            
            x = i
            y = j
            
            arr = []
            while x < m and y < n:
                arr.append(mat[x][y])
                x += 1
                y += 1
            else:
                arr.sort()
                x = i
                y = j
                z = 0
                while x<m and y<n:
                    mat[x][y] = arr[z]
                    x += 1
                    y += 1
                    z += 1

                if i > 0:
                    i -= 1
                else:
                    j += 1
                    
        return mat
           
print(Solution().diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))