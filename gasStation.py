'''
link
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3470/
'''

class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        
        if (sum(gas) - sum(cost) < 0):
            return -1
        
        gas_tank, start_index = 0, 0
        
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            
            if gas_tank < 0:
                start_index = i+1
                gas_tank = 0
            
        return start_index
        
        # l = len(gas)
        
        # starts = []
        # for i in range(l):
        #     if gas[i]>=cost[i]:
        #         starts.append(i)
                
        # if not starts: return -1
        
        # for start in starts:
            
        #     station = start
        #     count = 1
        #     tank = gas[station]
        #     while count <= l:
                
        #         if tank < cost[station]: break
                    
        #         tank -= cost[station]
        #         station = 0 if station==l-1 else station+1
        #         tank += gas[station]
                
        #         count += 1
        #     else: return start
            
        # return -1
                
        
print(Solution().canCompleteCircuit([5,1,2,3,4],
[4,4,1,5,1]))