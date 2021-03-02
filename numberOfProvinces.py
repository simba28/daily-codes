# link => https://leetcode.com/problems/number-of-provinces/


class Solution:

    # dfs solution
    def findCircleNum(self, isConnected) -> int:

        n = len(isConnected)
        visited = set()

        def dfs(node):

            for idx, conn in enumerate(isConnected[node]):
                if conn == 1 and idx not in visited:
                    visited.add(idx)
                    dfs(idx)

        ans = 0
        for x in range(n):
            if x not in visited:
                ans += 1
                visited.add(x)
                dfs(x)

        return ans

    '''
    # using Union find
    def findCircleNum(self, isConnected) -> int:
        
        graph = {x:x for x in range(len(isConnected))}
        n = len(isConnected)
        
        def find(x):
            if graph[x] != x:
                graph[x] = find(graph[x])
            return graph[x]
        
        def union(x,y):
            graph[find(x)] = find(y)
            
        for i in range(n):
            for j in range(n):
                if i==j: continue
                
                if isConnected[i][j] == 1:
                    union(i,j)
                    
        ans = set()
        for key in graph:
            key = find(key)
            ans.add(key)
            
        return len(ans)
    '''


print(Solution().findCircleNum([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
