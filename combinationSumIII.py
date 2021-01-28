'''
Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination 
should be a unique set of numbers.
'''

class Solution:
    def combinationSum3(self, k: int, n: int) :
        
        results = []
        
        def backtrack(remain, comb, start):
            
            if remain == 0 and len(comb) == k:
                results.append(comb.copy())
                return
            
            if remain < 0 or len(comb) == k:
                return
            
            for i in range(start,10):
                comb.append(i)
                backtrack(remain-i, comb, i+1)
                comb.pop()
                
        backtrack(n, [], 1)
        
        return results
    
print(Solution().combinationSum3(3,9))