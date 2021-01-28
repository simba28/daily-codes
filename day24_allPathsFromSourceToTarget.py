class Solution:
    def dfs(self, node):

        self.v.append(node)
        if len(self.graph[node])==0:
            self.ans.append(self.v.copy())
            return
        
        for i in self.graph[node]:
            self.dfs(i)
            self.v.pop()
    
    def allPathsSourceTarget(self, graph):
        
        # using DFS
        self.v = []
        self.ans = []
        self.graph = graph
        
        self.dfs(0)
        
        return self.ans
    
        # using BFS
        
#         res = []
#         queue = [[0]]
        
#         goal = len(graph)-1
        
#         while queue:
#             path = queue.pop(0)
#             if path[-1]==goal:
#                 res.append(path)
#             else:
#                 neigh = graph[path[-1]]
#                 for i in neigh:
#                     queue.append(path+[i])
                    
#         return res


print(Solution().allPathsSourceTarget([[1,2], [3], [3], []]))