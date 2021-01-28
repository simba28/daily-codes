class Solution:

    def dfs(self, u):
        self.visited[u] = 1

        for v in self.adj[u]:
            if self.visited[v] == 1:
                return True
            if self.visited[v] == 0 and self.dfs(v):
                return True
            
        self.visited[u] = 2
        self.s.append(u)

        return False
        
    def findOrder(self, numCourses, prerequisites):
        
        self.adj = [[] for i in range(numCourses)]
        for courses in prerequisites:
            self.adj[courses[1]].append(courses[0])
            
        self.s = []
        self.visited = [0]*numCourses

        for i in range(numCourses):
            if self.visited[i] == 0 and self.dfs(i):
                return []
                
        self.s.reverse()
        
        return self.s
            
                
print(Solution().findOrder(4, [[0,1],[1,2],[2,3]]))