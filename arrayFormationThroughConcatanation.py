#link => https://leetcode.com/problems/check-array-formation-through-concatenation/

class Solution:
    def canFormArray(self, arr, pieces) -> bool:
        
        l = len(arr)
        
        i = 0
        while i < l:
            
            n = arr[i]
            
            for j, piece in enumerate(pieces):
                if piece[0] == n:
                    pieces.pop(j)
                    i += 1
                    break
            else:
                return False
            
            for no in piece[1:]:
                if no != arr[i]:
                    return False
                i += 1
                
        return True
