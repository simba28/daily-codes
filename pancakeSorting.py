class Solution:
    def pancakeSort(self, A):
        
        def flip(sublist, k):
            i = 0
            while i< k/2 :
                sublist[i], sublist[k-i-1] = sublist[k-i-1], sublist[i]
                i += 1
                
        ans = []
        valueToSort = len(A)
        while valueToSort > 0:
            index = A.index(valueToSort)
            
            if index != valueToSort-1:
                if index != 0:
                    ans.append(index+1)
                    flip(A, index+1)
                    
                ans.append(valueToSort)
                flip(A, valueToSort)
                
            valueToSort -= 1
            
        return ans
                    
print(Solution().pancakeSort([4,2,3,1]))