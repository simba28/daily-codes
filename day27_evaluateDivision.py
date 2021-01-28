'''
You are given equations in the format A / B = k, where A and B are variables represented 
as strings, and k is a real number (floating-point number). Given some queries, return the 
answers. If the answer does not exist, return -1.0.

The input is always valid. You may assume that evaluating the queries will result in no 
division by zero and there is no contradiction.
'''
from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries) :
        
        self.res = []
        
        def dfs(s, d, visited, tmp):
            
            if s in visited: return
            
            if s == d:
                self.ans = tmp
                return
            
            visited.add(s)
            
            for child in graph[s]:
                dfs(child[0], d, visited, tmp*child[1])
            
            
        graph = defaultdict(list)
        
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1/values[i]))
        
        for i in range(len(queries)):
            
            s = queries[i][0]
            d = queries[i][1]
            visited = set()
            self.ans = -float(1)
            if s in graph:
                dfs(s, d, visited, float(1))
            self.res.append(self.ans)
            
        return self.res
        
print(Solution().calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]))