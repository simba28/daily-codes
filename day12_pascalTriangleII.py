class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        
        res = [1,1]
        
        for i in range(2,rowIndex+1):
            temp = [1]
            
            for j in range(i-1):
                temp.append(res[j]+res[j+1])
                
            temp.append(1)
            
            res = temp.copy()
            
        return res
                
# print(Solution().getRow(12))